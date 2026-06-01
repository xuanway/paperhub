---
title: "SIGMo: High-Throughput Batched Subgraph Isomorphism on GPUs for Molecular Matching"
description: "SC 2025 · Graph Processing and Pattern Matching · Antonio De Caro; Gennaro Cordasco; Federico Ficarelli; Biagio Cosenza"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# SIGMo: High-Throughput Batched Subgraph Isomorphism on GPUs for Molecular Matching

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Antonio De Caro; Gennaro Cordasco; Federico Ficarelli; Biagio Cosenza

**会议**：SC 2025 · St. Louis, MO

## 摘要

Subgraph isomorphism is a fundamental graph problem with applications in diverse domains. Of particular interest is molecular matching, which uses a subgraph isomorphism formulation for the drug discovery process. While subgraph isomorphism is known to be NP-complete, in molecular matching a number of domain constraints allow for efficient implementations. This paper presents SIGMo, a high-throughput, portable subgraph isomorphism framework for GPUs, specifically designed for batch molecular matching. SIGMo takes advantage of the specific domain formulation to provide a more efficient filter-and-join strategy: the framework introduces a novel multi-level iterative filtering technique based on neighborhood signature encoding to efficiently prune candidates before the join phase. SIGMo is written in SYCL, allowing portable execution on AMD, Intel, and NVIDIA GPUs. Our experimental evaluation on a large dataset from ZINC demonstrates up to 1,470x speedup over state-of-the-art frameworks, 

---

## 一句话总结

> 该工作属于 Graph Processing and Pattern Matching 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Graph Processing and Pattern Matching 领域贡献新的设计范式或评估框架。
