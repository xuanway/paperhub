---
title: "gParaKV: A GPGPU-Accelerated Key-Value Separation-Based KV Store with Optimized Compaction and Garbage Collection"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Hui Sun; Xiangxiang Jiang; Xiao Qin; Song Jiang; Enhui Wang"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# gParaKV: A GPGPU-Accelerated Key-Value Separation-Based KV Store with Optimized Compaction and Garbage Collection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Hui Sun; Xiangxiang Jiang; Xiao Qin; Song Jiang; Enhui Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

LSM tree-based key-value stores are widely deployed in modern cloud storage systems thanks to high data storage efficiency and retrieval capabilities. The compaction in the LSM tree, however, results in severe performance bottlenecks, especially in large-sized value cases. While key-value separation methods mitigate the performance bottlenecks caused by compaction, the existing methods do not fully address merge-sorting during compaction and expensive garbage collection (GC). We propose gParaKV, a GPGPU-empowered KV store with a KV separation mechanism, leveraging the GPGPU parallel technology to accelerate merge-sorting in compaction and GC. gParaKV embraces a GPGPU bitmap structure, parallel data marking, and a parallel GC mechanism. These critical components curtail the overhead of merge-sorting and GC by virtue of parallel computing. We compare it with state-of-the-art KV stores under various workloads. The experimental results show that gParaKV can improve the write performance an

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
