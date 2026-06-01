---
title: "UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Sitian Chen; Amelie Chi Zhou; Yucheng Shi; Yusen Li; Xin Yao"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Sitian Chen; Amelie Chi Zhou; Yucheng Shi; Yusen Li; Xin Yao

**会议**：SC 2025 · St. Louis, MO

## 摘要

Approximate Nearest Neighbor Search (ANNS) is a critical component of modern AI systems, such as recommendation engines and retrieval-augmented large language models (RAG-LLMs). However, scaling ANNS to billion-entry datasets exposes critical inefficiencies: CPU-based solutions are bottlenecked by memory bandwidth limitations, while GPU implementations underutilize hardware resources, leading to suboptimal performance and energy consumption. We introduce UpANNS, a novel framework leveraging Processing-in-Memory (PIM) architecture to accelerate billion-scale ANNS. UpANNS integrates four key innovations, including: architecture-aware data placement to minimize latency through workload balancing; dynamic resource management for optimal PIM utilization; co-occurrence optimized encoding to reduce redundant computations; and an early-pruning strategy for efficient top-k selection. Evaluation on commercial UPMEM hardware demonstrates that UpANNS achieves 4.3x higher QPS than CPU-based Faiss, 

---

## 一句话总结

> 该工作属于 Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search 领域贡献新的设计范式或评估框架。
