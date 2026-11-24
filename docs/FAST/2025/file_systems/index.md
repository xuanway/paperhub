---
title: "File Systems · FAST 2025"
description: "FAST 2025 · File Systems · 5 篇论文"
tags:
  - "FAST2025"
  - "File Systems"
---

# File Systems · FAST 2025

**中文主题**：文件系统

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-25 10:45–12:25 · **Chair**：Yu Hua（Huazhong University of Science and Technology）

除 Ananke 外的四篇论文面对同一个落差：NVM、CMM-H SSD 与多通道高带宽 SSD 的硬件能力已经到位，文件系统却仍按慢盘与单核设计，日志提交、写对齐和垃圾回收把可用并行度吃掉。应对方式分成两路：在成熟文件系统旁加一层介质感知的旁路（NVM 写前日志、目录粒度日志、异构 IO 划分），或者直接重写文件系统的回收路径；收益从 3.5 倍到 324.11 倍不等，差距本身就说明各系统的瓶颈并不在同一处。同 Session 的 Ananke 摘得最佳论文，它关注的不是吞吐而是微内核进程崩溃后的透明恢复。

本 Session 共收录 **5** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| **最佳论文** · [Fast, Transparent Filesystem Microkernel Recovery with Ananke](fast_transparent_filesystem_microkernel_recovery_with_ananke.md) | Ananke：快速、透明的文件系统微内核恢复 | Ananke 把微内核文件系统的进程崩溃当作一次可利用的恢复机会：在宿主 OS 协调下保留内存中的崩溃日志 p-log，让重启后的文件系统服务精确复原应用所见的全部状态，而不是只把磁盘恢复到一致状态。 | [页面](https://www.usenix.org/conference/fast25/presentation/liu-jing) · [PDF](https://www.usenix.org/system/files/fast25-liu-jing.pdf) |
| [Boosting File Systems Elegantly: A Transparent NVM Write-ahead Log for Disk File Systems](boosting_file_systems_elegantly_a_transparent_nvm_write_ahead_log_for_disk_file_systems.md) ([code](https://github.com/BugJLU/NVLog)) | 优雅地加速文件系统：面向磁盘文件系统的透明 NVM 写前日志 | NVM 的角色不是替代磁盘文件系统，而是做它旁边的写前日志：只把同步写记进 NVM，异步路径继续吃 DRAM 页缓存。 | [页面](https://www.usenix.org/conference/fast25/presentation/wang) · [PDF](https://www.usenix.org/system/files/fast25-wang.pdf) |
| [DJFS : Directory-Granularity Filesystem Journaling for CMM-H SSDs](djfs_directory_granularity_filesystem_journaling_for_cmm_h_ssds.md) | DJFS：面向 CMM-H SSD 的目录粒度文件系统日志 | 日志变慢的根因不是提交延迟而是事务锁定窗口；把事务边界从全局挪到目录，多核与 CMM-H SSD 的并行度才真正用得上。 | [页面](https://www.usenix.org/conference/fast25/presentation/yoo) · [PDF](https://www.usenix.org/system/files/fast25-yoo.pdf) |
| [ScaleLFS: A Log-Structured File System with Scalable Garbage Collection for Commodity SSDs](scalelfs_a_log_structured_file_system_with_scalable_garbage_collection_for_commodity_ssds.md) | ScaleLFS：面向商用 SSD、具备可扩展垃圾回收的日志结构文件系统 | LFS 的持续性能卡在 GC：把“一个回收器管所有段”换成每核一对一独占资源，才吃得到多核与多通道 SSD 的并行度。 | [页面](https://www.usenix.org/conference/fast25/presentation/ha) · [PDF](https://www.usenix.org/system/files/fast25-ha.pdf) |
| [Rethinking the Request-to-IO Transformation Process of File Systems for Full Utilization of High-Bandwidth SSDs](rethinking_the_request_to_io_transformation_process_of_file_systems_for_full_utilization_of_high_bandwidth_ssds.md) ([code](https://github.com/YekangZhan/OrchFS)) | 重新审视文件系统的请求到 IO 转换过程：充分利用高带宽 SSD | 对齐不是细节而是前提：把写请求按 SSD 页切开，对齐部分直接多线程下盘，残余小写交给 NVM 吸收。 | [页面](https://www.usenix.org/conference/fast25/presentation/zhan) · [PDF](https://www.usenix.org/system/files/fast25-zhan.pdf) |

> 获奖：**最佳论文**。

[返回 FAST 2025](../index.md)
