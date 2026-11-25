---
title: "MesaFS: An I/O-Efficient Metadata Service for Distributed File Systems"
description: "EuroSys 2026 · File Systems & Storage · Hao Guo (Tsinghua University), Jiwu Shu (Tsinghua University), Youyou Lu (Tsingh"
tags:
  - "EuroSys2026"
  - "File Systems & Storage"
---

# MesaFS: An I/O-Efficient Metadata Service for Distributed File Systems

**中文标题：** MesaFS：一种面向分布式文件系统的I/O高效元数据服务

**所属 Session：** [Session 2.1: File Systems & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：File Systems & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · File Systems & Storage</p>
</div>

**作者**：Hao Guo (Tsinghua University), Jiwu Shu (Tsinghua University), Youyou Lu (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803573)

## 英文摘要

Distributed file systems typically rely on an underlying storage backend, called a metadata store, to support metadata updates. Previous work focuses on efficient directory tree management, bridging the performance gap between metadata updates and metadata stores. However, there is still a huge performance gap between metadata updates and SSD performance. This gap is mainly caused by extra SSD writes from two sources. First, a single high-level operation often translates to multiple writes in the metadata store (called a divided update). Ensuring crash consistency for a divided update requires extra writes (e.g., journaling). Second, extra writes are required to maintain the physical order of metadata objects on the SSD (called layout ordering), which is necessary to support operations like directory listing.

We propose MesaFS, an I/O-efficient metadata service for distributed file systems. MesaFS supports most metadata updates with a single SSD write. To achieve this, first, we propose invariant-aware ordered updates. Instead of enforcing atomicity for each divided update, it allows a divided update to be partially completed by ensuring directory invariants are satisfied eventually or can be restored during crash recovery, thus avoiding extra SSD writes. Second, we design a semi-ordered metadata layout to reduce the extra writes caused by maintaining a total order for metadata objects. Our evaluation shows that MesaFS achieves 62.0%-95.1% of raw SSD performance, compared to 8.4%-37.2% in our emulation of the state-of-the-art InfiniFS.

## 中文摘要

分布式文件系统通常依赖一种称为元数据存储的底层存储后端来支持元数据更新。已有工作侧重于高效的目录树管理，以弥合元数据更新与元数据存储之间的性能差距。然而，元数据更新与SSD性能之间仍存在巨大的性能差距。这一差距主要由两个来源的额外SSD写造成。首先，单个高层操作往往在元数据存储中转化为多次写（称为分裂更新）。为保证分裂更新的崩溃一致性，需要额外的写（例如日志）。其次，需要额外的写来维持SSD上元数据对象的物理顺序（称为布局有序性），而这对支持目录列举等操作是必要的。

我们提出MesaFS，一种面向分布式文件系统的I/O高效元数据服务。MesaFS以单次SSD写支持大多数元数据更新。为此，我们首先提出不变量感知的有序更新。它不为每个分裂更新强制原子性，而是允许分裂更新部分完成，只需保证目录不变量最终得到满足或可在崩溃恢复期间恢复，从而避免额外的SSD写。其次，我们设计了一种半有序元数据布局，以减少为维护元数据对象全序而导致的额外写。评估表明，MesaFS达到原始SSD性能的62.0%–95.1%，而在我们对最先进InfiniFS的模拟中该比例仅为8.4%–37.2%。

**英文关键词：** Distributed file systems, Metadata management

**中文关键词：** 分布式文件系统、元数据管理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
