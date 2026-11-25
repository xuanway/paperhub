---
title: "RaidenSwap: A Multi-Swap Remote System for Multi-core Applications"
description: "EuroSys 2026 · OS & Virtualization · Kefan Liu (SKLP, Institute of Computing Technology, CAS; University of Chinese A"
tags:
  - "EuroSys2026"
  - "OS & Virtualization"
---

# RaidenSwap: A Multi-Swap Remote System for Multi-core Applications

**中文标题：** RaidenSwap：面向多核应用的多路交换远程系统

**所属 Session：** [Session 1.1: OS & Virtualization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：OS & Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · OS & Virtualization</p>
</div>

**作者**：Kefan Liu (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Ke Liu (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Xu Zhang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Hui Yuan (Huawei), Xiaolong Zheng (Huawei), Ning Liu (Huawei), Sa Wang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Guanghui Zhang (Shandong University), Yungang Bao (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Mingyu Chen (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Chenxi Wang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803575)

## 英文摘要

Kernel-based remote memory systems are gaining traction in datacenters due to their significant improvement in memory utilization and their ability to transparently provide applications with unlimited memory capacity. However, the high degree of parallelism in contemporary applications leads to a significant demand for remote access throughput, which mismatches with the state-of-the-art kernel swap path due to its inherently limited parallelism. As a result, it cannot scale up the multi-core applications. We dive into the implementation of the swap path and identify the root cause behind it – significant lock contentions and inefficient swap tasks offloading.

To address these challenges, we introduce RaidenSwap, a kernel-based remote memory system that aims to improve swap path efficiency with two key ideas. 1) It introduces a page swapping framework that parallelizes page swapping on a core basis with little thread synchronization. This is achieved by allocating a separate LRU list to each core, thereby avoiding lock contention for the global one, while the collective effect of all local LRU lists retains the behavior of using a global LRU list. Meanwhile, this separation also enables memory semantics tracking on a fine-grain thread level, providing opportunities for semantic-aware swapping. 2) It offloads both prefetching and reclaiming tasks with smaller batches to a pool of worker threads, which efficiently harnesses fine-grained CPU idle time, minimizing disruption to application threads. We implemented a RaidenSwap prototype as a kernel module, ported it to multiple Linux kernels (v4.11 and v6.1), and evaluated it with both microbenchmarks and real applications. Our results show that RaidenSwap significantly outperforms state-of-the-art remote systems, such as Hermit, Canvas and Fastswap, by improving swap throughput by a factor of 1.8 to 16.5 and reducing remote access latency by 70%. Consequently, RaidenSwap accelerates the completion time of real applications by 8% to 70%.

## 中文摘要

基于内核的远程内存系统因其在内存利用率上的显著提升以及能够透明地为应用提供近乎无限的内存容量，正在数据中心中日益受到青睐。然而，当代应用的高度并行性带来了对远程访问吞吐量的巨大需求，这与最先进的内核交换路径因其固有的并行性受限而不相匹配。因此，它无法随多核应用而扩展。我们深入研究了交换路径的实现，并找出了其背后的根本原因——严重的锁竞争与低效的交换任务卸载。

为解决这些挑战，我们提出 RaidenSwap，一个基于内核的远程内存系统，旨在通过两个核心思想提升交换路径的效率。1）它引入了一个以核为单位并行化页面交换、几乎不需要线程同步的页面交换框架。这通过为每个核分配单独的 LRU 链表来实现，从而避免了对全局链表的锁竞争，而所有本地 LRU 链表的集体效果仍保留了使用全局 LRU 链表的行为。同时，这种分离还使内存语义追踪能够在细粒度的线程级别进行，为语义感知的交换提供了机会。2）它将预取与回收任务以更小的批次卸载到工作线程池，从而高效利用细粒度的 CPU 空闲时间，最大限度减少对应用线程的干扰。我们以内核模块的形式实现了 RaidenSwap 原型，并将其移植到多个 Linux 内核（v4.11 和 v6.1），用微基准测试和真实应用对其进行了评估。结果表明，RaidenSwap 显著优于 Hermit、Canvas 和 Fastswap 等最先进的远程系统，交换吞吐量提升 1.8 至 16.5 倍，远程访问延迟降低 70%。因此，RaidenSwap 将真实应用的完成时间加速了 8% 至 70%。

**英文关键词：** Remote Memory System, Multicore Scalability

**中文关键词：** 远程内存系统、多核可扩展性

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
