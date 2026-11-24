---
title: "FuseFlow: A Fusion-Centric Compilation Framework for Sparse Deep Learning on Streaming Dataflow"
description: "ASPLOS 2026 · Session 4B · FuseFlow：面向流式数据流的稀疏深度学习融合式编译框架"
tags:
  - "ASPLOS2026"
  - "Session 4B"
  - "ML Compilers & Tensor Programs"
---

# FuseFlow: A Fusion-Centric Compilation Framework for Sparse Deep Learning on Streaming Dataflow

**中文标题：** FuseFlow：面向流式数据流的稀疏深度学习融合式编译框架

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Rubens Lacouture (Stanford University), Nathan Zhang (SambaNova Systems), Ritvik Sharma (Stanford University), Marco Siracusa (Barcelona Supercomputing Center), Fredrik Kjolstad (Stanford University), Kunle Olukotun (Stanford University), Olivia Hsu (Stanford University)

**单位：** Stanford University；SambaNova Systems；Barcelona Supercomputing Center

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790165) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

As deep learning models scale, sparse deep learning (DL) models that exploit sparsity in weights, activations, or inputs and specialized dataflow hardware have emerged as powerful solutions to address efficiency. We propose FuseFlow, a compiler that converts sparse machine learning models written in PyTorch to fused sparse dataflow graphs for reconfigurable dataflow architectures (RDAs). FuseFlow is the first compiler to support general cross-expression fusion of sparse operations. In addition to fusion across kernels (expressions), FuseFlow also supports optimizations like parallelization, dataflow ordering, and sparsity blocking. It targets a cycle-accurate dataflow simulator for microarchitectural analysis of fusion strategies. We use FuseFlow for design-space exploration across four real-world machine learning applications with sparsity, showing that full fusion (entire cross-expression fusion across all computation in an end-to-end model) is not always optimal for sparse models—fusion granularity depends on the model itself. FuseFlow also provides a heuristic to identify and prune suboptimal configurations. Using FuseFlow, we achieve performance improvements, including a ∼2.7x speedup over an unfused baseline for GPT-3 with BigBird block-sparse attention.

## 中文摘要

随着深度学习模型规模不断扩大，利用权重、激活值或输入中的稀疏性的稀疏深度学习（DL）模型，以及专用的数据流硬件，已成为应对效率问题的有力解决方案。我们提出 FuseFlow，这是一个编译器，可将用 PyTorch 编写的稀疏机器学习模型转换为面向可重构数据流架构（RDA）的融合稀疏数据流图。FuseFlow 是首个支持稀疏运算的通用跨表达式融合的编译器。除跨内核（表达式）的融合外，FuseFlow 还支持并行化、数据流排序和稀疏分块等优化。它面向一个周期精确的数据流模拟器，用于对融合策略进行微架构分析。我们使用 FuseFlow 在四个真实的带稀疏性的机器学习应用上进行设计空间探索，结果表明完全融合（对端到端模型中所有计算进行完整的跨表达式融合）对稀疏模型并不总是最优的——融合粒度取决于模型本身。FuseFlow 还提供一种启发式方法，用于识别并剪除次优配置。使用 FuseFlow，我们取得了性能提升，包括在采用 BigBird 块稀疏注意力的 GPT-3 上相对于未融合基线约 2.7 倍的加速。

## 英文关键词

sparse machine learning, Einsum, tensor compiler, kernel fusion, spatial dataflow accelerator

## 中文关键词

稀疏机器学习；Einsum；张量编译器；内核融合；空间数据流加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790165)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2026](../index.md)
