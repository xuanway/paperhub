---
title: "TSUE: A Two-Stage Data Update Method for an Erasure Coded Cluster File System"
description: "HPDC 2025 · Session 3 — Storage Systems"
tags:
  - "HPDC2025"
  - "Session 3"
  - "Storage Systems"
---

# TSUE: A Two-Stage Data Update Method for an Erasure Coded Cluster File System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 3</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731577) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/wei.pdf)

**作者**：Zheng Wei, Jing Xing, Yida Gu, Wenjing Huang, Dong Dai, Guangming Tan, Dingwen Tao

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）

---

## 英文摘要

Compared to replication-based storage systems, erasure-coded storage incurs significantly higher overhead during data updates. To address this issue, various parity logging methods have been proposed. Nevertheless, due to the long update path and substantial amount of random I/O involved in erasure code update processes, the resulting long latency and low throughput often fail to meet the requirements of high performance applications. To this end, we propose a two-stage data update method called TSUE. TSUE divides the update process into a synchronous stage that records updates in a data log, and an asynchronous stage that recycles the log in real-time. TSUE effectively reduces update latency by transforming random I/O into sequential I/O, and it significantly reduces recycle overhead by utilizing a three-layer log and the spatio-temporal locality of access patterns. In SSDs cluster, TSUE significantly improves update performance, achieving improvements of 7.6× under Ali-Cloud trace, 5× under Ten-Cloud trace, while it also extends the SSD’s lifespan by up to 13× through reducing the frequencies of reads/writes and of erase operations.

## 中文摘要

与基于副本的存储系统相比，纠删码存储在数据更新时产生显著更高的开销。为应对该问题，已有多种奇偶校验日志方法被提出。然而，由于纠删码更新过程路径长且涉及大量随机 I/O，由此产生的长延迟与低吞吐往往无法满足高性能应用的需求。为此，我们提出一种两阶段数据更新方法 TSUE。TSUE 将更新过程划分为同步阶段（将更新记录到数据日志）与异步阶段（实时回收日志）。TSUE 通过将随机 I/O 转化为顺序 I/O 有效降低更新延迟，并利用三层日志与访问模式的时空局部性显著降低回收开销。在 SSD 集群中，TSUE 显著提升更新性能：在阿里云轨迹下提升 7.6 倍，在腾讯云轨迹下提升 5 倍；同时通过降低读写与擦除操作频率，将 SSD 寿命最高延长 13 倍。

## 英文关键词

Erasure code, Cluster file system, Incremental update, Spatial-Temporal locality, Real-time log recycle.

## 中文关键词

纠删码，集群文件系统，增量更新，时空局部性，实时日志回收。

---

[← 返回 Session 3 — Storage Systems](index.md)
