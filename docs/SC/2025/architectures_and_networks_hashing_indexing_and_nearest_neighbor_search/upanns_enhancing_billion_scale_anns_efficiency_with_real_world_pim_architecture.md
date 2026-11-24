---
title: "UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture"
description: "SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search · Sitian Chen; Amelie Chi Zhou; Yucheng Shi; Yusen Li; Xin Yao"
tags:
  - "SC2025"
  - "Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search"
---

# UpANNS: Enhancing Billion-Scale ANNS Efficiency with Real-World PIM Architecture

**中文标题：** 利用真实存内处理架构提高十亿规模近似最近邻搜索效率

**所属 Session：** [Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Hashing, Indexing, and Nearest Neighbor Search</p>
</div>

**作者**：Sitian Chen; Amelie Chi Zhou; Yucheng Shi; Yusen Li; Xin Yao

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap166&sess=sess163)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Approximate Nearest Neighbor Search (ANNS) is a critical component of modern AI systems, such as recommendation engines and retrieval-augmented large language models (RAG-LLMs). However, scaling ANNS to billion-entry datasets exposes critical inefficiencies: CPU-based solutions are bottlenecked by memory bandwidth limitations, while GPU implementations underutilize hardware resources, leading to suboptimal performance and energy consumption. We introduce UpANNS, a novel framework leveraging Processing-in-Memory (PIM) architecture to accelerate billion-scale ANNS. UpANNS integrates four key innovations, including: architecture-aware data placement to minimize latency through workload balancing; dynamic resource management for optimal PIM utilization; co-occurrence optimized encoding to reduce redundant computations; and an early-pruning strategy for efficient top-k selection. Evaluation on commercial UPMEM hardware demonstrates that UpANNS achieves 4.3x higher QPS than CPU-based Faiss,

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
