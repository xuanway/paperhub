---
title: "Uni-STC: Unified Sparse Tensor Core"
description: "HPCA 2026 · Domain Specific Accelerators"
tags:
  - "HPCA2026"
  - "Domain Specific Accelerators"
---

# Uni-STC: Unified Sparse Tensor Core

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Domain Specific Accelerators。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Domain Specific Accelerators</p>
</div>

**论文链接**：
**作者**：Haocheng Lian China University of Petroleum-Beijing , Qiyue Zhang China University of Petroleum-Beijing , Xinran Zhao China University of Petroleum-Beijing , Meichen Dong China University of Petroleum-Beijing , Yijie Nie China University of Petroleum-Beijing , Zhengyi Zhao China University of Petroleum-Beijing , Junzhong Shen National University of Defense Technology , Wei Guo National University of Defense Technology , Chun Huang National University of Defense Technology , Bingcai Sui National University of Defense Technology , Weifeng Liu China University of Petroleum-Beijing
**会议**：HPCA 2026

---

## 中文标题

Uni-STC：统一稀疏张量核心

## 英文摘要

Modern processors are increasingly adopting tensor cores as key computational units. Compared to existing designs for dense and structured sparsity, recent dual-side sparse tensor cores have evolved to support general sparsity. However, existing methods still face limitations on generality (incomplete sparse kernel support prevents broad applicability) and performance (outer-product/row-row schemes yield unsatisfactory hardware utilisation, data reuse, and energy efficiency). In this paper, we propose Uni-STC, a unified sparse tensor core that delivers high-performance dataflows for four key sparse kernels: sparse matrix-vector multiplication (SpMV), sparse matrix-sparse vector multiplication (SpMSpV), sparse matrix-multiple vector multiplication (SpMM), and sparse general matrix-matrix multiplication (SpGEMM). To efficiently support these diverse sparse workloads, we first introduce BBC, a unified sparse format co-designed with Uni-STC’s dataflow. We then design Uni-STC’s architecture supporting (1) fine-grained task partitioning to improve resource utilisation, (2) parallel sparse-tile processing to enhance data reuse, and (3) a dynamic network to reduce intermediate data movement and energy consumption. Evaluated across 2893 SuiteSparse and 302 DLMC matrices, Uni-STC demonstrates significant improvements, outperforming the state-of-the-art RM-STC with a 2.21× geomean speedup and 2.96× higher energy efficiency.

## 中文摘要

现代处理器正日益采用张量核心作为关键计算单元。与面向稠密与结构化稀疏的现有设计相比，近期的双侧稀疏张量核心已发展到支持通用稀疏性。然而现有方法在通用性（稀疏内核支持不完整，难以广泛适用）与性能（外积与行行方案在硬件利用率、数据复用与能效上不尽人意）方面仍有局限。本文提出 Uni-STC，一个统一稀疏张量核心，为四个关键稀疏内核提供高性能数据流：稀疏矩阵向量乘法（SpMV）、稀疏矩阵稀疏向量乘法（SpMSpV）、稀疏矩阵多向量乘法（SpMM）与稀疏通用矩阵矩阵乘法（SpGEMM）。为高效支持这些多样的稀疏负载，我们首先引入 BBC，一种与 Uni-STC 数据流协同设计的统一稀疏格式；随后设计其架构，支持细粒度任务划分以提升资源利用率、并行稀疏块处理以增强数据复用、以及动态网络以减少中间数据移动与能耗。在 2893 个 SuiteSparse 与 302 个 DLMC 矩阵上的评估表明，Uni-STC 较最先进的 RM-STC 取得 2.21 倍的几何平均加速与 2.96 倍更高的能效。
