---
title: "I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention"
description: "ASPLOS 2026 · Session 3A · I/O 分析即所需：面向长序列注意力机制的 I/O 分析"
tags:
  - "ASPLOS2026"
  - "Session 3A"
  - "LLM Attention & KV Cache"
---

# I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention

**中文标题：** I/O 分析即所需：面向长序列注意力机制的 I/O 分析

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xiaoyang Lu (Illinois Institute of Technology), Boyu Long (Institute of Computing Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences), Xiaoming Chen (Institute of Computing Technology, Chinese Academy of Sciences), Yinhe Han (Institute of Computing Technology, Chinese Academy of Sciences), Xian-He Sun (Illinois Institute of Technology)

**单位：** Illinois Institute of Technology；Institute of Computing Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences；Institute of Computing Technology, Chinese Academy of Sciences

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790174) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

As GPUs and other accelerators become increasingly popular, optimizing I/O operations between on-chip and off-chip memory is increasingly critical. I/O analysis, however, is complex, requiring a deep understanding of application dataflow and memory hierarchy. Developing a practical I/O analysis methodology remains a timely challenge. Self-attention is employed extensively in transformer models, but its quadratic memory complexity poses significant challenges to modern memory systems. In this study, we explore how to use I/O analysis to develop optimal solutions for accelerating exact long-sequence self-attention. We first introduce a novel I/O analysis for tall-and-skinny matrix-matrix multiplication, which captures the dominant data movement behavior of long-sequence self-attention. Guided by systematic I/O analysis, we develop AttenIO, an I/O-driven accelerator for exact long-sequence self-attention with three key optimizations: (1) an analytically derived I/O-optimal tiling and scheduling to minimize I/O operations, (2) fine-grained three-level communication-computation overlapping to hide I/O stalls, and (3) parallel execution patterns for efficient softmax. Our evaluation shows that AttenIO achieves a 1.6×8.8× speedup over the state-of-the-art solutions. Although AttenIO is designed for self-attention, it also highlights the broader potential of I/O analysis as a principled foundation for guiding high-performance I/O optimizations.

## 中文摘要

随着 GPU 及其他加速器日益普及，优化片上与片外存储器之间的 I/O 操作正变得愈发关键。然而，I/O 分析本身是复杂的，需要深入理解应用的数据流与存储层次结构。开发一套实用的 I/O 分析方法学仍是一项紧迫的挑战。自注意力在 transformer 模型中被广泛采用，但其二次方的存储复杂度对现代存储系统构成了重大挑战。在本研究中，我们探索如何利用 I/O 分析为加速精确的长序列自注意力推导出最优方案。我们首先针对高瘦矩阵-矩阵乘法（tall-and-skinny matrix-matrix multiplication）提出一种新颖的 I/O 分析，该分析刻画了长序列自注意力的主要数据移动行为。在系统化 I/O 分析的指导下，我们开发了 AttenIO——一个面向精确长序列自注意力的 I/O 驱动加速器，它包含三项关键优化：（1）通过解析推导得到的 I/O 最优分块与调度，以最小化 I/O 操作；（2）细粒度的三级通信-计算重叠，以隐藏 I/O 停顿；（3）面向高效 softmax 的并行执行模式。我们的评估表明，AttenIO 相对最先进方案实现了 1.6×8.8× 的加速。尽管 AttenIO 是为自注意力而设计的，它同时也凸显了 I/O 分析作为指导高性能 I/O 优化的原理性基础所具有的更广泛潜力。

## 英文关键词

I/O Analysis; Dataflow Optimization; Attention Acceleration; Accelerator Architecture

## 中文关键词

I/O 分析；数据流优化；注意力加速；加速器架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790174)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2026](../index.md)
