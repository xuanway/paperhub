---
title: "A Nested Krylov Method Using Half-Precision Arithmetic"
description: "SC 2025 · Precision and Real Number Representations · Kengo Suzuki; Takeshi Iwashita"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# A Nested Krylov Method Using Half-Precision Arithmetic

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Kengo Suzuki; Takeshi Iwashita

**会议**：SC 2025 · St. Louis, MO

## 摘要

Low-precision computing is essential for efficiently utilizing memory bandwidth and computing cores. While many mixed-precision algorithms have been developed for iterative sparse linear solvers, effectively leveraging half-precision (fp16) arithmetic remains challenging. This study introduces a novel nested Krylov approach that integrates the flexible GMRES and Richardson methods in a deeply nested structure, progressively reducing precision from double-precision to fp16 toward the innermost solver. To avoid meaningless computations beyond precision limits, the low-precision inner solvers perform only a few iterations per invocation, while the nested structure ensures their frequent execution. Numerical experiments show that incorporating fp16 into the approach directly enhances solver performance without compromising convergence, achieving speedups of up to 2.42 and 1.65 over double-precision and double-single mixed-precision implementations, respectively. Furthermore, the proposed m

---

## 一句话总结

> 该工作属于 Precision and Real Number Representations 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Precision and Real Number Representations 领域贡献新的设计范式或评估框架。
