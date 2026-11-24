---
title: "Optimizing File Systems on Heterogeneous Memory by Integrating DRAM Cache with Virtual Memory Management"
description: "FAST 2024 · Caching · 第 71–88 页"
tags:
  - "FAST2024"
  - "Caching"
---

# Optimizing File Systems on Heterogeneous Memory by Integrating DRAM Cache with Virtual Memory Management

**中文标题**：通过将 DRAM 缓存与虚拟内存管理集成来优化异构内存上的文件系统

**Session**：Caching · 2024-02-27 14:00–15:15 · Chair：Carl Waldspurger（Carl Waldspurger Consulting）

**作者**：Yubo Liu, Yuxin Ren, Mingrui Liu, Hongbo Li, Hanjun Guo, Xie Miao, and Xinwei Hu, Huawei Technologies Co., Ltd.; Haibo Chen, Huawei Technologies Co., Ltd. and Shanghai Jiao Tong University

**会议**：FAST 2024 · Santa Clara, CA · 第 71–88 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/liu-yubo](https://www.usenix.org/conference/fast24/presentation/liu-yubo)

**论文 PDF**：[fast24-liu-yubo.pdf](https://www.usenix.org/system/files/fast24-liu-yubo.pdf)

---

## 英文摘要

This paper revisits the usage of DRAM cache in DRAM-PM heterogeneous memory file systems. With a comprehensive analysis of existing file systems with cache-based and DAX-based designs, we show that both suffer from suboptimal performance due to excessive data movement. To this end, this paper presents a cache management layer atop heterogeneous memory, namely FLAC, which integrates DRAM cache with virtual memory management. FLAC is further incorporated with two techniques called zero-copy caching and parallel-optimized cache management, which facilitates fast data transfer between file systems and applications as well as efficient data synchronization/migration between DRAM and PM. We further design and implement a library file system upon FLAC, called FlacFS. Micro benchmarks show that FlacFS provides up to two orders of magnitude performance improvement over existing file systems in file read/write. With real-world applications, FlacFS achieves up to 10.6 and 9.9 times performance speedup over state-of-the-art DAX-based and cache-based file systems, respectively.

## 中文摘要

本文重新审视 DRAM 缓存在 DRAM-PM 异构内存文件系统中的使用。通过对现有基于缓存和基于 DAX 设计的文件系统进行全面分析，我们表明两者都因过度的数据移动而性能欠佳。为此，本文提出一种位于异构内存之上的缓存管理层 FLAC，它将 DRAM 缓存与虚拟内存管理集成。FLAC 进一步结合零拷贝缓存和并行优化缓存管理这两项技术，从而促进文件系统与应用之间的快速数据传输，以及 DRAM 与 PM 之间的高效数据同步/迁移。我们进一步在 FLAC 之上设计并实现了一个库文件系统 FlacFS。微基准表明，FlacFS 在文件读写方面比现有文件系统提供最高两个数量级的性能提升。在真实应用中，FlacFS 相比最先进的基于 DAX 和基于缓存的文件系统分别取得最高 10.6 倍和 9.9 倍的性能加速。
