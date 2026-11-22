---
title: "Glaive: Cleaving Bandwidth and Latency Scheduling for Efficient Non-Uniform All-to-All Collective Communication"
description: "MICRO 2026 · Session 2A · Glaive：分离带宽与时延调度以实现高效非均匀全到全集合通信"
tags:
  - "MICRO2026"
---

# Glaive: Cleaving Bandwidth and Latency Scheduling for Efficient Non-Uniform All-to-All Collective Communication

**中文标题：** Glaive：分离带宽与时延调度以实现高效非均匀全到全集合通信

**所属 Session：** [Session 2A](index.md) · [MICRO 2026](../index.md)

**作者：** Le Qin, Junwei Cui, Weilin Cai, Chenyu Yuan, Jiayi Huang

**来源：** MICRO 2026，pp. 433–448；[DOI](https://doi.org/10.1109/MICRO67795.2026.00045)

## 英文摘要

Non-uniform All-to-All (Alltoallv) induced by expert parallelism (EP) is a major communication bottleneck in distributed Mixture-of-Experts (MoE) systems. Unlike regular collectives, MoE Alltoallv exhibits a bimodal demand matrix: a few source-destination flows dominate total transferred bytes, while a much larger set of flows is small and latency-sensitive. Existing collective synthesizers largely assume uniform chunking and global timestep-based scheduling. Under non-uniform Alltoallv, this formulation inflates solver state with both data volume and schedule horizon, leading to high synthesis cost and poor bandwidth utilization. We present Glaive, an efficient and scalable Alltoallv synthesizer that explicitly exploits this bimodality. Glaive decomposes the demand matrix into bandwidth-dominated HotSpot flows and latency-dominated ColdSpot flows, then schedules them with two specialized strategies. Thrust splits only large HotSpot flows into a few profitable chunks and places them on load-aware complete paths to improve bandwidth utilization. Sweep keeps ColdSpot flows intact and routes them along load-aware time-shortest paths to minimize overhead. This flow-grained, path-level formulation avoids the uniform chunk-and-timestep explosion of prior solver-based approaches while preserving schedule quality. Across common LLM system topologies and real MoE traces, Glaive achieves average speedups of 7.89x over bidirectional Ring and 6.93x over MPICH. On real 8- and 16-GPU testbeds, it delivers 1.25x higher bandwidth than TE-CCL on average while reducing synthesis time by over 1,000,000x. Glaive synthesizes schedules for 4,000 devices in 25 seconds.

## 中文摘要

由专家并行性（EP）引起的非均匀全对全（Alltoallv）是分布式专家混合（MoE）系统中的主要通信瓶颈。与常规集合不同，MoE Alltoallv 表现出双峰需求矩阵：少数源-目的地流主导总传输字节数，而更大的流集较小且对时延敏感。现有的集体合成器很大程度上假设统一分块和基于全局时间步的调度。在非均匀 Alltoallv 下，该公式会通过数据量和调度范围夸大求解器状态，从而导致综合成本高和带宽利用率低。我们推出 Glaive，一种高效且可扩展的 Alltoallv 合成器，它明确地利用了这种双峰性。 Glaive 将需求矩阵分解为带宽主导的 HotSpot 流和时延主导的 ColdSpot 流，然后使用两种专门的策略对它们进行调度。 Thrust 仅将大型 HotSpot 流量拆分为几个有利可图的块，并将它们放置在负载感知的完整路径上，以提高带宽利用率。 Sweep 保持 ColdSpot 流的完整性，并沿着负载感知的时间最短路径路由它们，以最大限度地减少开销。这种流程粒度、路径级公式避免了先前基于求解器的方法的统一块和时间步爆炸，同时保持了进度质量。在常见的 LLM 系统拓扑和真实的 MoE 轨迹中，Glaive 的平均加速比双向 Ring 提高了 7.89 倍，比 MPICH 平均加速了 6.93 倍。在真实的 8 和 16 GPU 测试台上，它的带宽平均比 TE-CCL 高 1.25 倍，同时将合成时间缩短超过 1,000,000 倍。 Glaive 在 25 秒内综合了 4,000 个设备的时间表。

## 中文关键词

集合通信；全互连通信；混合专家模型；分布式推理；通信调度

## 代码与研究制品

- 研究制品归档：[https://doi.org/10.5281/zenodo.22720374](https://doi.org/10.5281/zenodo.22720374)
- 代码与复现实验仓库：[https://github.com/redbird-arch/micro2026-glaive-artifact](https://github.com/redbird-arch/micro2026-glaive-artifact)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2A](index.md) · [MICRO 2026 主页](../index.md)
