---
title: "Loop-Decoupled Prefetcher for Linked Data Structure"
description: "MICRO 2026 · Session 6A · 面向链式数据结构的循环解耦预取器"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# Loop-Decoupled Prefetcher for Linked Data Structure

**中文标题：** 面向链式数据结构的循环解耦预取器

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Pengchen Zong, Gelin Fu, Qiang Luo, Yijiang Kong, Chenzhun Guo, Wenzhe Zhao, Pengju Ren, Tian Xia

**来源：** MICRO 2026，pp. 1815–1831；[DOI](https://doi.org/10.1109/MICRO67795.2026.00129)

## 英文摘要

Linked Data Structures (LDS) are widely used in databases, graph analysis, and operating system. To access such structures, intensive pointer-chasing accesses are performed, which have poor data locality and result in frequent memory stalls. Several LDS prefetchers have been proposed to resolve this memory bottleneck, which mainly exploits the work available in a single LDS chain. However, LDS in real-world applications is often constructed in nested loops, which makes it hard for them to efficiently detect and prefetch. This paper introduces Loop-Decoupled Prefetcher (LDP), an efficient prefetcher that captures the patterns of LDS traversal in nested loops and prefetch future loops for high timeliness. LDP exploits the numerical patterns in LDS, and introduces a novel loop decoupling method to eliminate interference between instructions. It also employs a bidirectional detection method, enabling it to explore from different initial instructions and construct the complete access pattern. Based on the identified relationships between different loop layers, LDP conducts cross-loop prefetching to address the untimeliness of pointer-chasing prefetching. Evaluation in 13 applications shows that LDP achieves an average 1.7× speedup against state-of-the-art hard-ware prefetchers and 1.29× against state-of-the-art compiler-based prefetchers, while incurring only 1.04% area overhead over a commercial processor.

## 中文摘要

链接数据结构（LDS）广泛应用于数据库、图形分析和操作系统。为了访问此类结构，需要执行密集的指针追踪访问，这会导致数据局部性较差并导致频繁的内存停顿。为了解决这个内存瓶颈，人们提出了几种 LDS 预取器，这些预取器主要利用单个 LDS 链中的可用工作。然而，现实应用中的 LDS 通常是在嵌套循环中构建的，这使得它们很难有效地检测和预取。本文介绍了循环解耦预取器 (LDP)，这是一种高效的预取器，可捕获嵌套循环中的 LDS 遍历模式并预取未来循环以实现高及时性。 LDP 利用 LDS 中的数值模式，并引入了一种新颖的循环解耦方法来消除指令之间的干扰。它还采用双向检测方法，使其能够从不同的初始指令进行探索并构建完整的访问模式。 LDP根据识别的不同循环层之间的关系，进行跨循环预取，以解决指针追踪预取的不及时性。对 13 个应用程序的评估表明，LDP 相对于最先进的硬件预取器平均加速 1.7 倍，相对于最先进的基于编译器的预取器平均加速 1.29 倍，而与商用处理器相比，仅产生 1.04% 的面积开销。

## 中文关键词

链式数据结构；预取；指针追逐；循环解耦

## 代码与研究制品

- 代码仓库：[https://github.com/Zongpc/LDP-gem5](https://github.com/Zongpc/LDP-gem5)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21502244](https://doi.org/10.5281/zenodo.21502244)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
