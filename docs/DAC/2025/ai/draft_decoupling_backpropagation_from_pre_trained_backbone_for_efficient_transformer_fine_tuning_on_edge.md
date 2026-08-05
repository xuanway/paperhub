---
title: "DRAFT: Decoupling Backpropagation from Pre-trained Backbone for Efficient Transformer Fine-Tuning on Edge"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DRAFT: Decoupling Backpropagation from Pre-trained Backbone for Efficient Transformer Fine-Tuning on Edge

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132748">https://ieeexplore.ieee.org/document/11132748</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 反向传播解耦，稀疏三元旁路网络，算法-硬件协同设计，边缘微调加速 </p>
</div>

---

## 研究概要
本文提出DRAFT软硬件协同框架面向边缘Transformer微调，设计FDA解耦反向传播算法，通过可训练适配器+N:M三值稀疏旁路网络BPN替代主干权重反向路径；配套可重构加速器适配稀疏稠密双数据流。多NLP/CV模型测试，精度损失低于1%，微调平均提速4.9倍、能效提升4.2倍。

## 背景和动机
1. Transformer微调前向与反向传播计算量差距巨大，反向传播需遍历海量冻结主干权重，边缘设备算力、显存难以承载。
2. LoRA、Adapter等主流PEFT仅减少权重梯度计算，仍无法规避输入梯度依赖主干矩阵转置带来的巨大开销，优化上限仅31%。
3. 局部微调、偏置微调等方案削减反向层数，但会造成明显精度下降，无法通用适配各类下游任务。
4. 传统非对称反馈对齐类算法无需主干反向，但缺少预训练权重信息补偿，微调精度损耗严重。
5. 现有训练加速器仅支持统一稠密矩阵运算，未针对稀疏旁路网络做硬件定制，稀疏计算收益无法充分释放。

## 相关工作
1. 参数高效微调（LoRA/Adapter/Bias-Only）：仅减少可更新参数量，无法解决输入梯度的主干反向开销，性能提升有限。
2. 局部分层微调：只更新网络顶层，牺牲模型泛化能力，通用场景适配性差。
3. 反馈对齐类非对称BP：解除权重对称约束，但无预训练权重补偿机制，微调精度大幅衰减。
4. 通用DNN训练加速器：仅支持稠密GEMM，缺少稀疏三值计算专用通路，稀疏优化收益低。
5. 稀疏Transformer推理硬件：面向前向推理，未针对微调双路径（前向/反向）做动态重构设计。

## 本文解决方案
### 1 FDA反馈解耦近似算法
将主干权重反向路径拆分为适配器、稀疏BPN两条轻量化通路；利用SVD分解预训练权重残差作为适配器，补偿旁路近似误差，冻结主干与BPN仅微调适配器，彻底跳过主干反向传播。
### 2 N:M三值稀疏旁路网络
块式TopK三值量化BPN权重，仅保留±/0三类数值，消除浮点乘法；搭配MX混合精度压缩主干（MXFP4）、适配器（MXFP8），块尺寸对齐提升硬件友好度。
### 3 离线三阶段预处理
模型注入适配器与BPN、主干混合精度量化、解耦近似初始化，线下完成稀疏与低比特转换，线上微调无需额外计算。
### 4 可重构DRAFT加速器
多组可重构PE阵列RPE，支持稠密（主干/适配器）、稀疏三值（BPN）双工作流；内置稀疏聚集单元利用蝴蝶网络加速零跳过；MPPE混合精度处理单元兼容FP4/FP8/三值三种乘算模式。
### 5 分层片上存储与乒乓调度
1MB片上SRAM分层缓存，批次数据超容采用乒乓分块处理；向量引擎统一处理Softmax、LN等非线性算子，平衡计算与访存开销。

## 实验分析
1. 实验基准：BERT、ViT、GPT2等模型，GLUE/CIFAR/E2E多数据集；对比全微调、LoRA、偏置微调、局部微调。硬件采用28nm工艺500MHz综合，14.74mm²总面积、1287.72mW功耗。
2. 算法指标：FDA反向计算量降至原版15%以内，各类任务精度损失控制在1%内；稀疏比St=1/4、适配器秩r=16为最优超参组合。
3. 性能指标：相较基线硬件全微调，整体微调平均提速4.9倍，反向阶段最高提速14.1倍；能效相比全微调提升4.2倍、相比LoRA提升2.3倍。
4. 时延能耗：序列越长优化收益越显著，DRAM访存大幅降低；计算核心与片上缓存为主要面积功耗来源。
5. 消融验证：适配器误差补偿、稀疏聚集单元、双重构工作流是提速三大核心模块，缺一将大幅削弱收益。

## 研究启发
1. 现有PEFT优化存在瓶颈，输入梯度的主干反向是微调核心算力浪费，解耦BP双路径是关键优化思路。
2. 非对称反向传播可落地，但必须引入低秩适配器补偿预训练权重丢失的信息，平衡算力与精度。
3. N:M块稀疏比无规则稀疏更适配硬件，三值量化可彻底消除浮点乘法，大幅降低反向开销。
4. 微调前向、反向数据流特征差异极大，加速器需动态重构稠密/稀疏双工作流才能充分释放稀疏收益。
5. 线下量化+稀疏预处理、线上轻量化微调的分离范式，可大幅降低边缘设备实时计算压力。
