---
title: "HetAuto: Cross-Cluster Auto-Parallelism for Heterogeneous Distributed Training"
description: "EuroSys 2026 · LLM Training at Scale · Guicheng Qi (The University of Hong Kong), Junwei Su (The University of Hong Kon"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# HetAuto: Cross-Cluster Auto-Parallelism for Heterogeneous Distributed Training

**中文标题：** HetAuto：面向异构分布式训练的跨集群自动并行

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Guicheng Qi (The University of Hong Kong), Junwei Su (The University of Hong Kong), Liqi Yang (Meituan Corporation), Tao Li (Meituan Corporation), Tingwen Xie (Meituan Corporation), Yerui Sun (Meituan Corporation), Yuchen Xie (Meituan Corporation), Chuan Wu (The University of Hong Kong)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803590)

## 英文摘要

As large neural network models (e.g., LLMs) grow in scale, single-cluster resources become insufficient, making cross-cluster distributed training essential. Cross-cluster training is challenging: hardware heterogeneity complicates load balancing and parallelization strategy and introduces hardware compatibility issues in implementation; cross-cluster communication bottlenecks severely impact training throughput. We present HetAuto, an automatic parallelization system for efficient cross-cluster heterogeneous large model training. HetAuto contributes three key innovations: (1) a principle-guided MCTS algorithm with a random forest-enhanced cost model that efficiently searches parallelization strategies and quickly evaluates their performance under heterogeneous configurations; (2) cross-cluster communication optimizations including Virtual-1F1B scheduling that overlaps communication with computation and an optimized resharding strategy for inter-stage communication; and (3) a unified API enabling seamless integration of diverse accelerators. We evaluate HetAuto across 4 different clusters with up to 736 heterogeneous devices. The evaluation results show that HetAuto achieves up to 1.57× training throughput improvement over representative baselines, and strikes an efficient balance between solution quality and search overhead.

## 中文摘要

随着大语言模型（LLM）等大型神经网络模型规模的增长，单集群资源已显不足，跨集群分布式训练因而变得不可或缺。跨集群训练面临诸多挑战：硬件异构性使负载均衡与并行策略选择复杂化，并在实现中引入硬件兼容性问题；跨集群通信瓶颈严重制约训练吞吐。我们提出 HetAuto，一个面向高效跨集群异构大模型训练的自动并行系统。HetAuto 有三项关键创新：（1）一种原理引导的 MCTS 算法，配合随机森林增强的成本模型，可高效搜索并行策略并在异构配置下快速评估其性能；（2）跨集群通信优化，包括将通信与计算重叠的 Virtual-1F1B 调度，以及针对阶段间通信的优化重分片策略；（3）统一的 API，支持多种加速器的无缝集成。我们在最多包含 736 个异构设备的 4 个不同集群上评估了 HetAuto。结果表明，HetAuto 相比代表性基线最高实现 1.57× 的训练吞吐提升，并在解的质量与搜索开销之间取得高效平衡。

**英文关键词：** Distributed Training, Heterogeneous Clusters, Auto-Parallelism

**中文关键词：** 分布式训练、异构集群、自动并行

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
