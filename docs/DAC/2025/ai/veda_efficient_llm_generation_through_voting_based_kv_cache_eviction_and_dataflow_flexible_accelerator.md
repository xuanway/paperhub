---
title: "VEDA: Efficient LLM Generation Through Voting-based KV Cache Eviction and Dataflow-flexible Accelerator"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# VEDA: Efficient LLM Generation Through Voting-based KV Cache Eviction and Dataflow-flexible Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2507.00797">https://arxiv.org/abs/2507.00797</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，算法，数据流，加速器，硬件 </p>
</div>


---

## 研究概要
本文提出VEDA端侧LLM专用加速器，实现算法-数据流-硬件三重协同优化。设计投票式KV缓存淘汰算法消除传统指标偏差；提出灵活内外积可重构PE阵列适配动态GEMV；元素串行调度将Softmax/LN硬件开销降至O(1)。28nm流片能效达GPU38.8倍，推理速度提升2.3~10倍，困惑度损失极小。

## 背景和动机
1. 端侧设备算力/存储受限，LLM生成阶段以GEMV为主，内存带宽瓶颈严重，现有加速器多针对预填充GEMM优化，生成阶段优化缺失。
2. 现有KV缓存淘汰方法存在计数、均值、离群三重偏差，易误删关键历史token，长文本困惑度大幅上升。
3. GEMV矩阵维度随序列动态变化，固定PE阵列硬件利用率极低，K矩阵转置带来不规则访存开销。
4. Softmax、LayerNorm存在强数据依赖，传统并行专用单元硬件规模O(N)，面积功耗成本过高。
5. 缺少算法缓存压缩、动态数据流、非线性算子三位一体协同的端侧LLM专用ASIC架构。

## 相关工作
1. KV缓存压缩算法：Streaming LLM滑动窗口丢失远端信息，H2O累积注意力得分存在多重偏差，均无法自适应动态序列。
2. Transformer加速器(A³/Spatten/Sanger)：仅面向预填充GEMM，无动态GEMV适配架构，未解决KV持续膨胀问题。
3. 固定数据流脉动阵列：采用单一内/外积，无法适配变长序列，转置操作增加访存代价。
4. 非线性算子硬件：批量并行SFU单元，硬件开销随通道线性增长，推理流水线阻塞PE阵列。
5. 云端批量LLM调度：依赖多请求GEMM合并，不适用于端侧单请求推理场景。

## 本文解决方案
### 1 投票式KV缓存淘汰算法
每个token作为投票者，基于单头注意力分布自适应均值-标准差阈值统计淘汰票数；保留前置基础窗口，淘汰票数最高KV向量，规避三类偏差，缓存可压缩至原10%精度损失微弱。
### 2 灵活乘积可重构PE阵列
支持运行时切换内积/外积数据流：Q×Kᵀ用内积、S'×V用外积，统一KV存储格式消除矩阵转置；8×8分层加法树适配任意动态隐藏维度。
### 3 元素串行调度机制
将Softmax/LN拆归约+归一化两阶段，串行输出同步送入SF并行计算，仅需1组指数/除法单元，非线性硬件开销从O(N)降至O(1)。
### 4 一体化VEDA硬件架构
包含可重构PE阵列、轻量SFU、独立投票引擎、片上权重缓存；投票引擎与计算流水线并行，不占用推理时延，支持预填充、生成双阶段全流程加速。
### 5 三层协同流水线
算法层动态裁剪KV缩减访存；数据流层匹配内外积消除转置；硬件层低开销非线性单元消除流水线气泡，三层同步优化时延与能耗。

## 实验分析
1. 实验环境：TSMC 28nm 1GHz，Llama2-7B、PG19数据集，对比H2O/Streaming LLM、Spatten/Sanger、RTX4090。
2. 算法效果：同等压缩比下困惑度优于主流淘汰策略，缓存压缩至0.1原始长度仍保持高质量生成。
3. 数据流消融：灵活数据流降低25%注意力时延；搭配元素串行调度整体时延下降60%。
4. 推理加速：开启KV淘汰相较无缓存压缩基线提速2.3~10倍。
5. 硬件指标：芯片总面积1.058mm²，能效达GPU 38.8倍，SFU硬件面积占比不足3%，投票引擎开销仅6.5%。

## 研究启发
1. LLM生成阶段GEMV是核心瓶颈，不能复用预填充GEMM加速器设计，必须提供动态可重构数据流。
2. 仅靠注意力累加值评判KV重要性存在固有偏差，投票机制利用二元投票可更公平筛选待淘汰向量。
3. 内/外积混合数据流可省去K矩阵转置，大幅改善片外HBM访存连续性。
4. 串行元素计算可复用单套非线性运算单元，解决Softmax/LN硬件面积膨胀问题。
5. 缓存压缩算法、数据流调度、计算硬件三层协同才能充分释放端侧ASIC能效，单一维度优化收益有限。
