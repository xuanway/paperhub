---
title: "DRIM-ANN: An Approximate Nearest Neighbor Search Engine Based on Commercial DRAM-PIMs"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Mingkai Chen; Tianhua Han; Cheng Liu; Shengwen Liang; Kuai Yu; Lei Dai; Ziming Y"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# DRIM-ANN: An Approximate Nearest Neighbor Search Engine Based on Commercial DRAM-PIMs

**中文标题：** 基于商用 DRAM-PIM 的近似最近邻搜索引擎

**所属 Session：** [Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Mingkai Chen; Tianhua Han; Cheng Liu; Shengwen Liang; Kuai Yu; Lei Dai; Ziming Yuan; Ying Wang; Lei Zhang; Huawei Li; Xiaowei Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap289&sess=sess163)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Approximate nearest neighbor search (ANNS) is essential for applications like recommendation systems and retrieval-augmented generation (RAG), but is highly I/O-intensive and memory-demanding. CPUs face I/O bottlenecks, while GPUs are constrained by limited memory. DRAM-based Processing-in-Memory (DRAM-PIM) offers a promising alternative by providing high bandwidth, large memory capacity, and near-data computation. This work introduces DRIM-ANN, the first optimized ANNS engine leveraging UPMEM’s DRAM-PIM. While UPMEM scales memory bandwidth and capacity, it suffers from low computing power because of the limited processor embedded in each DRAM bank. To address this, we systematically optimize ANNS approximation configurations and replace expensive squaring operations with lookup tables to align the computing requirements with UPMEM’s architecture. Additionally, we propose load-balancing and I/O optimization strategies to maximize parallel processing efficiency. Experimental results sho

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
