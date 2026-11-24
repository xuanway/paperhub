---
title: "TeRM: Extending RDMA-Attached Memory with SSD"
description: "FAST 2024 · Distributed Storage · 第 1–16 页"
tags:
  - "FAST2024"
  - "Distributed Storage"
---

# TeRM: Extending RDMA-Attached Memory with SSD

**中文标题**：TeRM：用 SSD 扩展 RDMA 附加内存

**Session**：Distributed Storage · 2024-02-27 10:45–12:00 · Chair：Raju Rangaswami（Florida International University）

**作者**：Zhe Yang, Qing Wang, Xiaojian Liao, and Youyou Lu, Tsinghua University; Keji Huang, Huawei Technologies Co., Ltd; Jiwu Shu, Tsinghua University

**会议**：FAST 2024 · Santa Clara, CA · 第 1–16 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/yang-zhe](https://www.usenix.org/conference/fast24/presentation/yang-zhe)

**论文 PDF**：[fast24-yang-zhe.pdf](https://www.usenix.org/system/files/fast24-yang-zhe.pdf)

---

## 英文摘要

RDMA-based in-memory storage systems offer high performance but are restricted by the capacity of physical memory. In this paper, we propose TeRM to extend RDMA-attached memory with SSD. TeRM achieves fast remote access on the SSD-extended memory by eliminating page faults of RDMA NIC and CPU from the critical path. We also introduce a set of techniques to reduce the consumption of CPU and network resources. Evaluation shows that TeRM performs close to the performance of the ideal upper bound where all pages are pinned in the physical memory. Compared with existing approaches TeRM significantly improves the performance of unmodified RDMA-based storage systems, including a file system and a key-value system.

## 中文摘要

基于 RDMA 的内存存储系统提供高性能，但受限于物理内存容量。本文提出 TeRM，用 SSD 扩展 RDMA 附加内存。TeRM 通过将 RDMA 网卡和 CPU 的缺页处理从关键路径中消除，实现 SSD 扩展内存上的快速远程访问。我们还引入一系列技术来降低 CPU 和网络资源消耗。评估表明，TeRM 的性能接近所有页面都固定在物理内存中的理想上限。与现有方法相比，TeRM 显著提升了未经修改的基于 RDMA 的存储系统（包括一个文件系统和一个键值系统）的性能。
