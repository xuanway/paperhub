---
title: "ARMOR: Accelerating RTL Simulation by Mitigating the Front-End Bottleneck Using Node Compression"
description: "MICRO 2026 · Session 7B · ARMOR：利用节点压缩缓解前端瓶颈，加速 RTL 仿真"
tags:
  - "MICRO2026"
  - "Simulation"
  - "RTL"
---

# ARMOR: Accelerating RTL Simulation by Mitigating the Front-End Bottleneck Using Node Compression

**中文标题：** ARMOR：利用节点压缩缓解前端瓶颈，加速 RTL 仿真

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Jiaping Tang, Jianan Mu, Zhiteng Chao, Jingzhong Wen, Jing Ye, Huawei Li

**来源：** MICRO 2026，pp. 2452–2467；[DOI](https://doi.org/10.1109/MICRO67795.2026.00168)

## 英文摘要

Register-transfer level (RTL) simulation is indispensable in chip design. High-performance simulators typically lower each node in the RTL graph into an instruction sequence. Although this per-node lowering enables aggressive compiler optimizations, it dramatically increases the code footprint, severely exceeding instruction cache capacity and causing front-end bottlenecks. Our profiling reveals that over 50% of pipeline stalls are caused by the CPU front-end, becoming a key performance bottleneck in state-of-the-art RTL simulators. However, reaping the optimization benefits of fully unrolling the RTL graph while simultaneously reducing the code footprint to mitigate front-end bottlenecks remains highly challenging. In this paper, we propose ARMOR, an efficient RTL simulator designed to alleviate the front-end bottleneck through node compression. The key idea is to exploit the data parallelism exposed by the unrolling RTL graph and the insufficient bit-space utilization revealed by per-node lowering, leveraging bit-level data parallelism to compress multiple nodes simultaneously, so that a single instruction sequence can serve multiple nodes instead of one per node. To achieve profitable node compression, we first propose a module-aware isomorphic subgraph identification method that leverages structural isomorphism across module instances to systematically identify compression opportunities at the subgraph level. We then propose an alignment-aware dense packing strategy that groups nodes into packs according to dataflow dependencies while preserving data reuse, complemented by greedy merging strategies to enhance bit-space utilization. Finally, we implement a unified bit-level parallelism scheme to support bit-level parallel execution of compressed nodes. Experimental results show that ARMOR compresses 57% of nodes on average, effectively mitigating front-end bottlenecks, and achieving 1.6x speedup on CPU designs and 2.7x speedup on AI accelerators compared to state-of-the-art simulators.

## 中文摘要

寄存器传输级（RTL）仿真在芯片设计中是必不可少的。高性能模拟器通常将 RTL 图中的每个节点降低为指令序列。尽管这种每个节点的降低可以实现积极的编译器优化，但它极大地增加了代码占用空间，严重超出了指令缓存容量并导致前端瓶颈。我们的分析显示，超过 50% 的管道停顿是由 CPU 前端引起的，成为最先进的 RTL 模拟器的关键性能瓶颈。然而，获得完全展开 RTL 图的优化优势，同时减少代码占用空间以缓解前端瓶颈仍然极具挑战性。在本文中，我们提出了 ARMOR，这是一种高效的 RTL 模拟器，旨在通过节点压缩缓解前端瓶颈。其关键思想是利用展开 RTL 图所暴露的数据并行性以及逐节点降低所暴露的位空间利用率不足的问题，利用位级数据并行性同时压缩多个节点，从而使单个指令序列可以服务于多个节点，而不是每个节点一个。为了实现有利可图的节点压缩，我们首先提出了一种模块感知的同构子图识别方法，该方法利用跨模块实例的结构同构来系统地识别子图级别的压缩机会。然后，我们提出了一种对齐感知的密集打包策略，该策略根据数据流依赖性将节点分组为包，同时保留数据重用，并辅之以贪婪合并策略以提高位空间利用率。最后，我们实现了统一的位级并行方案来支持压缩节点的位级并行执行。实验结果表明，ARMOR平均压缩57%的节点，有效缓解前端瓶颈，与最先进的模拟器相比，CPU设计加速1.6倍，AI加速器加速2.7倍。

## 中文关键词

硬件验证；RTL 仿真；前端瓶颈；子图同构；比特级数据并行；节点压缩

## 代码与研究制品

- 代码仓库：[https://github.com/jptang99-star/ARMOR](https://github.com/jptang99-star/ARMOR)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
