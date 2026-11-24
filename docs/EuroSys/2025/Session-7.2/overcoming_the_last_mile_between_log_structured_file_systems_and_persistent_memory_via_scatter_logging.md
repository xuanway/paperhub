---
title: "Overcoming the Last Mile between Log-Structured File Systems and Persistent Memory via Scatter Logging"
description: "EuroSys 2025 · Storage · Yifeng Zhang (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin insti"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Overcoming the Last Mile between Log-Structured File Systems and Persistent Memory via Scatter Logging

**中文标题：** 通过散射日志跨越日志结构文件系统与持久内存之间的最后一公里

**所属 Session：** [Session 7.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Yifeng Zhang (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin institute of Technology, Shenzhen), Hao Huang (Harbin Institute of Technology, Shenzhen), Yuchen Shan (Harbin Institute of Technology, Shenzhen), Wen Xia (Harbin Institute of Technology, Shenzhen)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717488)

## 英文摘要

Log-structured file system (LFS) has been a popular option for persistent memory (PM) for its high write performance and lightweight crash consistency protocols. However, even with PM’s byte-addressable I/O interface, existing PM LFSes still maintain contiguous space for log locality while using heavy garbage collection (GC) to synchronously reclaim space, causing up to 50% I/O performance degradation on PM. Thus, there exists a last-mile problem between the contiguous space management of LFS (that induces GC) and the non-contiguous byte-addressability of PM.

To overcome this, we propose a novel scatter logging technique called SLOT. The core idea is to efficiently manage non-contiguous log entries on byte-addressable PM to prevent GC in LFS. Specifically, SLOT scatters log entries across PM and manages them in a per-entry granularity, thereby enabling the immediate reallocation of invalidated entries and eliminating GC overheads. SLOT further introduces an array of techniques to exploit PM write buffer efficiency to fully unleash PM I/O performance potential. We implement SlotFS to realize the efficiency of SLOT. Experimental results driven by synthetic and real-world workloads show that SlotFS significantly outperforms state-of-the-art PM file systems. Compared to two representative PM LFSes, NOVA and MadFS, SlotFS achieves 27%–47% and 59%–175% performance improvement under a series of real-world workloads.

## 中文摘要

日志结构文件系统（LFS）因其高写性能和轻量级崩溃一致性协议，一直是持久内存（PM）上的热门选择。然而，即使有 PM 的字节可寻址 I/O 接口，现有 PM LFS 仍为保持日志局部性而维护连续空间，同时使用繁重的垃圾回收（GC）同步回收空间，导致 PM 上高达 50% 的 I/O 性能下降。因此，LFS 的连续空间管理（会引发 GC）与 PM 的非连续字节可寻址性之间存在最后一英里问题。

为克服这一问题，我们提出一种新颖的分散日志技术 SLOT。核心思想是在字节可寻址 PM 上高效管理非连续日志项，以避免 LFS 中的 GC。具体而言，SLOT 将日志项分散到 PM 上，并以每项为粒度进行管理，从而实现失效项的立即重新分配并消除 GC 开销。SLOT 进一步引入一系列技术来利用 PM 写缓冲效率，以充分释放 PM I/O 性能潜力。我们实现 SlotFS 以发挥 SLOT 的效率。由合成和真实工作负载驱动的实验结果表明，SlotFS 显著优于最先进的 PM 文件系统。与两个代表性 PM LFS（NOVA 和 MadFS）相比，SlotFS 在一系列真实工作负载下分别实现 27%–47% 和 59%–175% 的性能提升。

**英文关键词：** Log-structured file systems, persistent memory

**中文关键词：** 日志结构文件系统、持久内存

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
