---
title: "The Path to BTB Storage Efficiency Goes Through Tags"
description: "MICRO 2026 · Session 7D · 通过标签提高分支目标缓冲区存储效率"
tags:
  - "MICRO2026"
  - "Storage"
---

# The Path to BTB Storage Efficiency Goes Through Tags

**中文标题：** 通过标签提高分支目标缓冲区存储效率

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Roman K. Brunner, Rakesh Kumar

**来源：** MICRO 2026，pp. 2640–2653；[DOI](https://doi.org/10.1109/MICRO67795.2026.00180)

## 英文摘要

Modern server workloads exhibit multi-megabyte code footprints that overwhelm front-end structures such as the branch target buffer (BTB), leading to frequent misses and significant performance degradation. BTB misses are particularly costly, as they trigger pipeline flushes, expose fetch latency, and reduce the effectiveness of fetch-directed instruction prefetching. To mitigate these effects, modern processors deploy increasingly large BTBs, often requiring hundreds of kilobytes of storage. However, this trend is becoming untenable due to area, energy, and sustainability constraints. Recent work has aggressively optimized branch target representation, shifting the storage bottleneck from targets to tags. We observe that tags now dominate BTB storage and, more importantly, exhibit substantial redundancy as only 23.7% of entries contain unique tags in a 2K-entry BTB, decreasing to just 1.1% at 32K entries. This paper leverages this insight to improve BTB storage efficiency. We propose LiteBTB, a storage-efficient BTB design that eliminates tag redundancy by storing each unique tag once in a centralized structure called the Unique Tag Buffer (UTB) and replacing per-entry tags with compact pointers. To avoid increasing access latency, LiteBTB accesses the UTB and BTB in parallel. Our evaluation shows that LiteBTB reduces BTB storage by 5.4% to 13.1% compared to the state-of-the-art BTB-X, for storing 2K to 32K branches while providing similar performance.

## 中文摘要

现代服务器工作负载表现出多兆字节的代码占用量，压垮了分支目标缓冲区 (BTB) 等前端结构，导致频繁丢失和性能显着下降。 BTB 未命中的代价尤其高昂，因为它们会触发管道刷新、暴露提取时延并降低提取导向指令预取的有效性。为了减轻这些影响，现代处理器部署了越来越大的 BTB，通常需要数百 KB 的存储空间。然而，由于面积、能源和可持续性的限制，这种趋势变得难以为继。最近的工作积极优化了分支目标表示，将存储瓶颈从目标转移到标签。我们观察到标签现在在 BTB 存储中占据主导地位，更重要的是，它表现出大量的冗余，因为在 2K 条目 BTB 中只有 23.7% 的条目包含唯一标签，而在 32K 条目时则减少到仅 1.1%。本文利用这一见解来提高 BTB 存储效率。我们提出了 LiteBTB，这是一种高效存储的 BTB 设计，通过将每个唯一标签一次存储在称为唯一标签缓冲区 (UTB) 的集中式结构中，并用紧凑指针替换每个条目标签，从而消除标签冗余。为了避免增加访问时延，LiteBTB并行访问UTB和BTB。我们的评估表明，与最先进的 BTB-X 相比，LiteBTB 将 BTB 存储减少了 5.4% 至 13.1%，可存储 2K 至 32K 分支，同时提供相似的性能。

## 中文关键词

分支目标缓冲区；标签压缩；存储效率；分支预测

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
