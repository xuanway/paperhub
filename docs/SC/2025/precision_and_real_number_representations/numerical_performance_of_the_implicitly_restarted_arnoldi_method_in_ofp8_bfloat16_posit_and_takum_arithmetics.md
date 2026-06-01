---
title: "Numerical Performance of the Implicitly Restarted Arnoldi Method in OFP8, Bfloat16, Posit, and Takum Arithmetics"
description: "SC 2025 · Precision and Real Number Representations · Laslo Hunhold; James Quinlan; Stefan Wesner"
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# Numerical Performance of the Implicitly Restarted Arnoldi Method in OFP8, Bfloat16, Posit, and Takum Arithmetics

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Laslo Hunhold; James Quinlan; Stefan Wesner

**会议**：SC 2025 · St. Louis, MO

## 摘要

The computation of select eigenvalues and eigenvectors of large, sparse matrices is fundamental to a wide range of applications. Accordingly, evaluating the numerical performance of emerging alternatives to the IEEE 754 floating-point standard, such as OFP8 (E4M3 and E5M2), bfloat16, and the tapered-precision posit and takum formats, is of significant interest. Among the most widely used methods for this task is the implicitly restarted Arnoldi method, as implemented in ARPACK. This paper presents a comprehensive and untailored evaluation based on two real-world datasets: the SuiteSparse Matrix Collection, which includes matrices of varying sizes and condition numbers, and the Network Repository, a large collection of graphs from practical applications. The results demonstrate that the tapered-precision posit and takum formats provide improved numerical performance, with takum arithmetic avoiding several weaknesses observed in posits. While bfloat16 performs consistently better than fl

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
