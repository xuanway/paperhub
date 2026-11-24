---
title: "MedFS: Pursuing Low Update Overhead via Metadata-Enabled Delta Compression for Log-structured File System on Mobile Device"
description: "FAST 2025 · Compression and Deduplication · 把增量块写进 inode 内联区，移动端写流量降 55.1%"
tags:
  - "FAST2025"
  - "Compression and Deduplication"
  - "delta compression"
  - "log-structured file system"
---

# MedFS: Pursuing Low Update Overhead via Metadata-Enabled Delta Compression for Log-structured File System on Mobile Device

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">移动端日志结构文件系统引入增量压缩后，增量块与索引的维护开销会抵消收益；MedFS 把小块增量内联进 inode 约 3.69KB 的内联区，超出部分按热度打包成紧凑数据页。真实手机上写流量平均降低 55.1%，存储寿命延长 122.7%，I/O 性能最高提升 37.3%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Compression and Deduplication</p>
</div>

**中文标题**：MedFS：面向移动设备日志结构文件系统、以元数据支持增量压缩降低更新开销

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/wu](https://www.usenix.org/conference/fast25/presentation/wu)

**论文 PDF**：[fast25-wu.pdf](https://www.usenix.org/system/files/fast25-wu.pdf)

**作者**：Chao Wu、Cheng Ji（Nanjing University of Science and Technology）；Li-Pin Chang（National Yang Ming Chiao Tung University）；Zongwei Zhu（University of Science and Technology of China）；Congming Gao（Xiamen University）；Weichao Guo、Chao Yu（Guangdong Oppo Mobile Telecommunications Corp., Ltd）；Yanzhi Wang（Northeastern University）

**会议**：FAST 2025 · Santa Clara, CA · 第 461–478 页

**Session**：Compression and Deduplication · 2025-02-27 09:00–10:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**所属 Session**：[Compression and Deduplication](index.md) · [FAST 2025](../index.md)

**关键词**：delta compression, log-structured file system, F2FS, inode inline area, mobile storage, flash endurance

---

## 英文摘要

The increasing deployment of data-intensive applications on mobile devices poses a formidable challenge in designing flash-based file systems tailored to these needs. Studies have shown that adopting delta compression in log-structured file systems is promising for such an environment as it can effectively reduce the write stress and improve flash longevity. Unfortunately, delta compression suffers from large maintenance overhead. While prior works have introduced non-volatile memory buffer or battery-backed DRAM to mitigate this, they are less appealing for cost-sensitive mobile devices.

This paper introduces MedFS, a Metadata-enabled delta compression on log-structured File System for mobile devices, to achieve a good design trade-off in log-structured file systems employing delta compression. Through a comprehensive analysis of mobile applications and file update patterns, we develop delta-inlining technique, which consolidates delta updates within the inline area of the file's inode block. By leveraging the inherent inode structure and automatically flushing dirty inodes to storage, we effectively address the maintenance overhead associated with delta compression. Additionally, we propose a complementary delta maintenance strategy that selectively manages delta chunks in the data area, overcoming the space constraints of the inline area. Experimental results show that MedFS significantly reduces the write traffic by 55.1% on average, leading to the prolonged storage endurance by 122.7% and improved I/O performance by up to 37.3% over existing work.

## 中文摘要

数据密集型应用在移动设备上的不断部署，给面向这些需求设计基于闪存的文件系统带来了巨大挑战。已有研究表明，在日志结构文件系统中采用增量压缩对该环境很有前景，因为它能有效降低写入压力并延长闪存寿命。遗憾的是，增量压缩存在较大的维护开销。以往工作引入非易失内存缓冲或带电池的 DRAM 来缓解，但这对于成本敏感的移动设备并不划算。本文提出 MedFS——面向移动设备的、由元数据支持的日志结构文件系统增量压缩，以在采用增量压缩的日志结构文件系统中取得良好的设计折中。通过对移动应用与文件更新模式的全面分析，本文提出 delta-inlining 技术，把增量更新合并到文件 inode 块的内联区中。借助 inode 的固有结构并自动把脏 inode 刷写到存储，本文有效解决了增量压缩的维护开销问题。此外，本文提出一种补充的增量维护策略，在数据区中选择性地管理增量块，以克服内联区的空间限制。实验结果表明，相比现有工作，MedFS 平均降低写流量 55.1%，存储寿命延长 122.7%，I/O 性能最高提升 37.3%。

## 一句话总结

> 增量不必落到数据页：把差值塞进本就会变脏的 inode 内联区，一次更新只重写一个 4KB 块。

## 研究背景与问题

- **移动负载以小更新为主**：对 7 个流行应用的 17 类用户操作分析发现，77.1% 的写入流量来自文件更新，被修改页与原始页的平均差异只有 13.8%，增量压缩（delta compression）因此很有吸引力。
- **内联区容量限制小文件优化**：F2FS 的 inode 块中约 3.69KB 可作内联区（inline area），但真实设备上只有约 25% 的文件小于 3.69KB；90% 的文件小于 3.69MB，可把全部页索引放进内联区。
- **增量压缩的维护开销抵消收益**：需要同时维护原始页、增量块及二者的索引，写路径多落一份索引、读路径多取一次原始页；用外部 NVM 或带电池 DRAM 缓冲虽能缓解，但抬高成本敏感机型的硬件成本。
- **更新集中在少数文件类型**：SQLite 文件与临时文件分别占更新文件的 54.4% 与 14.5%；SQLite 文件的更新还会通过频繁的 fsync 触发急切刷盘，正是可以削减写压力的目标。

## 核心贡献

- **DCI（Delta Chunk Inlining）**：把小块增量直接嵌入文件 inode 块的内联区，借助 LFS 中文件更新本就会置脏 inode 的特性，使一次更新只重写 inode 块而不触碰数据页。
- **DCM（Delta Chunk Maintenance）**：针对内联区放不下的增量，按文件热度聚类后打包进紧凑数据页（Compact page）与元页（meta-page），把多个增量块的写合并为更少的块写。
- **移动 I/O 行为分析**：量化了移动应用的文件更新模式，据此论证增量压缩在移动端的利弊与取舍点。
- **真实设备原型**：在真实移动系统上实现 MedFS，并与 F2FS、FPC 等既有方案对比。

## 方法与技术要点

- **增量内联的落盘路径**：增量块写入 inode 的内联区并记录页内偏移与长度；由于 LFS 的更新已使 inode 变脏，只需把脏 inode 刷回，更新路径的块写次数从数据页加索引降为一次 inode 写。
- **内联区逐出**：内联区需要腾位时，先解压被逐出的增量并刷回数据页以保证一致性，这会短暂挂起对应偏移的页写，也正是 DCM 存在的理由。
- **热度聚类**：HCluster 按文件热度对增量块聚类（平均 1.2 微秒），再把增量打包进 Compact page，并保证至少 5 页压成 1 页，避免元页与 Compact page 的刷回造成读写放大。
- **后台整理**：聚类质心的更新只在后台线程 BGRes 中执行，平均耗时 0.9 毫秒，不占前台路径。
- **读路径优化**：增量块可从常驻内存的 inode 中直接取出，减少为取增量而产生的额外读放大。

## 评估与主要结果

- **写流量与寿命**：在真实移动平台上对比 F2FS 与 FPC，写流量平均降低 55.1%，存储寿命延长 122.7%。
- **I/O 性能**：写 I/O 平均提升 28.8%（最高 37.3%），读 I/O 平均提升 25.3%（最高 35.6%）。
- **能耗**：平均功耗比 F2FS-NODC 低 9.2%，比 FPC 低 2.6%。
- **开销**：增量压缩与解压平均 7.4 与 8.3 微秒，远低于常规压缩的 48.8 与 45.2 微秒，也低于 507.5 微秒的读 I/O 延迟；生成 4.2GB 文件时元页与 Compact page 只占 7.1MB；DCI 逐出增量时最坏 I/O 延迟中的处理时间平均为 42 至 475 毫秒。

[返回 Compression and Deduplication](index.md) · [返回 FAST 2025](../index.md)
