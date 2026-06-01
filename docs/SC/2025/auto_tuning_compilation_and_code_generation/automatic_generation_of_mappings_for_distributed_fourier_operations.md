---
title: "Automatic Generation of Mappings for Distributed Fourier Operations"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Doru Thom Popovici; Botao Wu; John Shalf; Martin Kong"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# Automatic Generation of Mappings for Distributed Fourier Operations

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Doru Thom Popovici; Botao Wu; John Shalf; Martin Kong

**会议**：SC 2025 · St. Louis, MO

## 摘要

The Fourier transform is an ubiquitous mathematical operation used in a multitude of scientific applications. Most distributed Fourier transform libraries provide rigid implementations that force developers of high performance applications to mold their code around the Fourier computation, omitting opportunities for minimizing communication across the Fourier transforms and the surrounding computation. In this work, we introduce a new automatic approach to generate distributed mappings for multi-dimensional Fourier operations, offering a solution to this problem. Our approach decides how to decompose, map, and schedule the computation as smaller and lower-dimensional parallel operations. We design and implement a novel non-linear iterative formulation that optimizes across Fourier and linear algebra operations. Our scheme leverages the Z3 SMT solver to minimize the number of communication steps across key MPI collectives, while selecting the grid shape. We evaluate the effectiveness of

---

## 一句话总结

> 该工作属于 Auto-Tuning, Compilation, and Code Generation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Auto-Tuning, Compilation, and Code Generation 领域贡献新的设计范式或评估框架。
