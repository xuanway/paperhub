---
title: "STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems"
description: "ASPLOS 2026 · Session 3A · STARC：面向 PIM 系统上高效 LLM 解码的带重映射与聚类的选择性 token 访问"
tags:
  - "ASPLOS2026"
  - "Session 3A"
  - "LLM Attention & KV Cache"
---

# STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems

**中文标题：** STARC：面向 PIM 系统上高效 LLM 解码的带重映射与聚类的选择性 token 访问

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zehao Fan (Rensselaer Polytechnic Institute), Yunzhen Liu (University of Massachusetts, Amherst), Garrett Gagnon (Rensselaer Polytechnic Institute), Zhenyu Liu (Rensselaer Polytechnic Institute), Yayue Hou (Rensselaer Polytechnic Institute), Hadjer Benmeziane (IBM Research – Ruschlikon, Switzerland), Kaoutar El Maghraoui (IBM T. J. Watson Research Center), Liu Liu (Rensselaer Polytechnic Institute)

**单位：** Rensselaer Polytechnic Institute；University of Massachusetts, Amherst；IBM Research – Ruschlikon, Switzerland；IBM T. J. Watson Research Center

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790226) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Serving large language models (LLMs) places significant pressure on memory systems due to frequent accesses and growing key–value (KV) caches as context lengths increase. Processing-in-memory (PIM) architectures offer high internal bandwidth and near-data compute parallelism, but current designs target dense attention and perform poorly under the irregular access patterns of dynamic KV cache sparsity. To mitigate this limitation, we propose STARC, a sparsity-optimized data mapping scheme for efficient LLM decoding on PIM. STARC clusters semantically similar KV pairs and co-locates them contiguously within PIM banks, enabling retrieval at cluster granularity by matching queries against precomputed centroids. This bridges the gap between fine-grained sparse attention and row-level PIM operations, improving utilization while minimizing overhead. On a simulated HBM-PIM system, under constrained KV budgets, STARC achieves up to 78% and 65% reductions in attention-layer latency and energy over token-wise sparsity methods, and up to 93% and 92% reductions relative to full attention, while preserving model accuracy.

## 中文摘要

由于频繁的访问以及随上下文长度增长而不断增大的键值（KV）缓存，大语言模型（LLM）的服务对存储系统造成了显著压力。存内计算（PIM）架构提供高内部带宽和近数据计算并行性，但当前的设计面向稠密注意力，在动态 KV 缓存稀疏性的不规则访问模式下表现不佳。为缓解这一局限，我们提出 STARC——一种用于在 PIM 上高效解码 LLM 的稀疏优化（sparsity-optimized）数据映射方案。STARC 对语义相似的 KV 对进行聚类，并将其在 PIM bank 内连续地共置，从而通过将查询与预先计算的质心进行匹配，实现以簇为粒度的检索。这弥合了细粒度稀疏注意力与行级 PIM 操作之间的差距，在最小化开销的同时提升了利用率。在模拟的 HBM-PIM 系统上，在受限的 KV 预算下，相比按 token 的稀疏方法，STARC 将注意力层（attention-layer）延迟和能耗最多降低 78% 和 65%；相比全注意力，最多降低 93% 和 92%，同时保持模型精度。

## 英文关键词

Processing-in-memory (PIM); Large language model (LLM); Sparse attention; KV clustering; KV cache

## 中文关键词

存内计算（PIM）；大语言模型（LLM）；稀疏注意力；KV 聚类；KV 缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790226)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2026](../index.md)
