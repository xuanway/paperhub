---
title: "FastAP: Unleashing Bit-Level Parallelism in Associative Processor Architectures."
description: "MICRO 2026 · Session 9B · FastAP：释放关联处理器架构中的比特级并行性"
tags:
  - "MICRO2026"
---

# FastAP: Unleashing Bit-Level Parallelism in Associative Processor Architectures.

**中文标题：** FastAP：释放关联处理器架构中的比特级并行性

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Socrates S. Wong, Cecilio C. Tamarit, Rajit Manohar, José F. Martínez

**来源：** MICRO 2026，pp. 3330–3343；[DOI](https://doi.org/10.1109/MICRO67795.2026.00223)

## 英文摘要

Associative processors (APs) are an approach to processing-using-memory (PUM) that relies entirely on bulk searches and updates to content-addressable storage to perform computation. APs map cleanly to general-purpose vector ISAs and have been shown to deliver large speedups over area-equivalent out-of-order CPUs and GPUs, primarily by enabling massive data-level parallelism across tens of thousands of vector elements. Still, modern APs implement arithmetic as long bit-serial sweeps across chains of smaller bit-sliced subarrays and underutilize the massive data-level parallelism these architectures can offer. We present FastAP, an improved AP microarchitecture that enables more efficient implementations of arithmetic instructions by relying on "chain-aware" enhancements that unleash bit-parallelism: (1) an execution model that allows subarray chains to be logically split into co-operating sub-chains, and to pipeline their microprograms; and (2) a new set of micro-operations (e.g., masked search, tag writeback, and tag broadcast) that expose these capabilities. Experiments show a dramatic reduction in AP vector instruction latency, resulting in average (peak) speedups of 1.78x and 2.87x (6.53x and 7.96x) relative to a state-of-the-art AP design running a diverse set of integer and floating-point applications, respectively. Furthermore, by opportunistically employing a redundant binary internal representation, average (peak) speedups further improve to 1.92x and 4.07x (8.25x and 12.81x), respectively.

## 中文摘要

关联处理器 (AP) 是一种使用内存进行处理 (PUM) 的方法，完全依赖于对内容可寻址存储的批量搜索和更新来执行计算。 AP 干净地映射到通用矢量 ISA，并且已被证明可以比面积等效的无序 CPU 和 GPU 提供大幅加速，主要是通过在数万个矢量元素上实现大规模数据级并行。尽管如此，现代 AP 仍以长位串行扫描较小位片子阵列链的方式实现算术，并且未充分利用这些架构可以提供的大规模数据级并行性。我们提出了 FastAP，一种改进的 AP 微体系结构，通过依赖释放位并行性的“链感知”增强功能，可以更有效地实现算术指令：（1）一个执行模型，允许子阵列链在逻辑上分为协作子链，并通过管道传输它们的微程序； (2) 一组新的微操作（例如，屏蔽搜索、标签写回和标签广播），用于公开这些功能。实验表明，与运行各种整数和浮点应用程序的最先进的 AP 设计相比，AP 向量指令时延显着减少，平均（峰值）加速分别为 1.78 倍和 2.87 倍（6.53 倍和 7.96 倍）。此外，通过机会性地采用冗余二进制内部表示，平均（峰值）加速分别进一步提高到 1.92 倍和 4.07 倍（8.25 倍和 12.81 倍）。

## 中文关键词

联想处理器；利用存储器计算；向量架构；比特级并行性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
