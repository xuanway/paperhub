---
title: "Transitive Array: An Efficient GEMM Accelerator with Result Reuse"
description: "ISCA 2025 · Session 6A · Transitive Array：支持结果复用的高效 GEMM 加速器"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# Transitive Array: An Efficient GEMM Accelerator with Result Reuse

**中文标题：** Transitive Array：支持结果复用的高效 GEMM 加速器

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Cong Guo, Chiyue Wei, Jiaming Tang, Bowen Duan, Song Han, Hai "Helen" Li, Yiran Chen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731043) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Deep Neural Networks (DNNs) and Large Language Models (LLMs) have revolutionized artificial intelligence, yet their deployment faces significant memory and computational challenges, especially in resource-constrained environments. Quantization techniques have mitigated some of these issues by reducing data precision, primarily focusing on General Matrix Multiplication (GEMM). This study introduces a novel sparsity paradigm, transitive sparsity, which leverages the reuse of previously computed results to sub- stantially minimize computational overhead in GEMM operations. By representing transitive relations using a directed acyclic graph, we develop an efficient strategy for determining optimal execution orders, thereby overcoming inherent challenges related to execu- tion dependencies and parallelism. Building on this foundation, we present the Transitive Array, a multiplication-free accelerator designed to exploit transitive sparsity in GEMM. Our architecture effectively balances computational workloads across multiple paral- lel lanes, ensuring high efficiency and optimal resource utilization. Comprehensive evaluations demonstrate that the Transitive Array achieves approximately 7.46×and 3.97×speedup and 2.31×and 1.65×energy reduction compared to state-of-the-art accelerators such as Olive and BitVert while maintaining comparable model accuracy on LLaMA models.

## 中文摘要

深度神经网络（DNN）与大语言模型（LLM）重塑了人工智能领域，但它们的部署面临严峻的内存与算力挑战，在资源受限环境下尤为突出。量化技术通过降低数据精度缓解了部分压力，这类方案主要面向通用矩阵乘法（GEMM）。本文提出一种全新稀疏范式：传递稀疏（transitive sparsity），它复用已计算结果，大幅削减GEMM的计算开销。
该方法利用有向无环图刻画传递关系，给出求解最优执行顺序的高效策略，克服执行依赖与并行度带来的固有难题。在此基础上，本文设计传递阵列（Transitive Array）——一款无乘法加速器，专门挖掘GEMM中的传递稀疏特性。该架构在多条并行通道之间均衡计算负载，保证高执行效率与资源利用率。
大量评测表明：在LLaMA模型上，传递阵列在精度相当的前提下，对比Olive、BitVert等前沿加速器，最高分别实现7.46倍、3.97倍提速，功耗降低2.31倍、1.65倍。

## 英文关键词

Matrix Multiplication, Quantization, Sparsity, Transitive Array

## 中文关键词

矩阵乘法, 量化, 稀疏性, 传递阵列

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731043)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
