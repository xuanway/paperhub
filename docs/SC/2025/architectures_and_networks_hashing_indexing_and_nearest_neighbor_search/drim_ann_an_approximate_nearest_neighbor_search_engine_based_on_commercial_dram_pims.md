---
title: "DRIM-ANN: An Approximate Nearest Neighbor Search Engine Based on Commercial DRAM-PIMs"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Mingkai Chen; Tianhua Han; Cheng Liu; Shengwen Liang; Kuai Yu; Lei Dai; Ziming Y"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# DRIM-ANN: An Approximate Nearest Neighbor Search Engine Based on Commercial DRAM-PIMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Mingkai Chen; Tianhua Han; Cheng Liu; Shengwen Liang; Kuai Yu; Lei Dai; Ziming Yuan; Ying Wang; Lei Zhang; Huawei Li; Xiaowei Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

Approximate nearest neighbor search (ANNS) is essential for applications like recommendation systems and retrieval-augmented generation (RAG), but is highly I/O-intensive and memory-demanding. CPUs face I/O bottlenecks, while GPUs are constrained by limited memory. DRAM-based Processing-in-Memory (DRAM-PIM) offers a promising alternative by providing high bandwidth, large memory capacity, and near-data computation. This work introduces DRIM-ANN, the first optimized ANNS engine leveraging UPMEM’s DRAM-PIM. While UPMEM scales memory bandwidth and capacity, it suffers from low computing power because of the limited processor embedded in each DRAM bank. To address this, we systematically optimize ANNS approximation configurations and replace expensive squaring operations with lookup tables to align the computing requirements with UPMEM’s architecture. Additionally, we propose load-balancing and I/O optimization strategies to maximize parallel processing efficiency. Experimental results sho

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
