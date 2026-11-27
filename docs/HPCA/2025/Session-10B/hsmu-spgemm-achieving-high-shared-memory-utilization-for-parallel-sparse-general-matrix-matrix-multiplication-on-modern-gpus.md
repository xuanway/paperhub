---
title: "HSMU-SpGEMM: Achieving High Shared Memory Utilization for Parallel Sparse General Matrix-Matrix Multiplication on Modern GPUs"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# HSMU-SpGEMM: Achieving High Shared Memory Utilization for Parallel Sparse General Matrix-Matrix Multiplication on Modern GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Min Wu (Hunan University), Huizhang Luo (Hunan University), Fenfang Li (Hunan University), Yiran Zhang (Arizona State University), Zhuo Tang (Hunan University), Kenli Li (Hunan University), Jeff Zhang (Arizona State University), Chubo Liu (Hunan University)
**会议**：HPCA 2025

---

## 中文标题

HSMU-SpGEMM：在现代 GPU 上为并行稀疏通用矩阵乘法实现高共享内存利用率

## 英文摘要

Sparse general matrix-matrix multiplication (SpGEMM) is a core primitive for numerous scientific applications. Traditional hash-based approaches fail to strike a balance between reducing hash collisions and efficiently utilizing fast shared memory, which significantly undermines the performance of executing SpGEMM on GPUs. To address this issue, this paper introduces a novel accumulator design that achieves high shared memory utilization on modern GPUs. For the proposed high shared memory utilization algorithm, i.e., HSMU-SpGEMM1, we further optimize different symbolic stages. Our evaluations with four state-of-the-art hash-based SpGEMM libraries (Nsparse, spECK, OpSparse, and NVIDIA’s cuSPARSE) on three NVIDIA GPUs (Ampere, Ada Lovelace, Turing) demonstrate significant performance benefits from HSMU-SpGEMM.

## 中文摘要

稀疏通用矩阵乘法（SpGEMM）是众多科学应用中广泛使用的核心基础算子。传统的基于哈希的方法始终无法在减少哈希冲突与高效利用高速共享内存之间取得平衡，这严重损害了在 GPU 上执行 SpGEMM 时的性能表现。为解决这一问题，本文引入了一种新颖的累加器设计方案，它能够在现代 GPU 上实现很高的共享内存利用率。针对所提出的高共享内存利用率算法，即 HSMU-SpGEMM1，我们还对其不同的符号阶段做了进一步优化。我们在三种 NVIDIA GPU（Ampere、Ada Lovelace 与 Turing）上，将 HSMU-SpGEMM 与四个当前最先进的基于哈希的 SpGEMM 库（Nsparse、spECK、OpSparse 以及 NVIDIA 的 cuSPARSE）进行了对比评测，评测结果表明 HSMU-SpGEMM 能够带来显著的性能收益。
