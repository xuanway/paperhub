---
title: "BitPattern: Enabling Efficient Bit-Serial Acceleration of Deep Neural Networks through Bit-Pattern Pruning"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# BitPattern: Enabling Efficient Bit-Serial Acceleration of Deep Neural Networks through Bit-Pattern Pruning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133000">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133000</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 比特串行计算，深度神经网络加速，稀疏性，算法-硬件协同设计，压缩 </p>
</div>


---


## 研究概要
本文提出BitPattern软硬件协同框架，面向位串行DNN加速器设计比特模式剪枝算法与专用解码PE硬件。自定义1:M稀疏比特模式，搭配相似度合并均衡计算负载，配套轻量化解码器。ResNet/ViT验证，模型压缩最高1.72倍，推理提速2.11倍、能耗降低1.86倍，精度损失低于0.8%。

## 背景和动机
1. 位串行加速器依靠零比特跳过提速，但原生权重比特分布无规则，造成PE负载严重不均衡，硬件利用率低下。
2. 非结构化比特稀疏地址不可预测，片外/片上缓存访存碎片化，内存能耗开销巨大。
3. 现有列级比特剪枝BitWave、BBS约束死板，高稀疏度下精度暴跌，或引入补偿常数增加硬件成本。
4. 比特N:M稀疏仅均衡单权重比特数，无法压缩存储，需要额外掩码带来内存冗余。
5. 现有方案大多依赖QAT重训练，商用数据集受限场景落地成本极高，缺少免训练的结构化比特压缩方案。

## 相关工作
1. 基础位串行加速器（Pragmatic/Bitlet）：仅原生跳过零比特，无结构化剪枝，负载失衡严重。
2. Bit-Balance/BitPruner：通道级N:M比特约束，需量化重训练，不减少存储占用。
3. BitWave列剪枝：整列删除比特，格式固定，高稀疏精度衰减明显。
4. BBS双向列剪枝：引入组补偿常量，额外加法逻辑增大硬件面积。
5. ANT数值量化加速器：仅低比特量化，未挖掘比特层稀疏，无位串行并行收益。

## 本文解决方案
### 1 多类型1:M比特模式压缩编码
设计0:0/1:1/1:2/1:3四类预定义稀疏模式，将M比特段压缩为少量存储位，仅需单周期位串行运算；元数据存储模式ID与零列数，内存开销极低。
### 2 面向输出的模式匹配剪枝算法
无需重训练，按权重分组遍历模式组合，以输出误差最小为目标匹配最优比特组合，列方向逐层补偿剪枝误差，兼容后量化流程。
### 3 模式相似度合并负载均衡
将邻近相似比特模式合并统一规格，减少各PE计算周期差异，消除同步等待，大幅均衡位串行工作负载。
### 4 专用BitPattern解码器
基于模式ID最低位区分编码逻辑，内置移位偏移快速生成运算控制信号，复用移位通路，仅极小硬件开销。
### 5 输出驻留32×32位串行PE阵列
8输入通道PE单元搭配定制移位累加链路，解码器与阵列按列绑定，匹配压缩权重数据流，高效跳过结构化零比特。

## 实验分析
1. 实验环境：TSMC 28nm、800MHz，Cycle精准仿真，测试ResNet、ViT系列ImageNet模型，对比多款SOTA位串行加速器。
2. 模型精度：同等剪枝条件下BitPattern平均精度损失仅0.67%，优于BitWave、BBS，单权重平均比特降至4.3~4.5bit。
3. 存储压缩：权重内存最高压缩1.72倍，元数据开销可控，远优于列级剪枝方案。
4. 性能能耗：相较Bitlet提速2.11倍、能耗降低1.86倍；PE单位面积算力、能效均领先所有基线。
5. 硬件开销：整套加速器总面积2.98mm²，解码器仅占0.007mm，新增逻辑可忽略。

## 研究启发
1. 单一整列比特删除灵活性不足，多粒度1:M混合比特模式可同时兼顾存储压缩与精度保持。
2. 位串行加速器性能瓶颈是最大非零比特周期，模式合并是低成本均衡负载的有效手段。
3. 剪枝优化应直接面向矩阵输出误差，而非仅单权重比特误差，可显著降低精度损耗。
4. 比特压缩编码与硬件移位运算天然适配，可省去复杂解压缩算术单元，控制硬件成本。
5. 免训练结构化比特剪枝更适配工业部署，避免QAT带来的数据集、算力额外消耗。
