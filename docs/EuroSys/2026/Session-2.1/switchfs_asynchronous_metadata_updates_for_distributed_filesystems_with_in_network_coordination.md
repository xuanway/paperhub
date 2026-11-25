---
title: "SwitchFS: Asynchronous Metadata Updates for Distributed Filesystems with In-Network Coordination"
description: "EuroSys 2026 · File Systems & Storage · Jingwei Xu (Shanghai Jiao Tong University), Mingkai Dong (Shanghai Jiao Tong Uni"
tags:
  - "EuroSys2026"
  - "File Systems & Storage"
---

# SwitchFS: Asynchronous Metadata Updates for Distributed Filesystems with In-Network Coordination

**中文标题：** SwitchFS：借助网内协同实现分布式文件系统的异步元数据更新

**所属 Session：** [Session 2.1: File Systems & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：File Systems & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · File Systems & Storage</p>
</div>

**作者**：Jingwei Xu (Shanghai Jiao Tong University), Mingkai Dong (Shanghai Jiao Tong University), Qiulin Tian (Shanghai Jiao Tong University), Ziyi Tian (Shanghai Jiao Tong University), Tong Xin (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769349)

## 英文摘要

Distributed filesystem metadata updates are typically synchronous. This creates inherent challenges for access efficiency, load balancing, and directory contention, especially under dynamic and skewed workloads. This paper argues that synchronous updates are overly conservative. We propose SwitchFS with asynchronous metadata updates that allow operations to return early and defer directory updates until reads, both hiding latency and amortizing overhead. The key challenge lies in efficiently maintaining the synchronous POSIX semantics of metadata updates. To address this, SwitchFS is co-designed with a programmable switch, leveraging the limited on-switch resources to track directory states with negligible overhead. This allows SwitchFS to aggregate and apply delayed updates efficiently, using batching and consolidation before directory reads. Evaluation shows that SwitchFS achieves up to 13.34× and 3.85× higher throughput, and 61.6% and 57.3% lower latency than two state-of-the-art distributed filesystems, Emulated-InfiniFS and Emulated-CFS, respectively, under skewed workloads. For real-world workloads, SwitchFS improves end-to-end throughput by 21.1×, 1.1×, and 0.3× over CephFS, Emulated-InfiniFS, and Emulated-CFS, respectively.

## 中文摘要

分布式文件系统的元数据更新通常是同步的。这给访问效率、负载均衡和目录争用带来了固有挑战，在动态且倾斜的工作负载下尤为如此。本文认为同步更新过于保守。我们提出 SwitchFS，采用异步元数据更新，允许操作提前返回，并把目录更新推迟到读取时进行，从而既隐藏了延迟，又分摊了开销。其关键挑战在于高效地维持元数据更新的同步 POSIX 语义。为此，SwitchFS 与可编程交换机协同设计，利用交换机上有限的资源以可忽略的开销跟踪目录状态。这使 SwitchFS 能够在目录读取之前，通过批处理与合并来高效地聚合和应用延迟更新。评估表明，在倾斜工作负载下，SwitchFS 相比两种最先进的分布式文件系统 Emulated-InfiniFS 和 Emulated-CFS，吞吐量分别最高提升 13.34 倍和 3.85 倍，延迟分别降低 61.6% 和 57.3%。在真实工作负载下，SwitchFS 相比 CephFS、Emulated-InfiniFS 和 Emulated-CFS 将端到端吞吐量分别提升了 21.1 倍、1.1 倍和 0.3 倍。

**英文关键词：** Distributed file system, Metadata management, Programmable switches

**中文关键词：** 分布式文件系统、元数据管理、可编程交换机

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
