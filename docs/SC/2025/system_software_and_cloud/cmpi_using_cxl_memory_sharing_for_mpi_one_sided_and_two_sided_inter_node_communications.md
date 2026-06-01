---
title: "cMPI: Using CXL Memory Sharing for MPI One-Sided and Two-Sided Inter-Node Communications"
description: "SC 2025 · System Software and Cloud · Xi Wang; Bin Ma; Jongryool Kim; Byungil Koh; Hoshik Kim; Dong Li"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# cMPI: Using CXL Memory Sharing for MPI One-Sided and Two-Sided Inter-Node Communications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Xi Wang; Bin Ma; Jongryool Kim; Byungil Koh; Hoshik Kim; Dong Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

Message Passing Interface (MPI) is a foundational programming model for high-performance computing. MPI libraries traditionally employ network interconnects (e.g., Ethernet and InfiniBand) and network protocols (e.g., TCP and RoCE) with complex software stacks for cross-node communication. We present cMPI, the first work to optimize MPI point-to-point communication (both one-sided and two-sided) using CXL memory sharing on a real CXL platform, transforming cross-node communication into memory transactions and data copies within CXL memory, bypassing traditional network protocols. We analyze performance across various interconnects and find that CXL memory sharing achieves 7.2×-8.1× lower latency than TCP-based interconnects deployed in small- and medium-scale clusters. We address challenges of CXL memory sharing for MPI communication, including data object management over the dax representation [50], cache coherence, and atomic operations. Overall, cMPI outperforms TCP over standard Et

---

## 一句话总结

> 该工作属于 System Software and Cloud 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 System Software and Cloud 领域贡献新的设计范式或评估框架。
