---
title: "A Logically Disaggregated Cache for Replicated Storage Systems"
description: "EuroSys 2026 · File Systems & Storage · Kiran Hombal (University of Illinois Urbana-Champaign), Henry Zhu (University of"
tags:
  - "EuroSys2026"
  - "File Systems & Storage"
---

# A Logically Disaggregated Cache for Replicated Storage Systems

**中文标题：** 面向副本存储系统的逻辑解耦缓存

**所属 Session：** [Session 2.1: File Systems & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：File Systems & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · File Systems & Storage</p>
</div>

**作者**：Kiran Hombal (University of Illinois Urbana-Champaign), Henry Zhu (University of Illinois Urbana-Champaign), Shreesha G. Bhat (University of Illinois Urbana Champaign), Neil Kaushikkar (Jump Trading Group), Ramnatthan Alagappan (University of Illinois Urbana-Champaign), Aishwarya Ganesan (University of Illinois Urbana-Champaign)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803608)

## 英文摘要

We study if replicated storage systems effectively utilize the caches embedded within each replica. Our study reveals that existing systems manage the embedded caches in each replica in silos, leading to significant cache redundancy across replicas and consequently low performance. To address this problem, we introduce logically disaggregated cache (Ldc), a new approach to managing caches in replicated storage systems. Ldc disaggregates the embedded caches from the replicas to form a single, logical cache. Ldc then allows any replica to access any part of the logical cache, which reduces redundancy caused by reads. Because writes pollute all caches, Ldc quickly demotes written objects to limit redundancy caused by writes. Ldc, however, realizes that reducing redundancy may hurt performance in some cases and thus employs an online analyzer to strike a balance between cache redundancy and coverage. We implement Ldc in three systems: an eventually-consistent KV store, a strongly-consistent KV store, and a production database. Using microbenchmarks, macrobenchmarks, and real-world traces, we show that the Ldc versions perform significantly better than the original systems (e.g., 2.6× to 5.4× higher throughput in the eventually-consistent KV store under YCSB).

## 中文摘要

我们研究副本存储系统是否有效利用了各副本内置的缓存。我们的研究表明，现有系统以孤立的方式管理每个副本中的内置缓存，导致副本之间出现严重的缓存冗余，进而造成性能低下。为解决这一问题，我们提出逻辑解耦缓存（Ldc），一种管理副本存储系统中缓存的新方法。Ldc 将内置缓存从副本中解耦出来，构成单一的逻辑缓存。随后 Ldc 允许任意副本访问该逻辑缓存的任意部分，从而减少读操作造成的冗余。由于写操作会污染所有缓存，Ldc 会迅速将已写入的对象降级，以限制写操作造成的冗余。然而，Ldc 也意识到减少冗余在某些情况下可能损害性能，因此引入一个在线分析器，在缓存冗余与缓存覆盖之间取得平衡。我们将 Ldc 实现在三个系统中：一个最终一致性 KV 存储、一个强一致性 KV 存储和一个生产数据库。借助微基准测试、宏基准测试和真实负载轨迹，我们表明 Ldc 版本显著优于原系统（例如，在 YCSB 下最终一致性 KV 存储的吞吐量提高 2.6 倍至 5.4 倍）。

**英文关键词：** Key-value store, Replication, Cache management, Remote memory

**中文关键词：** 键值存储、副本复制、缓存管理、远端内存

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
