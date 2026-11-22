---
title: "NiF: Hybrid In-Flash and In-Storage Acceleration for Approximate Nearest Neighbor Search"
description: "MICRO 2026 · Session 4A · NiF：面向近似最近邻搜索的闪存内与存储内混合加速"
tags:
  - "MICRO2026"
  - "Storage"
---

# NiF: Hybrid In-Flash and In-Storage Acceleration for Approximate Nearest Neighbor Search

**中文标题：** NiF：面向近似最近邻搜索的闪存内与存储内混合加速

**所属 Session：** [Session 4A](index.md) · [MICRO 2026](../index.md)

**作者：** Myoungjun Chun, Jaeyong Lee, Gwuiin Kim, Minhyeong Kim, Inhyuk Choi, Myungsuk Kim, Nam Sung Kim, Jihong Kim

**来源：** MICRO 2026，pp. 1332–1348；[DOI](https://doi.org/10.1109/MICRO67795.2026.00100)

## 英文摘要

While approximate nearest neighbor search (ANNS) has become a key primitive in modern AI applications, achieving scalability, efficiency, and accuracy on billion-scale vector datasets remains challenging. In-storage processing (ISP)-based ANNS offers strong potential by storing vectors in high-capacity SSDs and returning only search results to the host. However, existing ISP-based ANNS is constrained by two fundamental limitations. First, the high raw bit error rate of modern NAND flash memory forces costly error mitigation before computation, sacrificing either scalability or efficiency. Second, the two main compute placements for ISP-based ANNS—at the SSD controller and inside flash chips—create a fundamental tradeoff between performance and implementation overhead. To address these limitations, we propose NiF, a new ISP-based ANNS technique that enables scalable, efficient, and accurate billion-scale ANNS by unifying a lightweight in-flash accelerator with controller-side processing. NiF is enabled by two key innovations. First, NiF inverts the error-mitigation-first, compute-later pipeline of existing ISP-based ANNS to reduce error-mitigation overhead: it performs in-flash computation without prior error mitigation and invokes controller-side correction only when needed. Second, NiF employs cluster-wise exponent sharing to reduce the in-flash computation overhead: it enables lightweight integer-MAC-based distance computation using a block floating-point representation. Across four billion-scale vector datasets, NiF achieves 1.7× higher ANNS throughput than a state-of-the-art ISP-based ANNS design, while preserving accuracy.

## 中文摘要

虽然近似最近邻搜索（ANNS）已成为现代人工智能应用中的关键原语，但在数十亿规模的矢量数据集上实现可扩展性、效率和准确性仍然具有挑战性。基于存储内处理 (ISP) 的 ANNS 通过将向量存储在大容量 SSD 中并仅将搜索结果返回给主机，提供了强大的潜力。然而，现有的基于 ISP 的 ANNS 受到两个基本限制的限制。首先，现代 NAND 闪存的高原始误码率迫使在计算之前进行代价高昂的错误缓解，从而牺牲了可扩展性或效率。其次，基于 ISP 的 ANNS 的两个主要计算位置（SSD 控制器和闪存芯片内部）在性能和实现开销之间建立了基本的权衡。为了解决这些限制，我们提出了 NiF，这是一种基于 ISP 的新型 ANNS 技术，通过将轻量级闪存内加速器与控制器端处理相结合，实现可扩展、高效且准确的十亿级 ANNS。 NiF 由两项关键创新推动。首先，NiF 反转了现有基于 ISP 的 ANN 的先错误缓解、后计算的管道，以减少错误缓解开销：它执行闪存内计算，无需事先缓解错误，并且仅在需要时调用控制器端校正。其次，NiF 采用集群式指数共享来减少闪存内计算开销：它使用块浮点表示来实现轻量级基于整数 MAC 的距离计算。在四个十亿级向量数据集上，NiF 的 ANNS 吞吐量达到最先进的基于 ISP 的 ANNS 设计的 1.7 倍，同时保持准确性。

## 中文关键词

固态硬盘；NAND 闪存；存储内处理；近似最近邻搜索

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4A](index.md) · [MICRO 2026 主页](../index.md)
