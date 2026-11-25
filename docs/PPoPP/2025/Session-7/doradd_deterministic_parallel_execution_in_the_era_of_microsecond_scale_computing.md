---
title: "DORADD: Deterministic Parallel Execution in the Era of Microsecond-Scale Computing"
description: "PPoPP 2025 Session 7（Scheduling and Resource Management）：单调度器 + 无同步 worker pool，尾延迟改善 150×/300×"
tags:
  - "PPoPP2025"
  - "Session-7"
  - "Scheduling and Resource Management"
  - "Deterministic Parallelism"
  - "Runtime Scheduling"
  - "Datacenter Systems"
authors:
  - "Zhengqing Liu"
  - "Musa Unal"
  - "Matthew J. Parkinson"
  - "Marios Kogias"
session: "Session 7: Scheduling and Resource Management"
session_number: 7
session_chair: "Jie Ren"
date: "2025-03-04"
time: "11:40–12:00"
room: "Acacia D"
doi: "10.1145/3710848.3710872"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# DORADD: Deterministic Parallel Execution in the Era of Microsecond-Scale Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出低延迟、高吞吐的确定性并行运行时 DORADD，用单调度器确定性地构建请求依赖图，由 worker pool 无同步执行，并以核心流水化突破调度瓶颈。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 7: Scheduling and Resource Management</p>
</div>

**作者**：Zhengqing Liu (Imperial College London); Musa Unal (EPFL); Matthew J. Parkinson (Azure Research, Microsoft); Marios Kogias (Imperial College London)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 11:40–12:00 · Session 7: Scheduling and Resource Management（主席：Jie Ren）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710872) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出低延迟、高吞吐的确定性并行运行时 DORADD，用单调度器确定性地构建请求依赖图，由 worker pool 无同步执行，并以核心流水化突破调度瓶颈。

## 研究问题

现有确定性并行系统（DPS）存在批处理执行、运行时同步低效等设计缺陷，无法满足现代数据中心微秒级、高吞吐分布式系统的需求。

## 方法简述

- 混合调度方案把请求分发与执行解耦：单个 dispatcher 确定性地构建动态依赖图。
- worker pool 以 work-conserving、无同步的方式独立执行请求。
- 基于 core pipelining 突破单 dispatcher 的吞吐瓶颈。

## 主要结果

- 用 DORADD 构建内存数据库，在 YCSB 与 TPC-C 上相比 SOTA 确定性数据库 Caracal，吞吐最高提升 2.5×。
- 非竞争与竞争场景下尾延迟分别改善 150× 与 300× 以上；相比非确定性 RPC 调度器 Caladan，确定性未带来额外性能开销。

<details>
<summary>原文摘要（英文）</summary>

Deterministic parallelism is a key building block for distributed and fault-tolerant systems that offers substantial performance benefits while guaranteeing determinism. By studying existing deterministically parallel systems (DPS), we identify certain design pitfalls, such as batched execution and inefficient runtime synchronization, that preclude them from meeting the demands of 𝜇𝑠-scale and high-throughput distributed systems deployed in modern datacenters. We present DORADD, a deterministically parallel runtime with low latency and high throughput, designed for modern datacenter services. DORADD introduces a hybrid scheduling scheme that effectively decouples request dispatching from execution. It employs a single dispatcher to deterministically construct a dynamic dependency graph of incoming requests and worker pools that can independently execute requests in a work-conserving and synchronization-free manner. Furthermore, DORADD overcomes the single-dispatcher throughput bottleneck based on core pipelining. We use DORADD to build an in-memory database and compare it with Caracal, the current state-of-the-art deterministic database, via the YCSB and TPC-C benchmarks. Our evaluation shows up to 2.5× better throughput and more than 150× and 300× better tail latency in non-contended and contended cases, respectively. We also compare DORADD with Caladan, the state-of-the-art non-deterministic remote procedure call (RPC) scheduler, and demonstrate that determinism in DORADD does not incur any performance overhead. This work is licensed under 0.

</details>

---

> 所属 Session：[Session 7: Scheduling and Resource Management](index.md) · 返回 [PPoPP 2025 总览](../index.md)
