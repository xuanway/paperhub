---
title: "MetoHash: A Memory-Efficient and Traffic-Optimized Hashing Index on Hybrid PMem-DRAM Memories"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Zixiang Yu; Guangyang Deng; Zhirong Shen; Qiangsheng Su; Ronglong Wu; Xiaoli Wan"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# MetoHash: A Memory-Efficient and Traffic-Optimized Hashing Index on Hybrid PMem-DRAM Memories

**中文标题：** 面向混合持久内存与 DRAM 的内存高效、流量优化哈希索引

**所属 Session：** [Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Zixiang Yu; Guangyang Deng; Zhirong Shen; Qiangsheng Su; Ronglong Wu; Xiaoli Wang; Quanqing Xu; Chuanhui Yang; Zhifeng Bao

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap163&sess=sess163)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Persistent memory (PMem) brings new design considerations in realizing high-performance and scalable hashing indexes. We uncover that existing hashing indexes for PMem still suffer from traffic amplification and memory inefficiency. We present MetoHash, a memory-efficient and traffic-optimized hashing index on hybrid PMem-DRAM memories. MetoHash proposes a three-layer index structure spanning across CPU caches, DRAM, and PMem for data management. It aggregates the incoming key-value items in CPU caches for fast inserts, which are then arranged in DRAM and flushed to PMem, to eliminate traffic amplification. MetoHash also uses fingerprinting to reduce unnecessary probings over PMem and removes duplicate items during bucket relocations. We implement MetoHash on PMem with persistent and volatile CPU caches, and show that compared to state-of-the-art hashing indexes for PMem, MetoHash improves the throughput by 86.1%–257.6% under various workloads.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
