---
title: "PaCaR: Improved Buffered I/O Locality on NUMA Systems with Page Cache Replication"
description: "EuroSys 2026 · OS & Virtualization · Jérôme Coquisart (RWTH Aachen University), Julien Sopena (LIP6 (UPMC/CNRS) - Inr"
tags:
  - "EuroSys2026"
  - "OS & Virtualization"
---

# PaCaR: Improved Buffered I/O Locality on NUMA Systems with Page Cache Replication

**中文标题：** PaCaR：通过页缓存复制提升 NUMA 系统上的缓冲 I/O 局部性

**所属 Session：** [Session 1.1: OS & Virtualization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：OS & Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · OS & Virtualization</p>
</div>

**作者**：Jérôme Coquisart (RWTH Aachen University), Julien Sopena (LIP6 (UPMC/CNRS) - Inria), Redha Gouicem (RWTH Aachen University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769359)

**获奖：** 最佳论文、Gilles Muller 最佳研究制品（[官方获奖名单](https://2026.eurosys.org/eurosys-awards.html)）

## 英文摘要

Modern systems featuring multiple sockets suffer from the non-uniformity of performance of their memory accesses. Accessing memory of a remote node can lead to doubled latencies and halved bandwidth. This is particularly critical for I/O-intensive applications relying on the Linux page cache, where locality is paramount. Existing solutions migrating threads or memory across nodes fail to address the issue with highly parallel workloads, where a small working set is constantly accessed by multiple threads across nodes.

We present PaCaR, a novel page cache replication mechanism that enhances locality by transparently replicating cached pages across Non-Uniform Memory Access (NUMA) nodes. PaCaR ensures write consistency, adapts to memory pressure, and operates seamlessly without requiring application modifications. Evaluations on a dual socket NUMA server demonstrate up to 1.4x performance improvements in synthetic workloads and up to 25% gains in real-world workloads, showcasing the effectiveness of PaCaR in optimizing NUMA-aware buffered I/O operations.

## 中文摘要

支持多插槽的现代系统受内存访问性能非均匀性的困扰。访问远端节点的内存可能导致延迟翻倍、带宽减半。对于依赖 Linux 页缓存的 I/O 密集型应用而言，局部性至关重要，因此该问题尤为关键。现有方案通过跨节点迁移线程或内存来应对，但对于高度并行的工作负载仍无法奏效——这类负载中，一个小小的工作集会被多个节点上的多个线程持续访问。

我们提出 PaCaR，一种新颖的页缓存复制机制，通过在非统一内存访问（NUMA）节点之间透明地复制缓存页来增强局部性。PaCaR 保证写一致性，能够适应内存压力，且无需修改应用即可无缝运行。在双插槽 NUMA 服务器上的评测表明，PaCaR 在合成负载上带来最高 1.4 倍的性能提升，在真实负载上最高提升 25%，展现了其在优化 NUMA 感知的缓冲 I/O 操作方面的有效性。

**英文关键词：** NUMA, Memory Management, Page Cache, Replication, Data Locality, I/O Performance

**中文关键词：** NUMA、内存管理、页缓存、复制、数据局部性、I/O 性能

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
