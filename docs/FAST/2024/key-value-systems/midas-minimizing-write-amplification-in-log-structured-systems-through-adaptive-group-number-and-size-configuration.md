---
title: "MIDAS: Minimizing Write Amplification in Log-Structured Systems through Adaptive Group Number and Size Configuration"
description: "FAST 2024 · Key-Value Systems · 第 259–276 页"
tags:
  - "FAST2024"
  - "Key-Value Systems"
---

# MIDAS: Minimizing Write Amplification in Log-Structured Systems through Adaptive Group Number and Size Configuration

**中文标题**：MIDAS：通过自适应组数量与大小配置最小化日志结构系统中的写放大

**Session**：Key-Value Systems · 2024-02-28 14:00–15:40 · Chair：Angela Demke Brown（University of Toronto）

**作者**：Seonggyun Oh, Jeeyun Kim, and Soyoung Han, DGIST; Jaeho Kim, Gyeongsang National University; Sungjin Lee, DGIST; Sam H. Noh, Virginia Tech

**会议**：FAST 2024 · Santa Clara, CA · 第 259–276 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/oh](https://www.usenix.org/conference/fast24/presentation/oh)

**论文 PDF**：[fast24-oh.pdf](https://www.usenix.org/system/files/fast24-oh.pdf)

---

## 英文摘要

Log-structured systems are widely used in various applications because of its high write throughput. However, high garbage collection (GC) cost is widely regarded as the primary obstacle for its wider adoption. There have been numerous attempts to alleviate GC overhead, but with ad-hoc designs. This paper introduces MiDAS that minimizes GC overhead in a systematic and analytic manner. It employs a chain-like structure of multiple groups, automatically segregating data blocks by age. It employs analytical models, Update Interval Distribution (UID) and Markov-Chain-based Analytical Model (MCAM), to dynamically adjust the number of groups as well as their sizes according to the workload I/O patterns, thereby minimizing the movement of data blocks. Furthermore, MiDAS isolates hot blocks into a dedicated *HOT* group, where the size of *HOT* is dynamically adjusted according to the workload to minimize overall WAF. Our experiments using simulations and a proof-of-concept prototype for flash-based SSDs show that MiDAS outperforms state-of-the-art GC techniques, offering 25% lower WAF and 54% higher throughput, while consuming less memory and CPU cycles.

## 中文摘要

日志结构系统因其高写吞吐量而被广泛用于各种应用。然而，高垃圾回收（GC）成本被普遍视为其更广泛采用的主要障碍。已有大量尝试来缓解 GC 开销，但都是临时性设计。本文提出 MiDAS，以系统化和分析化的方式最小化 GC 开销。它采用由多个组构成的链状结构，按数据年龄自动分离数据块。它采用更新间隔分布（UID）和基于马尔可夫链的分析模型（MCAM）这两个分析模型，根据负载 I/O 模式动态调整组数量及其大小，从而最小化数据块的移动。此外，MiDAS 将热块隔离到一个专用的 *HOT* 组中，*HOT* 的大小根据负载动态调整，以最小化总体 WAF。我们使用仿真和基于闪存 SSD 的概念验证原型进行实验，结果表明 MiDAS 优于最先进的 GC 技术，WAF 低 25%，吞吐量高 54%，同时消耗更少的内存和 CPU 周期。
