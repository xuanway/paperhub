---
title: "DPAR: High-Performance, Secure, and Scalable Differential Privacy-Based AllReduce"
description: "SC 2025 · Collective Operations and Communication · Hao Qi; Weicong Chen; Chenghong Wang; Xiaoyi Lu"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# DPAR: High-Performance, Secure, and Scalable Differential Privacy-Based AllReduce

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Hao Qi; Weicong Chen; Chenghong Wang; Xiaoyi Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Secure, efficient, and scalable AllReduce-based data aggregation is essential for artificial intelligence (AI) and scientific applications on modern high performance computing (HPC) and cloud infrastructures. As AllReduce is increasingly used across these distributed infrastructures, privacy has become a critical concern. State-of-the-art (SOTA) homomorphic encryption (HE)-based AllReduce solutions introduce high overhead, require secure key exchanges, and remain vulnerable to collusion. We propose DPAR, the first differentially private, collusion-resistant AllReduce framework optimized for large-scale HPC and AI workloads. DPAR introduces three key innovations: integrating differential privacy (DP) to eliminate collusion risks without key exchanges, scalable noise growth to preserve accuracy, and performance optimizations using a noise pooling mechanism. DPAR is a drop-in Message Passing Interface (MPI) AllReduce replacement, providing strong privacy with minimal performance cost. Eva

---

## 一句话总结

> 该工作属于 Collective Operations and Communication 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Collective Operations and Communication 领域贡献新的设计范式或评估框架。
