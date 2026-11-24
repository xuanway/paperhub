---
title: "Accelerating Retrieval-Augmented Generation"
description: "ASPLOS 2025 · Session 1A · 加速检索增强生成"
tags:
  - "ASPLOS2025"
  - "Session 1A"
  - "ML Acceleration"
---

# Accelerating Retrieval-Augmented Generation

**中文标题：** 加速检索增强生成

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Derrick Quinn (Cornell University), Mohammad Nouri (Cornell University), Neel Patel (Cornell University), John Salihu (University of Kansas), Alireza Salemi (UMass Amherst), Sukhan Lee (Samsung Electronics), Hamed Zamani (UMass Amherst), Mohammad Alian (Cornell University)

**单位：** Cornell University；University of Kansas；UMass Amherst；Samsung Electronics

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707264) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

An evolving solution to address hallucination and enhance accuracy in large language models (LLMs) is Retrieval-Augmented Generation (RAG), which involves augmenting LLMs with information retrieved from an external knowledge source, such as the web. This paper profiles several RAG execution pipelines and demystifies the complex interplay between their retrieval and generation phases. We demonstrate that while exact retrieval schemes are expensive, they can reduce inference time compared to approximate retrieval variants because an exact retrieval model can send a smaller but more accurate list of documents to the generative model while maintaining the same end-to-end accuracy. This observation motivates the acceleration of the exact nearest neighbor search for RAG. In this work, we design Intelligent Knowledge Store (IKS), a type-2 CXL device that implements a scale-out near-memory acceleration architecture with a novel cache-coherent interface between the host CPU and near-memory accelerators. IKS offers 13.4–27.9× faster exact nearest neighbor search over a 512GB vector database compared with executing the search on Intel Sapphire Rapids CPUs. This higher search performance translates to 1.7–26.3× lower end-to-end inference time for representative RAG applications. IKS is inherently a memory expander; its internal DRAM can be disaggregated and used for other applications running on the server to prevent DRAM – which is the most expensive component in today's servers – from being stranded.

## 中文摘要

应对大语言模型（LLM）幻觉并提升其准确性的一种不断演进的方案是检索增强生成（RAG），即用从外部知识源（如网络）检索到的信息来增强 LLM。本文对若干 RAG 执行流水线进行剖析，并揭示了其检索阶段与生成阶段之间复杂的相互作用。我们表明，尽管精确检索方案开销昂贵，但与近似检索变体相比，它们能够减少推理时间，因为精确检索模型可以在保持相同端到端准确率的同时，向生成模型发送更小但更准确的文档列表。这一观察促使我们加速面向 RAG 的精确最近邻搜索。在本工作中，我们设计了 Intelligent Knowledge Store（IKS），一种 type-2 CXL 设备，它实现了横向扩展的近内存加速架构，并在主机 CPU 与近内存加速器之间提供了新颖的缓存一致性接口。与在 Intel Sapphire Rapids CPU 上执行搜索相比，IKS 在 512GB 向量数据库上提供的精确最近邻搜索快 13.4–27.9×。这一更高的搜索性能转化为代表性 RAG 应用端到端推理时间降低 1.7–26.3×。IKS 本质上是一种内存扩展器；其内部 DRAM 可以被解聚并用于服务器上运行的其他应用，从而避免当今服务器中最昂贵的组件 DRAM 被闲置搁浅。

## 英文关键词

database acceleration, dense retrieval, retrieval-augmented generation (RAG)

## 中文关键词

数据库加速；稠密检索；检索增强生成（RAG）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707264)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2025](../index.md)
