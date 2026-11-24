---
title: "A Nested Krylov Method Using Half-Precision Arithmetic"
description: "SC 2025 · Precision and Real Number Representations · Kengo Suzuki; Takeshi Iwashita"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# A Nested Krylov Method Using Half-Precision Arithmetic

**中文标题：** 使用半精度算术的嵌套 Krylov 方法

**所属 Session：** [Precision and Real Number Representations](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Kengo Suzuki; Takeshi Iwashita

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap310&sess=sess304)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Low-precision computing is essential for efficiently utilizing memory bandwidth and computing cores. While many mixed-precision algorithms have been developed for iterative sparse linear solvers, effectively leveraging half-precision (fp16) arithmetic remains challenging. This study introduces a novel nested Krylov approach that integrates the flexible GMRES and Richardson methods in a deeply nested structure, progressively reducing precision from double-precision to fp16 toward the innermost solver. To avoid meaningless computations beyond precision limits, the low-precision inner solvers perform only a few iterations per invocation, while the nested structure ensures their frequent execution. Numerical experiments show that incorporating fp16 into the approach directly enhances solver performance without compromising convergence, achieving speedups of up to 2.42 and 1.65 over double-precision and double-single mixed-precision implementations, respectively. Furthermore, the proposed m

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
