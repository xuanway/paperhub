---
title: "UnICom: A Universally High-Performant I/O Completion Mechanism for Modern Computer Systems"
description: "FAST 2026 · OS · 第 721–736 页"
tags:
  - "FAST2026"
  - "OS"
---

# UnICom: A Universally High-Performant I/O Completion Mechanism for Modern Computer Systems

**中文标题**：UnICom：面向现代计算机系统的通用高性能 I/O 完成机制

**Session**：OS · 2026-02-26 15:50–17:10 · Chair：Yu Liang（ETH Zurich）

**作者**：Riwei Pan, City University of Hong Kong; Yu Liang, ETH Zurich and Inria-Paris; Sam H. Noh, Virginia Tech; Lei Li and Nan Guan, City University of Hong Kong; Tei-Wei Kuo, Delta Electronics and National Taiwan University; Chun Jason Xue, Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)

**会议**：FAST 2026 · Santa Clara, CA · 第 721–736 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/pan](https://www.usenix.org/conference/fast26/presentation/pan)

**论文 PDF**：[fast26-pan.pdf](https://www.usenix.org/system/files/fast26-pan.pdf)

---

## 英文摘要

Modern computer systems are increasingly equipped with dozens to hundreds of cores, while high-performance Solid-State Drives (SSDs), enabled by NVMe and emerging technologies such as CXL-SSDs, provide massive I/O bandwidth and microsecond-scale latency. Yet, software overhead in the I/O stack remains a critical bottleneck, often contributing up to 50% of total I/O latency. Existing I/O completion mechanisms fall short: polling achieves low latency but wastes CPU cycles, whereas interrupts conserve CPU resources but incur significant wake-up overhead. This paper presents UnICom (Universal I/O Completion), a new I/O completion mechanism that unifies the benefits of polling and interrupts while avoiding their drawbacks. The key insight is that a kernel trap is negligible compared to disk I/O latency, yet enables access to kernel infrastructure for efficiency and security. Building on this, UnICom introduces three core techniques: TagSched, a lightweight tag-guided scheduling mechanism that minimizes sleep and wake-up overhead; TagPoll, a centralized kernel-level I/O completion thread that consolidates polling across threads and processes; and SKIP, a kernel-assisted direct-access mechanism that eliminates complex user-space permission management. Together, these techniques enable efficient multi-process support and direct SSD access while bypassing much of the kernel I/O stack. We implement UnICom in the Linux kernel and evaluate it against ext4, BypassD, and io_uring. Across all experiments, UnICom consistently delivers high I/O performance, matching or exceeding the best of polling and interrupts under both low and high CPU utilization.

## 中文摘要

现代计算机系统正越来越多地配备数十到数百个核心，而由 NVMe 和 CXL-SSD 等新兴技术赋能的高性能固态硬盘（SSD）提供了巨大 I/O 带宽和微秒级延迟。然而，I/O 栈中的软件开销仍是关键瓶颈，通常占总 I/O 延迟的 50%。现有 I/O 完成机制存在不足：轮询可实现低延迟，但浪费 CPU 周期；中断节省 CPU 资源，但带来显著的唤醒开销。本文提出 UnICom（通用 I/O 完成），一种新的 I/O 完成机制，它统一了轮询和中断的优点，同时避免其缺点。关键洞见是：与磁盘 I/O 延迟相比，内核陷入可忽略不计，但它能够访问内核基础设施，从而兼顾效率与安全。基于此，UnICom 引入三项核心技术：TagSched，一种轻量级标签引导调度机制，可最小化睡眠和唤醒开销；TagPoll，一个集中式内核级 I/O 完成线程，整合跨线程和跨进程的轮询；SKIP，一种内核辅助的直接访问机制，消除复杂的用户态权限管理。这些技术共同实现了高效的多进程支持和直接 SSD 访问，同时绕过大部分内核 I/O 栈。我们在 Linux 内核中实现 UnICom，并与 ext4、BypassD 和 io_uring 进行对比评估。在所有实验中，UnICom 始终提供高 I/O 性能，在低 CPU 利用率和高 CPU 利用率下均达到或超过轮询和中断的最佳表现。
