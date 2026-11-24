---
title: "DPAR: High-Performance, Secure, and Scalable Differential Privacy-Based AllReduce"
description: "SC 2025 · Collective Operations and Communication · Hao Qi; Weicong Chen; Chenghong Wang; Xiaoyi Lu"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# DPAR: High-Performance, Secure, and Scalable Differential Privacy-Based AllReduce

**中文标题：** 高性能、安全且可扩展的基于差分隐私的全归约

**所属 Session：** [Collective Operations and Communication](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Hao Qi; Weicong Chen; Chenghong Wang; Xiaoyi Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap458&sess=sess296)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Secure, efficient, and scalable AllReduce-based data aggregation is essential for artificial intelligence (AI) and scientific applications on modern high performance computing (HPC) and cloud infrastructures. As AllReduce is increasingly used across these distributed infrastructures, privacy has become a critical concern. State-of-the-art (SOTA) homomorphic encryption (HE)-based AllReduce solutions introduce high overhead, require secure key exchanges, and remain vulnerable to collusion. We propose DPAR, the first differentially private, collusion-resistant AllReduce framework optimized for large-scale HPC and AI workloads. DPAR introduces three key innovations: integrating differential privacy (DP) to eliminate collusion risks without key exchanges, scalable noise growth to preserve accuracy, and performance optimizations using a noise pooling mechanism. DPAR is a drop-in Message Passing Interface (MPI) AllReduce replacement, providing strong privacy with minimal performance cost. Eva

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
