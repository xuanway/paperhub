---
title: "HyPIM: A Unified PIM Architecture for Accelerating Mamba-Transformer Hybrid Model Inference"
description: "MICRO 2026 · Session 1B · HyPIM：用于加速 Mamba-Transformer 混合模型推理的统一存内处理架构"
tags:
  - "MICRO2026"
  - "Processing-in-Memory"
---

# HyPIM: A Unified PIM Architecture for Accelerating Mamba-Transformer Hybrid Model Inference

**中文标题：** HyPIM：用于加速 Mamba-Transformer 混合模型推理的统一存内处理架构

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Hyemin Park, Isaac Jeong, Junghwan Lim, Jungi Hyun, Hyuk-Jae Lee

**来源：** MICRO 2026，pp. 158–173；[DOI](https://doi.org/10.1109/MICRO67795.2026.00027)

## 英文摘要

While Transformer-based large language models (LLMs) achieve remarkable accuracy, their large KV cache footprint and quadratic attention complexity make long-context inference increasingly inefficient. Hybrid architectures that combine Transformers with state space models (SSMs) have emerged as a promising alternative, offering improved performance-efficiency trade-offs. Since both Transformer attention and SSM state updates are limited by memory bandwidth, processing-in-memory (PIM) offers an attractive path to efficient acceleration. However, accelerating hybrid models on PIM remains challenging because attention and state updates exhibit fundamentally different dataflows and memory access patterns. Attention relies on parallel reduction over streaming read-only accesses, whereas state updates require sequential execution with recurrent read-modify-write operations. Existing PIM units specialized for either attention or SSM execution are ineffective for the other workload, while integrating multiple dedicated engines is impractical under the tight area constraints of commodity DRAM. To address this challenge, we propose HyPIM, a unified PIM architecture for end-to-end hybrid-model inference. HyPIM efficiently accelerates both attention and state updates through a mode-adaptive reconfigurable datapath and a switching-aware burst scheduling mechanism that groups same-direction accesses to reduce read write switching overhead during state updates. Experimental results show that HyPIM achieves 2.41x (up to 2.98x), 1.32x, and 1.21x speedups over the GPU, attention-centric PIMs, and SSM-centric PIMs, respectively. Furthermore, HyPIM scales robustly to long-context inference, reaching a 3.26x speedup over the GPU at a 32K sequence length.

## 中文摘要

虽然基于 Transformer 的大语言模型 (LLM) 实现了卓越的准确性，但其庞大的 KV 缓存占用空间和二次注意力复杂性使得长上下文推理变得越来越低效。将 Transformer 与状态空间模型 (SSM) 相结合的混合架构已成为一种有前景的替代方案，可提供改进的性能与效率权衡。由于 Transformer 注意力和 SSM 状态更新都受到内存带宽的限制，因此存内处理 (PIM) 提供了一条有吸引力的高效加速途径。然而，加速 PIM 上的混合模型仍然具有挑战性，因为注意力和状态更新表现出根本不同的数据流和内存访问模式。注意力依赖于流式只读访问的并行减少，而状态更新需要通过循环读取-修改-写入操作顺序执行。现有的专用于注意力或 SSM 执行的 PIM 单元对于其他工作负载来说是无效的，而在商用 DRAM 的严格面积限制下集成多个专用引擎是不切实际的。为了应对这一挑战，我们提出了 HyPIM，这是一种用于端到端混合模型推理的统一 PIM 架构。 HyPIM 通过模式自适应可重配置数据路径和切换感知突发调度机制有效加速注意力和状态更新，该机制对同向访问进行分组，以减少状态更新期间的读写切换开销。实验结果表明，与 GPU、以注意力为中心的 PIM 和以 SSM 为中心的 PIM 相比，HyPIM 分别实现了 2.41 倍（高达 2.98 倍）、1.32 倍和 1.21 倍的加速。此外，HyPIM 可以稳健地扩展到长上下文推理，在 32K 序列长度下比 GPU 加速 3.26 倍。

## 中文关键词

存内处理；异构系统；大语言模型；Mamba-Transformer 混合模型

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
