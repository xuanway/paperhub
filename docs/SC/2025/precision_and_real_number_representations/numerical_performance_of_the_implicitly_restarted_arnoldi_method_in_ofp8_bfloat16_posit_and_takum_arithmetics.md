---
title: "Numerical Performance of the Implicitly Restarted Arnoldi Method in OFP8, Bfloat16, Posit, and Takum Arithmetics"
description: "SC 2025 · Precision and Real Number Representations · Laslo Hunhold; James Quinlan; Stefan Wesner"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# Numerical Performance of the Implicitly Restarted Arnoldi Method in OFP8, Bfloat16, Posit, and Takum Arithmetics

**中文标题：** 隐式重启 Arnoldi 方法在 OFP8、Bfloat16、Posit 和 Takum 算术中的数值性能

**所属 Session：** [Precision and Real Number Representations](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Laslo Hunhold; James Quinlan; Stefan Wesner

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap518&sess=sess304)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The computation of select eigenvalues and eigenvectors of large, sparse matrices is fundamental to a wide range of applications. Accordingly, evaluating the numerical performance of emerging alternatives to the IEEE 754 floating-point standard, such as OFP8 (E4M3 and E5M2), bfloat16, and the tapered-precision posit and takum formats, is of significant interest. Among the most widely used methods for this task is the implicitly restarted Arnoldi method, as implemented in ARPACK. This paper presents a comprehensive and untailored evaluation based on two real-world datasets: the SuiteSparse Matrix Collection, which includes matrices of varying sizes and condition numbers, and the Network Repository, a large collection of graphs from practical applications. The results demonstrate that the tapered-precision posit and takum formats provide improved numerical performance, with takum arithmetic avoiding several weaknesses observed in posits. While bfloat16 performs consistently better than fl

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
