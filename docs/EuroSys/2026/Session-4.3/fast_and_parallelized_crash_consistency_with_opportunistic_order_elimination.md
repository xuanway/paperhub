---
title: "Fast and Parallelized Crash Consistency with Opportunistic Order Elimination"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Jiahao Chen (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin Instit"
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# Fast and Parallelized Crash Consistency with Opportunistic Order Elimination

**中文标题：** 通过机会性顺序消除实现快速且并行化的崩溃一致性

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Jiahao Chen (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin Institute of Technology, Shenzhen), Wen Xia (Harbin Institute of Technology, Shenzhen), Hao Huang (Harbin Institute of Technology, Shenzhen), Peixin Zeng (Harbin Institute of Technology, Shenzhen), Yuchen Shan (Harbin Institute of Technology, Shenzhen)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769368)

**获奖：** Gilles Muller 最佳研究制品（[官方获奖名单](https://2026.eurosys.org/eurosys-awards.html)）

## 英文摘要

File systems rely on enforcing storage order for crash recovery. However, this ordering requirement limits I/O parallelism, especially in persistent memory (PM) file systems where ordered I/Os are synchronized for direct access, preventing file systems from fully exploiting PM I/O parallelism. This paper proposes a new I/O mechanism, called opportunistic order elimination, to achieve fast and parallelized crash consistency in PM file systems. The key idea is to eliminate the order between user data and file system metadata via fast checksums, and overlap checksum computation and metadata I/O with parallel data writes, thereby fully exploiting the parallelism of PM. An array of techniques are further introduced to control, dispatch, and recover parallelized I/O for efficiency, concurrency, and reliability. Based on this, we build ChimeraFS atop Linux kernel. A range of benchmarks and applications suggest that ChimeraFS achieves reliable crash recovery, significantly outperforms state-of-the-art PM file systems (e.g., OdinFS), and potentially approaches the ideal parallel write bandwidth of PM.

## 中文摘要

文件系统依赖强制执行存储顺序来实现崩溃恢复。然而，这种顺序要求限制了 I/O 并行性，尤其是在持久内存（PM）文件系统中，有序 I/O 需要被同步以保证直接访问，使文件系统无法充分利用 PM 的 I/O 并行性。本文提出一种新的 I/O 机制，称为机会性顺序消除，以在 PM 文件系统中实现快速且并行化的崩溃一致性。其核心思想是通过快速校验和消除用户数据与文件系统元数据之间的顺序，并将校验和计算与元数据 I/O 同并行数据写入重叠，从而充分利用 PM 的并行性。本文进一步引入一系列技术来控制、分发和恢复并行化 I/O，以保证效率、并发性和可靠性。在此基础上，我们在 Linux 内核之上构建了 ChimeraFS。一系列基准测试和应用表明，ChimeraFS 实现了可靠的崩溃恢复，显著优于最先进的 PM 文件系统（如 OdinFS），并有可能接近 PM 的理想并行写入带宽。

**英文关键词：** Crash consistency, Persistent memory

**中文关键词：** 崩溃一致性、持久内存

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
