---
title: "Towards Singular Value Decomposition for Rank-Deficient Matrices: An Efficient and Accurate Algorithm on GPU Architectures"
description: "PPoPP 2026 Session 13（Matrix and Linear Algebra Algorithms）：秩揭示 QB 分解的秩亏 SVD，较 cuSOLVER 满 SVD 最高 6978×"
tags:
  - "PPoPP2026"
  - "Session-13"
  - "Matrix and Linear Algebra Algorithms"
  - "SVD"
  - "GPU"
  - "Mixed Precision"
authors:
  - "Lu Shi"
  - "WeiWei Xu"
  - "Shaoshuai Zhang"
session: "Session 13: Matrix and Linear Algebra Algorithms"
session_number: 13
session_chair: "William S. Moses"
date: "2026-02-04"
time: "09:50–10:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786427"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Towards Singular Value Decomposition for Rank-Deficient Matrices: An Efficient and Accurate Algorithm on GPU Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向秩亏矩阵的 GPU SVD 算法，基于秩揭示 QB 分解并用 Householder QB 与混合精度保证精度，较 cuSOLVER 满 SVD 加速 6978.71×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 13: Matrix and Linear Algebra Algorithms</p>
</div>

**作者**：Lu Shi, WeiWei Xu, and Shaoshuai Zhang — University of Electronic Science and Technology of China, China; Nanjing University of Information Science and Technology, China

**会议**：PPoPP 2026 · 2026 年 2 月 4 日 09:50–10:10 · Session 13: Matrix and Linear Algebra Algorithms（主席：William S. Moses）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786427) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Singular Value Decomposition (SVD) is a fundamental tool in numerous scientific and engineering domains. Many high-performance libraries, such as LAPACK, MAGMA, and cuSOLVER, provide general, truncated, and randomized SVD routines. However, when the input is a low-rank matrix whose rank is not explicitly known, existing routines usually treat it as full-rank, which leads to suboptimal performance. In this paper, we propose an efficient SVD algorithm specifically for rank-deficient matrices based on a recently proposed rank-revealing QR factorization, termed QB factorization. To further enhance numerical stability and efficiency, we introduce a Householder QB factorization and a mixed-precision SVD algorithm, accompanied by a rigorous error analysis demonstrating correctness and stability. Experimental results show that our method achieves up to 6978.71x speedup over the general (full) SVD routine in cuSOLVER and is 9.99x faster than randomized SVD in FP32 precision. Moreover, our method exhibits higher numerical accuracy than cuSOLVER full SVD, achieving substantially smaller backward errors while maintaining stable and reliable singular values. Beyond synthetic benchmarks, we also demonstrate its effectiveness in an image compression application with higher efficiency.

## 中文摘要

奇异值分解（SVD）是众多科学与工程领域的基础工具。许多高性能库（如 LAPACK、MAGMA 和 cuSOLVER）提供通用、截断与随机化 SVD 例程。然而，当输入是秩未被显式给出的低秩矩阵时，现有例程通常将其视为满秩，从而导致性能次优。本文基于近期提出的一种秩揭示 QR 分解——称为 QB 分解——提出一种专为秩亏矩阵设计的高效 SVD 算法。为进一步提升数值稳定性与效率，我们引入 Householder QB 分解与混合精度 SVD 算法，并给出严格的误差分析以证明其正确性与稳定性。实验结果表明，我们的方法相对 cuSOLVER 中的通用（满）SVD 例程最高取得 6978.71× 的加速，在 FP32 精度下比随机化 SVD 快 9.99×。此外，我们的方法具有比 cuSOLVER 满 SVD 更高的数值精度，在保持奇异值稳定可靠的同时取得显著更小的后向误差。除合成基准测试之外，我们还在图像压缩应用中展示了其有效性，且效率更高。

## 英文关键词

Singular Value Decomposition, GPGPU, Numerical Linear Algebra, HPC, Matrix Computation

## 中文关键词

奇异值分解；GPGPU；数值线性代数；HPC；矩阵计算

---

## 一句话总结

> 提出面向秩亏矩阵的 GPU SVD 算法，基于秩揭示 QB 分解并用 Householder QB 与混合精度保证精度，较 cuSOLVER 满 SVD 加速 6978.71×。

## 研究问题

当输入是秩未知的低秩矩阵时，LAPACK、MAGMA、cuSOLVER 等现有 SVD 例程通常按满秩处理，导致性能次优。

## 方法简述

- 提出面向秩亏矩阵的高效 GPU SVD 算法，构建在近期提出的秩揭示 QR 分解（QB 分解）之上。
- 引入 Householder QB 分解，以进一步提升数值稳定性与效率。
- 设计混合精度 SVD 算法，并给出严格误差分析以证明其正确性与稳定性。

## 主要结果

- 相对 cuSOLVER 通用（满秩）SVD 最高取得 6978.71× 加速；在 FP32 精度下比随机化 SVD 快 9.99×。
- 数值精度高于 cuSOLVER 满秩 SVD，反向误差显著更小，奇异值稳定可靠。
- 在图像压缩应用中同样表现出更高效率。

---

> 所属 Session：[Session 13: Matrix and Linear Algebra Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
