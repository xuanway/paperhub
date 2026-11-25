---
title: "Session 9: Linear Algebra"
description: "PPoPP 2024 Session 9（Linear Algebra），2024 年 3 月 6 日 10:00–11:00，Moorfoot，共 3 篇论文。"
tags:
  - "PPoPP2024"
  - "Session-9"
  - "Linear Algebra"
---

# Session 9: Linear Algebra

**PPoPP 2024 · 2024 年 3 月 6 日 10:00–11:00 · Moorfoot · Session Chair：I-Ting Angelina Lee**

围绕线性代数：GPU 上 SpMM/SDDMM 的行分解方法、Kronecker 矩阵乘，以及面向通信效率的 Arrow 矩阵分解。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2024 Main Conference Papers](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [A Row Decomposition-based Approach for Sparse Matrix Multiplication on GPUs](a_row_decomposition_based_approach_for_sparse_matrix_multiplication_on_gpus.md) | Meng Pang 等 5 人 | RoDe 按行拆分规则/残差部分，SpMM 几何平均提速 1.45×，预处理开销仅 16% |
| 2 | [Fast Kronecker Matrix-Matrix Multiplication on GPUs](fast_kronecker_matrix_matrix_multiplication_on_gpus.md) | Abhinav Jangda 等 2 人 | FastKron 摆脱线性代数算子依赖，单卡最高 40.7×、16 卡 7.85× 加速 |
| 3 | [Arrow Matrix Decomposition: A Novel Approach for Communication-Efficient Sparse Matrix Multiplication](arrow_matrix_decomposition_a_novel_approach_for_communication_efficient_sparse_matrix_multiplication.md) | Lukas Gianinazzi 等 12 人 | 箭头矩阵分解实现通信规避 SpMM，亿级行矩阵上近线性强弱扩展 |

---

[← Session 8: Optimizing for Memory](../Session-8/index.md) · [PPoPP 2024 总览](../index.md) · [Session 10: Applications →](../Session-10/index.md)
