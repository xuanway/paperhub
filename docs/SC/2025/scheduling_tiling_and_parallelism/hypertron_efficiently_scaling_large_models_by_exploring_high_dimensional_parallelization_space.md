---
title: "Hypertron: Efficiently Scaling Large Models by Exploring High-Dimensional Parallelization Space"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Shigang Li; Jingkun Dong; Jihao Chen; Zhi Ma; Zhongzhe Hu"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# Hypertron: Efficiently Scaling Large Models by Exploring High-Dimensional Parallelization Space

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Shigang Li; Jingkun Dong; Jihao Chen; Zhi Ma; Zhongzhe Hu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Large models are evolving towards massive scale, diverse model architectures (dense and sparse), and long-context processing, which makes it very challenging to efficiently scale large models on parallel machines. The current widely-used parallelization strategies are often sub-optimal due to their limited parallelization strategy space. Therefore, we propose Hypertron, a scalable parallel large-model training framework which incorporates an unprecedented high-dimensional (up to 7D) parallelization space, a holistic scheme for efficient dimension fusion, and a comprehensive performance model to guide the high-dimensional exploration. By exploiting the high-dimensional space to discover the optimal strategy not supported by existing frameworks, Hypertron significantly reduces memory and communication cost while improving parallel scalability. Extensive evaluations demonstrate that Hypertron achieves up to 56.7% Model FLOPs Utilization (MFU) on 2,048 new-generation Ascend NPU accelerator

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
