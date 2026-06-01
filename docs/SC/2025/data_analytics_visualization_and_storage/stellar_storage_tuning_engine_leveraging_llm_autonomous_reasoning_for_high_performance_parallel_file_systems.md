---
title: "STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High-Performance Parallel File Systems"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Chris Egersdoerfer; Philip Carns; Shane Snyder; Robert Ross; Dong Dai"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High-Performance Parallel File Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Chris Egersdoerfer; Philip Carns; Shane Snyder; Robert Ross; Dong Dai

**会议**：SC 2025 · St. Louis, MO

## 摘要

I/O performance is crucial to efficiency in data-intensive scientific computing, but tuning large-scale storage systems is complex, costly, and notoriously manpower-intensive, making it inaccessible for most domain scientists. In this study, we propose STELLAR, an autonomous tuner for high-performance parallel file systems. Our evaluations show that STELLAR always selects near-optimal configurations for the parallel file systems within the first five attempts, even for previously unseen applications. STELLAR’s human-like efficiency is fundamentally different from existing auto-tuning methods, which often require hundreds of thousands of iterations to converge. STELLAR achieves this through Retrieval-Augmented Generation, external tool execution, LLM-based reasoning, and a multi-step agent design to stabilize reasoning and combat hallucinations. STELLAR's architecture opens new avenues for addressing complex system optimization problems, especially those characterized by vast search spa

---

## 一句话总结

> 该工作属于 Data Analytics, Visualization, and Storage 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Data Analytics, Visualization, and Storage 领域贡献新的设计范式或评估框架。
