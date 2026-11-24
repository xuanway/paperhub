---
title: "Efficient Lossless Compression of Scientific Floating-Point Data on CPUs and GPUs"
description: "ASPLOS 2025 · Session 4C · 面向 CPU 与 GPU 的科学浮点数据高效无损压缩"
tags:
  - "ASPLOS2025"
  - "Session 4C"
  - "Potpourri 1"
---

# Efficient Lossless Compression of Scientific Floating-Point Data on CPUs and GPUs

**中文标题：** 面向 CPU 与 GPU 的科学浮点数据高效无损压缩

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Noushin Azami (Department of Computer Science, Texas State University), Alex Fallin (Department of Computer Science, Texas State University), Martin Burtscher (Department of Computer Science, Texas State University)

**单位：** Department of Computer Science, Texas State University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707280) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The amount of scientific data being produced, transferred, and processed increases rapidly. Whereas GPUs have made faster processing possible, storage limitations and slow data transfers remain key bottlenecks. Data compression can help, but only if it does not create a new bottleneck. This paper presents four new lossless compression algorithms for singleand double-precision data that compress well and are fast even though they are fully compatible between CPUs and GPUs. Averaged over many SDRBench inputs, our implementations outperform most of the 18 compressors from the literature we compare to in compression ratio, compression throughput, and decompression throughput. Moreover, they outperform all of them in either throughput or compression ratio on the two CPUs and two GPUs we used for evaluation. For example, on an RTX 4090 GPU, our fastest code compresses and decompresses at over 500 GB/s while delivering one of the highest compression ratios.

## 中文摘要

科学数据的产生、传输与处理量正在快速增长。尽管 GPU 使更快的处理成为可能，但存储限制与缓慢的数据传输仍是主要瓶颈。数据压缩可以提供帮助，但前提是它不会制造新的瓶颈。本文提出四种新的无损压缩算法，面向单精度与双精度数据，压缩效果好且速度快，同时在 CPU 与 GPU 之间完全兼容。在众多 SDRBench 输入上取平均，我们的实现在压缩率、压缩吞吐率与解压吞吐率方面优于我们所对比的文献中 18 个压缩器中的大多数。此外，在我们评测所用的两个 CPU 和两个 GPU 上，它们在吞吐率或压缩率之一上均优于所有这些压缩器。例如，在 RTX 4090 GPU 上，我们最快的代码压缩与解压速度超过 500 GB/s，同时提供最高的压缩率之一。

## 英文关键词

Data Compression; Lossless Compression; Floatingpoint Data; CPU and GPU Parallelization

## 中文关键词

数据压缩；无损压缩；浮点数据；CPU 与 GPU 并行化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707280)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2025](../index.md)
