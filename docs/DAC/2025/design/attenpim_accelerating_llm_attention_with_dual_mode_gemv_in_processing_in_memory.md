---
title: "AttenPIM: Accelerating LLM Attention with Dual-mode GEMV in Processing-in-Memory"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# AttenPIM: Accelerating LLM Attention with Dual-mode GEMV in Processing-in-Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133230">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133230</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型注意力，存内处理，双模式GEMV，KV缓存，软件-硬件协同设计</p>
</div>



---

## 研究概要
本文软硬件协同设计AttenPIM存内计算架构，针对LLM注意力两类GEMV运算设计双模式计算单元，配套KV专用存储布局、头/令牌级并行调度，结合动态分配与算子融合优化。基于28nm工艺验证，对比NeuPIM、AttAcc，速度提升1.13~5.26倍，能耗降低17%~49%。

## 背景和动机
1. LLM推理中多头注意力是访存瓶颈，GPU/TPU带宽受限，长序列场景耗时占比超50%，存内计算PIM是优化路线。
2. 注意力包含Q×K分数、S×上下文两类维度互逆GEMV，现有PIM采用统一划分方案，分别存在KV填充低效、TSV总线拥塞问题。
3. 生成式推理令牌长度动态增长，KV缓存频繁扩容，传统静态内存分配浪费存储空间。
4. 主流NeuPIM、AttAcc架构无法同时适配两类GEMV访存特征，单一模式造成大量掩码访问或多级单元通信损耗。

## 相关工作
1. NeuPIM：列向划分KV矩阵，全局广播向量，但新增V元素无法利用DRAM突发传输，填充耗时提升50倍。
2. AttAcc：分层BG/Die PIM单元，采用转置布局，上下文计算时跨单元TSV传输拥堵，性能下降15%~58%。
3. 通用HBM-PIM（Newton等）：面向静态权重通用GEMV，未适配LLM动态KV与两类互逆矩阵乘。
4. XPU推理优化：仅优化片上缓存，无法解决长序列KV反复片外搬运的内存墙问题。

## 本文解决方案
### 1. 双模式Bank级PIM计算单元
可配置PU分别实现内积（分数Q×K）、外积（上下文S×V）运算；K按整行存储适配广播，V按突发块打散存储，充分利用DRAM突发带宽。
### 2. 专用KV存储布局
K矩阵单令牌向量连续存入同一Bank；V矩阵按突发块分Bank存放，同索引块统一存储，消除掩码低效读写。
### 3. 头/令牌双层并行调度
单通道多注意力头并行执行上下文运算，匹配Bank数量均衡负载；分数计算全Bank并行，无跨层级单元通信。
### 4. 内存与算子联合优化
动态KV分配策略，按需整行申请内存减少碎片；算子融合重叠Softmax与PIM计算，释放TSV传输带宽。

## 实验分析
1. 仿真与工艺：修改DRAMSim3搭建周期模拟器，28nm RTL综合PU单元，测试GPT3-7B/13B/30B/175B与长短四类数据集。
2. 性能收益：相对NeuPIM提速1.20~5.26倍，相对AttAcc提速1.13~3.91倍，V填充阶段开销大幅削减。
3. 能耗表现：整体能耗下降17%~49%，核心增益来自无掩码访存与消除多级TSV数据传输。
4. 硬件开销：PU面积0.86mm，仅比NeuPIM高0.07mm²，远低于AttAcc的1.58mm²，硬件代价极低。
5. 内存利用率：V缓存分配利用率超90，相比基线大幅降低内存碎片浪费。

## 研究启发
1. LLM注意力两类GEMV访存模式完全不同，单一PIM划分方案无法兼顾，双模式硬件是核心优化思路。
2 DRAM突发传输带宽是关键资源，KV存储布局必须贴合硬件访存粒度，掩码访问会带来量级耗时损耗。
3 跨存储层（BG/Die）PIM单元通信存在严重TSV瓶颈，计算约束在Bank内部可规避传输开销。
4 长序列生成推理不能静态预分配最大KV空间，动态行分配平衡吞吐与内存占用。
5 面向大模型的PIM架构需算法数据流、内存布局、硬件计算单元三层软硬件协同优化。