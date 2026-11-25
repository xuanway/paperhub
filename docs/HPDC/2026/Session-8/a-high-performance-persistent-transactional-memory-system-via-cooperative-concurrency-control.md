---
title: "A High-Performance Persistent Transactional Memory System via Cooperative Concurrency Control"
description: "HPDC 2026 · Session 8 — Storage & I/O for Data-Intensive Workloads"
tags:
  - "HPDC2026"
  - "Session 8"
  - "Storage & I/O for Data-Intensive Workloads"
---

# A High-Performance Persistent Transactional Memory System via Cooperative Concurrency Control

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 8</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807586)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#HuZCZXWX26](https://dblp.org/db/conf/hpdc/hpdc2026.html#HuZCZXWX26)

**作者**：Hao Hu, Xinrui Zheng, Yizou Chen, Xiangyu Zou, Erci Xu, Hongpeng Wang, Wen Xia

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）

---

## 英文摘要

Persistent Transactional Memory (PTM) simplifies crash-consistent programming on PM by providing atomicity and durability through transactional abstractions. Existing PTM systems suffer from fundamental limitations: sync-based PTMs couple transaction execution with data persistence, leading to poor concurrency and high latency. To address this, async-based PTMs decouple execution and persistence (log replay), but introduce significant coordination persistence overhead during log replay, which degrades performance. We present Courier, a high-performance PTM system that bridges execution and persistence through deterministic concurrency control. The key idea is to leverage the serializable transaction order established at runtime to deterministically schedule log replay, avoiding expensive coordination ordering overheads in persistence. To this end, Courier proposes a lightweight cooperative transaction framework to outline the persistence order in each individual log replay. By employing a series of techniques to coordinate with deterministic persistence order, Courier achieves effective and scalable log replay and avoids the need for sequential writes. Extensive evaluations using micro-benchmarks, YCSB, and TPCC show that Courier improves throughput by up to 10.4× and reduces 99th percentile latency by up to 16× compared to state-of-the-art PTM systems.

## 中文摘要

持久事务内存（PTM）通过事务抽象提供原子性与持久性，简化了 PM 上崩溃一致的程序设计。现有 PTM 系统存在根本性局限：基于同步的 PTM 将事务执行与数据持久化耦合，导致并发性差、延迟高。为此，基于异步的 PTM 将执行与持久化（日志重放）解耦，但在日志重放期间引入了显著的协调持久化开销，损害性能。我们提出 Courier，一个通过确定性并发控制衔接执行与持久化的高性能 PTM 系统。其核心思想是利用运行时建立的可串行化事务顺序来确定性地调度日志重放，避免持久化中昂贵的协调排序开销。为此，Courier 提出轻量级协作事务框架，在每次日志重放中勾勒持久化顺序。通过一系列与确定性持久化顺序协同的技术，Courier 实现了有效且可扩展的日志重放，并避免了对顺序写入的需求。使用微基准、YCSB 和 TPCC 的大量评估表明，与最先进的 PTM 系统相比，Courier 将吞吐最高提升 10.4 倍，并将第 99 百分位延迟最高降低 16 倍。

## 英文关键词

Non-volatile memory, persistent memory, transactional memory

## 中文关键词

非易失内存，持久内存，事务内存

---

[← 返回 Session 8 — Storage & I/O for Data-Intensive Workloads](index.md)
