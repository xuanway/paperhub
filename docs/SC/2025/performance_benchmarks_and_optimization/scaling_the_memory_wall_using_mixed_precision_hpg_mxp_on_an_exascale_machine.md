---
title: "Scaling the Memory Wall Using Mixed-Precision — HPG-MxP on an Exascale Machine"
description: "SC 2025 · Performance: Benchmarks and Optimization · Aditya Kashi; Nicholson Koukpaizan; Hao Lu; Michael Matheson; Sarp Oral; Feiyi W"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# Scaling the Memory Wall Using Mixed-Precision — HPG-MxP on an Exascale Machine

**中文标题：** 利用混合精度攀越内存墙：百亿亿次机器上的 HPG-MxP

**所属 Session：** [Performance: Benchmarks and Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Aditya Kashi; Nicholson Koukpaizan; Hao Lu; Michael Matheson; Sarp Oral; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap769&sess=sess184)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Mixed-precision algorithms have been proposed as a way for scientific computing to benefit from some of the gains seen for AI on recent high performance computing (HPC) platforms. A few applications dominated by dense matrix operations have seen substantial speedups by utilizing low-precision formats such as FP16. However, a majority of scientific simulation applications are memory bandwidth limited. Beyond preliminary studies, the practical gain from using mixed-precision algorithms on a given HPC system is largely unclear. The High Performance GMRES Mixed Precision (HPG-MxP) benchmark has been proposed to measure the useful performance of an HPC system on sparse matrix-based mixed-precision applications. In this work, we present a highly optimized implementation of the HPG-MxP benchmark for an exascale system and describe our algorithm enhancements. We show for the first time a speedup of 1.6x using a combination of double and single precision on modern GPU-based supercomputers.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
