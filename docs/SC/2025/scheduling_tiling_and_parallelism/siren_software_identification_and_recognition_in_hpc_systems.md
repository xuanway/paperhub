---
title: "SIREN: Software Identification and Recognition in HPC Systems"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Thomas Jakobsche; Fredrik Robertsén; Jessica R. Jones; Utz-Uwe Haus; Florina M. "
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# SIREN: Software Identification and Recognition in HPC Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Thomas Jakobsche; Fredrik Robertsén; Jessica R. Jones; Utz-Uwe Haus; Florina M. Ciorba

**会议**：SC 2025 · St. Louis, MO

## 摘要

HPC systems use monitoring and operational data analytics to ensure efficiency, performance, and orderly operations. Application-specific insights are crucial for analyzing the increasing complexity and diversity of HPC workloads, particularly through the identification of unknown software and recognition of repeated executions, which facilitate system optimization and security improvements. However, traditional identification methods using job or file names are unreliable for arbitrary user-provided names. Fuzzy hashing the content of executables detects similarities despite different code versions or compilation approaches while preserving privacy and file integrity, overcoming these limitations. We introduce SIREN, a process-level data collection framework for software identification and recognition. SIREN improves observability in HPC job execution by enabling analysis of process metadata, environment information, and executable fuzzy hashes. Findings from an opt-in deployment camp

---

## 一句话总结

> 该工作属于 Scheduling, Tiling, and Parallelism 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Scheduling, Tiling, and Parallelism 领域贡献新的设计范式或评估框架。
