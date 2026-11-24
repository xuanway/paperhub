---
title: "High-Performance Branch-Free Algorithms for Extended-Precision Floating-Point Arithmetic"
description: "SC 2025 · Precision and Real Number Representations · David Kai Zhang; Alex Aiken"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# High-Performance Branch-Free Algorithms for Extended-Precision Floating-Point Arithmetic

**中文标题：** 扩展精度浮点算术的高性能无分支算法

**所属 Session：** [Precision and Real Number Representations](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：David Kai Zhang; Alex Aiken

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap766&sess=sess304)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

We present new branch-free algorithms for floating-point arithmetic at double, triple, or quadruple the native machine precision. These algorithms are the fastest known by at least an order of magnitude and are conjectured to be optimal, not only in an asymptotic sense, but in their exact FLOP count and circuit depth. Unlike previous algorithms, which either use complex branching logic or are only correct on specific classes of inputs, our algorithms have computer-verified proofs of correctness for all floating-point inputs within machine overflow and underflow thresholds. Compared to state-of-the-art multiprecision libraries, our algorithms achieve up to 11.7x the peak performance of QD, 34.4x over CAMPARY, 35.6x over MPFR, and 41.4x over FLINT.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
