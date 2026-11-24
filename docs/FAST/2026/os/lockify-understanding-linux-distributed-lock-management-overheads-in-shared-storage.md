---
title: "Lockify: Understanding Linux Distributed Lock Management Overheads in Shared Storage"
description: "FAST 2026 · OS · 第 691–700 页"
tags:
  - "FAST2026"
  - "OS"
---

# Lockify: Understanding Linux Distributed Lock Management Overheads in Shared Storage

**中文标题**：Lockify：理解共享存储中 Linux 分布式锁管理的开销

**Session**：OS · 2026-02-26 15:50–17:10 · Chair：Yu Liang（ETH Zurich）

**作者**：Taeyoung Park, Yunjae Jo, Daegyu Han, Beomseok Nam, and Jaehyun Hwang, Sungkyunkwan University

**会议**：FAST 2026 · Santa Clara, CA · 第 691–700 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/park](https://www.usenix.org/conference/fast26/presentation/park)

**论文 PDF**：[fast26-park.pdf](https://www.usenix.org/system/files/fast26-park.pdf)

---

## 英文摘要

This paper presents Lockify, a novel distributed lock manager (DLM) for shared-disk file systems. Our key observation in shared-storage scenarios is that, for file or directory creation, lock acquisition overhead in the Linux kernel DLM increases with the number of clients, even in low-contention scenarios. Lockify minimizes this lock acquisition latency by avoiding unnecessary communication with remote directory nodes through *self-owner notifications* and *asynchronous ownership management*. We implement Lockify in the Linux kernel and evaluate its performance on real-world workloads using two representative shared-disk file systems, GFS2 and OCFS2. Our experimental results demonstrate that Lockify improves overall throughput by ~6.4× compared to the kernel DLM and O2CB, consistently across different numbers of clients.

## 中文摘要

本文提出 Lockify，一种面向共享磁盘文件系统的新型分布式锁管理器（DLM）。我们在共享存储场景中的关键观察是：对于文件或目录创建，即使在低竞争场景下，Linux 内核 DLM 的锁获取开销也会随客户端数量增加而增长。Lockify 通过 *自所有者通知（self-owner notifications）* 和 *异步所有权管理* 避免与远程目录节点进行不必要的通信，从而将锁获取延迟降至最低。我们在 Linux 内核中实现 Lockify，并使用两种具有代表性的共享磁盘文件系统 GFS2 和 OCFS2，在真实负载上评估其性能。实验结果表明，与内核 DLM 和 O2CB 相比，Lockify 将整体吞吐量提升约 6.4 倍，且在不同客户端数量下表现一致。
