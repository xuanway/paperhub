---
title: "Accelerating Transactional Execution via Processing-In-Memory"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · André Lopes (INESC-ID, IST, Universidade de Lisboa), Daniel Castro (INESC-ID, IS"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# Accelerating Transactional Execution via Processing-In-Memory

**中文标题：** 通过存内计算加速事务执行

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：André Lopes (INESC-ID, IST, Universidade de Lisboa), Daniel Castro (INESC-ID, IST, Universidade de Lisboa), Paolo Romano (INESC-ID, IST, Universidade de Lisboa)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803621)

## 英文摘要

Processing-in-Memory (PIM) integrates compute capabilities directly into memory modules to reduce costly data movement, promising large performance gains for data-intensive workloads. In PIM systems, small processors—Data Processing Units (DPUs)—are embedded near memory banks to execute computations close to where data resides. Although PIM has shown strong benefits for analytical tasks, supporting transactional workloads such as online transaction processing (OLTP) remains challenging due to decentralized DPUs and the lack of efficient hardware coordination mechanisms.

We present PIM-TIDE (Processing-in-Memory with Transactional Isolation via Deterministic Execution), a new transaction execution platform designed for PIM architectures. PIM-TIDE provides a lightweight software-based coordination mechanism that enables transactions to span multiple DPUs, while ensuring consistency, atomicity, and isolation. By using the CPU selectively for transaction coordination, PIM-TIDE avoids the performance penalties of frequent inter-DPU communication. We evaluate PIM-TIDE on real PIM hardware (UPMEM) and show that it achieves scalable transaction processing with low overhead, both in terms of performance and energy efficiency, in TPC-C based workloads.

## 中文摘要

存内计算（PIM）将计算能力直接集成到内存模块中，以减少昂贵的数据移动，为数据密集型工作负载带来大幅性能提升的潜力。在 PIM 系统中，称为数据处理单元（DPU）的小型处理器被嵌入到内存存储体附近，以便在数据所在之处就近执行计算。尽管 PIM 在分析型任务上表现出显著优势，但由于 DPU 是分布化的，且缺乏高效的硬件协调机制，支持在线事务处理（OLTP）等事务型工作负载仍然具有挑战性。

我们提出 PIM-TIDE（Processing-in-Memory with Transactional Isolation via Deterministic Execution，即通过确定性执行实现事务隔离的存内计算），一个为 PIM 架构设计的新事务执行平台。PIM-TIDE 提供一种轻量级、基于软件的协调机制，使事务能够跨多个 DPU 执行，同时确保一致性、原子性和隔离性。通过有选择地使用 CPU 进行事务协调，PIM-TIDE 避免了频繁的 DPU 间通信带来的性能损失。我们在真实的 PIM 硬件（UPMEM）上评估 PIM-TIDE，表明它在基于 TPC-C 的工作负载中实现了可扩展的事务处理，且在性能和能效两方面都具有低开销。

**英文关键词：** Processing-in-Memory, Transaction processing systems, Concurrency control, Transactional memory

**中文关键词：** 存内计算、事务处理系统、并发控制、事务内存

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
