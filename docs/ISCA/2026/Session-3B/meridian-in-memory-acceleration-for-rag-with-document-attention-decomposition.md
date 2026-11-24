---
title: "MERIDIAN: In-Memory Acceleration for RAG with Document Attention Decomposition"
description: "ISCA 2026 · Session 3B · MERIDIAN: In-Memory Acceleration for RAG with Document Attention Decomposition"
tags:
  - "ISCA2026"
  - "Session 3B"
  - "DRAM and SRAM PIM/PNM"
---

# MERIDIAN: In-Memory Acceleration for RAG with Document Attention Decomposition

**中文标题：** MERIDIAN: 通过文档注意力分解实现 RAG 的内存内加速

**所属 Session：** [Session 3B](index.md) · [ISCA 2026](../index.md)

**作者：** Chaoqiang Liu, Yu Huang, Haifeng Liu, Yi Zhang, Qihang Qiu, Xueqi Li, Long Zheng, Xiaofei Liao, Hai Jin, Jingling Xue

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Retrieval-Augmented Generation (RAG) improves the factuality and timeliness of large language model outputs by incorporating external knowledge during inference. Recent systems accelerate RAG by precomputing and caching document-side Key-Value (KV) pairs, eliminating repeated encoding of long retrieved documents. However, this centralized KV-reuse paradigm introduces two fundamental bottlenecks: (1) massive off-chip KV transfers, since large-scale document KVs must reside in host memory and be moved to the device at query time, and (2) severely underutilized compute resources, as short queries yield skinny GEMMs during prefilling and memory-bound GEMVs during decoding. We address these limitations with MERIDIAN, a decentralized RAG system built on two key components. First, we introduce document attention decomposition, which replaces centralized KV processing with a distributed execution model: document-side K and V matrices are sharded across PIM-enabled memory modules, and each device computes attention over its local shard, producing compact partial summaries that are merged through a lightweight global aggregation step. This sharply reduces off-chip KV movement. Second, to improve compute efficiency, MERIDIAN incorporates a PIM-based accelerator co-designed with the decomposition mechanism. It provides a resource-conscious in-memory compute substrate for accelerating skinny GEMM and nonlinear operations, and employs a coordination-aware hybrid scheduler to sustain efficient intra-device execution and scalable inter-device parallelism. Evaluations show that MERIDIAN achieves average throughput improvements of 5.36×/6.64×/3.98×/3.32×/3.91× and latency reductions of 4.30×/5.34×/3.31×/2.73×/2.79× over TurboRAG, BlockAttention, CENT, PAPI, and HeterRAG, respectively.

## 中文摘要

检索增强生成（RAG）通过在推理过程中引入外部知识来提高大语言模型输出的事实性和时效性。最近的系统通过预计算和缓存文档侧的键值（KV）对来加速RAG，从而避免了对检索到的长文档进行重复编码。然而，这种集中式KV复用范式带来了两个根本性瓶颈：（1）大量片外KV传输，因为大规模文档KV必须驻留在主机内存中并在查询时传输到设备；（2）计算资源严重利用不足，因为短查询在预填充阶段产生瘦GEMM，在解码阶段产生内存受限的GEMV。我们通过MERIDIAN——一个基于两个关键组件的去中心化RAG系统——来解决这些限制。首先，我们引入了文档注意力分解，用分布式执行模型替代集中式KV处理：文档侧的K和V矩阵被分片到支持PIM的内存模块上，每个设备在其本地分片上计算注意力，产生紧凑的部分摘要，通过轻量级的全局聚合步骤进行合并。这大幅减少了片外KV移动。其次，为了提高计算效率，MERIDIAN结合了与分解机制协同设计的基于PIM的加速器。它提供了一个资源意识型的内存计算底层平台，用于加速瘦GEMM和非线性操作，并采用协调感知的混合调度器来维持高效的设备内执行和可扩展的设备间并行性。评估表明，与TurboRAG、BlockAttention、CENT、PAPI和HeterRAG相比，MERIDIAN分别实现了平均吞吐量提升5.36×/6.64×/3.98×/3.32×/3.91×和延迟降低4.30×/5.34×/3.31×/2.73×/2.79×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2026](../index.md)
