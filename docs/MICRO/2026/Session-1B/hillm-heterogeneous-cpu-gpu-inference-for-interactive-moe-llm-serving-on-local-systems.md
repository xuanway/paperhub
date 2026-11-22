---
title: "HiLLM: Heterogeneous CPU-GPU Inference for Interactive MoE LLM Serving on Local Systems"
description: "MICRO 2026 · Session 1B · HiLLM：面向本地交互式 MoE 大语言模型服务的 CPU-GPU 异构推理"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
---

# HiLLM: Heterogeneous CPU-GPU Inference for Interactive MoE LLM Serving on Local Systems

**中文标题：** HiLLM：面向本地交互式 MoE 大语言模型服务的 CPU-GPU 异构推理

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Insu Choi, Seungchan Lee, Joon-Sung Yang

**来源：** MICRO 2026，pp. 129–142；[DOI](https://doi.org/10.1109/MICRO67795.2026.00025)

## 英文摘要

Scaling large language models (LLMs) with mixture-of-experts (MoE) architectures enables massive model capacity without a proportional increase in per-token computation. However, serving large MoE LLMs on local CPU–GPU systems remains challenging when the expert weights exceed the memory capacity of a single GPU, in which inactive experts must reside in host memory, making PCIe transfers, expert caching, and CPU–GPU scheduling critical performance bottlenecks. In this paper, we present HiLLM, a heterogeneous CPU–GPU inference framework for GPU-memory-constrained local MoE serving. HiLLM jointly manages expert residency, prefetching, and execution placement through an expert-cache architecture, an LTR replacement policy, and asynchronous prefetching with partial expert transfers. HiLLM further uses runtime scheduling and expert sharding to balance CPU execution with PCIe/GPU execution and shorten critical paths. Across diverse MoE LLMs and local CPU–GPU platforms, HiLLM improves throughput over HybriMoE by 1.17× on average and up to 1.43×.

## 中文摘要

使用专家混合 (MoE) 架构扩展大语言模型 (LLM) 可实现海量模型容量，而无需按比例增加每个词元的计算量。然而，当专家权重超过单个 GPU 的内存容量时，在本地 CPU-GPU 系统上为大型 MoE LLM 提供服务仍然具有挑战性，其中不活动的专家必须驻留在主机内存中，从而使 PCIe 传输、专家缓存和 CPU-GPU 调度成为关键性能瓶颈。在本文中，我们提出了 HiLLM，一种用于 GPU 内存受限的本地 MoE 服务的异构 CPU-GPU 推理框架。 HiLLM 通过专家缓存架构、LTR 替换策略以及部分专家传输的异步预取来联合管理专家驻留、预取和执行放置。 HiLLM 进一步使用运行时调度和专家分片来平衡 CPU 执行与 PCIe/GPU 执行并缩短关键路径。在不同的 MoE LLM 和本地 CPU-GPU 平台中，HiLLM 的吞吐量比 HybriMoE 平均提高了 1.17 倍，最高可达 1.43 倍。

## 中文关键词

专家缓存；异构推理；大语言模型；负载均衡；混合专家模型；预取

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
