---
title: "MLP-Offload: Multi-Level, Multi-Path Offloading for LLM Pre-Training To Break the GPU Memory Wall"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Avinash Kumar Maurya; M. Mustafa Rafique; Franck Cappello; Bogdan Nicolae"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# MLP-Offload: Multi-Level, Multi-Path Offloading for LLM Pre-Training To Break the GPU Memory Wall

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Avinash Kumar Maurya; M. Mustafa Rafique; Franck Cappello; Bogdan Nicolae

**会议**：SC 2025 · St. Louis, MO

## 摘要

Large language models (LLMs) have been rapidly adopted across all domains, supporting divergent use cases with remarkable accuracy. However, training these massive models requires scaling across multiple GPUs. Given the expensive and limited GPU resources, advanced redundancy elimination and parallelization techniques are employed to maximize training throughput. Furthermore, to run LLMs larger than the aggregated memory of multiple GPUs, host memory or disk offloading techniques are leveraged. Despite advanced asynchronous multi-tier read/write strategies, such offloading strategies result in significant I/O overheads in the critical path of training. To this end, we propose MLP-Offload, a novel multi-level, multi-path offloading engine specifically designed for optimizing LLM training on resource-constrained setups by mitigating I/O bottlenecks. We design and implement MLP-Offload to offload the optimizer states across multiple tiers in a cache-efficient and concurrency-controlled fa

---

## 一句话总结

> 该工作属于 Machine Learning: Training at Scale 2 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Training at Scale 2 领域贡献新的设计范式或评估框架。
