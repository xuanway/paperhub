---
title: "Mist: Efficient Distributed Training of Large Language Models via Memory-Parallelism Co-Optimization"
description: "EuroSys 2025 · LLM Training · Zhanda Zhu (University of Toronto, CentML, Vector Institute), Christina Giannoul"
tags:
  - "EuroSys2025"
  - "LLM Training"
---

# Mist: Efficient Distributed Training of Large Language Models via Memory-Parallelism Co-Optimization

**中文标题：** 通过内存与并行性协同优化实现高效分布式大语言模型训练

**所属 Session：** [Session 9.2: LLM Training](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Training。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Training</p>
</div>

**作者**：Zhanda Zhu (University of Toronto, CentML, Vector Institute), Christina Giannoula (University of Toronto), Muralidhar Andoorveedu (CentML), Qidong Su (University of Toronto, CentML, Vector Institute), Karttikeya Mangalam (UC Berkeley), Bojian Zheng (Independent Researcher), Gennady Pekhimenko (CentML, University of Toronto, Vector Institute)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717461)

## 英文摘要

Various parallelism, such as data, tensor, and pipeline parallelism, along with memory optimizations like activation checkpointing, redundancy elimination, and offloading, have been proposed to accelerate distributed training for Large Language Models. To find the best combination of these techniques, automatic distributed training systems are proposed. However, existing systems only tune a subset of optimizations, due to the lack of overlap awareness, inability to navigate the vast search space, and ignoring the inter-microbatch imbalance, leading to sub-optimal performance. To address these shortcomings, we propose Mist, a memory, overlap, and imbalance-aware automatic distributed training system that comprehensively co-optimizes all memory footprint reduction techniques alongside parallelism. Mist is based on three key ideas: (1) fine-grained overlap-centric scheduling, orchestrating optimizations in an overlapped manner, (2) symbolic-based performance analysis that predicts runtime and memory usage using symbolic expressions for fast tuning, and (3) imbalance-aware hierarchical tuning, decoupling the process into an inter-stage imbalance and overlap aware Mixed Integer Linear Programming problem and an intra-stage Dual-Objective Constrained Optimization problem, and connecting them through Pareto frontier sampling. Our evaluation results show that Mist achieves an average of 1.28× (up to 1.73×) and 1.27× (up to 2.04×) speedup compared to state-of-the-art manual system Megatron-LM and state-of-the-art automatic system Aceso, respectively.

## 中文摘要

数据并行、张量并行、流水线并行等各种并行方式，以及激活检查点、冗余消除、卸载等内存优化，已被提出用于加速大语言模型的分布式训练。为找到这些技术的最佳组合，人们提出了自动分布式训练系统。然而，现有系统仅调优部分优化，原因在于缺乏重叠感知、无法在庞大搜索空间中导航，以及忽略微批间不均衡，导致性能次优。为弥补这些不足，我们提出 Mist，一个感知内存、重叠与不均衡的自动分布式训练系统，可全面协同优化所有内存占用削减技术与并行方式。Mist 基于三个关键思想：（1）以重叠为中心的细粒度调度，以重叠的方式编排各项优化；（2）基于符号的性能分析，使用符号表达式预测运行时和内存使用以快速调优；（3）感知不均衡的层次化调优，将过程解耦为阶段间不均衡与重叠感知的混合整数线性规划问题，以及阶段内双目标约束优化问题，并通过 Pareto 前沿采样将二者连接。评估结果表明，与最先进的人工系统 Megatron-LM 和最先进的自动系统 Aceso 相比，Mist 分别实现平均 1.28 倍（最高 1.73 倍）和 1.27 倍（最高 2.04 倍）的加速。

**英文关键词：** LLM, Systems for Machine Learning, Distributed training

**中文关键词：** LLM、机器学习系统、分布式训练

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
