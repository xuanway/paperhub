---
title: "Automatic Generation of Mappings for Distributed Fourier Operations"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Doru Thom Popovici; Botao Wu; John Shalf; Martin Kong"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# Automatic Generation of Mappings for Distributed Fourier Operations

**中文标题：** 分布式傅里叶运算映射的自动生成

**所属 Session：** [Auto-Tuning, Compilation, and Code Generation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Doru Thom Popovici; Botao Wu; John Shalf; Martin Kong

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap723&sess=sess290)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The Fourier transform is an ubiquitous mathematical operation used in a multitude of scientific applications. Most distributed Fourier transform libraries provide rigid implementations that force developers of high performance applications to mold their code around the Fourier computation, omitting opportunities for minimizing communication across the Fourier transforms and the surrounding computation. In this work, we introduce a new automatic approach to generate distributed mappings for multi-dimensional Fourier operations, offering a solution to this problem. Our approach decides how to decompose, map, and schedule the computation as smaller and lower-dimensional parallel operations. We design and implement a novel non-linear iterative formulation that optimizes across Fourier and linear algebra operations. Our scheme leverages the Z3 SMT solver to minimize the number of communication steps across key MPI collectives, while selecting the grid shape. We evaluate the effectiveness of

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
