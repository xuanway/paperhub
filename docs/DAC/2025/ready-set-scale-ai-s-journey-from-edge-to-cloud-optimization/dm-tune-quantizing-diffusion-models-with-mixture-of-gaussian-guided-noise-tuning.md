---
title: "DM-Tune: Quantizing Diffusion Models with Mixture-of-Gaussian Guided Noise Tuning"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DM-Tune: Quantizing Diffusion Models with Mixture-of-Gaussian Guided Noise Tuning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132501">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132501</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 扩散模型，量化，混合精度，GPU </p>
</div>


---


## 研究概要
本文提出DM-Tune扩散模型量化框架，打破全精度最优固有认知，设计BF16/FP8浮点混合量化策略。构建三高斯噪声调优头补偿统一FP8量化误差，搭配敏感层筛选、时序/提示感知量化与融合GPU内核。多扩散模型测试，画质、多样性优于FP3，推理速度较SOTA提升5.2倍。

## 背景和动机
1. 扩散模型参数量大，FP32推理显存、算力开销极高，低比特量化是落地刚需，但纯FP8量化图像失真严重。
2. 传统认知认为全精度生成效果最优，本文发现浮点混合量化噪声可与扩散原生噪声融合，反而提升生成细节与提示对齐度。
3. 现有混合量化存在海量时序-层搜索空间，且多精度频繁类型转换带来巨大运行时开销，拖慢推理。
4. 整数混合量化动态范围受限，裁剪失真明显，难以生成高清人像等细节内容。
5. 量化误差呈非线性分布，现有线性校正方法无法完整还原混合精度输出效果。

## 相关工作
1. 整数后量化方案（Q-Diffusion、PTQ4DM）：采用INT4/8量化，动态范围不足，细节生成能力差，仅线性补偿量化误差。
2. PTQD：基于整数量化做误差修正，假设FP32为最优基准，未利用扩散随机噪声增益。
3. 通用低比特浮点量化：仅全局统一FP8，无分层、时序定制策略，生成画质衰减明显。
4. 通用GPU低精度算子：未融合非线性高斯噪声计算，噪声校正带来访存瓶颈。

## 本文解决方案
### 1 高效浮点混合量化搜索
选定BF16高精度、FP8(E4M3)低精度组合；依据激活值域、标准差判定敏感层，二分搜索划分高低精度层；提出提示感知、时序感知量化两大优化策略，可控引入增益噪声。
### 2 三高斯混合噪声建模
剖析FP8量化误差由线性相关项+多高斯非线性残差构成，构造含可学习均值、方差、缩放参数的噪声调优头，仅微调少量参数即可拟合混合精度输出。
### 3 轻量噪声调优训练
条件模型以FP-MP输出为真值，无条件模型以FP32为真值；冻结主干仅训练噪声头，5-10轮即可收敛，训练成本极低。
### 4 三层融合优化GPU内核
共享内存LUT查表、预取计算重叠、8分组向量指令并行，将矩阵乘与高斯非线性运算融合，消除噪声校正访存瓶颈。
### 5 通用模型适配流水线
基于PyTorch钩子实现模型无关量化，BN与激活层保持高精度，兼容Stable Diffusion、DiT、DDIM等多类扩散架构。

## 实验分析
1. 测试负载：Stable Diffusion、DiT、DDIM、LDM、IDDPM，搭配COCO/ImageNet/CelebAHQ数据集，指标采用FID、CLIP对齐、精度/召回等。
2. 生成质量：DM-Tune（含噪声调优）FID全面低于FP32、纯FP8、整数量化，图像细节、文本对齐、样本多样性显著提升。
3. 消融实验：三层高斯噪声建模收敛远快于单高斯；提示+时序量化是混合量化超越全精度核心手段。
4. 运行性能：优化后FP8推理开销几乎无增加，相较Q-Diffusion、PTQ4DM等SOTA平均提速5.2倍。
5. 通用性：条件模型增益更突出，无条件模型需开启噪声调优才能超越FP32基准，跨架构稳定有效。

## 研究启发
1. 扩散模型具备随机噪声机制，适度可控量化噪声可优化生成效果，打破“全精度画质最优”固有思维。
2. 浮点混合量化优于整数混合量化，动态范围优势可避免裁剪带来的图像失真问题。
3. 量化误差非线性不能用线性函数拟合，多高斯叠加建模可低成本还原高精度输出分布。
4. 混合量化高转换开销可通过“统一低精度+后置轻量校正”思路规避，兼顾速度与画质。
5. 扩散不同时序、分支对量化敏感度差异极大，分层、时序、提示三粒度定制量化策略是轻量化关键。
