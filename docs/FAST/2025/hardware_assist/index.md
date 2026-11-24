---
title: "Hardware Assist · FAST 2025"
description: "FAST 2025 · Hardware Assist · 5 篇论文"
tags:
  - "FAST2025"
  - "Hardware Assist"
---

# Hardware Assist · FAST 2025

**中文主题**：硬件辅助

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-26 10:50–12:30 · **Chair**：Kiran Kumar Muniswamy Reddy（Amazon）

这一组工作共享同一个判断：把文件系统、数据库或锁协议的一部分职责下推到离数据更近的那层硬件——带透明压缩的计算存储盘、内嵌 FPGA 的 SmartSSD、FTL 自身的回收能力、RDMA 网卡与 SSD 控制器里的处理器。路线差别很大：有的重画索引与页面布局去换分析新鲜度，有的把 GC 这类后台重活整体搬进设备，有的反过来要求主机把段回收的责任交给设备，还有的只在设备资源恰好空闲时才下推。收益量级也随之分化：最高的一例把 goodput 提升 3.62 倍，D2FS 比 F2FS 快 3 倍；最谨慎的一例只换来 41% 吞吐与 3.85% 的尾延迟改善，说明硬件辅助的真实边界取决于设备算力与主机栈延迟的相对大小。

本 Session 共收录 **5** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [HaSiS: A Hardware-assisted Single-index Store for Hybrid Transactional and Analytical Processing](hasis_a_hardware_assisted_single_index_store_for_hybrid_transactional_and_analytical_processing.md) | HaSiS：面向混合事务与分析处理的硬件辅助单索引存储 | 把和解行列格式冲突的任务交给压缩盘：故意留空的 4KB 逻辑块不花物理容量，于是一个大页 B+-树就能同时服务交易与分析。 | [页面](https://www.usenix.org/conference/fast25/presentation/huang) · [PDF](https://www.usenix.org/system/files/fast25-huang.pdf) |
| [AegonKV: A High Bandwidth, Low Tail Latency, and Low Storage Cost KV-Separated LSM Store with SmartSSD-based GC Offloading](aegonkv_a_high_bandwidth_low_tail_latency_and_low_storage_cost_kv_separated_lsm_store_with_smartssd_based_gc_offloading.md) ([code](https://github.com/CGCL-codes/AegonKV)) | AegonKV：基于 SmartSSD GC 卸载的高带宽、低尾延迟、低存储成本 KV 分离 LSM 存储 | GC 本来就不该和前台读写抢带宽：把它整条流水线放进 SSD 的 FPGA，让吞吐、尾延迟、空间同时变好而不是互相交换。 | [页面](https://www.usenix.org/conference/fast25/presentation/duan) · [PDF](https://www.usenix.org/system/files/fast25-duan.pdf) |
| [D2FS: Device-Driven Filesystem Garbage Collection](d2fs_device_driven_filesystem_garbage_collection.md) ([code](https://github.com/ESOS-Lab/D2FS)) | D2FS：设备驱动的文件系统垃圾回收 | 既然闪存本来就会做 GC，就让它顺手把段的逻辑位置也搬一搬——有效页在物理与逻辑上同时聚簇，文件系统不必再动手。 | [页面](https://www.usenix.org/conference/fast25/presentation/kim-juwon) · [PDF](https://www.usenix.org/system/files/fast25-kim-juwon.pdf) |
| **杰出工件奖** · [ShiftLock: Mitigate One-sided RDMA Lock Contention via Handover](shiftlock_mitigate_one_sided_rdma_lock_contention_via_handover.md) ([code](https://github.com/thustorage/shiftlock)) | ShiftLock：通过锁移交缓解单边 RDMA 锁竞争 | 竞争不该表现为重试，而该表现为排队：持锁者把锁直接递给下一个客户端，等待者只在本机等一条通知。 | [页面](https://www.usenix.org/conference/fast25/presentation/gao) · [PDF](https://www.usenix.org/system/files/fast25-gao.pdf) |
| [Selective On-Device Execution of Data-Dependent Read I/Os](selective_on_device_execution_of_data_dependent_read_i_os.md) ([code](https://github.com/cssl-unist/sode)) | 数据依赖读 I/O 的选择性设备内执行 | 设备内计算的价值不在省带宽，而在让下一次读离数据更近——前提是那一刻设备处理器正好空闲。 | [页面](https://www.usenix.org/conference/fast25/presentation/park) · [PDF](https://www.usenix.org/system/files/fast25-park.pdf) |

> 获奖：**杰出工件奖**。

[返回 FAST 2025](../index.md)
