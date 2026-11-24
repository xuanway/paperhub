---
title: "SIGMo: High-Throughput Batched Subgraph Isomorphism on GPUs for Molecular Matching"
description: "SC 2025 · Graph Processing and Pattern Matching · Antonio De Caro; Gennaro Cordasco; Federico Ficarelli; Biagio Cosenza"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# SIGMo: High-Throughput Batched Subgraph Isomorphism on GPUs for Molecular Matching

**中文标题：** 面向分子匹配的 GPU 高吞吐批量子图同构

**所属 Session：** [Graph Processing and Pattern Matching](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Antonio De Caro; Gennaro Cordasco; Federico Ficarelli; Biagio Cosenza

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap173&sess=sess180)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Subgraph isomorphism is a fundamental graph problem with applications in diverse domains. Of particular interest is molecular matching, which uses a subgraph isomorphism formulation for the drug discovery process. While subgraph isomorphism is known to be NP-complete, in molecular matching a number of domain constraints allow for efficient implementations. This paper presents SIGMo, a high-throughput, portable subgraph isomorphism framework for GPUs, specifically designed for batch molecular matching. SIGMo takes advantage of the specific domain formulation to provide a more efficient filter-and-join strategy: the framework introduces a novel multi-level iterative filtering technique based on neighborhood signature encoding to efficiently prune candidates before the join phase. SIGMo is written in SYCL, allowing portable execution on AMD, Intel, and NVIDIA GPUs. Our experimental evaluation on a large dataset from ZINC demonstrates up to 1,470x speedup over state-of-the-art frameworks,

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
