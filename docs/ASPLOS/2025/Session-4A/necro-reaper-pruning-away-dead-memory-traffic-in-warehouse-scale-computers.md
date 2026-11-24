---
title: "Necro-reaper: Pruning away Dead Memory Traffic in Warehouse-Scale Computers"
description: "ASPLOS 2025 · Session 4A · Necro-reaper：剪除仓库级计算机中的死内存流量"
tags:
  - "ASPLOS2025"
  - "Session 4A"
  - "Cloud Computing 2"
---

# Necro-reaper: Pruning away Dead Memory Traffic in Warehouse-Scale Computers

**中文标题：** Necro-reaper：剪除仓库级计算机中的死内存流量

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sotiris Apostolakis (Google), Chris Kennelly (Google), Xinliang David Li (Google), Parthasarathy Ranganathan (Google)

**单位：** Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716007) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Memory bandwidth is emerging as a critical bottleneck in warehouse-scale computing (WSC). This work reveals that a significant portion of memory traffic in WSC is surprisingly unnecessary, consisting of needless writebacks of deallocated data and fetches of uninitialized data. This issue is particularly acute in WSC, where short-lived heap allocations bigger than a cache line are prevalent. To address this problem, this work proposes a pragmatic approach tailored to WSC. Leveraging the existing WSC ecosystem of vertical integration, profile-guided compilation flows, and customized memory allocators, this work presents Necro-reaper, a novel software/hardware co-design that avoids dead memory traffic without requiring the hardware tracking of prior work. New ISA instructions enable the hardware to avoid unnecessary dead traffic, while extended software components, including a profile-guided compiler and memory allocator, optimize the utilization of these instructions. Evaluation across a diverse set of 10 WSC workloads demonstrates that Necro-reaper achieves a geomean memory traffic reduction of 26% and a geomean IPC increase of 6%.

## 中文摘要

内存带宽正逐渐成为仓库级计算（WSC）的关键瓶颈。本工作揭示，WSC 中相当大一部分内存流量出乎意料地是不必要的，它们由对已释放数据的无谓写回和对未初始化数据的读取构成。该问题在 WSC 中尤为突出，因为大于一个缓存行的短生命周期堆分配在其中十分普遍。为解决这一问题，本工作提出了一种针对 WSC 量身定制的务实方法。借助 WSC 现有的垂直集成生态、profile-guided 编译流程以及定制化内存分配器，本工作提出 Necro-reaper，一种新颖的软硬件协同设计，它无需先前工作所需的硬件追踪即可避免死内存流量。新的 ISA 指令使硬件能够避免不必要的死流量，而扩展的软件组件（包括 profile-guided 编译器和内存分配器）则优化了这些指令的使用。在 10 个多样化 WSC 工作负载上的评估表明，Necro-reaper 取得了 26% 的几何平均内存流量降低以及 6% 的几何平均 IPC 提升。

## 英文关键词

Datacenter, Warehouse-Scale Computing, Memory Allocator, Profile-Guided Optimization, Hardware Caches, Instruction Set Architecture, Memory Bandwidth

## 中文关键词

数据中心；仓库级计算；内存分配器；profile-guided 优化；硬件缓存；指令集架构；内存带宽

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716007)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2025](../index.md)
