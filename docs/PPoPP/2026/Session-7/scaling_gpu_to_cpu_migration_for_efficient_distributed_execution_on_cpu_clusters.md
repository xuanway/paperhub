---
title: "Scaling GPU-to-CPU Migration for Efficient Distributed Execution on CPU Clusters"
description: "PPoPP 2026 Session 7（Cluster and Cloud Computing）：把 GPU 程序分布式迁移到 CPU 集群，集群吞吐平均比 GPU 高 2.59×"
tags:
  - "PPoPP2026"
  - "Session-7"
  - "Cluster and Cloud Computing"
  - "GPU-to-CPU migration"
  - "CPU cluster"
  - "distributed execution"
authors:
  - "Ruobing Han"
  - "Hyesoon Kim"
session: "Session 7: Cluster and Cloud Computing"
session_number: 7
session_chair: "Ruslan Nikolaev"
date: "2026-02-03"
time: "12:10–12:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786435"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Scaling GPU-to-CPU Migration for Efficient Distributed Execution on CPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 CuCC 框架，把 GPU 到 CPU 的程序迁移扩展到 CPU 集群，通过分布式执行流程与通信优化降低跨节点网络开销，使集群整体吞吐平均比 GPU 高 2.59 倍。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 7: Cluster and Cloud Computing</p>
</div>

**作者**：Ruobing Han and Hyesoon Kim — Georgia Tech, USA

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 12:10–12:30 · Session 7: Cluster and Cloud Computing（主席：Ruslan Nikolaev）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786435) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

The growing demand for GPU resources has led to widespread shortages in data centers, prompting the exploration of CPUs as an alternative for executing GPU programs. While prior research supports executing GPU programs on single CPUs, these approaches struggle to achieve competitive performance due to the computational capacity gap between GPUs and CPUs. To further improve performance, we introduce CuCC, a framework that scales GPU-to-CPU migration to CPU clusters and utilizes distributed CPU nodes to execute GPU programs. Compared to single-CPU execution, CPU cluster execution requires cross-node communication to maintain data consistency. We present the CuCC execution workflow and communication optimizations, which aim to reduce network overhead. Evaluations demonstrate that CuCC achieves high scalability on large-scale CPU clusters and delivers runtimes approaching those of GPUs. In terms of cluster-wide throughput, CuCC enables CPUs to achieve an average of 2.59× higher throughput than GPUs.

## 中文摘要

对 GPU 资源日益增长的需求导致数据中心普遍出现短缺，促使人们探索以 CPU 作为执行 GPU 程序的替代方案。已有研究支持在单个 CPU 上执行 GPU 程序，但由于 GPU 与 CPU 之间的计算能力差距，这些方法难以获得有竞争力的性能。为进一步提升性能，我们提出 CuCC，一个将 GPU 到 CPU 的迁移扩展到 CPU 集群、并利用分布式 CPU 节点执行 GPU 程序的框架。与单 CPU 执行相比，CPU 集群执行需要跨节点通信来维护数据一致性。我们给出了 CuCC 的执行工作流与通信优化，旨在降低网络开销。评估表明，CuCC 在大规模 CPU 集群上具有良好的可扩展性，并能提供接近 GPU 的运行时间。在集群整体吞吐方面，CuCC 使 CPU 平均获得比 GPU 高 2.59 倍的吞吐量。

## 英文关键词

compiler optimization, GPU-to-CPU migration, CPU cluster

## 中文关键词

编译优化；GPU 到 CPU 迁移；CPU 集群

---

## 一句话总结

> 提出 CuCC 框架，把 GPU 到 CPU 的程序迁移扩展到 CPU 集群，通过分布式执行流程与通信优化降低跨节点网络开销，使集群整体吞吐平均比 GPU 高 2.59 倍。

## 研究问题

GPU 资源短缺促使人们用 CPU 执行 GPU 程序，但已有工作只支持单 CPU 执行，受 GPU 与 CPU 之间算力差距制约，性能难以与 GPU 竞争。

## 方法简述

- 提出 CuCC 框架，将 GPU-to-CPU 迁移扩展到 CPU 集群，利用多个分布式 CPU 节点协同执行 GPU 程序。
- 设计 CuCC 的执行流程，通过跨节点通信维持分布式执行中的数据一致性。
- 采用通信优化手段，降低集群执行 GPU 程序时的网络开销。

## 主要结果

- 评测显示 CuCC 在大规模 CPU 集群上具有良好的可扩展性，运行时间接近 GPU。
- 在集群整体吞吐方面，CuCC 使 CPU 平均获得比 GPU 高 2.59 倍的吞吐。

---

> 所属 Session：[Session 7: Cluster and Cloud Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
