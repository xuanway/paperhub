---
title: "DMA-Latte: Expanding the Reach of DMA Offloads to Latency-Bound ML Communication"
description: "MICRO 2026 · Session 1C · DMA-Latte：将 DMA 卸载扩展至受时延限制的机器学习通信"
tags:
  - "MICRO2026"
---

# DMA-Latte: Expanding the Reach of DMA Offloads to Latency-Bound ML Communication

**中文标题：** DMA-Latte：将 DMA 卸载扩展至受时延限制的机器学习通信

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Suchita Pati, Shaizeen Aga, Mahzabeen Islam, Ryan Quach, Saleel Kudchadker, Mohamed Ibrahim

**来源：** MICRO 2026，pp. 269–282；[DOI](https://doi.org/10.1109/MICRO67795.2026.00034)

## 英文摘要

Offloading communication to existing direct memory access (DMA) engines, available on most state-of-the-art commercial GPUs, has emerged as a practical and low-cost solution to efficiently overlap computation and communication in machine learning (ML). However, the reach of DMA offloads has so far been limited to bandwidth-bound scenarios only (10s of MB to GB transfer sizes). In this work, we break this barrier and extend DMA communication offloads to latency-bound regions (KB to low MB). Specifically, we leverage hitherto untapped features available in the state-of-the-art AMD Instinct" MI300X GPUs that render DMA communication offloads competitive even in latency-bound regions. We demonstrate the efficacy of these features both at the operator level (ML communication collectives such as all-gather and all-to-all), and at the end-to-end workload level (LLM inference). At the operator level, our optimizations provide up to 4.5× speedups (3.2× geomean in the latency-bound region) over baseline DMA offload, narrowing the performance gap while delivering additional power savings (3-10%) for ML collectives compared to state-of-the-art GPU core-based communication library, RCCL. At the workload level, we demonstrate acceleration for LLM inference: up to 1.65× lower latency and up to 1.9× higher throughput over the state-of-the-art vLLM inference framework. We conclude with a discussion of AMD Instinct GPU runtime innovations that stand to expose these features.

## 中文摘要

将通信卸载到先进商用 GPU 普遍具备的直接内存访问（DMA）引擎，已成为机器学习中实现计算与通信高效重叠的实用、低成本方案。然而，DMA 卸载此前主要适用于带宽受限场景，即数十 MB 至 GB 级传输。本文突破这一限制，将 DMA 通信卸载扩展到时延受限的 KB 至较小 MB 级传输。具体而言，我们利用 AMD Instinct MI300X GPU 中此前未充分开发的功能，使 DMA 通信卸载即使在时延受限区域也具有竞争力。我们从算子层面（all-gather、all-to-all 等机器学习集合通信）和端到端工作负载层面（大语言模型推理）验证这些功能的有效性。在算子层面，相比基线 DMA 卸载，优化最高获得 4.5 倍加速，在时延受限区域的几何平均加速比为 3.2；相较先进的基于 GPU 核的通信库 RCCL，优化在缩小性能差距的同时，为机器学习集合通信额外节省 3–10% 功耗。在工作负载层面，相比先进的 vLLM 推理框架，LLM 推理时延最低降至原来的 1/1.65，吞吐量最高达到原来的 1.9 倍。最后，本文讨论有望向软件暴露这些功能的 AMD Instinct GPU 运行时创新。

## 中文关键词

直接内存访问；通信卸载；机器学习集合通信；图形处理器

## 代码与研究制品

- 代码仓库：[https://github.com/AMDResearch/AMD-DMA-Latte](https://github.com/AMDResearch/AMD-DMA-Latte)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
