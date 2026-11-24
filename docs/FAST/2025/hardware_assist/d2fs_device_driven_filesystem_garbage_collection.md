---
title: "D2FS: Device-Driven Filesystem Garbage Collection"
description: "FAST 2025 · Hardware Assist · 让闪存设备替 F2FS 回收空闲段，FIO 下吞吐比 F2FS 高 3 倍"
tags:
  - "FAST2025"
  - "Hardware Assist"
  - "log-structured filesystem"
  - "F2FS"
---

# D2FS: Device-Driven Filesystem Garbage Collection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">日志结构文件系统的 GC 要暂停写入并做检查点，设备级 GC 又与它重复劳动。D2FS 用耦合 GC、迁移上调用与虚拟超配把段回收交给 FTL：FIO 下比 F2FS 快 3 倍、比 zoned F2FS 快 1.7 倍，YCSB-F 下比 IPLFS 快 1.5 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Hardware Assist</p>
</div>

**中文标题**：D2FS：设备驱动的文件系统垃圾回收

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/kim-juwon](https://www.usenix.org/conference/fast25/presentation/kim-juwon)

**论文 PDF**：[fast25-kim-juwon.pdf](https://www.usenix.org/system/files/fast25-kim-juwon.pdf)

**作者**：Juwon Kim、Seungjae Lee（Korea Advanced Institute of Science and Technology (KAIST)）；Joontaek Oh（University of Wisconsin–Madison）；Dongkun Shin（Sungkyunkwan University）；Youjip Won（Korea Advanced Institute of Science and Technology (KAIST)）

**会议**：FAST 2025 · Santa Clara, CA · 第 337–353 页

**Session**：Hardware Assist · 2025-02-26 10:50–12:30 · Chair：Kiran Kumar Muniswamy Reddy（Amazon）

**所属 Session**：[Hardware Assist](index.md) · [FAST 2025](../index.md)

**关键词**：log-structured filesystem, F2FS, garbage collection, FTL, zoned namespace SSD, overprovisioning

---

## 英文摘要

In this work, we propose a mechanism to free the log-structured filesystem from running the garbage collection. We exploit the garbage collection functionality of the underlying flash storage to reclaim the invalid sections in the filesystem partition. We call it a Log-structured Filesystem with Device-Driven Garbage Collection, D2FS . D2FS consists of three key ingredients: Coupled Garbage Collection, Migration Upcall, and Virtual Overprovisioning. Coupled Garbage Collection consolidates the valid flash pages at the storage device and remaps the migrated flash pages to new filesystem locations so that the valid pages are clustered not only physically but also logically. Migration Upcall asynchronously notifies the host about the file mappings updated by the Coupled Garbage Collection, minimizing interference with the foreground filesystem operations. Virtual Overprovisioning separates the size of the filesystem partition from the physical capacity of the associated storage partition and sets the size of the filesystem partition larger than the physical storage partition. Virtual overprovisioning ensures that FTL runs the device-level garbage collection on time so that the filesystem partition never runs out of free sections. By integrating these techniques, we save the log-structured filesystem from the garbage collection overhead, a primary obstacle hindering its widespread adoption in production environments. D2FS outperforms F2FS by 3× (FIO), zoned F2FS by 1.7× (FIO), and IPLFS by 1.5× (MySQL YCSB-F).

## 中文摘要

本文提出一种让日志结构文件系统不再运行垃圾回收的机制。本文利用底层闪存的垃圾回收功能回收文件系统分区中的无效 section，并将该系统称为设备驱动垃圾回收的日志结构文件系统 D2FS。D2FS 由三个关键部分组成：耦合垃圾回收、迁移上调用与虚拟超配。耦合垃圾回收在存储设备内整合有效闪存页，并把迁移后的闪存页重映射到新的文件系统位置，使有效页不仅在物理上、也在逻辑上聚簇。迁移上调用把耦合垃圾回收更新的文件映射异步通知主机，从而最小化对前台文件系统操作的干扰。虚拟超配把文件系统分区大小与关联存储分区的物理容量解耦，并把文件系统分区设置得大于物理存储分区；这确保 FTL 按时执行设备级垃圾回收，使文件系统分区永不耗尽空闲 section。通过整合这些技术，D2FS 使日志结构文件系统摆脱了垃圾回收开销——这一阻碍其在大规模生产环境中被广泛采用的主要障碍。D2FS 在 FIO 下比 F2FS 快 3 倍、比 zoned F2FS 快 1.7 倍，在 MySQL YCSB-F 下比 IPLFS 快 1.5 倍。

## 一句话总结

> 既然闪存本来就会做 GC，就让它顺手把段的逻辑位置也搬一搬——有效页在物理与逻辑上同时聚簇，文件系统不必再动手。

## 研究背景与问题

- **文件系统 GC 的代价**：日志结构文件系统（LFS、F2FS）在空闲段耗尽时必须整合有效块，GC 期间取独占锁、暂停 write/unlink/create 等一切改变文件系统状态的操作，前后还要做检查点以保证崩溃一致性，于是吞吐骤降、尾延迟拉长。
- **既有优化各有短板**：完全可抢占的 GC 实际上做不到；预测空闲期容易出错；导出超大分区（如 IPLFS 的 ZByte 级）要求 FTL 处理极大的 LBA 空间，L2P 映射的内存压力与设计复杂度都过高。
- **双向重复劳动**：文件系统与闪存设备各跑各的 GC 且互不协调，写放大叠加；反过来把 GC 全部交给主机、取消设备级 GC 的做法，仍然保留了检查点开销与用户请求暂停。
- **实测差距**：在 512GB SSD 上划 256GB 分区、填 70% 后做随机写，文件系统级 GC 对吞吐的打击远大于设备级 GC（后者最多只降低 20%）。

## 核心贡献

- **耦合 GC（Coupled Garbage Collection）**：设备级 GC 在整合有效闪存页的同时把这些页重映射到新的文件系统位置，使有效页在物理与逻辑上都聚簇；整合过程不真的把有效块拷到新位置。
- **迁移上调用（Migration Upcall）**：设备把 LBA 更新事件搭在已有的 I/O 完成通知上送回主机，既不需要专门轮询，也不需要新定义中断，且不消耗主机 CPU。
- **虚拟超配（Virtual Overprovisioning）**：把文件系统分区大小与物理存储容量解耦，分区逻辑上大于物理容量，保证设备级 GC 在文件系统耗尽空闲段之前完成回收。
- **只编排现有 IO 栈能力**：依赖设备 GC、文件系统超配与 NVMe 接口的既有特性，不对 IO 栈设计做大改动，就把主机 CPU 从 GC 开销中解放出来。
- **超配程度的发现**：适度超配（如 2.4 倍）就足以让设备级 GC 持续供给空闲段，无需 IPLFS 那样夸张的超大分区。

## 方法与技术要点

- **背景约束**：闪存以页为写单位（4 到 64KB）、块为擦除单位（512 到 1024 页），FTL 负责 L2P 映射、GC 与磨损均衡，现代 SSD 常以 superblock 粒度做设备级 GC。F2FS 的分配与刷写单位是 2MB segment，而 GC 单位是 section，section 大小可与设备 GC 单位对齐。
- **耦合 GC 的执行**：设备按 victim 选择策略挑出待回收块，把其中有效页搬到目标空闲块，同时为每个被迁移页生成文件系统映射更新记录；主机侧据此更新 filemap，使文件系统看到的逻辑位置与设备上的新物理位置一致。
- **上调用与缓冲**：设备在内部缓冲迁移记录，把通知 piggyback 到其他 I/O 完成信号上；实测各基准下 2MB 的记录缓冲即可覆盖运行中的迁移记录，无需为通知开辟专用通道。
- **虚拟超配的时机**：文件系统分区逻辑容量大于物理分区后，设备会先于文件系统耗尽空闲块，从而在文件系统用尽 section 之前触发设备级 GC 并产出空闲 section。
- **实现形态**：D2FS 是 F2FS 的一个变体，文件系统侧的 GC 线程被移除，回收工作由设备在 GC 过程中顺带完成。

## 评估与主要结果

- **平台与基线**：在 512GB SSD 上划 256GB 分区，与 stock F2FS、zoned F2FS（zF2FS）、IPLFS 对比，负载为 FIO 与 MySQL YCSB-F。
- **吞吐**：FIO 下比 F2FS 快 3 倍、比 zoned F2FS 快 1.7 倍；MySQL YCSB-F 下比 IPLFS 快 1.5 倍。
- **FTL 内存开销**（256GB SSD）：D2FS 为 27.2MB，IPLFS 为 392.0MB，F2FS 为 256.0MB，zF2FS 为 10.4MB；D2FS 因虚拟超配比 zF2FS 多占 2.4 倍内存，但仍比 IPLFS 低一个量级。
- **被省掉的到底是什么**：文件系统级 GC 的时延里，分配 page cache 条目与遍历 filemap 占 60%，向设备下发写命令最多占 13%（YCSB-F），从设备读回有效块只占约 5%（多数有效块已在 page cache 中），检查点（含写出新整合段）约占 20%——D2FS 的设备级 GC 把这四项全部省去。

## 代码与研究制品

- [代码仓库](https://github.com/ESOS-Lab/D2FS)

[返回 Hardware Assist](index.md) · [返回 FAST 2025](../index.md)
