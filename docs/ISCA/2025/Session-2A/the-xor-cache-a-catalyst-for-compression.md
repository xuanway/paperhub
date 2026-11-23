---
title: "The XOR Cache: A Catalyst for Compression"
description: "ISCA 2025 · Session 2A · XOR Cache：压缩的催化剂"
tags:
  - "ISCA2025"
  - "Session 2A"
  - "Best Paper Nominees"
---

# The XOR Cache: A Catalyst for Compression

**中文标题：** XOR Cache：压缩的催化剂

**所属 Session：** [Session 2A](index.md) · [ISCA 2025](../index.md)

**作者：** Zhewen Pan, Joshua San Miguel

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730995) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Modern computing systems allocate significant amounts of resources for caching, especially for the last level cache (LLC). We observe that there is untapped potential for compression by leveraging redundancy due to private caching and inclusion that are common in today’s systems. We introduce the XOR Cache to exploit this redundancy via XOR compression. Unlike conventional cache architectures, XOR Cache stores bitwise XOR values of line pairs, halving the number of stored lines via a form of inter-line compression. When combined with other compression schemes, XOR Cache can further boost intra-line compression ratios by XORing lines of similar value, reducing the entropy of the data prior to compression. Evaluation results show that the XOR Cache can save LLC area by 1.93×and power by 1.92× at a cost of 2.06% performance overhead compared to a larger uncompressed cache, reducing energy-delay product by 26.3%.

## 中文摘要

现代计算系统分配大量资源用于缓存，尤其是最后一级缓存 (LLC)。我们观察到，由于当今系统中常见的私有缓存和包含性，通过利用冗余来进行压缩有尚未开发的潜力。我们引入了 XOR 高速缓存，通过 XOR 压缩来利用这种冗余。与传统的缓存架构不同，XOR 缓存存储缓存行对的按位 XOR 值，通过行间压缩的形式将存储的行数减半。当与其他压缩方案结合使用时，XOR Cache 可以通过对相似值的行进行异或来进一步提高行内压缩率，从而降低压缩前数据的熵。评估结果表明，与更大的未压缩缓存相比，XOR Cache 可以节省 1.93 倍的 LLC 面积和 1.92 倍的功耗，但代价是 2.06% 的性能开销，从而将能量-延迟积降低 26.3%。

## 英文关键词

Cache hierarchy, Cache compression, Low-power architecture

## 中文关键词

缓存层次结构, 缓存压缩, 低功耗架构

## 代码与研究制品

- [代码仓库](https://github.com/zhewen404/gem5_xorcache)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730995)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2025](../index.md)
