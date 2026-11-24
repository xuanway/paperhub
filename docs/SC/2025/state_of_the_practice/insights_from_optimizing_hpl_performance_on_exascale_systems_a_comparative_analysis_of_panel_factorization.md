---
title: "Insights from Optimizing HPL Performance on Exascale Systems: A Comparative Analysis of Panel Factorization"
description: "SC 2025 · State of the Practice · Hao Lu; Michael Matheson; Noel Chalmers; Aditya Kashi; Nicholas Malaya; Feiyi Wa"
tags:
  - "SC2025"
  - "State of the Practice"
---

# Insights from Optimizing HPL Performance on Exascale Systems: A Comparative Analysis of Panel Factorization

**中文标题：** 优化百亿亿次系统 HPL 性能的经验：面板分解比较分析

**所属 Session：** [State of the Practice](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：State of the Practice。</p>
<p class="paper-seo-summary__tags">SC 2025 · State of the Practice</p>
</div>

**作者**：Hao Lu; Michael Matheson; Noel Chalmers; Aditya Kashi; Nicholas Malaya; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap759&sess=sess301)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

High Performance LINPACK (HPL) remains the primary benchmark for evaluating supercomputing performance. It includes many parts with substantial internal complexity, and its performance is affected by a large number of parameters that interact in ways that are difficult to predict on large-scale heterogeneous supercomputer systems. We present a comprehensive performance analysis of HPL on Frontier, the world's first exascale supercomputer, which achieved HPL performance of 1.35 exaflops. Through empirical parameter tuning, detailed modeling, and comparative evaluation, we uncover critical performance insights, share lessons learned, and outline best practices for effective parameter tuning on exascale systems. We introduce and evaluate two novel PDFACT strategies: a dedicated-thread (DT) variant and a GPU-based variant (GPUPDFACT) implementation using HIP cooperative groups, demonstrating that GPU-based factorization outperforms conventional CPU-based PDFACT on Frontier's architecture.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
