---
title: "LiteForm: Lightweight and Automatic Format Composition for Sparse Matrix-Matrix Multiplication on GPUs"
description: "HPDC 2025 · Session 1 — Numerical Methods"
tags:
  - "HPDC2025"
  - "Session 1"
  - "Numerical Methods"
---

# LiteForm: Lightweight and Automatic Format Composition for Sparse Matrix-Matrix Multiplication on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 1</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731574) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/peng.pdf)

**作者**：Zhen Peng, Polykarpos Thomadakis, Jacques Pienaar, Gokcen Kestor

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

Graphics Processing Units (GPUs) have excelled in parallelism and high throughput for dense, regular computations in modern computing. However, sparse computations, such as sparse matrix-matrix multiplication (SpMM), are essential for large-scale, data-intensive applications, where much of the data is inherently sparse. The challenge lies in the sparsity and irregularity of sparse matrices or tensors, which makes achieving high performance on GPU architectures difficult. Consequently, the utilization of suitable sparse data formats is imperative for achieving computational efficiency. Traditional computational libraries often require input in specific formats, which may not accommodate the diversity of matrix characteristics or the varying sparse patterns within a single matrix. While some frameworks support composable formats, they often lack guidance on how to compose these formats effectively or require costly auto-tuning for optimal performance. In this paper, we introduce LiteForm, a novel, lightweight framework designed to automatically compose sparse formats for SpMM computation. We start by presenting CELL, a composable format featuring a three-level blockwise representation that optimizes sparse data for GPUs. LiteForm uses this format and composes it based on the input’s characteristics. First, it employs a lightweight model trained to predict whether the CELL format will yield good performance for a given sparse input matrix. Then LiteForm uses a low-overhead predictor and an SpMM cost model to automatically configure the format according to the characteristics of the input matrix. Our experimental evaluation indicates that LiteForm achieves a geometric mean speedup of 2.06×, 1.81×, 1.77×, and 4.18× in comparison to cuSPARSE, Sputnik, dgSPARSE, and TACO, respectively, and demonstrates speedups of 1.26× and 1.52× over state-of-the-art SparseTIR and STile, respectively.

## 中文摘要

图形处理器（GPU）在现代计算中于稠密、规则计算的并行性与高吞吐方面表现卓越。然而，稀疏矩阵-矩阵乘法（SpMM）等稀疏计算对大规模数据密集型应用至关重要，而这类应用中大量数据本质上是稀疏的。挑战在于稀疏矩阵或张量的稀疏性与不规则性，使得在 GPU 架构上取得高性能十分困难。因此，采用合适的稀疏数据格式是实现计算效率的必要条件。传统计算库往往要求输入为特定格式，难以适应矩阵特征的多样性或单个矩阵内不同的稀疏模式。尽管部分框架支持可组合格式，但通常缺乏如何有效组合的指导，或需要昂贵的自动调优才能达到最优性能。本文提出 LiteForm，一个新颖的轻量级框架，旨在为 SpMM 计算自动组合稀疏格式。我们首先提出 CELL——一种具有三级分块表示的可组合格式，为 GPU 优化稀疏数据。LiteForm 使用该格式，并根据输入特征进行组合。首先，它采用一个训练好的轻量模型，预测 CELL 格式对给定稀疏输入矩阵是否能带来良好性能。随后，LiteForm 使用低开销预测器和 SpMM 代价模型，根据输入矩阵特征自动配置格式。实验评估表明，LiteForm 相比 cuSPARSE、Sputnik、dgSPARSE 和 TACO 分别取得 2.06 倍、1.81 倍、1.77 倍和 4.18 倍的几何平均加速，并相比最先进的 SparseTIR 和 STile 分别取得 1.26 倍和 1.52 倍加速。

## 英文关键词

sparse matrix format, format composition, composable format, SpMM, GPU, machine learning, cost model

## 中文关键词

稀疏矩阵格式，格式组合，可组合格式，SpMM，GPU，机器学习，代价模型

---

[← 返回 Session 1 — Numerical Methods](index.md)
