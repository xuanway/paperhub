---
title: "RFUSE: Modernizing Userspace Filesystem Framework through Scalable Kernel-Userspace Communication"
description: "FAST 2024 · File Systems · 第 141–158 页"
tags:
  - "FAST2024"
  - "File Systems"
---

# RFUSE: Modernizing Userspace Filesystem Framework through Scalable Kernel-Userspace Communication

**中文标题**：RFUSE：通过可扩展的内核—用户态通信实现用户态文件系统框架现代化

**Session**：File Systems · 2024-02-27 15:45–17:00 · Chair：Peter Macko（MongoDB）

**作者**：Kyu-Jin Cho, Jaewon Choi, Hyungjoon Kwon, and Jin-Soo Kim, Seoul National University

**会议**：FAST 2024 · Santa Clara, CA · 第 141–158 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/cho](https://www.usenix.org/conference/fast24/presentation/cho)

**论文 PDF**：[fast24-cho.pdf](https://www.usenix.org/system/files/fast24-cho.pdf)

---

## 英文摘要

With the advancement of storage devices and the increasing scale of data, filesystem design has transformed in response to this progress. However, implementing new features within an in-kernel filesystem is a challenging task due to development complexity and code security concerns. As an alternative, userspace filesystems are gaining attention, owing to their ease of development and reliability. FUSE is a renowned framework that allows users to develop custom filesystems in userspace. However, the complex internal stack of FUSE leads to notable performance overhead, which becomes even more prominent in modern hardware environments with high-performance storage devices and a large number of cores.

In this paper, we present RFUSE, a novel userspace filesystem framework that utilizes scalable message communication between the kernel and userspace. RFUSE employs a per-core ring buffer structure as a communication channel and effectively minimizes transmission overhead caused by context switches and request copying. Furthermore, RFUSE enables users to utilize existing FUSE-based filesystems without making any modifications. Our evaluation results indicate that RFUSE demonstrates comparable throughput to in-kernel filesystems on high-performance devices while exhibiting high scalability in both data and metadata operations.

## 中文摘要

随着存储设备的进步和数据规模的日益增长，文件系统设计也因应这些进展而转变。然而，由于开发复杂性和代码安全顾虑，在内核文件系统中实现新功能是一项艰巨任务。作为一种替代方案，用户态文件系统因其易于开发和可靠性而受到关注。FUSE 是一个著名框架，允许用户在用户态开发自定义文件系统。然而，FUSE 复杂的内部栈导致显著的性能开销，在高性能存储设备和大规模多核的现代硬件环境中尤为突出。

本文提出 RFUSE，一个新颖的用户态文件系统框架，利用内核与用户态之间可扩展的消息通信。RFUSE 采用每核环形缓冲区结构作为通信通道，并有效最小化上下文切换和请求拷贝带来的传输开销。此外，RFUSE 使用户能够使用现有的基于 FUSE 的文件系统而无需任何修改。我们的评估结果表明，RFUSE 在高性能设备上展现出与内核文件系统相当的吞吐量，同时在数据和元数据操作方面都具有高可扩展性。
