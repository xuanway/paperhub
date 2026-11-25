---
title: "Pome: Parallelizing I/Os and Computations for Efficient LSM-tree-based Data Storage"
description: "HPDC 2026 · Session 8 — Storage & I/O for Data-Intensive Workloads"
tags:
  - "HPDC2026"
  - "Session 8"
  - "Storage & I/O for Data-Intensive Workloads"
---

# Pome: Parallelizing I/Os and Computations for Efficient LSM-tree-based Data Storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 8</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807603)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#HuZJW26](https://dblp.org/db/conf/hpdc/hpdc2026.html#HuZJW26)

**获奖**：HPDC 2026 最佳论文奖（[官方议程](https://hpdc.sci.utah.edu/2026/program.html)标注 Best Paper Winner）

**作者**：Yanpeng Hu, Li Zhu, Lei Jia, Chundong Wang

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）

---

## 英文摘要

CPU computations and I/O operations are fundamental to data storage systems. Storage systems conduct computations with their user threads, such as sorting data for orderliness. They handle I/Os through system calls (syscalls) including file write, read, and fsync, which the OS’s kernel threads perform with storage devices. Today, LSM-tree-based storage systems are widely deployed in production environments. Compaction is an essential operation that LSM-tree employs to maintain its tiered tree-like structure by re-sorting and re-storing data through computations and I/Os, respectively. In this paper, we first overhaul the procedure of a compaction. We find that computations and I/Os execute in a sequential order. After re-sorting data, the user thread waits for a kernel thread to complete file write and fsync I/Os. These costly synchronous I/Os create a severely long critical path that affects the performance of LSM-tree. To address this issue, we propose parallelizing I/Os and computations for efficient LSM-tree-based data storage (Pome). Pome decouples computations from I/Os within each compaction by referring to its new protocol that moves I/O operations out of the critical path. To this end, it conducts asynchronous I/Os by using io_uring. Furthermore, regarding the potential I/O congestion caused by accelerated compactions, Pome incorporates an adaptive I/O rate limiter to achieve smooth execution. We prototype Pome on top of RocksDB. Experimental results demonstrate that Pome significantly improves the performance of RocksDB and outperforms several state-of-the-art LSM-tree variants.

## 中文摘要

CPU 计算与 I/O 操作是数据存储系统的基础。存储系统用其用户线程执行计算，例如为保持有序而对数据排序。它们通过系统调用（syscall）处理 I/O，包括文件写、读和 fsync，由操作系统内核线程与存储设备完成。如今，基于 LSM 树的存储系统被广泛部署于生产环境。压缩（compaction）是 LSM 树用于维持其分层树状结构的关键操作，它分别通过计算与 I/O 重新排序并重新存储数据。本文首先彻底剖析了压缩流程。我们发现计算与 I/O 按顺序执行：在重新排序数据后，用户线程等待内核线程完成文件写入和 fsync I/O。这些昂贵的同步 I/O 形成极长的关键路径，影响 LSM 树的性能。为解决该问题，我们提出将 I/O 与计算并行化以实现高效的基于 LSM 树的数据存储（Pome）。Pome 依据其新协议将 I/O 操作移出关键路径，从而在每次压缩内将计算与 I/O 解耦。为此，它使用 io_uring 执行异步 I/O。此外，针对加速压缩可能引发的 I/O 拥塞，Pome 引入自适应 I/O 限速器以实现平滑执行。我们在 RocksDB 之上实现 Pome 原型。实验结果表明，Pome 显著提升 RocksDB 的性能，并优于若干最先进的 LSM 树变体。

## 英文关键词

Parallel I/O and Computation Model, LSM-tree, Compaction

## 中文关键词

并行 I/O 与计算模型，LSM 树，压缩

---

[← 返回 Session 8 — Storage & I/O for Data-Intensive Workloads](index.md)
