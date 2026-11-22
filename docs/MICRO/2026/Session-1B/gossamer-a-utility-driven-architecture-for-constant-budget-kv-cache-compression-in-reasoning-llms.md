---
title: "Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs"
description: "MICRO 2026 · Session 1B · Gossamer：面向推理型大语言模型的固定预算 KV 缓存压缩效用驱动架构"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Cache"
---

# Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs

**中文标题：** Gossamer：面向推理型大语言模型的固定预算 KV 缓存压缩效用驱动架构

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Feng Cheng, Cong Guo, Junyao Zhang, Haoxuan Shan, Chiyue Wei, Hong Wang, Hai Li, Yiran Chen

**来源：** MICRO 2026，pp. 207–221；[DOI](https://doi.org/10.1109/MICRO67795.2026.00030)

## 英文摘要

Transformer-based large language models (LLMs) are increasingly applied to complex reasoning tasks, yet their inference efficiency is fundamentally constrained by the rapid growth of the KV cache. As reasoning contexts extend to hundreds of thousands of tokens, the KV cache becomes the dominant contributor to memory footprint and bandwidth demand, tightly coupling computation and memory utilization and limiting scalability. Existing compression methods, such as quantization and eviction, alleviate capacity pressure but remain algorithmically oriented, often introducing additional passes and compute overhead that reduce system efficiency. This paper presents Gossamer, a KV cache compression architecture for reasoning LLMs that bridges the algorithm–system–hardware gap. Gossamer introduces a unified utility-based action framework that dynamically selects compression operations, quantization, merging, or eviction, under a constant KV cache budget. Through cross-domain co-design, we fuse cosine-similarity estimation directly into the attention computation, exploiting idle compute cycles to perform similarity evaluation without latency or bandwidth cost, a mechanism we call Free-Lunch Utilization. This enables real-time, fine-grained KV management with near-constant memory usage and negligible overhead. Under tight memory constraints, Gossamer sustains reasoning quality comparable to uncompressed inference while improving end-to-end throughput by up to 16.7x over uncompressed baselines, 5.5x and 4.9x over the quantization-based Oaken and Ecco, and 1.8x over the eviction-based R-KV.

## 中文摘要

基于Transformer的大语言模型（LLM）越来越多地应用于复杂的推理任务，但其推理效率从根本上受到KV缓存快速增长的限制。随着推理上下文扩展到数十万个词元，KV 缓存成为内存占用和带宽需求的主要贡献者，紧密耦合计算和内存利用率并限制可扩展性。现有的压缩方法（例如量化和驱逐）可以减轻容量压力，但仍然以算法为导向，通常会引入额外的通道和计算开销，从而降低系统效率。本文提出了 Gossamer，一种用于推理 LLM 的 KV 缓存压缩架构，它弥补了算法-系统-硬件之间的差距。 Gossamer 引入了一个基于实用程序的统一操作框架，可以在恒定的 KV 缓存预算下动态选择压缩操作、量化、合并或逐出。通过跨域协同设计，我们将余弦相似度估计直接融合到注意力计算中，利用空闲计算周期来执行相似度评估，而无需时延或带宽成本，我们将这种机制称为“免费午餐利用”。这可以实现实时、细粒度的 KV 管理，并且内存使用量接近恒定，开销可以忽略不计。在严格的内存限制下，Gossamer 保持了与未压缩推理相当的推理质量，同时将端到端吞吐量比未压缩基线提高了 16.7 倍，比基于量化的 Oaken 和 Ecco 提高了 5.5 倍和 4.9 倍，比基于驱逐的 R-KV 提高了 1.8 倍。

## 中文关键词

计算机体系结构；硬件加速；推理型大语言模型；内存管理；键值缓存压缩

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
