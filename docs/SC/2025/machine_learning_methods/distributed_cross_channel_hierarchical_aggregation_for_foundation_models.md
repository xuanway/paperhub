---
title: "Distributed Cross-Channel Hierarchical Aggregation for Foundation Models"
description: "SC 2025 · Machine Learning: Methods · Aristeidis Tsaris; Isaac Lyngaas; John Lagergren; Mohamed Wahib; Larry York; Pra"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Distributed Cross-Channel Hierarchical Aggregation for Foundation Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Aristeidis Tsaris; Isaac Lyngaas; John Lagergren; Mohamed Wahib; Larry York; Prasanna Balaprakash; Dan Lu; Feiyi Wang; Xiao Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Vision-based scientific foundation models hold significant promise for advancing scientific discovery and innovation. This potential stems from their ability to aggregate images from diverse sources—such as varying physical groundings or data acquisition systems—and to learn spatio-temporal correlations using transformer architectures. However, tokenizing and aggregating images can be compute-intensive, a challenge not fully addressed by current distributed methods. In this work, we introduce the Distributed Cross-Channel Hierarchical Aggregation (D-CHAG) approach designed for datasets with a large number of channels across image modalities. Our method is compatible with any model-parallel strategy and any type of vision transformer architecture, significantly improving computational efficiency. We evaluated D-CHAG on hyperspectral imaging and weather forecasting tasks. When integrated with tensor parallelism and model sharding, our approach achieved up to a 75% reduction in memory usa

---

## 一句话总结

> 该工作属于 Machine Learning: Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Methods 领域贡献新的设计范式或评估框架。
