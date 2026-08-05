---
title: "SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2501.15448">https://arxiv.org/abs/2501.15448</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量化，时间稀疏性，混合精度稠密-稀疏架构，扩散模型加速 </p>
</div>

---

## 研究概要
本文提出软硬件协同SQ-DM加速方案，面向EDM扩散模型设计分层混合4bit量化，将SiLU替换为ReLU挖掘时序通道激活稀疏；配套异构稠密-稀疏加速器，集成时序稀疏检测器与通道末地址映射。相比FP16稠密基线最高提速6.91倍，能耗降低51.5%，4bit下图像FID显著优于现有INT4量化方案。

## 背景和动机
1. 扩散模型需多步迭代去噪，低比特量化误差随时间步累积，主流INT4量化生成图像存在严重噪点，画质大幅衰减。
2. 模型各模块量化敏感度差异极大，统一4bit会损害关键编码器/解码器块精度，统一8bit又无法充分压缩算力与存储。
3. 原生SiLU激活数值分布利用率低，难以形成有效稀疏，现有稀疏方案仅针对权重，激活稀疏挖掘不足。
4. 扩散激活存在时序通道动态稀疏特性，通用稀疏硬件无法按时间步动态区分稠密/稀疏通道，算力浪费严重。
5. 现有扩散加速器均为单一稠密阵列，不能混合处理稠密、稀疏通道，无法利用时序稀疏削减计算量。

## 相关工作
1. 扩散量化算法（PTQ4DM、Q-Diffusion）：仅支持8bit量化，4bit方案依赖低秩分支，硬件开销高、画质差。
2. SVDquant：扩散4bit量化，需FP16低秩辅助分支，无法生成原生4bit权重/激活，无配套稀疏硬件。
3. 结构化权重稀疏方案：仅裁剪权重，不挖掘激活时序稀疏，算力削减幅度有限。
4. 通用稠密神经网络加速器：无稀疏计算通路，无法利用激活零值降低乘加开销。
5. 通用稀疏加速器：不感知扩散时序通道稀疏规律，缺少动态稀疏检测逻辑，适配性差。

## 本文解决方案
### 1 分层混合精度4bit量化策略
通过块量化敏感度测试，仅对首尾敏感模块使用MXINT8，占90%算力的Conv+SiLU模块采用自研带FP8缩放因子的INT4格式，兼顾压缩率与生成FID指标。
### 2 ReLU激活替换与微调优化
将原生SiLU替换为ReLU，数值全部非负可采用UINT4充分利用量化区间；少量微调即可维持生成质量，平均激活稀疏度提升至65%。
### 3 时序通道稀疏挖掘机制
ReLU输出呈现通道级时序动态稀疏，设置30%稀疏阈值，每时间步更新通道稠密/稀疏标签，分离两类通道分别送入对应计算单元。
### 4 异构稠密-稀疏混合PE阵列
架构包含DPE稠密单元、SPE稀疏单元，复用MAERI稠密通路与SIGMA稀疏通路，控制器搭载时序稀疏检测器，逐时间步更新通道调度信息。
### 5 通道末内存地址映射
激活按宽-高-通道排布、权重按核尺寸-输出-输入通道排布，完整通道连续存取，大幅降低稀疏通道索引寻址开销。

## 实验分析
1. 实验环境：28nm工艺Stonne仿真，EDM1/EDM2模型，CIFAR10/AFHQv2/FFHQ/ImageNet数据集，对比FP16、INT4、INT4-VSQ稠密加速器。
2. 量化画质：纯4bit混合量化FID远优于传统INT4-VSQ，ReLU优化后指标进一步逼近FP16基线。
3. 算力存储：混合量化平均计算、内存开销分别降低73%、72%。
4. 硬件收益：仅4bit量化带来3.78倍提速，叠加时序稀疏总加速6.91倍，系统能耗减少51.5%。
5. 消融实验：ReLU是激活稀疏核心；时序逐步更新稀疏标签收益最高，阈值30%可平衡稠密/稀疏单元负载。

## 研究启发
1. 扩散模型不能统一低比特，分层混合量化可仅对少量敏感块保留高位宽，兼顾画质与压缩收益。
2. 更换激活函数是低成本提升激活稀疏的关键手段，ReLU比SiLU更适配低比特量化与稀疏硬件。
3. 扩散稀疏具备通道+时序双重动态特征，静态稀疏硬件无法充分挖掘迭代过程算力冗余。
4. 稠密-稀疏异构PE阵列配合时序动态检测器，是适配生成模型迭代计算的高效硬件架构。
5. 内存数据排布需匹配通道分组逻辑，通道末映射可消除稀疏通道碎片化寻址带来的额外访存开销。
