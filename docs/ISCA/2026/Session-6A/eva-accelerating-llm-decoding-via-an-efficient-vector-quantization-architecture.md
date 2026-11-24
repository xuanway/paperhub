---
title: "EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture"
description: "ISCA 2026 · Session 6A · EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture"
tags:
  - "ISCA2026"
  - "Session 6A"
  - "LLM 4"
---

# EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture

**中文标题：** EVA: 通过高效向量量化架构加速 LLM 解码

**所属 Session：** [Session 6A](index.md) · [ISCA 2026](../index.md)

**作者：** Bowen Duan, Cong Guo, Chiyue Wei, Haoxuan Shan, Yuzhe Fu, Xinhua Chen, Yifan Xu, Ziyue Zhang, Changchun Zhou, Hai Li, Yiran Chen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large Language Models (LLMs) have achieved impressive performance across diverse domains but remain inefficient during the autoregressive decoding phase. Unlike the prefill stage, which employs compute-bound GEMM operations, decoding executes a sequence of small GEMV-like computations that are memory-bound and underutilize modern accelerators. Weight-only vector quantization (VQ) has emerged as an effective compression technique that clusters model weights into a shared codebook and replaces the original weight matrix with low-precision indices, enabling 2-bit-level weight compression. While this approach substantially reduces model size and memory bandwidth, it still suffers from two critical inefficiencies: the low utilization of GEMV computation and frequent memory conflicts during codebook lookups. This paper presents EVA, an efficient vector-quantization-based architecture that addresses both computational and memory bottlenecks in LLM decoding. EVA builds on a simple yet effective insight that combines input-codebook computation with conflict-free memory access. Instead of reconstructing quantized weights from indices, EVA directly performs dot products between input vectors and the weight codebook, transforming LLM decoding from GEMV to GEMM computation. It then performs structured lookups from an intermediate output buffer, eliminating memory bank conflicts. We further design a hardware-software co-optimized architecture specialized for LLM decoding while remaining compatible with conventional prefill execution. Evaluations show that EVA achieves up to 11.17× speedup and 7.17× higher energy efficiency compared with the SOTA lookup-based architecture, while preserving arithmetic precision after vector quantization. Our code is available at https://github.com/dbw6/Eva.git.

## 中文摘要

大语言模型（LLM）在众多领域取得了令人瞩目的性能，但在自回归解码阶段仍然效率低下。与采用计算密集型 GEMM 操作的预填充阶段不同，解码执行一系列类似 GEMV 的小规模计算，这些计算受内存带宽限制，无法充分利用现代加速器。仅权重向量量化（VQ）已成为一种有效的压缩技术，它将模型权重聚类到共享码本中，并用低精度索引替代原始权重矩阵，从而实现 2 比特级别的权重压缩。尽管该方法大幅减小了模型规模并降低了内存带宽需求，但仍存在两个关键的低效问题：GEMV 计算利用率低，以及码本查找过程中频繁的内存冲突。本文提出 EVA，一种高效的基于向量量化的架构，同时解决 LLM 解码中的计算与内存瓶颈。EVA 基于一个简单而有效的洞见，将输入-码本计算与无冲突内存访问相结合。EVA 不根据索引重建量化权重，而是直接在输入向量与权重码本之间执行点积，从而将 LLM 解码从 GEMV 转变为 GEMM 计算。随后，它从中间输出缓冲区执行结构化查找，消除存储体冲突。我们进一步设计了面向 LLM 解码的软硬件协同优化架构，同时保持与传统预填充执行的兼容性。评估表明，与最先进的基于查找的架构相比，EVA 最高实现 11.17 倍加速和 7.17 倍的能效提升，同时在向量量化后保持算术精度。我们的代码已在 https://github.com/dbw6/Eva.git 开源。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：dbw6/Eva](https://github.com/dbw6/Eva)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2026](../index.md)
