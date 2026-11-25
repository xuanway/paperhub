---
title: "FlashSparse: Minimizing Computation Redundancy for Fast Sparse Matrix Multiplications on Tensor Cores"
description: "PPoPP 2025 Session 8（Tensor Cores）：swap-and-transpose 最小化稀疏粒度，几何平均 5.5× 加速"
tags:
  - "PPoPP2025"
  - "Session-8"
  - "Tensor Cores"
  - "Sparse Matrix Multiplication"
  - "SpMM"
authors:
  - "Jinliang Shi"
  - "Shigang Li"
  - "Youxuan Xu"
  - "Rongtian Fu"
  - "Xueying Wang"
  - "Tong Wu"
session: "Session 8: Tensor Cores"
session_number: 8
session_chair: "Jeffrey Vetter"
date: "2025-03-04"
time: "14:00–14:20"
room: "Acacia D"
doi: "10.1145/3710848.3710858"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# FlashSparse: Minimizing Computation Redundancy for Fast Sparse Matrix Multiplications on Tensor Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FlashSparse，通过 swap-and-transpose 矩阵乘策略把 TCU 上的稀疏粒度降到最小，在减少计算冗余的同时充分利用张量核算力。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 8: Tensor Cores</p>
</div>

**作者**：Jinliang Shi, Shigang Li, Youxuan Xu, Rongtian Fu, Xueying Wang, Tong Wu (Beijing University of Posts and Telecommunications)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 14:00–14:20 · Session 8: Tensor Cores（主席：Jeffrey Vetter）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710858) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 FlashSparse，通过 swap-and-transpose 矩阵乘策略把 TCU 上的稀疏粒度降到最小，在减少计算冗余的同时充分利用张量核算力。

## 研究问题

SpMM 与 SDDMM 是科学与深度学习中的重要稀疏算子，但非结构化稀疏数据的不规则性使它们难以在 Tensor Core 上获得实际加速。

## 方法简述

- 提出 swap-and-transpose 矩阵乘策略，最小化 SpMM 与 SDDMM 在 TCU 上的稀疏粒度。
- 设计内存高效的线程映射策略，实现合并访存。
- 采用稀疏矩阵存储格式以降低内存占用。

## 主要结果

- 在 H100 与 RTX 4090 上刷新稀疏矩阵乘的性能纪录。
- 相比 DTC-SpMM 几何平均加速 5.5×，相比 RoDe 加速 3.22×。

<details>
<summary>原文摘要（英文）</summary>

Sparse Matrix-matrix Multiplication (SpMM) and Sampled Dense-dense Matrix Multiplication (SDDMM) are important sparse operators in scientific computing and deep learning. Tensor Core Units (TCUs) enhance modern accelerators with superior computing power, which is promising to boost the performance of matrix operators to a higher level. However, due to the irregularity of unstructured sparse data, it is difficult to deliver practical speedups on TCUs. To this end, we propose FlashSparse, a novel approach to bridge the gap between sparse workloads and the TCU architecture. Specifically, FlashSparse minimizes the sparse granularity for SpMM and SDDMM on TCUs through a novel swap-and-transpose matrix multiplication strategy. Benefiting from the minimum sparse granularity, the computation redundancy is remarkably reduced while the computing power of TCUs is fully utilized. Besides, FlashSparse is equipped with a memory-efficient thread mapping strategy for coalesced data access and a sparse matrix storage format to save memory footprint. Extensive experimental results on H100 and RTX 4090 GPUs show that FlashSparse sets a new state-of-the-art for sparse matrix multiplications (geometric mean 5.5x speedup over DTC-SpMM and 3.22x speedup over RoDe). This work is licensed under.

</details>

---

> 所属 Session：[Session 8: Tensor Cores](index.md) · 返回 [PPoPP 2025 总览](../index.md)
