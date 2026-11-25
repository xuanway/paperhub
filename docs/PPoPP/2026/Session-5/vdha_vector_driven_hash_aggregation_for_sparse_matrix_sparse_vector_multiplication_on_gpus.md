---
title: "VDHA: Vector-Driven Hash Aggregation for Sparse Matrix-Sparse Vector Multiplication on GPUs"
description: "PPoPP 2026 Session 5（Stencil and Sparse Matrix Computation）：块私有哈希表做局部聚合，网页图几何平均 1.41×"
tags:
  - "PPoPP2026"
  - "Session-5"
  - "Stencil and Sparse Matrix Computation"
  - "SpMSpV"
  - "Hash Table"
  - "GPU"
authors:
  - "Yuchen Li"
  - "Zhe Pan"
  - "Peng Qu"
  - "Youhui Zhang"
session: "Session 5: Stencil and Sparse Matrix Computation"
session_number: 5
session_chair: "Shoaib Kamil"
date: "2026-02-03"
time: "10:50–11:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786447"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# VDHA: Vector-Driven Hash Aggregation for Sparse Matrix-Sparse Vector Multiplication on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 GPU 加权 SpMSpV 内核 VDHA，用块私有哈希表做局部聚合以缓解写回冲突，配合列分裂重排序与流水线重叠，整体优于 SOTA 基线。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 5: Stencil and Sparse Matrix Computation</p>
</div>

**作者**：Yuchen Li, Zhe Pan, Peng Qu, and Youhui Zhang — Tsinghua University, China; Zhongguancun Laboratory, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 10:50–11:10 · Session 5: Stencil and Sparse Matrix Computation（主席：Shoaib Kamil）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786447) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Sparse matrix-sparse vector multiplication (SpMSpV) is a core primitive in graph analytics and scientific computing, also arising in spiking neural networks for event-driven spike propagation. On GPUs, the performance of the prevalent and efficient SpMSpV paradigm is often bottlenecked by the write-back phase of accumulating non-zero multiply–accumulate results; its many-to-one index scatter pattern causes severe conflicts and poor bandwidth utilization on GPUs. We present VDHA, a GPU-based weighted SpMSpV kernel that leverages block-private hash tables for local aggregation, substantially reducing write conflicts and improving memory coalescing. To further amplify this benefit, we incorporate column splitting with lightweight reordering to expose more locality, and employ a fetch–compute– writeback pipeline to overlap hash computation with memory accesses. Extensive evaluation on over 300 matrices with more than 5 million nonzeros, including web-scale graphs (Konect/LAW) and scientific workloads (SuiteSparse), shows that VDHA consistently outperforms state-of-the-art baselines. On web graphs, it achieves a 1.41× geometric-mean speedup (up to 3.42×), while on SuiteSparse it delivers 1.13× (up to 2.55×). We also provide a lightweight predictive model that identifies matrices favorable to VDHA with 91.3% accuracy.

## 中文摘要

稀疏矩阵–稀疏向量乘法（SpMSpV）是图分析与科学计算中的核心原语，也出现在脉冲神经网络的事件驱动脉冲传播中。在 GPU 上，主流且高效的 SpMSpV 范式的性能往往受制于累加非零乘累加结果的写回阶段；其多对一的索引散射模式在 GPU 上造成严重冲突与带宽利用率低下。我们提出 VDHA，一个基于 GPU 的带权 SpMSpV 内核，它利用块私有哈希表进行局部聚合，大幅减少写冲突并改善访存合并。为进一步放大这一收益，我们引入列切分与轻量级重排序以暴露更多局部性，并采用取数–计算–写回流水线，将哈希计算与内存访问重叠。在 300 多个非零元数超过 500 万的矩阵（包括 web 规模图（Konect/LAW）与科学工作负载（SuiteSparse））上的广泛评估表明，VDHA 始终优于最先进的基线。在 web 图上，它取得 1.41 倍的几何平均加速（最高 3.42 倍），而在 SuiteSparse 上则达到 1.13 倍（最高 2.55 倍）。我们还提供了一个轻量级预测模型，能够以 91.3% 的准确率识别出适合 VDHA 的矩阵。

## 英文关键词

SpMSpV, sparse matrix, GPU, Hashing, SNN

## 中文关键词

SpMSpV；稀疏矩阵；GPU；哈希；SNN（脉冲神经网络）

---

## 一句话总结

> 提出 GPU 加权 SpMSpV 内核 VDHA，用块私有哈希表做局部聚合以缓解写回冲突，配合列分裂重排序与流水线重叠，整体优于 SOTA 基线。

## 研究问题

主流 SpMSpV 范式的瓶颈在非零乘累加结果的写回阶段：多对一的索引散射在 GPU 上引发严重冲突与带宽利用率低下。

## 方法简述

- 采用块私有哈希表在块内完成局部聚合，显著减少写冲突并提升访存合并。
- 引入列分裂与轻量重排序，暴露更多局部性。
- 设计 fetch-compute-writeback 流水线，使哈希计算与内存访问重叠。
- 提供轻量预测模型，用于识别适合 VDHA 的矩阵。

## 主要结果

- 在 300 多个含 500 万以上非零元的矩阵（Konect/LAW 网页图与 SuiteSparse）上一致优于 SOTA 基线。
- 网页图上取得 1.41× 几何平均加速（最高 3.42×），SuiteSparse 上为 1.13×（最高 2.55×）。
- 预测模型识别有利矩阵的准确率达 91.3%。

---

> 所属 Session：[Session 5: Stencil and Sparse Matrix Computation](index.md) · 返回 [PPoPP 2026 总览](../index.md)
