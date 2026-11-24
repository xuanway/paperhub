---
title: "ScaleLFS: A Log-Structured File System with Scalable Garbage Collection for Commodity SSDs"
description: "FAST 2025 · File Systems · 把 LFS 的垃圾回收改成每核独立回收器加并发受害者管理，持续性能最高提升 3.5 倍"
tags:
  - "FAST2025"
  - "File Systems"
  - "log-structured file system"
  - "garbage collection"
---

# ScaleLFS: A Log-Structured File System with Scalable Garbage Collection for Commodity SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">LFS 老化后必须回收无效页，而回收只有一条写流，受害者选择与元数据更新都要抢锁，并行度用不上。ScaleLFS 为每核配独立回收器与专属资源，用原子位图并发选受害者并把回收细化到页级，持续性能比 F2FS、MAX、P-GC 分别最高提升 3.5 倍、4.6 倍与 7.0 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · File Systems</p>
</div>

**中文标题**：ScaleLFS：面向商用 SSD、具备可扩展垃圾回收的日志结构文件系统

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/ha](https://www.usenix.org/conference/fast25/presentation/ha)

**论文 PDF**：[fast25-ha.pdf](https://www.usenix.org/system/files/fast25-ha.pdf)

**作者**：Jin Yong Ha（Seoul National University）；Sangjin Lee（Chung-Ang University）；Hyeonsang Eom（Seoul National University）；Yongseok Son（Chung-Ang University）

**会议**：FAST 2025 · Santa Clara, CA · 第 53–67 页

**Session**：File Systems · 2025-02-25 10:45–12:25 · Chair：Yu Hua（Huazhong University of Science and Technology）

**所属 Session**：[File Systems](index.md) · [FAST 2025](../index.md)

**关键词**：log-structured file system, garbage collection, F2FS, scalability, SSD, concurrency

---

## 英文摘要

We present a log-structured file system (LFS) with scalable garbage collection (GC) called ScaleLFS for providing higher sustained performance on commodity SSDs. Specifically, we first introduce a per-core dedicated garbage collector to parallelize the GC operations and utilize dedicated resources. Second, we present a scalable victim manager that selects victim segments and updates the metadata of the segments concurrently. Finally, we propose a scalable victim protector to enable a page-level GC procedure instead of a file level to increase GC concurrency while resolving the conflict with victim pages. We implement ScaleLFS with three techniques based on F2FS in the Linux kernel. Our evaluations show that ScaleLFS provides higher sustained performance by up to 3.5×, 4.6×, and 7.0× compared with F2FS, a scalable LFS, and a parallel GC scheme, respectively.

## 中文摘要

本文提出一种具备可扩展垃圾回收（GC）的日志结构文件系统 ScaleLFS，用于在商用 SSD 上提供更高的持续性能。具体而言，本文首先引入每核专属的垃圾回收器，以并行化 GC 操作并利用专属资源。其次，本文提出可扩展的受害者管理器，用于并发选择受害者段并更新段元数据。最后，本文提出可扩展的受害者保护器，把 GC 过程从文件级改为页级，以提升 GC 并发度，同时解决与受害者页的冲突。本文在 Linux 内核中基于 F2FS 实现了 ScaleLFS 的三项技术。评估表明，相比 F2FS、一个可扩展 LFS 与一种并行 GC 方案，ScaleLFS 分别带来最高 3.5 倍、4.6 倍与 7.0 倍的持续性能提升。

## 一句话总结

> LFS 的持续性能卡在 GC：把“一个回收器管所有段”换成每核一对一独占资源，才吃得到多核与多通道 SSD 的并行度。

## 研究背景与问题

- LFS 把随机小写聚成顺序大写，适合 SSD，但依赖连续空闲段；文件系统老化后必须回收无效页，前台 GC 会冻结整个文件系统直到完成，带来高延迟与低带宽。
- 为保护一致性，GC 期间要持有 i_gc_rwsem 这类文件级信号量；LFS 又只有一条 GC 写流（cold data stream），空闲空间分配被 curseg_mutex 串行化，SSD 与多核的并行度都用不上。
- 受害者段选择与段元数据更新同样存在过度竞争；已有并行 GC 方案（P-GC）把有效页分给多个线程，但线程越多锁竞争越重，性能反而下降。
- 可扩展 LFS（MAX）优化了内存数据结构访问与磁盘格式，GC 过程仍是串行的 one-to-all 模型。

## 核心贡献

- 提出每核专属垃圾回收器（DGC）：每核一个回收器，各自独占受害者段、页缓冲与写流，形成 one-to-one 资源模型，替代一个回收器负责所有段的 one-to-all 模型。
- 设计可扩展受害者管理器（SVM）：用原子位图与原子指令并发选择受害者段，并以松同步（loose-synchronization）方式并发更新段元数据。
- 提出可扩展受害者保护器（SVP）：借助并发哈希表把 GC 从文件级细化到页级，使同一文件内的多个页可被并行清理，同时消解 I/O 线程与 DGC 对受害者页的冲突。
- 基于 F2FS 在 Linux 6.0.0 内核中实现三个组件，并公开源码。

## 方法与技术要点

- 资源独占：DGC 为每核配专属写流与页缓冲，把单一 curseg_mutex 上的串行分配拆开，回收器之间不再共享资源。
- 并发选受害者：SVM 以原子位图与原子指令做低锁选择，牺牲少量最优性与少量 false-positive 读，换取可扩展性，且不破坏 LFS 一致性。
- 松同步元数据更新：逐项原子更新段元数据，避免全局锁；代价是受害者选择不够最优、可能多读已失效地址。
- 页级 GC 与保护：SVP 用并发哈希表登记受害者页，允许多个 GC 线程同时清理同一文件，解决 I/O 与 GC 的页冲突。
- 部署取舍：需要 I/O 密集、应用常因等待 GC 而阻塞、且有多余 CPU 核的场景，例如数据中心的 disaggregated 存储服务器与文件服务器。

## 评估与主要结果

- 实现基于 F2FS 与 Linux 6.0.0，使用 micro 与 macro 基准以及真实应用评估。
- 持续性能相对 F2FS 最高 3.5 倍、相对可扩展 LFS（MAX）4.6 倍、相对并行 GC 方案（P-GC）7.0 倍。
- 组件逐项叠加的分解实验（基线为 F2FS 的 LFS 模式）显示：带宽从 213.5 MB/s 升到 509.3 MB/s，平均延迟从 615.5 微秒降到 254.1 微秒，执行时间从 577.8 秒降到 236.1 秒；i_gc_rwsem、curseg_mutex、sentry_lock、seglist_lock 的开销最终全部降为 0。
- 只把 GC 改成简单的每核回收器（SPGC）反而退化：带宽降到 98.4 MB/s、平均延迟升到 1157.7 微秒、执行时间升到 1221.5 秒，说明仅增加线程并不够。

[返回 File Systems](index.md) · [返回 FAST 2025](../index.md)
