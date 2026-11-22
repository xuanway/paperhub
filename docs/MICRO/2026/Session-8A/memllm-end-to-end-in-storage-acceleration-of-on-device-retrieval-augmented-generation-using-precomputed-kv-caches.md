---
title: "MemLLM: End-to-end In-Storage Acceleration of On-Device Retrieval-Augmented Generation using Precomputed KV Caches"
description: "MICRO 2026 · Session 8A · MemLLM：利用预计算 KV 缓存实现端侧检索增强生成的端到端存储内加速"
tags:
  - "MICRO2026"
  - "Cache"
  - "Storage"
---

# MemLLM: End-to-end In-Storage Acceleration of On-Device Retrieval-Augmented Generation using Precomputed KV Caches

**中文标题：** MemLLM：利用预计算 KV 缓存实现端侧检索增强生成的端到端存储内加速

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Seungkwan Kang, Hyungseok Ko, Heemin Kim, Myoungsoo Jung

**来源：** MICRO 2026，pp. 2815–2829；[DOI](https://doi.org/10.1109/MICRO67795.2026.00191)

## 英文摘要

Retrieval-augmented generation (RAG) on edge devices enables personalized large language model (LLM) inference while preserving privacy. However, RAG's inherent length asymmetry makes the prefill phase the dominant bottleneck. While precomputing the KV caches offline alleviates the prefill cost on server systems, the multi-gigabyte caches over the narrow interconnect create a severe I/O wall for on-device systems. To mitigate this, we propose MemLLM, an end-to-end in-storage processing (ISP) architecture that executes the complete attention pipeline based on precomputed KV caches within the SSD. MemLLM utilizes per-channel accelerators to fully utilize the aggregated NAND channel bandwidth and accelerates all KV cache-related computations on the storage-side to minimize PCIe transfers. To efficiently handle the sparse updates required by RAG, MemLLM introduces a fused recomputation-query kernel paired with a hardware-based filter logic to halve the NAND read volume and eliminate write-back penalties. Furthermore, MemLLM's global SRAM-based stateful reduction engine enables a completely DRAM-less dataflow, thereby removing the internal memory bottlenecks and bounding the PCIe egress to an O(1) footprint. A full-stack software stack allows asynchronous, zero-copy transfers from the ISP to the host and provides transparent execution within modern ML frameworks. Evaluated across eight real-world RAG datasets and six on-device LLM models, MemLLM achieves an average end-to-end speedup of 4.06× over the GPU baseline.

## 中文摘要

边缘设备上的检索增强生成 (RAG) 可实现个性化大语言模型 (LLM) 推理，同时保护隐私。然而，RAG 固有的长度不对称性使得预填充阶段成为主要瓶颈。虽然离线预计算 KV 缓存可以减轻服务器系统上的预填充成本，但窄互连上的数 GB 缓存为设备上的系统创建了严重的 I/O 墙。为了缓解这个问题，我们提出了 MemLLM，这是一种端到端存储内处理 (ISP) 架构，它基于 SSD 内预先计算的 KV 缓存执行完整的注意力管道。 MemLLM 利用每通道加速器来充分利用聚合的 NAND 通道带宽，并加速存储端所有与 KV 缓存相关的计算，以最大限度地减少 PCIe 传输。为了有效处理 RAG 所需的稀疏更新，MemLLM 引入了融合的重新计算查询内核，与基于硬件的过滤器逻辑配对，以将 NAND 读取量减半并消除回写惩罚。此外，MemLLM 的基于 SRAM 的全局状态缩减引擎可实现完全无 DRAM 的数据流，从而消除内部内存瓶颈并将 PCIe 出口限制在 O(1) 占用空间内。全栈软件堆栈允许从 ISP 到主机的异步、零拷贝传输，并在现代机器学习框架内提供透明的执行。通过对 8 个真实世界的 RAG 数据集和 6 个设备上的 LLM 模型进行评估，MemLLM 的平均端到端加速比 GPU 基线提高了 4.06 倍。

## 中文关键词

存储内处理；检索增强生成；大语言模型推理；键值缓存；近数据处理；端侧机器学习

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
