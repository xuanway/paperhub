---
title: "Compression and Deduplication · FAST 2025"
description: "FAST 2025 · Compression and Deduplication · 4 篇论文"
tags:
  - "FAST2025"
  - "Compression and Deduplication"
---

# Compression and Deduplication · FAST 2025

**中文主题**：压缩与去重

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-27 09:00–10:20 · **Chair**：Gala Yadgar（Technion—Israel Institute of Technology）

压缩与去重的收益常被维护成本吃掉，本 Session 的四项工作都在把这份成本从关键路径上挪走：有的把增量放进文件系统元数据，有的把去重映射并入逻辑地址映射，有的让内存压缩粒度跟随页间关联，有的用 CPU 向量指令改写分块扫描。共同点是不新增硬件，而是在 inode、映射表、LRU 与指令选择上重新分配元数据与计算。代表性结果是写流量下降 55.1%、去重 I/O 吞吐提升 5.6%–35.0%、应用启动快 1.55 倍、CDC 吞吐提升 21–46 倍。

本 Session 共收录 **4** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [MedFS: Pursuing Low Update Overhead via Metadata-Enabled Delta Compression for Log-structured File System on Mobile Device](medfs_pursuing_low_update_overhead_via_metadata_enabled_delta_compression_for_log_structured_file_system_on_mobile_device.md) | MedFS：面向移动设备日志结构文件系统、以元数据支持增量压缩降低更新开销 | 增量不必落到数据页：把差值塞进本就会变脏的 inode 内联区，一次更新只重写一个 4KB 块。 | [页面](https://www.usenix.org/conference/fast25/presentation/wu) · [PDF](https://www.usenix.org/system/files/fast25-wu.pdf) |
| **杰出工件奖** · [Don't Maintain Twice, It's Alright: Merged Metadata Management in Deduplication File System with GogetaFS](don_t_maintain_twice_it_s_alright_merged_metadata_management_in_deduplication_file_system_with_gogetafs.md) ([code](https://github.com/GogetaFS/GogetaFS-AE)) | 不必重复维护：GogetaFS 去重文件系统中的合并元数据管理 | 去重条目与文件系统条目本就指向同一个物理块，维护两遍纯属多余，合并成一条 LFP 映射即可。 | [页面](https://www.usenix.org/conference/fast25/presentation/pan) · [PDF](https://www.usenix.org/system/files/fast25-pan.pdf) |
| [Archer: Adaptive Memory Compression with Page-Association-Rule Awareness for High-Speed Response of Mobile Devices](archer_adaptive_memory_compression_with_page_association_rule_awareness_for_high_speed_response_of_mobile_devices.md) | Archer：面向移动设备快速响应的页关联规则感知自适应内存压缩 | 约四分之一的匿名页存在隐性关联，把它们成组压缩比逐页压缩更快，而且不需要改动硬件。 | [页面](https://www.usenix.org/conference/fast25/presentation/li) · [PDF](https://www.usenix.org/system/files/fast25-li.pdf) |
| [VectorCDC: Accelerating Data Deduplication with Vector Instructions](vectorcdc_accelerating_data_deduplication_with_vector_instructions.md) ([code](https://github.com/UWASL/dedup-bench)) | VectorCDC：利用向量指令加速数据去重 | 无哈希分块只有两个热点阶段，找窗口极值和范围扫描，都能用整寄存器比较并行化。 | [页面](https://www.usenix.org/conference/fast25/presentation/udayashankar) · [PDF](https://www.usenix.org/system/files/fast25-udayashankar.pdf) |

> 获奖：**杰出工件奖**。

[返回 FAST 2025](../index.md)
