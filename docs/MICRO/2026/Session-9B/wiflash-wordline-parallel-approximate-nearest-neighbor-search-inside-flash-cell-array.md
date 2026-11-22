---
title: "WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array"
description: "MICRO 2026 · Session 9B · WiFlash：闪存单元阵列内的字线并行近似最近邻搜索"
tags:
  - "MICRO2026"
---

# WiFlash: Wordline-Parallel Approximate Nearest Neighbor Search Inside Flash Cell Array

**中文标题：** WiFlash：闪存单元阵列内的字线并行近似最近邻搜索

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Hyunjin Kim, Juchan Lee, Inseong Choi, Jinho Lee, Jae-Joon Kim

**来源：** MICRO 2026，pp. 3297–3314；[DOI](https://doi.org/10.1109/MICRO67795.2026.00221)

## 英文摘要

Nearest neighbor search (NNS) is a fundamental operation for retrieving semantically similar vectors from large-scale vector databases and serves as a core building block for applications such as recommendation, semantic search, and retrieval-augmented generation (RAG). To improve performance, approximate nearest neighbor search (ANNS) is widely adopted, trading a small amount of accuracy for reduced latency. In personal AI systems such as AI personal computers (PCs), large vector databases often reside in NAND flash memory due to limited DRAM capacity. However, the limited I/O bandwidth and high data movement cost of flash significantly degrade ANNS performance. Moreover, due to the interactive nature of personal AI workloads, queries are typically processed with a batch size of one, where graph-based ANNS methods that rely on batching for efficient memory access become less effective. In-flash processing has emerged as a promising solution by exploiting the high internal bandwidth of flash cell arrays. Nevertheless, existing architectures remain fundamentally constrained by single-wordline access, limiting achievable throughput. This paper proposes WiFlash, a new in-flash processing architecture for efficient ANNS in personal AI systems. WiFlash enables reliable multi-wordline access within flash cell arrays, significantly increasing internal bandwidth. It further introduces a TCAM-based similarity search mechanism with an input double-sampling scheme to achieve high-accuracy filtering while preserving parallelism. As a result, WiFlash performs similarity computation directly inside NAND flash and filters out 99.5% of vectors with negligible accuracy loss (recall difference < 0.005). Experimental results across multiple datasets show that WiFlash achieves a 7.2× speedup over state- of-the-art designs with only 1.7% additional area overhead, while improving in-flash similarity search throughput by 2.8× (INT8) and 5.7× (FP32).

## 中文摘要

最近邻搜索 (NNS) 是从大规模向量数据库中检索语义相似向量的基本操作，并且是推荐、语义搜索和检索增强生成 (RAG) 等应用的核心构建块。为了提高性能，近似最近邻搜索（ANNS）被广泛采用，以少量的精度换取减少的时延。在人工智能个人计算机（PC）等个人人工智能系统中，由于 DRAM 容量有限，大型矢量数据库通常驻留在 NAND 闪存中。然而，有限的 I/O 带宽和闪存的高数据移动成本显着降低了 ANNS 性能。此外，由于个人 AI 工作负载的交互性质，查询通常以批量大小 1 进行处理，其中依赖批处理来实现高效内存访问的基于图的 ANNS 方法变得不太有效。通过利用闪存单元阵列的高内部带宽，闪存内处理已成为一种有前景的解决方案。然而，现有架构仍然从根本上受到单字线访问的限制，从而限制了可实现的吞吐量。本文提出了 WiFlash，这是一种新的闪存内处理架构，可在个人人工智能系统中实现高效的 ANNS。 WiFlash 可在闪存单元阵列内实现可靠的多字线访问，从而显着增加内部带宽。它还引入了基于 TCAM 的相似性搜索机制和输入双采样方案，以在保持并行性的同时实现高精度过滤。因此，WiFlash 直接在 NAND 闪存内部执行相似性计算，并过滤掉 99.5% 的向量，精度损失可以忽略不计（召回差异 < 0.005）。跨多个数据集的实验结果表明，WiFlash 比最先进的设计实现了 7.2 倍的加速，仅增加了 1.7% 的区域开销，同时将闪存内相似性搜索吞吐量提高了 2.8 倍 (INT8) 和 5.7 倍 (FP32)。

## 中文关键词

NAND 闪存；近似最近邻搜索；闪存内处理；字线并行

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21489392](https://doi.org/10.5281/zenodo.21489392)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
