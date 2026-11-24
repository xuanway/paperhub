---
title: "Rethinking the Request-to-IO Transformation Process of File Systems for Full Utilization of High-Bandwidth SSDs"
description: "FAST 2025 · File Systems · 把写拆成 SSD 页对齐 IO 与残余 NVM 小 IO，写性能最高提升 29.76 倍"
tags:
  - "FAST2025"
  - "File Systems"
  - "SSD"
  - "NVM"
---

# Rethinking the Request-to-IO Transformation Process of File Systems for Full Utilization of High-Bandwidth SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">SSD 带宽持续上涨，但把请求转成内存页对齐同构块 IO 的文件系统连大块写都用不满带宽，根因是页对齐代价、页缓存开销与 IO 并发不足。OrchFS 用少量 NVM 吸收未对齐小写，只把对齐部分多线程直接下盘，写与读性能最高提升 29.76 倍与 6.79 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · File Systems</p>
</div>

**中文标题**：重新审视文件系统的请求到 IO 转换过程：充分利用高带宽 SSD

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/zhan](https://www.usenix.org/conference/fast25/presentation/zhan)

**论文 PDF**：[fast25-zhan.pdf](https://www.usenix.org/system/files/fast25-zhan.pdf)

**作者**：Yekang Zhan、Haichuan Hu、Xiangrui Yang、Qiang Cao（Huazhong University of Science and Technology）；Hong Jiang（University of Texas at Arlington）；Shaohua Wang、Jie Yao（Huazhong University of Science and Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 69–86 页

**Session**：File Systems · 2025-02-25 10:45–12:25 · Chair：Yu Hua（Huazhong University of Science and Technology）

**所属 Session**：[File Systems](index.md) · [FAST 2025](../index.md)

**关键词**：SSD, NVM, hybrid storage, request-to-IO transformation, direct IO, file system

---

## 英文摘要

The capacity and bandwidth of modern Solid-State Drives (SSDs) have been steadily increasing in recent years. Unfortunately, existing SSD file systems that transform user requests to memory-page aligned homogeneous block IOs have by and large failed to make full use of the superior write bandwidth of SSDs even for large writes. Our experimental analysis identifies three main root causes of this write inefficiency, namely, 1) SSD-page alignment cost, 2) page caching overhead, and 3) insufficient IO concurrency.

To fully exploit the potentials offered by modern SSDs, this paper proposes a heterogeneous-IO orchestrated file system with an alignment-based write-partition, or OrchFS, that leverages a small-size NVM (Non-Volatile Memory) to maximize SSD performance. OrchFS extends and improves the request-to-IO transformation functionality of file systems to proactively transform file-writes into SSD-page aligned SSD-IOs and/or remaining SSD-page unaligned NVM-IOs, and then to perform these IOs via their respective optimal data paths and in an explicit multi-threaded manner. To this end, OrchFS presents several novel enabling techniques, including heterogeneous-unit data layout, alignment-based file write partition, unified per-file mapping structure and embedded parallel IO engine. The experimental results show that OrchFS outperforms 1) EXT4 and F2FS on SSD, 2) NOVA, OdinFS and ArckFS on NVM, and 3) Strata, SPFS and PHFS on hybrid NVM-SSD by up to 29.76× and 6.79× in write and read performances, respectively.

## 中文摘要

近年来，现代固态盘（SSD）的容量与带宽持续增长。遗憾的是，现有 SSD 文件系统把用户请求转换为内存页对齐的同构块 IO，即使对大块写也基本未能充分利用 SSD 的优异写带宽。本文的实验分析识别出这种写低效的三个主要根因：1）SSD 页对齐代价；2）页缓存开销；3）IO 并发不足。为充分发挥现代 SSD 的潜力，本文提出一种以异构 IO 编排、基于对齐的写划分为核心的文件系统 OrchFS，它利用小容量 NVM（非易失内存）来最大化 SSD 性能。OrchFS 扩展并改进了文件系统的请求到 IO 转换功能，主动把文件写转换为 SSD 页对齐的 SSD-IO 和/或剩余未对齐的 NVM-IO，然后通过各自最优的数据路径、以显式多线程方式执行这些 IO。为此，OrchFS 提出了若干新的使能技术，包括异构单元数据布局、基于对齐的文件写划分、统一的每文件映射结构与内嵌并行 IO 引擎。实验结果表明，相比 1）SSD 上的 EXT4 与 F2FS、2）NVM 上的 NOVA、OdinFS 与 ArckFS、3）混合 NVM-SSD 上的 Strata、SPFS 与 PHFS，OrchFS 在写与读性能上分别最高提升 29.76 倍与 6.79 倍。

