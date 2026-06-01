---
title: "MetoHash: A Memory-Efficient and Traffic-Optimized Hashing Index on Hybrid PMem-DRAM Memories"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Zixiang Yu; Guangyang Deng; Zhirong Shen; Qiangsheng Su; Ronglong Wu; Xiaoli Wan"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# MetoHash: A Memory-Efficient and Traffic-Optimized Hashing Index on Hybrid PMem-DRAM Memories

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Zixiang Yu; Guangyang Deng; Zhirong Shen; Qiangsheng Su; Ronglong Wu; Xiaoli Wang; Quanqing Xu; Chuanhui Yang; Zhifeng Bao

**会议**：SC 2025 · St. Louis, MO

## 摘要

Persistent memory (PMem) brings new design considerations in realizing high-performance and scalable hashing indexes. We uncover that existing hashing indexes for PMem still suffer from traffic amplification and memory inefficiency. We present MetoHash, a memory-efficient and traffic-optimized hashing index on hybrid PMem-DRAM memories. MetoHash proposes a three-layer index structure spanning across CPU caches, DRAM, and PMem for data management. It aggregates the incoming key-value items in CPU caches for fast inserts, which are then arranged in DRAM and flushed to PMem, to eliminate traffic amplification. MetoHash also uses fingerprinting to reduce unnecessary probings over PMem and removes duplicate items during bucket relocations. We implement MetoHash on PMem with persistent and volatile CPU caches, and show that compared to state-of-the-art hashing indexes for PMem, MetoHash improves the throughput by 86.1%–257.6% under various workloads.

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
