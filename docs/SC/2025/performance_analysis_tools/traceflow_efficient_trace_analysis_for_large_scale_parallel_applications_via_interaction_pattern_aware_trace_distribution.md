---
title: "TraceFlow: Efficient Trace Analysis for Large-Scale Parallel Applications via Interaction Pattern-Aware Trace Distribution"
description: "SC 2025 · Performance: Analysis Tools · Yuyang Jin; Xirui Shui; Mingshu Zhai; Zan Zong; Feng Zhang; Felix Wolf; Jidong Z"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# TraceFlow: Efficient Trace Analysis for Large-Scale Parallel Applications via Interaction Pattern-Aware Trace Distribution

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Yuyang Jin; Xirui Shui; Mingshu Zhai; Zan Zong; Feng Zhang; Felix Wolf; Jidong Zhai

**会议**：SC 2025 · St. Louis, MO

## 摘要

Trace analysis of large-scale parallel applications is crucial for understanding and optimizing performance. It primarily focuses on the interaction behaviors between different parallel processes, such as synchronization waits and asynchronous overlaps. The trace size explodes as the parallel scale of applications, thus current methods analyze traces in parallel to ensure analysis speed. However, due to the interaction pattern-agnostic trace distribution, they often introduce inter-process communications to fetch non-local event data during interaction analysis, leading to excessively long trace analysis time. To address this issue, we propose TraceFlow, a trace analysis tool for large-scale parallel applications, which achieves a nearly communication-free analysis through an interaction pattern-aware trace distribution strategy. We evaluate the efficiency of TraceFlow on widely used benchmarks and several real-world applications with up to 8,192 processes. Experimental results show th

---

## 一句话总结

> 该工作属于 Performance: Analysis Tools 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Analysis Tools 领域贡献新的设计范式或评估框架。