## 一句话总结

> 对齐不是细节而是前提：把写请求按 SSD 页切开，对齐部分直接多线程下盘，残余小写交给 NVM 吸收。

## 研究背景与问题

- SSD 带宽持续上升，PCIe4.0 NVMe 的读带宽约 5 至 7 GB/s、写带宽约 3 至 6 GB/s，PCIe5.0 还要再翻倍；但转成内存页对齐同构块 IO 的文件系统，随机写吞吐只有裸带宽的约三分之一与四分之一，1MB 上下的大块写也不到二分之一。
- 作者把写低效归为三点：SSD 页（如 16KB）对齐代价使未对齐写的延迟最高相差 10.71 倍、页缓存带来软件开销、IO 并发不足；而最优写路径要同时满足页对齐、直接 IO 与显式多线程三个条件，现有文件系统很少同时满足。
- 混合 NVM-SSD 系统要么把上层 NVM 当 SSD 的缓存，因而浪费高带宽 SSD；要么按大小把写分给 NVM 与 SSD，却忽视 SSD 侧的写低效。
- NVM 字节可寻址、偏好没有对齐代价的小访问，与 SSD 的 IO 偏好正好互补。

## 核心贡献

- 提出基于对齐的写划分（alignment-based write partition）：把一次文件写主动拆成 SSD 页对齐的 SSD-IO 与残余的未对齐 NVM-IO，使落到 SSD 的 IO 全部对齐。
- 设计异构单元数据布局（heterogeneous-unit data layout）：用 SSD block、NVM page 与 subpage chunk 三类存储单元承载不同粒度的数据。
- 设计统一的每文件映射结构（unified per-file mapping structure）：一次索引即可定位被拆分到 NVM 与 SSD 的数据。
- 构建内嵌并行 IO 引擎（embedded parallel IO engine）：协调三条数据路径的显式多线程下发，并保证数据一致性。

## 方法与技术要点

- 写划分策略：对齐优先（alignment-prioritization）决定哪些字节组成完整的 SSD 页，碎片最小化（fragmentation-minimization）再决定剩余字节并入 SSD 还是留在 NVM。
- 三路径：对齐的 SSD-IO 走直接 IO 的最优写路径；NVM-IO 走内存语义路径；SSD 读保留带页缓存的缓冲 IO，因为读能受益于页对齐的大写。
- 索引：统一映射结构把文件偏移映射到 SSD block 或 NVM 的 Upage，避免为跨介质的碎片做多次查找。
- IO 引擎与一致性：内嵌并行 IO 引擎把多路径 IO 显式多线程下发，并沿用 LibFS-KernelFS 架构与日志机制保证崩溃一致性。
- 碎片治理：SSD 侧按 block 对齐放置，块内不再碎片化；NVM 侧 Upage 内的 chunk 可合并，并可在后台迁移合并进 SSD block。

## 评估与主要结果

- 原型提供 30 多个常用 POSIX API，并在多种工作负载与真实应用上评估。
- 相对 SSD 文件系统 EXT4/F2FS、NVM 文件系统 NOVA/OdinFS/ArckFS、混合 NVM-SSD 系统 Strata/SPFS/PHFS，写性能最高领先 29.76 倍、3.49 倍与 7.16 倍，峰值读吞吐最高领先 3.08 倍、6.79 倍与 6.34 倍。
- 在图处理负载（LiveJournal、Twitter、Friendster）上表现出较好的负载适应性。
- 碎片：对 10GB 文件持续写入不同大小的未对齐随机写，NVM Upage 占比随写入量先升后降；1KB、4KB、16KB 用例因数据全部写入 NVM 而占比最高，写入越大 Upage 越少；开启迁移后，1KB 极端用例的 NVM 数据在 12 秒内全部迁到 SSD。

## 代码与研究制品

- [代码仓库](https://github.com/YekangZhan/OrchFS)

[返回 File Systems](index.md) · [返回 FAST 2025](../index.md)
