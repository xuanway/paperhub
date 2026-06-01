---
title: "High-Performance Branch-Free Algorithms for Extended-Precision Floating-Point Arithmetic"
description: "SC 2025 · Precision and Real Number Representations · David Kai Zhang; Alex Aiken"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# High-Performance Branch-Free Algorithms for Extended-Precision Floating-Point Arithmetic

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：David Kai Zhang; Alex Aiken

**会议**：SC 2025 · St. Louis, MO

## 摘要

We present new branch-free algorithms for floating-point arithmetic at double, triple, or quadruple the native machine precision. These algorithms are the fastest known by at least an order of magnitude and are conjectured to be optimal, not only in an asymptotic sense, but in their exact FLOP count and circuit depth. Unlike previous algorithms, which either use complex branching logic or are only correct on specific classes of inputs, our algorithms have computer-verified proofs of correctness for all floating-point inputs within machine overflow and underflow thresholds. Compared to state-of-the-art multiprecision libraries, our algorithms achieve up to 11.7x the peak performance of QD, 34.4x over CAMPARY, 35.6x over MPFR, and 41.4x over FLINT.

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
