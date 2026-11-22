---
title: "C2P-Cache: Scalable GPU L1 Cache Sharing via Concurrent Candidate Pruning"
description: "MICRO 2026 · Session 7A · C2P-Cache：通过并发候选剪枝实现可扩展 GPU L1 缓存共享"
tags:
  - "MICRO2026"
  - "GPU"
  - "Cache"
---

# C2P-Cache: Scalable GPU L1 Cache Sharing via Concurrent Candidate Pruning

**中文标题：** C2P-Cache：通过并发候选剪枝实现可扩展 GPU L1 缓存共享

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Hanqing Li, Lizhou Wu, Tiejun Li, Sheng Ma, Hanzhi Xun, Jianmin Zhang, Yuhan Tang, Jixuan Tang, Xuchao Xie

**来源：** MICRO 2026，pp. 2326–2341；[DOI](https://doi.org/10.1109/MICRO67795.2026.00160)

## 英文摘要

Modern GPUs rely on private per-SM L1 caches and a shared L2 cache, but this organization obscures cross-SM reuse: an L1 miss is typically forwarded to L2 even when the requested line already resides in a peer L1 cache, leading to redundant L2 access. Prior GPU L1-sharing designs attempt to recover such reuse through exact or broad remote-hit searches, which become increasingly difficult to scale and can interfere with the critical L1 miss path under high concurrency. We observe that eliminating redundant L2 accesses does not require exact, chip-wide knowledge of private L1 contents. Instead, it requires only sufficient visibility to sharply narrow down a small set of candidate caches, leaving exact confirmation to a much smaller number of L1s. Based on this insight, we propose C2P-Cache, a scalable GPU L1-sharing mechanism that transforms remote-hit discovery from a chip-wide exact search problem into a lightweight filtering-and-confirmation process. C2P-Cache maintains compact Bloom-filter-based snapshots of private L1 tags, performs parallel chip-wide candidate filtering, and selectively probes only a small number of likely peer caches. To sustain high concurrency, C2P-Cache organizes filtering as bit-sliced matching over a banked and replicated snapshot matrix, enabling efficient, parallel processing of many concurrent misses without interfering with normal L1 accesses. Across a wide range of GPU workloads, C2P-Cache improves instructions per cycle (IPC) by up to 49.7% and by 23.5% on average for applications with high remote-L1 reuse and strong sensitivity to L2 latency, demonstrating that lightweight, scalable filtering can effectively unlock cross-SM reuse with modest overhead.

## 中文摘要

现代 GPU 依赖于每个 SM 的私有 L1 缓存和共享的 L2 缓存，但这种组织掩盖了跨 SM 的重用：即使请求的行已经驻留在对等 L1 缓存中，L1 未命中通常也会转发到 L2，从而导致冗余的 L2 访问。先前的 GPU L1 共享设计试图通过精确或广泛的远程命中搜索来恢复这种重用，这变得越来越难以扩展，并且可能会干扰高并发下关键的 L1 缺失路径。我们观察到，消除冗余的 L2 访问并不需要对私有 L1 内容进行精确的、芯片范围的了解。相反，它只需要足够的可见性来大幅缩小一小组候选缓存的范围，将精确确认留给数量少得多的 L1。基于这一见解，我们提出了 C2P-Cache，这是一种可扩展的 GPU L1 共享机制，可将远程命中发现从芯片范围的精确搜索问题转变为轻量级的过滤和确认过程。 C2P-Cache 维护私有 L1 标签的紧凑的基于 Bloom-filter 的快照，执行并行芯片范围的候选过滤，并有选择地仅探测少量可能的对等缓存。为了维持高并发性，C2P-Cache 将过滤组织为在存储和复制的快照矩阵上进行位片匹配，从而能够高效、并行地处理许多并发未命中，而不会干扰正常的 L1 访问。在广泛的 GPU 工作负载中，对于远端 L1 复用率高、对 L2 时延敏感的应用，C2P-Cache 使每周期指令数（IPC）最高提高 49.7%，平均提高 23.5%，这表明轻量级、可扩展的过滤可以以适度的开销有效地解锁跨 SM 重用。

## 中文关键词

GPU 架构；布隆过滤器；缓存共享；候选剪枝

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
