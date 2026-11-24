---
title: "Boosting File Systems Elegantly: A Transparent NVM Write-ahead Log for Disk File Systems"
description: "FAST 2025 · File Systems · 用 NVM 写前日志只吸收同步写，为磁盘文件系统透明加速最高 15.09 倍"
tags:
  - "FAST2025"
  - "File Systems"
  - "NVM"
  - "write-ahead log"
---

# Boosting File Systems Elegantly: A Transparent NVM Write-ahead Log for Disk File Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">NVM 专用文件系统受容量限制，overlay 方案又会引入双重索引并拖慢读路径。NVLog 把 NVM 做成 VFS 页缓存旁的写前日志，只吸收同步写，为磁盘文件系统带来最高 15.09 倍加速，并比 NOVA、SPFS 分别快 3.72 倍与 324.11 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · File Systems</p>
</div>

**中文标题**：优雅地加速文件系统：面向磁盘文件系统的透明 NVM 写前日志

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/wang](https://www.usenix.org/conference/fast25/presentation/wang)

**论文 PDF**：[fast25-wang.pdf](https://www.usenix.org/system/files/fast25-wang.pdf)

**作者**：Guoyu Wang、Xilong Che、Haoyang Wei、Shuo Chen、Puyi He、Juncheng Hu（Jilin University）

**会议**：FAST 2025 · Santa Clara, CA · 第 19–34 页

**Session**：File Systems · 2025-02-25 10:45–12:25 · Chair：Yu Hua（Huazhong University of Science and Technology）

**所属 Session**：[File Systems](index.md) · [FAST 2025](../index.md)

**关键词**：NVM, write-ahead log, crash consistency, disk file system, page cache, transparency

---

## 英文摘要

We propose NVLog, an NVM-based write-ahead log for disk file systems, designed to transparently harness the high performance of NVM within the legacy storage stack. NVLog provides on-demand byte-granularity sync absorption, reserving the fast DRAM path for asynchronous operations, meanwhile occupying NVM space only temporarily. To accomplish this, we designed a highly efficient log structure, developed mechanisms to address heterogeneous crash consistency, optimized for small writes, and implemented robust crash recovery and garbage collection methods. Compared to previous solutions, NVLog is lighter, more stable, and delivers higher performance, all while leveraging the mature kernel software stack and avoiding data migration overhead. Experimental results demonstrate that NVLog can accelerate disk file systems by up to 15.09x and outperform NOVA and SPFS in various scenarios by up to 3.72x and 324.11x, respectively.

## 中文摘要

本文提出 NVLog，一种面向磁盘文件系统的、基于 NVM 的写前日志，旨在传统存储栈内透明地利用 NVM 的高性能。NVLog 提供按需的字节粒度同步写吸收，为异步操作保留快速的 DRAM 路径，同时只临时占用 NVM 空间。为此，本文设计了高效的日志结构，开发了处理异构崩溃一致性的机制，针对小写进行了优化，并实现了稳健的崩溃恢复与垃圾回收方法。与以往方案相比，NVLog 更轻量、更稳定、性能更高，同时复用成熟的内核软件栈并避免数据迁移开销。实验结果表明，NVLog 能为磁盘文件系统带来最高 15.09 倍加速，并在多种场景下比 NOVA 与 SPFS 分别快最高 3.72 倍与 324.11 倍。

## 一句话总结

> NVM 的角色不是替代磁盘文件系统，而是做它旁边的写前日志：只把同步写记进 NVM，异步路径继续吃 DRAM 页缓存。

## 研究背景与问题

- NVM 的速度、容量与价格都介于 DRAM 与磁盘之间；专用 NVM 文件系统受容量限制，走 DAX 的 NOVA 在不少场景下甚至不如带 DRAM 页缓存的传统文件系统。
- 跨介质文件系统（Strata、Ziggurat）重设单体架构，难裁剪、难验证、成熟度低，且与在线系统正在使用的文件系统不兼容，迁移成本高。
- 在磁盘文件系统之上叠一层 NVM 也有副作用：SPFS 依赖对同步写的预测，预测未命中时仍走慢 I/O，数据被吸收后读也落在 NVM，两层设计还带来双重索引；P2CACHE 连普通写也写进 NVM，反而拖慢异步写。
- 只把日志搬到 NVM 只能加速日志阶段，数据仍要落盘；而带日志的文件系统写流量本就比不带日志的高 2.7 倍，同步场景下磁盘 I/O 的开销依然躲不掉。

## 核心贡献

- 提出 NVLog：把 NVM 实现为与 VFS 页缓存并列的写前日志而非 overlay 文件系统，既避免双层索引，又对现有应用保持透明。
- 按需、字节粒度的同步写吸收（on-demand byte-granularity sync absorption）：只把同步写记入 NVM，普通与异步读写继续走 DRAM 页缓存；日志只占少量 NVM 空间且仅临时占用，剩余空间仍可作分层缓存或直接供应用使用。
- 面向 DRAM、NVM、磁盘异构的崩溃一致性机制：严格定义 NVM 同步与磁盘回写的先后顺序，保证磁盘文件系统最终一致。
- 针对小写优化的日志结构与同步触发机制，抑制零散小写造成的写放大，并配套崩溃恢复与垃圾回收。

## 方法与技术要点

- 落点选择：日志挂在 VFS 页缓存一侧，读命中仍由 DRAM 服务，避免数据被 NVM 吸收后读延迟反而上升。
- 记录策略：仅同步写进入 NVM 日志，异步写不碰 NVM，因而不像 P2CACHE 那样把普通写也拖慢。
- 一致性顺序：以 NVM 同步与磁盘回写的严格先后关系维护跨设备最终一致性，崩溃后按日志补齐尚未落盘的同步写。
- 写放大抑制：优化同步操作的触发机制，把分散的小写合并处理，减少为提交与对齐产生的额外写。
- 空间回收：日志按需占用、及时回收，垃圾回收与恢复流程保证日志空间可循环使用。

## 评估与主要结果

- 评估对象是以 Ext-4 为代表的磁盘文件系统：SQLite 使用 YCSB 的 A 至 F 六种负载，RocksDB 使用 readrandomwriterandom 与 readseq；基线为 Ext-4、NOVA 与 SPFS。
- 相对磁盘文件系统最高加速 15.09 倍；在多种场景下比 NOVA 高 3.72 倍、比 SPFS 高 324.11 倍。
- RocksDB 的 readrandomwriterandom：比 Ext-4 快 1.38 倍、比 NOVA 快 1.24 倍；readseq 与 Ext-4 相当且优于 NOVA。
- SQLite 的 YCSB 写负载 A、B、D、F 均优于 Ext4 与 NOVA，最高加速 Ext-4 1.91 倍、超过 NOVA 1.33 倍；SPFS 在 RocksDB 清理既有数据库时多次崩溃，且无法在 O_DIRECT 模式下运行。

## 代码与研究制品

- [代码仓库](https://github.com/BugJLU/NVLog)

[返回 File Systems](index.md) · [返回 FAST 2025](../index.md)
