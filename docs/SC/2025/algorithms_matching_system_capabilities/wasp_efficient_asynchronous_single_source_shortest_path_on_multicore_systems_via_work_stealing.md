---
title: "Wasp: Efficient Asynchronous Single-Source Shortest Path on Multicore Systems via Work Stealing"
description: "SC 2025 · Algorithms: Matching System Capabilities · Marco D'Antonio; Thai Son Mai; Philippas Tsigas; Hans Vandierendonck"
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# Wasp: Efficient Asynchronous Single-Source Shortest Path on Multicore Systems via Work Stealing

**中文标题：** 利用工作窃取在多核系统上高效异步求解单源最短路径

**所属 Session：** [Algorithms: Matching System Capabilities](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Marco D'Antonio; Thai Son Mai; Philippas Tsigas; Hans Vandierendonck

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap734&sess=sess307)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The Single-Source Shortest Path (SSSP) problem is a fundamental graph problem with an extensive set of real-world applications. State-of-the-art parallel algorithms for SSSP, such as the ∆-stepping algorithm, create parallelism through priority coarsening. Priority coarsening results in redundant computations that diminish the benefits of parallelization and limit parallel scalability. This paper introduces Wasp, a novel SSSP algorithm that reduces parallelism-induced redundant work by utilizing asynchrony and an efficient priority-aware work stealing scheme. Contrary to previous work, Wasp introduces redundant computations only when threads have no high-priority work locally available to execute. This is achieved by a novel priority-aware work stealing mechanism that controls the inefficiencies of indiscriminate priority coarsening. Experimental evaluation shows competitive or better performance compared to GAP, GBBS, MultiQueues, Galois, ∆*-stepping, and ρ-stepping on 13 diverse grap

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
