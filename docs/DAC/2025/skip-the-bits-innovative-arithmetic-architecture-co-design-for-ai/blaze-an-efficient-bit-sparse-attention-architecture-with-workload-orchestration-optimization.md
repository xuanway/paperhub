---
title: "Blaze: An Efficient Bit-Sparse Attention Architecture With Workload Orchestration Optimization"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Blaze: An Efficient Bit-Sparse Attention Architecture With Workload Orchestration Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132475">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132475</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 注意力机制，比特稀疏加速器，负载编排优化，近似计算 </p>
</div>

---


## 研究概要
本文提出Blaze面向注意力的位稀疏加速器，软硬件协同挖掘数值、比特双层稀疏。设计ACB负载调度机制解决PE阵列内外负载失衡，搭配Leading-Booth简化QK计算，搭载可重构位串行PE。BERT系列测试精度损失≤0.9%，性能2.37~6.18倍、能效9.69~43.96倍优于主流注意力加速器，超越AdaS达1.58倍。

## 背景和动机
1. Transformer注意力QKV、QK^T、PV矩阵乘计算量巨大，推理功耗高，传统值稀疏/量化优化未利用海量比特稀疏。
2. 现有位串行加速器多针对CNN，注意力QKV运行时动态生成，无法提前均衡有效比特，非零Booth项分布混乱，PE内外负载严重不均、硬件利用率低。
3. AdaS仅实现单PE内部负载均衡，同行PE间等待阻塞；BitBalance、BitCluster依赖离线权重量化，不适用于动态QKV。
4. 注意力模型对小幅近似误差鲁棒，但缺少低损耗、硬件级动态负载均衡方案，无法充分利用计算冗余。
5. 现有位稀疏架构无分阶段适配注意力流水线的优化，QK、PV、QKV各阶段负载特征差异未被区分利用。

## 相关工作
1. 值稀疏注意力加速器（SpAtten/Sanger/DTQAtten/DEQ）：仅裁剪token或动态量化数值，完全忽略比特层面冗余，算力提升上限低。
2. CNN位串行架构（BitPragmatic/Laconic/AdaS）：仅面向静态权重，AdaS仅单PE内均衡，无法解决注意力跨PE同步等待问题。
3. 离线比特均衡方案（BitBalance/BitCluster）：基于训练前权重预处理，适配CNN固定权重，不支持运行时QKV张量。
4. ViT专用BSViT：仅优化图像patch量化，未针对多头注意力三段矩阵乘做分阶段比特加速。
5. 通用稀疏脉动阵列：无Booth编码近似计算，无法利用注意力计算冗余降低周期。

## 本文解决方案
### 1 自适应单侧位串行乘法AOBM
双向选择更少非零项一侧做串行展开，搭配Booth编码跳过零偏置，原生挖掘比特稀疏，作为PE基础计算单元。
### 2 ACB近似计算负载调度机制
硬件动态统计各PE、AOBM负载WL与近似阈值AT；重负载单元舍弃最低有效Booth项，同时完成同行跨PE、单PE内两层负载均衡，大幅减少空闲周期。
### 3 Leading-Booth单周期计算机制
QK^T阶段仅保留首个非零Booth项，多轮乘简并为单周期，无需精度补偿重算，适配注意力高冗余特性。
### 4 可重构位串行PE阵列
8×8PE阵列，单PE集成4路AOBM；配套WL负载分析器WLA实时生成WL/AT，可切换ACB、Leading-Booth两种计算模式。
### 5 分层注意力流水线适配
QKV生成、PV矩阵乘启用ACB，QK^T专用Leading-Booth，搭配分层片上Nnz/权重/激活缓存降低片外访存。

## 实验分析
1. 实验环境：TSMC 28nm 500MHz Verilog综合，8×8PE阵列，总芯片面积0.968mm²，缓存总容量308KB；测试BERT-base在GLUE、SQuAD等NLP数据集。
2. 精度表现：整体最大精度衰减仅0.9%，多数任务与基线差距极小，无需重算补偿。
3. 性能对比：相较Sanger/DTQAtten/DEQ提速2.37~6.18倍，能效提升9.69~43.96倍；相比最优位稀疏AdaS最高提速1.58倍。
4. 负载利用率：ACB机制使MAC利用率平均提升7%~11%，QK阶段Leading-Booth较AC再提升8%利用率。
5. 硬件开销：RAM占面积/功耗主体，WLA、Softmax模块硬件占比极低，额外控制逻辑开销可忽略。

## 研究启发
1. 注意力张量比特稀疏度远高于数值稀疏，比特级优化是大幅提升推理能效的核心突破口。
2. CNN离线比特均衡方案不适用于动态QKV，必须硬件实时统计负载、动态近似才能消除阵列同步阻塞。
3. 注意力不同计算段冗余程度不同，分阶段切换近似策略可在极小精度损失下最大化加速收益。
4. 仅做单PE内部负载均衡存在瓶颈，跨行PE全局调度才能彻底消除最慢PE带来的整体等待。
5. 基于Booth项的轻量近似计算硬件成本极低，利用Transformer噪声鲁棒性是兼顾精度与算力的高效协同思路。