---
title: "NN-AdderNet: Nonnegative and Sparse Weight Optimization for Ultra-Low Bitwidth AdderNet Quantization and Compression"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# NN-AdderNet: Nonnegative and Sparse Weight Optimization for Ultra-Low Bitwidth AdderNet Quantization and Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132907">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132907</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 低比特量化，模型压缩，双稀疏分布 </p>
</div>


---

## 研究概要
本文提出NN-AdderNet非负加法网络，通过等价变换将带符号SAD转为无负权重运算，搭配面向激活量化挖掘权重双重稀疏。采用霍夫曼无损压缩实现4bit甚至更低比特存储，精度仅损失0.3%~1.6%；硬件仿真相较CNN推理延迟降低34.8%~38.6%、能耗显著下降。

## 背景和动机
1. AdderNet用SAD替代乘法，硬件能效更高，但SAD要求权重与激活共用量化缩放因子，传统CNN量化方案无法直接复用。
2. 现有AdderNet量化方案最高仅能做到INT6，带符号权重存在符号位开销，动态范围大、压缩率低。
3. 原生AdderNet权重服从拉普拉斯分布，正负数值均衡，熵编码稀疏度差，模型压缩收益有限。
4. WSQ、AOQ等低比特AdderNet方法精度损耗明显，且无法实现4bit以下极致轻量化，边缘部署受限。
5. 带符号权重存储需额外符号比特，片上SRAM与片外DRAM传输开销大，加速器时延、能耗居高不下。

## 相关工作
1. 原生AdderNet：用绝对差替代MAC，但未优化量化，仅支持INT16高位宽硬件实现。
2. WSQ-AdderNet：权重标准化压缩至INT8，会带来固有精度衰减，压缩能力有限。
3. AdderNet2.0(AOQ)：面向激活量化实现INT6，仍保留符号位，无法突破4bit压缩瓶颈。
4. CNN低比特量化：独立缩放权重/激活，不适用于SAD运算数学约束。
5. 神经网络无损压缩：霍夫曼、游程编码依赖高稀疏数据，AdderNet原始权重稀疏度不足。

## 本文解决方案
### 1 SAD等价非负变换定理
推导数学等价转换公式，将带符号权重SAD运算转为ReLU非负权重计算；负权重绝对值和作为固定常量融合偏置，推理无额外计算开销，消除符号存储需求。
### 2 面向激活的非负量化方案
复用AOQ权重裁剪策略，结合非负变换，权重统一转为无符号整数；裁剪偏差预计算并融合BN层，解决低比特量化误差累积问题。
### 3 双重稀疏权重优化
非负量化后权重呈现双稀疏分布：大量零值、饱和极值占比极高，大幅提升霍夫曼编码压缩效率；激活经ReLU也具备高零稀疏特性。
### 4 端到端无损压缩流水线
量化后权重、激活统一采用霍夫曼编码，无需专用复杂编解码硬件，平均压缩比特可降至3bit以内。
### 5 配套低比特Adder加速器设计
基于65nm转45nm工艺完成SAD单元RTL设计，搭建CNNergy仿真平台评估PE算力、片上SRAM、DRAM带宽带来的时延与能耗收益。

## 实验分析
1. 实验环境：ResNet20/32/50，CIFAR10/100、ImageNet；RTX3090训练，65nm RTL综合、CNNergy硬件仿真。
2. 压缩效果：8bit原始模型压缩至平均4bit内，5bit原始模型压缩至3bit内；相较CNN压缩比特节省0.6~2.65bit。
3. 精度表现：4bit以内极低比特下分类精度仅下降0.3%~1.6%，远优于WSQ、AOQ基线。
4. 硬件指标：8bit NN-Adder推理时延较CNN降低34.8%~38.6%，5bit版本降低13%~16.2%；整体能耗最高下降16%。
5. 消融验证：非负变换消除符号位、双重稀疏是压缩提升两大核心，二者缺一无法实现超低位宽无损压缩。

## 研究启发
1. AdderNet独特SAD运算不能照搬CNN量化逻辑，通过数学等价变换消除符号位是低位宽量化关键前置手段。
2. 权重分布改造可显著提升熵压缩收益，构造双重稀疏能以极小精度代价实现极致模型轻量化。
3. 推理阶段常量偏置可预计算融合至BN，无需实时额外运算，不会引入硬件延时开销。
4. DRAM访存是边缘加速器主要能耗与时延瓶颈，权重压缩能大幅降低片外数据传输量。
5. 加法网络轻量化路线可分两步：先算法改造权重数值分布，再搭配通用无损编码，无需定制复杂压缩硬件。
