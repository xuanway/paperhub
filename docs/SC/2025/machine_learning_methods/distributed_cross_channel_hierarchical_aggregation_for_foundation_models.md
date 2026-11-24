---
title: "Distributed Cross-Channel Hierarchical Aggregation for Foundation Models"
description: "SC 2025 · Machine Learning: Methods · Aristeidis Tsaris; Isaac Lyngaas; John Lagergren; Mohamed Wahib; Larry York; Pra"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Distributed Cross-Channel Hierarchical Aggregation for Foundation Models

**中文标题：** 面向基础模型的分布式跨通道分层聚合

**所属 Session：** [Machine Learning: Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Aristeidis Tsaris; Isaac Lyngaas; John Lagergren; Mohamed Wahib; Larry York; Prasanna Balaprakash; Dan Lu; Feiyi Wang; Xiao Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap725&sess=sess183)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Vision-based scientific foundation models hold significant promise for advancing scientific discovery and innovation. This potential stems from their ability to aggregate images from diverse sources—such as varying physical groundings or data acquisition systems—and to learn spatio-temporal correlations using transformer architectures. However, tokenizing and aggregating images can be compute-intensive, a challenge not fully addressed by current distributed methods. In this work, we introduce the Distributed Cross-Channel Hierarchical Aggregation (D-CHAG) approach designed for datasets with a large number of channels across image modalities. Our method is compatible with any model-parallel strategy and any type of vision transformer architecture, significantly improving computational efficiency. We evaluated D-CHAG on hyperspectral imaging and weather forecasting tasks. When integrated with tensor parallelism and model sharding, our approach achieved up to a 75% reduction in memory usa

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
