---
title: "D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation"
description: "MICRO 2026 · Session 9B · D-NOVA：通过双界限与向量自适应的三维 NAND 优化相似性搜索，实现存储内检索加速"
tags:
  - "MICRO2026"
  - "Storage"
---

# D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation

**中文标题：** D-NOVA：通过双界限与向量自适应的三维 NAND 优化相似性搜索，实现存储内检索加速

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Chang Eun Song, Sumukh Pinge, Tianqi Zhang, Sung Eun Kim, Tajana S. Rosing, Mingu Kang

**来源：** MICRO 2026，pp. 3344–3360；[DOI](https://doi.org/10.1109/MICRO67795.2026.00224)

## 英文摘要

Retrieval-Augmented Generation (RAG) enhances the factual grounding of large language model (LLM) inference by retrieving relevant information from external knowledge bases. However, its dense vector retrieval introduces significant latency and energy overhead, becoming the primary performance bottleneck. Although recent in-storage accelerators aim to reduce data movement, they still rely on host or embedded processors outside the memory, where nearly 70% of the total retrieval time is spent. As a result, they cannot fully overcome the bandwidth limitations, leading to yet another memory bottleneck. To tackle these limitations, we present D-NOVA, a hardware–software co-designed in-storage retrieval accelerator. D-NOVA executes an inverted file (IVF)-based hierarchical retrieval pipeline by deeply embedding the search functionality directly into the NAND memory array. This is achieved by incorporating a new distance metric, Dual-bound Tight Similarity Sensing (DTS), which is specifically tailored for searching within the NAND string. In addition, we introduce a lightweight contrastive adapter that maps embedding vectors into a DTS-friendly domain, recovering near-software recall while improving performance and energy efficiency. D-NOVA is up to 41.7× faster and 71× more energy- efficient than a CPU baseline, and achieves 12.13× higher throughput while being up to 1.26× more energy-efficient than state-of-the-art in-storage RAG accelerators, demonstrating the potential of fully in-storage vector search for scalable RAG acceleration.

## 中文摘要

检索增强生成 (RAG) 通过从外部知识库检索相关信息来增强大语言模型 (LLM) 推理的事实基础。然而，其密集向量检索引入了显着的时延和能量开销，成为主要的性能瓶颈。尽管最近的存储内加速器旨在减少数据移动，但它们仍然依赖于内存外部的主机或嵌入式处理器，其中近 70% 的总检索时间都花费在内存上。因此，它们无法完全克服带宽限制，从而导致另一个内存瓶颈。为了解决这些限制，我们推出了 D-NOVA，这是一种软硬件共同设计的存储内检索加速器。 D-NOVA 通过将搜索功能直接深度嵌入 NAND 内存阵列来执行基于倒排文件 (IVF) 的分层检索管道。这是通过结合新的距离度量、双界紧密相似性传感 (DTS) 来实现的，该度量是专门为在 NAND 字符串内进行搜索而定制的。此外，我们还引入了一种轻量级对比适配器，可将嵌入向量映射到 DTS 友好的域中，恢复近乎软件的召回率，同时提高性能和能效。 D-NOVA 的速度比 CPU 基准快 41.7 倍，能效高 71 倍，吞吐量提高 12.13 倍，能效比最先进的存储内 RAG 加速器高 1.26 倍，展示了完全存储内向量搜索在可扩展 RAG 加速方面的潜力。

## 中文关键词

检索增强生成；向量搜索；存储内处理；三维 NAND 闪存；相似性搜索；硬件加速

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
