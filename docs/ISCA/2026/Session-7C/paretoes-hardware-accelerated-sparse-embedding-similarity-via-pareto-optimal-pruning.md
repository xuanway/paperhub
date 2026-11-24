---
title: "ParetoES: Hardware-Accelerated Sparse Embedding Similarity via Pareto-Optimal Pruning"
description: "ISCA 2026 · Session 7C · ParetoES: Hardware-Accelerated Sparse Embedding Similarity via Pareto-Optimal Pruning"
tags:
  - "ISCA2026"
  - "Session 7C"
  - "Domain Specific Accelerators 2"
---

# ParetoES: Hardware-Accelerated Sparse Embedding Similarity via Pareto-Optimal Pruning

**中文标题：** ParetoES: 经由帕累托最优剪枝的硬件加速稀疏嵌入相似度

**所属 Session：** [Session 7C](index.md) · [ISCA 2026](../index.md)

**作者：** Jiaqi Zhai, Xuanhua Shi, Wenju Zhao, Kaiyi Huang, Chencheng Ye, Shunsen Lv, Zhongtian Long, Bingsheng He, Hai Jin

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Efficient retrieval of sparse embeddings, a critical task in modern information systems, is fundamentally challenged by the memory-bound nature of Top-K sparse matrix–vector multiplication (SpMV). Existing solutions often pursue full computation for absolute accuracy, which is not Pareto-optimal and results in excessive memory transfers and redundant work. We propose ParetoES, an FPGA-accelerated retrieval system that adopts a selective computation strategy to optimize the trade-off between recall and throughput. ParetoES integrates algorithmic and architectural co-design, featuring: (1) a Spherical K-means++ Refine algorithm that combines clustering, low-bit quantization, and unstructured pruning to reduce the candidate search space and memory access overhead; (2) a Hierarchical Hotspot-Balancing (H2Balance) strategy to mitigate workload skew in multicore environments; and (3) a lightweight Adaptive Cluster Probing Engine (ACPE) architecture with distributed micro-sorters to enable flexible, high-throughput retrieval. Experiments on five datasets show that when maintaining Recall@100 > 0.8, ParetoES achieves up to 540× and 79× higher Queries Per Second (QPS) than CPU and GPU baselines, respectively. It also demonstrates an average throughput improvement of 2.27× over the state-of-the-art FPGA accelerator.

## 中文摘要

稀疏嵌入的高效检索是现代信息系统中的关键任务，但其根本上受限于 Top-K 稀疏矩阵–向量乘法（SpMV）的内存受限特性。现有方案往往追求完整计算以获得绝对精度，这并非帕累托最优，会导致过多的内存传输和冗余工作。我们提出 ParetoES，一个采用选择性计算策略的 FPGA 加速检索系统，以优化召回率与吞吐量之间的权衡。ParetoES 融合了算法与架构协同设计，具有：(1) 一种 Spherical K-means++ Refine 算法，结合聚类、低位量化和非结构化剪枝，以减小候选搜索空间和内存访问开销；(2) 一种层次化热点均衡（H2Balance）策略，以缓解多核环境中的工作负载倾斜；(3) 一种轻量级自适应簇探测引擎（ACPE）架构，配备分布式微排序器，以实现灵活的高吞吐检索。在五个数据集上的实验表明，在保持 Recall@100 > 0.8 时，ParetoES 的每秒查询数（QPS）分别比 CPU 和 GPU 基线高最多 540× 和 79×。与最先进的 FPGA 加速器相比，其平均吞吐量提升 2.27×。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2026](../index.md)
