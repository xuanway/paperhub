---
title: "ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving"
description: "ISCA 2026 · Session 5A · ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving"
tags:
  - "ISCA2026"
  - "Session 5A"
  - "LLM 3"
---

# ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving

**中文标题：** ConServe: 面向多轮 LLM 服务的连续性保持内存管理

**所属 Session：** [Session 5A](index.md) · [ISCA 2026](../index.md)

**作者：** Bingyao Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Interacting with humans through multi-turn conversations is a fundamental capability of large language models (LLMs). Multi-turn serving stresses GPU memory systems as KV caches grow, persist, and are heavily reused across turns. PagedAttention, the prevailing dynamic allocator in modern systems, mitigates fragmentation and increases batch size by managing the KV cache in blocks, but in doing so converts an originally contiguous virtual address space into a non-contiguous layout, introducing non-trivial programming complexity and additional address translation overheads from scattered virtual pages and block table lookups. We reveal that translation locality is a critical bottleneck under such paged KV designs, and we present ConServe, a contiguity-aware virtual memory allocator that retains per-conversation contiguity in the virtual address space while mitigating fragmentation in physical memory. ConServe reserves a single contiguous virtual address slice per conversation, maps physical pages on demand with CUDA VMM, and resizes virtual address slices via lazy, copy-free remapping at negligible overhead. Across diverse models and workloads, ConServe achieves up to 74.4%, 43.4%, and 19.1% lower TTFT and 35.1%, 15.6%, and 12.1% higher end-to-end throughput than vLLM, vAttention-Turn, and vAttention-Conv, respectively.

## 中文摘要

通过多轮对话与人类交互是大语言模型（LLM）的一项基本能力。多轮服务中 KV 缓存不断增长、长期驻留并在各轮之间被大量复用，给 GPU 存储系统带来压力。PagedAttention 作为现代系统中主流的动态分配器，通过以块为单位管理 KV 缓存来缓解碎片并提升批大小，但这样做把原本连续的虚拟地址空间转变为非连续布局，从而引入了不小的编程复杂度，并因虚拟页分散和块表查找而带来额外的地址转换开销。我们揭示出，在此类分页 KV 设计下，转换局部性是一个关键瓶颈。为此我们提出 ConServe——一种连续性感知的虚拟内存分配器，在虚拟地址空间中为每个会话保持连续性，同时缓解物理内存中的碎片。ConServe 为每次会话预留一段连续的虚拟地址切片，借助 CUDA VMM 按需映射物理页，并通过惰性、免拷贝的重映射以可忽略的开销调整虚拟地址切片的大小。在多种模型与负载下，ConServe 相比 vLLM、vAttention-Turn 和 vAttention-Conv，首 token 时延（TTFT）分别最多降低 74.4%、43.4% 和 19.1%，端到端吞吐分别提升 35.1%、15.6% 和 12.1%。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2026](../index.md)
