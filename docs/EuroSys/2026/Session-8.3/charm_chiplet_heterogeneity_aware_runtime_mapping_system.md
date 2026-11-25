---
title: "CHARM: Chiplet Heterogeneity-Aware Runtime Mapping System"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · Alessandro Fogli (Imperial College London), Bo Zhao (Aalto University), Peter Pi"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# CHARM: Chiplet Heterogeneity-Aware Runtime Mapping System

**中文标题：** CHARM：感知 Chiplet 异构性的运行时映射系统

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：Alessandro Fogli (Imperial College London), Bo Zhao (Aalto University), Peter Pietzuch (Imperial College London), Jana Giceva (TU Munich)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769390)

## 英文摘要

The growing disparity between CPU core counts and available memory bandwidth has intensified memory contention in servers. This particularly affects highly parallelizable applications, which must achieve efficient cache utilization to maintain performance as CPU core counts grow. Optimizing cache utilization, however, is complex for recent chiplet-based CPUs, whose partitioned L3 caches lead to varying latencies and bandwidths, even within a single NUMA domain. Classical NUMA optimizations and task scheduling fail to address the performance issues of chiplet-based CPUs.

We describe Chiplet Heterogeneity Aware Runtime Mapping (CHARM), a new runtime system designed for chiplet-based CPUs. CHARM combines chiplet-aware task scheduling heuristics, hardware-aware memory allocation, and fine-grained performance monitoring to optimize workload execution. It implements a lightweight concurrency model that combines user-level threading features, such as individual stacks, per-task scheduling, and state management, with coroutine-like behavior, allowing tasks to suspend and resume execution at defined points while efficiently managing task migration across chiplets. Our evaluation across diverse scenarios shows CHARM’s effectiveness in optimizing the performance of memory-intensive parallel applications.

## 中文摘要

CPU 核心数量与可用内存带宽之间日益扩大的差距加剧了服务器中的内存争用。这对高度可并行化的应用影响尤为明显，随着 CPU 核心数增长，这类应用必须实现高效的缓存利用才能保持性能。然而，对近期基于 chiplet 的 CPU 而言，优化缓存利用十分复杂，其分区的 L3 缓存即使在单个 NUMA 域内也会导致不同的延迟与带宽。经典的 NUMA 优化和任务调度无法解决基于 chiplet 的 CPU 的性能问题。

我们介绍 Chiplet 异构性感知运行时映射（CHARM），一个为基于 chiplet 的 CPU 设计的新型运行时系统。CHARM 结合了感知 chiplet 的任务调度启发式方法、硬件感知的内存分配和细粒度性能监控，以优化工作负载执行。它实现了一个轻量级并发模型，将用户级线程特性（如独立栈、按任务调度和状态管理）与类协程行为相结合，允许任务在指定点挂起和恢复执行，同时高效管理跨 chiplet 的任务迁移。我们在多种场景下的评估表明，CHARM 在优化内存密集型并行应用的性能方面是有效的。

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
