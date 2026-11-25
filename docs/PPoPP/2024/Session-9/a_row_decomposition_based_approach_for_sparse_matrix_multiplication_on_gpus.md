---
title: "A Row Decomposition-based Approach for Sparse Matrix Multiplication on GPUs"
description: "PPoPP 2024 Session Linear Algebra：RoDe 按行拆分规则/残差部分，SpMM 几何平均提速 1.45×，预处理开销仅 16%"
tags:
  - "PPoPP2024"
  - "Session-9"
  - "Linear Algebra"
  - "SpMM"
  - "SDDMM"
  - "GPU"
authors:
  - "Meng Pang"
  - "Xiang Fei"
  - "Peng Qu"
  - "Youhui Zhang"
  - "Zhaolin Li"
session: "Session 9: Linear Algebra"
session_number: 9
session_chair: "I-Ting Angelina Lee"
date: "2024-03-06"
time: "10:00–10:20"
room: "Moorfoot"
doi: "10.1145/3627535.3638470"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# A Row Decomposition-based Approach for Sparse Matrix Multiplication on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出按行分解（RoDe）方法，将 CSR 稀疏矩阵行拆为规则与残差部分分别优化，配合负载均衡与细粒度流水线，SpMM 与 SDDMM 几何平均提速 1.45× 与 1.49×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 9: Linear Algebra</p>
</div>

**作者**：Meng Pang, Xiang Fei, Peng Qu, Youhui Zhang, Zhaolin Li (Department of Computer Science and Technology, Tsinghua University)

**会议**：PPoPP 2024 · 2024 年 3 月 6 日 10:00–10:20 · Session 9: Linear Algebra（主席：I-Ting Angelina Lee）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638470) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Sparse-Matrix Dense-Matrix Multiplication (SpMM) and Sampled Dense Dense Matrix Multiplication (SDDMM) are important sparse kernels in various computation domains. The uneven distribution of nonzeros in the sparse matrix and the tight data dependence between sparse and dense matrices make it a challenge to run sparse matrix multiplication efficiently on GPUs. By analyzing the aforementioned problems, we propose a row decomposition (RoDe)-based approach to optimize the two kernels on GPUs, using the standard Compressed Sparse Row (CSR) format. Specifically, RoDe divides the sparse matrix rows into regular parts and residual parts, to fully optimize their computations separately. We also devise the corresponding load balancing and fine-grained pipelining technologies. Profiling results show that RoDe can achieve more efficient memory access and reduce warp stall cycles significantly. Compared to the state-of-the-art (SOTA) alternatives, RoDe achieves a speedup of up to 7.86× with a geometric mean of 1.45× for SpMM, and a speedup of up to 8.99× with a geometric mean of 1.49× for SDDMM; the dataset is SuiteSparse. RoDe also outperforms its counterpart in the deep learning dataset. Furthermore, its preprocessing overhead is significantly smaller, averaging only 16% of the SOTA.

## 中文摘要

稀疏-稠密矩阵乘法（SpMM）与采样稠密-稠密矩阵乘法（SDDMM）是诸多计算领域中的重要稀疏内核。稀疏矩阵中非零元分布不均，以及稀疏矩阵与稠密矩阵之间紧密的数据依赖，使得在 GPU 上高效运行稀疏矩阵乘法成为一项挑战。通过分析上述问题，我们提出一种基于行分解（RoDe）的方法，在标准压缩稀疏行（CSR）格式下对这两个内核进行 GPU 优化。具体而言，RoDe 将稀疏矩阵的行划分为规则部分与残差部分，以便分别对其计算进行充分优化。我们还设计了相应的负载均衡与细粒度流水线技术。性能剖析结果表明，RoDe 能够实现更高效的访存并显著减少 warp 停顿周期。与最先进（SOTA）的对比方案相比，RoDe 在 SpMM 上最高取得 7.86× 加速、几何平均 1.45×，在 SDDMM 上最高取得 8.99× 加速、几何平均 1.49×；数据集为 SuiteSparse。RoDe 在深度学习数据集上同样优于其对比方案。此外，其预处理开销显著更小，平均仅为 SOTA 的 16%。

## 英文关键词

Sparse Matrices, SpMM, SDDMM, GPU

## 中文关键词

稀疏矩阵；SpMM；SDDMM；GPU

---

## 一句话总结

> 提出按行分解（RoDe）方法，将 CSR 稀疏矩阵行拆为规则与残差部分分别优化，配合负载均衡与细粒度流水线，SpMM 与 SDDMM 几何平均提速 1.45× 与 1.49×。

## 研究问题

稀疏矩阵中非零元分布不均，且稀疏矩阵与稠密矩阵之间存在紧密的数据依赖，使得稀疏矩阵乘法难以在 GPU 上高效运行；现有方法未针对这种不规则性对计算分别优化。

## 方法简述

- 提出按行分解（RoDe）方法，在标准 CSR 格式下将稀疏矩阵的行划分为规则部分与残差部分，对两部分计算分别进行充分优化
- 设计相应的负载均衡技术，缓解非零元分布不均导致的线程工作量失衡
- 设计细粒度流水线技术，掩盖稀疏矩阵与稠密矩阵之间紧密数据依赖造成的访存停顿

## 主要结果

- 在 SuiteSparse 数据集上，SpMM 相比最先进方案最高加速 7.86×，几何平均 1.45×
- SDDMM 最高加速 8.99×，几何平均 1.49×
- 在深度学习数据集上同样优于对比方案，且预处理开销显著更小，平均仅为 SOTA 的 16%

---

> 所属 Session：[Session 9: Linear Algebra](index.md) · 返回 [PPoPP 2024 总览](../index.md)
