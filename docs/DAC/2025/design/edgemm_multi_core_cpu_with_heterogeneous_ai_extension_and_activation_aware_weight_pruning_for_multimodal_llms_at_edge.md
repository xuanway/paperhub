---
title: "EdgeMM: Multi-Core CPU with Heterogeneous AI-Extension and Activation-aware Weight Pruning for Multimodal LLMs at Edge"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# EdgeMM: Multi-Core CPU with Heterogeneous AI-Extension and Activation-aware Weight Pruning for Multimodal LLMs at Edge


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.10782">https://arxiv.org/abs/2505.10782</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多模态大语言模型，多核CPU，异构架构，CPU扩展</p>
</div>


---

## 研究概要
本文提出EdgeMM异构多核RISC-V CPU架构，面向边缘多模态大模型。分计算型脉动阵列核、存内CIM存储型核适配GEMM/GEMV两类算子，配套动态激活感知剪枝与令牌驱动带宽调度。22nm流片验证，相比笔记本RTX306提速2.84倍，能效达0.217token/J。

## 背景和动机
1. 边缘MLLM存在异构负载：图像编码器、Prefill是计算密集GEMM，解码阶段为访存受限GEMV，单一硬件无法兼顾两类瓶颈。
2. 边缘GPU成本高、CPU-GPU数据搬运开销大，独立ASIC总线冲突、编译器开发成本高。
3. 现有AI扩展架构仅适配单一计算模式，无法同时兼顾算力与带宽需求。
4. 边缘短序列场景KV缓存占比低，FFN权重是访存主体，现有剪枝方案固定阈值，精度损失严重。

## 相关工作
1. 通用AI ISA扩展（AMX/SME/RISC-V矩阵扩展）：仅单一计算单元，不能区分GEMM/GEMV负载特性。
2. 单类AI加速器（纯脉动阵列/纯CIM）：只能适配单一算子，另一阶段资源利用率极低。
3. 固定权重剪枝算法：全局统一剪枝比例，浅层网络精度损失大，未利用激活通道稀疏性。
4. 边缘GPU推理方案：数据搬运、低负载时SM闲置，算力与带宽资源浪费。

## 本文解决方案
### 1. 双异构核分层集群架构
CC计算核集成脉动阵列加速编码器/Prefill GEMM；MC存储核搭载6T数字CIM宏高效执行解码GEMV；四级分层AXI互联，可弹性扩展集群规模。
### 2. 定制RISC-V异构矩阵向量ISA
新增GEMM矩阵、GEM矩阵向量专用扩展指令，复用原生工具链，无需重构编译器。
### 3. 分层动态激活感知Top-K剪枝
依据各层激活幅值自适应保留通道，浅层不剪枝、深层增大裁剪比例；硬件集成剪枝单元，按需读取权重降低DRAM访问。
### 4. 令牌动态带宽分配调度
根据输出令牌长度调整CC/集群带宽配额；长令牌场景带宽向MC解码核倾斜，批量流式输入并行编码解码。

## 实验分析
1. 实现环境：22nm工艺1GHz，基于Snitch集群搭建，测试SPHINX-Tiny、KarmaVLM两类边缘多模态模型。
2. 架构对比：纯CC/纯MC同构架构性能仅为EdgeMM的0.56/0.38倍，异构匹配负载利用率大幅提升。
3. 剪枝收益：解码延迟平均降低42%，余弦相似度损失极小，浅层精度无明显衰减。
4. 带宽调度：令牌长度128时整体延迟降低40.3%，吞吐量提升2.14倍；超长令牌批量吞吐提升13.98倍。
5. 系统对比：相较RTX306原始性能提升2.15倍，叠加剪枝达2.84倍，峰值138token/s，能效更优。

## 研究启发
1. MLLM前后阶段负载特性完全对立，必须采用计算/存储双异构硬件才能同时消除算力、带宽瓶颈。
2. FFN激活天然通道稀疏，分层动态剪枝优于全局固定阈值，兼顾访存削减与模型精度。
3. CPU内置协处理器相比外挂ASIC/GPU，省去总线竞争，软件适配成本更低。
4. 推理流水线负载随输出令牌长度动态变化，带宽资源不能静态均分，需动态重分配。
5. 数字SRAM CIM针对向量运算优势显著，脉动阵列更适合稠密矩阵运算，二者互补适配多模态全链路。