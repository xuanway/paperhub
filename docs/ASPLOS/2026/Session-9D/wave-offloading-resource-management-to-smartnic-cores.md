---
title: "Wave: Offloading Resource Management to SmartNIC Cores"
description: "ASPLOS 2026 · Session 9D · Wave：将资源管理卸载到 SmartNIC 核心"
tags:
  - "ASPLOS2026"
  - "Session 9D"
  - "Network & Cloud Infrastructure"
---

# Wave: Offloading Resource Management to SmartNIC Cores

**中文标题：** Wave：将资源管理卸载到 SmartNIC 核心

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jack Tigar Humphries (Stellar Development Foundation), Neel Natu (Google, Inc.), Kostis Kaffes (Columbia University), Stanko Novaković (Google, Inc.), Paul Turner (Google, Inc.), Henry M. Levy (Google, Inc. and University of Washington), David Culler (Google, Inc. and University of California, Berkeley), Christos Kozyrakis (Stanford University)

**单位：** Stellar Development Foundation；Google, Inc.；Columbia University；Google, Inc. and University of Washington；Google, Inc. and University of California, Berkeley；Stanford University

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736113) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

SmartNICs are increasingly deployed in datacenters to offload tasks from server CPUs, improving the efficiency and flexibility of datacenter security, networking and storage. Optimizing cloud server efficiency in this way is critically important to ensure that virtually all server resources are available to paying customers. Userspace system software, specifically, decision-making tasks performed by various operating system subsystems, is particularly well suited for execution on mid-tier SmartNIC ARM cores. To this end, we introduce Wave, a framework for offloading userspace system software to processes/agents running on the SmartNIC. Wave uses Linux userspace systems to better align system functionality with SmartNIC capabilities. It also introduces a new host-SmartNIC communication API that enables offloading of even 𝜇s-scale system software. To evaluate Wave, we offloaded preexisting userspace system software including kernel thread scheduling, memory management, and an RPC stack to SmartNIC ARM cores, which showed a performance degradation of 1.1%-7.4% in an apples-to-apples comparison with on-host implementations. Wave recovered host resources consumed by on-host system software for memory management (saving 16 host cores), RPCs (saving 8 host cores), and virtual machines (an 11.2% performance improvement). Wave highlights the potential for rethinking system software placement in modern datacenters, unlocking new opportunities for efficiency and scalability.

## 中文摘要

SmartNIC 正越来越多地部署到数据中心中，用于从服务器 CPU 卸载任务，从而提升数据中心安全、网络和存储的效率与灵活性。以这种方式优化云服务器效率至关重要，可确保几乎所有服务器资源都可供付费用户使用。具体而言，用户态系统软件——特别是各类操作系统子系统所执行的决策类任务——非常适合在中等性能的 SmartNIC ARM 核上执行。为此，我们提出 Wave，一个将用户态系统软件卸载到运行于 SmartNIC 上的进程/代理的框架。Wave 借助 Linux 用户态系统，使系统功能与 SmartNIC 能力更好地对齐。它还引入了一种新的主机–SmartNIC 通信 API，使得甚至微秒（μs）级的系统软件也能被卸载。为评估 Wave，我们将现有的用户态系统软件（包括内核线程调度、内存管理和一个 RPC 栈）卸载到 SmartNIC ARM 核上；在与主机上实现进行同等条件对比时，性能下降为 1.1%–7.4%。Wave 为主机上系统软件所占用的资源实现了主机资源回收：内存管理（节省 16 个主机核心）、RPC（节省 8 个主机核心）以及虚拟机（11.2% 的性能提升）。Wave 凸显了重新思考现代数据中心中系统软件布局的潜力，为效率与可扩展性开辟了新的机遇。

## 英文关键词

Operating systems, SmartNICs

## 中文关键词

操作系统；SmartNIC

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736113)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 9D](index.md) · [返回 ASPLOS 2026](../index.md)
