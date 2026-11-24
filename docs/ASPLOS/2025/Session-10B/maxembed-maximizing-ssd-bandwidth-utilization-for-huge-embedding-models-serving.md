---
title: "MaxEmbed: Maximizing SSD bandwidth utilization for huge embedding models serving"
description: "ASPLOS 2025 · Session 10B · MaxEmbed：最大化巨型嵌入模型服务中的 SSD 带宽利用率"
tags:
  - "ASPLOS2025"
  - "Session 10B"
  - "Solid State Storage"
---

# MaxEmbed: Maximizing SSD bandwidth utilization for huge embedding models serving

**中文标题：** MaxEmbed：最大化巨型嵌入模型服务中的 SSD 带宽利用率

**所属 Session：** [Session 10B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ruwen Fan (Tsinghua University), Minhui Xie (Tsinghua University), Haodi Jiang (Tsinghua University), Youyou Lu (Tsinghua University)

**单位：** Tsinghua University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674172) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Deep learning recommendation models (DLRMs) have gained widespread application across search, advertising, and ecommerce. Still, DLRMs present notable challenges as they depend heavily on large embedding tables to represent sparse features in recommendation systems. This raises concerns about both memory capacity and cost. Solid-state drives (SSDs) offer a cost-effective solution with a significantly larger capacity, but they introduce read amplification issues because of the mismatch between embedding size and SSD read granularity. Prior SSD embedding storage systems aim to tackle these challenges by employing hypergraph partitioning to co-locate co-appearing embeddings onto the same SSD page, alleviating read amplification. However, this approach has a drawback as it divides embeddings into completely disjoint clusters, limiting potential combinations between embeddings. In response to this limitation, we introduce MaxEmbed. Capitalizing on the extensive storage capacity of SSDs, MaxEmbed effectively mines relationships between storage combinations of embeddings with replication, thereby enhancing the effective bandwidth of SSDs. Additionally, MaxEmbed incorporates a corresponding online service module for embedding query request handling, leveraging two key optimizations to reduce the overhead brought by replication. Our evaluations demonstrate that MaxEmbed boosts SSD embedding serving throughput by up to 18.7% under various settings.

## 中文摘要

深度学习推荐模型（DLRM）已在搜索、广告和电商领域得到广泛应用。然而，DLRM 也带来了显著挑战，因为它们严重依赖大型嵌入表来表示推荐系统中的稀疏特征。这引发了对内存容量与成本两方面的担忧。固态盘（SSD）以显著更大的容量提供了一种高性价比的解决方案，但由于嵌入尺寸与 SSD 读粒度不匹配，它们引入了读放大问题。此前的 SSD 嵌入存储系统旨在通过采用超图划分将共同出现的嵌入共置到同一 SSD 页上来应对这些挑战，从而缓解读放大。然而，这种方法存在一个缺陷：它将嵌入划分为完全不相交的簇，限制了嵌入之间可能的组合。针对这一局限，我们提出了 MaxEmbed。借助 SSD 的大容量存储，MaxEmbed 通过副本有效地挖掘嵌入存储组合之间的关系，从而提升 SSD 的有效带宽。此外，MaxEmbed 还包含一个相应的在线服务模块来处理嵌入查询请求，利用两项关键优化来降低副本带来的开销。我们的评估表明，在各种设置下 MaxEmbed 将 SSD 嵌入服务吞吐量提升最高达 18.7%。

## 英文关键词

Embedding models, SSD, Data placement, Data replication

## 中文关键词

嵌入模型；SSD；数据放置；数据复制

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674172)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10B](index.md) · [返回 ASPLOS 2025](../index.md)
