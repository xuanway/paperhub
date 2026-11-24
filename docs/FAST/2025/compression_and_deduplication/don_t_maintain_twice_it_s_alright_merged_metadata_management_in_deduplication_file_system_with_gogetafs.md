---
title: "Don't Maintain Twice, It's Alright: Merged Metadata Management in Deduplication File System with GogetaFS"
description: "FAST 2025 · Compression and Deduplication · 把去重指纹映射并入文件系统 L2P，吞吐高 5.6%–35.0%"
tags:
  - "FAST2025"
  - "Compression and Deduplication"
  - "deduplication file system"
  - "metadata management"
  - "杰出工件奖"
---

# Don't Maintain Twice, It's Alright: Merged Metadata Management in Deduplication File System with GogetaFS

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">去重文件系统为指纹到物理块的映射单独维护一张表，还要求它先于文件系统映射落盘，元数据维护最多吃掉 38% 的 I/O 时间。GogetaFS 把两张表合并为逻辑地址—指纹—物理地址映射，一次 I/O 同时持久化两侧元数据，I/O 吞吐比现有去重文件系统高 5.6%–35.0%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Compression and Deduplication · 杰出工件奖</p>
</div>

**中文标题**：不必重复维护：GogetaFS 去重文件系统中的合并元数据管理

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/pan](https://www.usenix.org/conference/fast25/presentation/pan)

**论文 PDF**：[fast25-pan.pdf](https://www.usenix.org/system/files/fast25-pan.pdf)

**作者**：Yanqi Pan、Wen Xia（Harbin Institute of Technology, Shenzhen）；Erci Xu（Alibaba Group）；Hao Huang、Xiangyu Zou、Shiyi Li（Harbin Institute of Technology, Shenzhen）

**会议**：FAST 2025 · Santa Clara, CA · 第 479–495 页 · **杰出工件奖**

**Session**：Compression and Deduplication · 2025-02-27 09:00–10:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**所属 Session**：[Compression and Deduplication](index.md) · [FAST 2025](../index.md)

**关键词**：deduplication file system, metadata management, crash consistency, persistent memory, fingerprint, F2FS

---

## 英文摘要

Emerging storage technologies, such as persistent memory and ultra-low latency SSD, enable the deduplication file system (DedupFS) to use non-cryptographic hash for fast fingerprinting. However, we find that the accelerated computation exposes another major performance penalty: the seemingly innocuous in-storage deduplication metadata maintenance incurs up to 38% overhead in the I/O path.

We find the root cause is that DedupFSes maintain dedup-specific fingerprint-to-physical mappings, which incurs additional crash consistency overheads. However, this overhead is unnecessary. Our insight is that the deduplication mapping can be merged with the file system logical-to-physical mapping, forming a logical-fingerprint-physical (LFP) mapping. Thus, we can persist deduplication metadata alongside file system metadata in a single I/O. We propose GOGETAFS to realize the efficiency of LFP. Using a series of techniques to manage data and metadata atop LFP, GOGETAFS achieves compatible, effective, and memory-efficient deduplication within the file system. Experiments across a range of workloads show that GOGETAFS consistently outperforms existing DedupFSes and can minimize metadata maintenance overheads.

## 中文摘要

持久内存与超低延迟 SSD 等新兴存储技术，使去重文件系统（DedupFS）能够使用非加密哈希进行快速指纹计算。然而本文发现，计算加速后暴露出另一个主要性能损失：看似无害的存储内去重元数据维护会在 I/O 路径上带来高达 38% 的开销。本文发现根因在于，DedupFS 单独维护去重专用的指纹到物理地址映射，这引入了额外的崩溃一致性开销；而这种开销其实并不必要。本文的洞见是：去重映射可以与文件系统的逻辑到物理映射合并，形成逻辑—指纹—物理（LFP）映射，从而用一次 I/O 同时持久化去重元数据与文件系统元数据。本文提出 GogetaFS 来实现 LFP 的效率，并用一系列技术基于 LFP 管理数据与元数据，使去重在文件系统内实现兼容、有效且内存高效。多种负载上的实验表明，GogetaFS 稳定优于现有 DedupFS，并能最小化元数据维护开销。

## 一句话总结

> 去重条目与文件系统条目本就指向同一个物理块，维护两遍纯属多余，合并成一条 LFP 映射即可。

## 研究背景与问题

- **计算瓶颈转移后暴露新瓶颈**：持久内存与超低延迟 SSD 让去重文件系统（deduplication file system, DedupFS）可以用非加密哈希（non-cryptographic hash）做快速指纹，指纹计算开销从加密哈希的最多 65% 降到 15%–18%，但存储内的去重元数据维护随之成为主要惩罚。
- **元数据维护占 I/O 时间 18%–38%**：对 DeNOVA、NV-Dedup、Light-Dedup 的拆解显示，去重元数据维护消耗 18%–38% 的 I/O 时间；在 0% 去重率下，去重文件系统比理想系统慢 20%–42%，且 DeNOVA 因加密指纹计算比其他方案慢 1.9 至 3.4 倍。
- **根因是强制的更新顺序**：去重文件系统要求指纹到物理块的 FP2P 条目先于文件系统的 L2P 条目落盘，以便崩溃后高效修复不一致，代价是元数据写两遍，并因排序限制 I/O 并行度。

## 核心贡献

- **LFP 映射**：利用去重条目与文件系统条目共享同一物理块号这一事实，把 FP2P 与 L2P 合并为逻辑地址—指纹—物理地址（logical-fingerprint-physical, LFP）映射。
- **单次 I/O 持久化**：去重元数据随文件系统元数据一起落盘，复用文件系统成熟的崩溃一致性机制，不再需要额外的写入顺序。
- **基于 LFP 的 GogetaFS**：用存储端指纹区间表与可重建的内存指纹表，化解数据按区间管理与去重按块管理、文件系统按逻辑块号索引与去重按指纹检索之间的不兼容。
- **内存效率设计空间**：探索条目放置、内存分配与数据结构等多种变体，适配不同可用内存量的场景。

## 方法与技术要点

- **合并写路径**：写入时只更新带指纹的 L2P 条目，指纹与物理块号同处一条，省去独立 FP2P 表的更新及其排序约束。
- **数据管理**：按块区间（extent）记录指纹并存入存储端表，由文件系统的崩溃一致性机制负责持久化，无需额外顺序。
- **元数据管理**：把 LFP 条目转换成以指纹为键的 FP2P 条目放入内存表；该表可从 LFP 重建，因此不必为其做崩溃一致性保护，设计上可自由取舍。
- **实现代价**：在 F2FS 中只增加约 50 行代码（主要是宏与块索引），其余去重逻辑模块化在内存结构中，便于移植。
- **指纹选择**：采用 4 至 8 字节的非加密指纹（如 xxHash、wyHash），使 LFP 带来的空间开销可控。

## 评估与主要结果

- **吞吐**：在持久内存与模拟超低延迟 SSD 两类平台上，用 FIO 合成负载和真实负载（Homes、OSLab、Mails、WebVMs）对比 DeNOVA、NV-Dedup、Light-Dedup 等系统，I/O 吞吐高出 5.6%–35.0%。
- **SSD 平台**：在 Z-SSD 上的单线程测试中，GogetaFS 有时领先一个数量级。
- **内存变体**：针对特定内存场景选择的变体可再提升最多 10% 吞吐；即便实现理想的 PM 到 DRAM 换出，收益也只有 1%–19%。

## 代码与研究制品

- [代码仓库](https://github.com/GogetaFS/GogetaFS-AE)

[返回 Compression and Deduplication](index.md) · [返回 FAST 2025](../index.md)
