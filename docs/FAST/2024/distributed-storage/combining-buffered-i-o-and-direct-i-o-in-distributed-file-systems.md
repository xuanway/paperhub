---
title: "Combining Buffered I/O and Direct I/O in Distributed File Systems"
description: "FAST 2024 · Distributed Storage · 第 17–34 页"
tags:
  - "FAST2024"
  - "Distributed Storage"
---

# Combining Buffered I/O and Direct I/O in Distributed File Systems

**中文标题**：在分布式文件系统中结合缓冲 I/O 与直接 I/O

**Session**：Distributed Storage · 2024-02-27 10:45–12:00 · Chair：Raju Rangaswami（Florida International University）

**作者**：Yingjin Qian, Data Direct Networks; Marc-André Vef, Johannes Gutenberg University Mainz; Patrick Farrell and Andreas Dilger, Whamcloud Inc.; Xi Li and Shuichi Ihara, Data Direct Networks; Yinjin Fu, Sun Yat-Sen University; Wei Xue, Tsinghua University and Qinghai University; André Brinkmann, Johannes Gutenberg University Mainz

**会议**：FAST 2024 · Santa Clara, CA · 第 17–34 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/qian](https://www.usenix.org/conference/fast24/presentation/qian)

**论文 PDF**：[fast24-qian.pdf](https://www.usenix.org/system/files/fast24-qian.pdf)

---

## 英文摘要

Direct I/O allows I/O requests to bypass the Linux page cache and was introduced over 20 years ago as an alternative to the default buffered I/O mode. However, high-performance computing (HPC) applications still mostly rely on buffered I/O, even if direct I/O could perform better in a given situation. This is because users tend to use the I/O mode they are most familiar with. Moreover, with complex distributed file systems and applications, it is often unclear which I/O mode to use.

In this paper, we show under which conditions both I/O modes are beneficial and present a new transparent approach that dynamically switches to each I/O mode within the file system. Its decision is based not only on the I/O size but also on file lock contention and memory constraints. We exemplary implemented our design into the Lustre client and server and extended it with additional features, e.g., delayed allocation. Under various conditions and real-world workloads, our approach achieved up to 3× higher throughput than the original Lustre and outperformed other distributed file systems that include varying degrees of direct I/O support by up to 13×.

## 中文摘要

直接 I/O 允许 I/O 请求绕过 Linux 页缓存，它于 20 多年前作为默认缓冲 I/O 模式的替代方案被引入。然而，高性能计算（HPC）应用仍大多依赖缓冲 I/O，即使在特定情况下直接 I/O 可能表现更好。这是因为用户倾向于使用自己最熟悉的 I/O 模式。此外，面对复杂的分布式文件系统和应用，人们往往不清楚该使用哪种 I/O 模式。

本文展示了两种 I/O 模式在哪些条件下各自有益，并提出一种新的透明方法，在文件系统内部动态切换 I/O 模式。其决策不仅基于 I/O 大小，还基于文件锁竞争和内存约束。我们示例性地将该设计实现到 Lustre 客户端和服务器中，并用延迟分配等附加功能对其进行了扩展。在各种条件和真实负载下，我们的方法比原始 Lustre 取得最高 3 倍的吞吐量提升，并且比其他具有不同程度直接 I/O 支持的分布式文件系统高出最多 13 倍。
