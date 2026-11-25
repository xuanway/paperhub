---
title: "Fast Kronecker Matrix-Matrix Multiplication on GPUs"
description: "PPoPP 2024 Session Linear Algebra：FastKron 摆脱线性代数算子依赖，单卡最高 40.7×、16 卡 7.85× 加速"
tags:
  - "PPoPP2024"
  - "Session-9"
  - "Linear Algebra"
  - "CUDA"
  - "Kronecker Product"
  - "GPU"
authors:
  - "Abhinav Jangda"
  - "Mohit Yadav"
session: "Session 9: Linear Algebra"
session_number: 9
session_chair: "I-Ting Angelina Lee"
date: "2024-03-06"
time: "10:20–10:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638489"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Fast Kronecker Matrix-Matrix Multiplication on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FastKron，摆脱矩阵乘、转置等已有张量代数算子，为 Kron-Matmul 解锁专属优化，单 GPU 与 16 GPU 上最高分别快 40.7× 与 7.85×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 9: Linear Algebra</p>
</div>

**作者**：Abhinav Jangda (Microsoft Research); Mohit Yadav (University of Massachusetts Amherst)

**会议**：PPoPP 2024 · 2024 年 3 月 6 日 10:20–10:40 · Session 9: Linear Algebra（主席：I-Ting Angelina Lee）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638489) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Kronecker Matrix-Matrix Multiplication (Kron-Matmul) is the multiplication of a matrix with the Kronecker Product of several smaller matrices. Kron-Matmul is a core operation for many scientific and machine learning computations. State-of-the-art Kron-Matmul implementations utilize existing tensor algebra operations, such as matrix multiplication, transpose, and tensor matrix multiplication. However, this design choice prevents several Kron-Matmul specific optimizations, thus, leaving significant performance on the table. To address this issue, we present FastKron, an efficient technique for Kron-Matmul on single and multiple GPUs. FastKron is independent of linear algebra operations enabling several new optimizations for Kron-Matmul. Thus, it performs up to 40.7× and 7.85× faster than existing implementations on 1 and 16 GPUs respectively.

## 中文摘要

Kronecker 矩阵-矩阵乘法（Kron-Matmul）是指一个矩阵与若干较小矩阵的 Kronecker 积相乘。Kron-Matmul 是许多科学与机器学习计算中的核心操作。最先进的 Kron-Matmul 实现利用已有的张量代数操作，例如矩阵乘法、转置和张量矩阵乘法。然而，这一设计选择阻碍了若干 Kron-Matmul 专属优化，因而损失了可观的性能。为解决该问题，我们提出 FastKron，一种在单 GPU 与多 GPU 上高效的 Kron-Matmul 技术。FastKron 不依赖线性代数操作，从而为 Kron-Matmul 带来若干新的优化。因此，它在 1 块和 16 块 GPU 上分别比现有实现最高快 40.7× 和 7.85×。

## 英文关键词

Graphics Processing Units, CUDA, Kronecker Product, Linear Algebra

## 中文关键词

图形处理器；CUDA；Kronecker 积；线性代数

---

## 一句话总结

> 提出 FastKron，摆脱矩阵乘、转置等已有张量代数算子，为 Kron-Matmul 解锁专属优化，单 GPU 与 16 GPU 上最高分别快 40.7× 与 7.85×。

## 研究问题

最先进的 Kron-Matmul 实现基于矩阵乘法、转置、张量矩阵乘法等已有张量代数操作构建，这一设计选择阻碍了若干 Kron-Matmul 专属优化，因而损失了可观的性能。

## 方法简述

- 提出 FastKron，一种独立于线性代数操作的 Kron-Matmul 技术，使多项 Kron-Matmul 专属优化成为可能
- 设计面向单 GPU 与多 GPU 场景的 FastKron 实现，覆盖单卡与 16 卡部署

## 主要结果

- 在 1 块 GPU 上，FastKron 比现有实现最高快 40.7×
- 在 16 块 GPU 上，FastKron 比现有实现最高快 7.85×

---

> 所属 Session：[Session 9: Linear Algebra](index.md) · 返回 [PPoPP 2024 总览](../index.md)
