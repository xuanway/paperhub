---
title: "Compile-Time QoS Scheme for Deep Learning Inferences"
description: "SC 2025 · Machine Learning: Inference and Serving · Sungin Hong; Hyunjun Kim; Hwansoo Han"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# Compile-Time QoS Scheme for Deep Learning Inferences

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Sungin Hong; Hyunjun Kim; Hwansoo Han

**会议**：SC 2025 · St. Louis, MO

## 摘要

With the proliferation of deep learning technologies across various service domains, the sharing of accelerators such as GPUs, TPUs, and NPUs for inference processing has become increasingly common. These accelerators must efficiently handle multiple deep learning services operating concurrently. However, inference requests, characterized by sequences of short-duration kernels, create significant challenges for online schedulers attempting to maintain quality of service (QoS) guarantees. This paper presents QoSlicer, a novel compile-time QoS management framework that employs kernel slicing to relieve the burden on schedulers. By generating multiple pre-determined slicing plans, QoSlicer enables more efficient, lightweight QoS scheduling while ensuring target latency requirements are met. Our approach incorporates a heuristic search algorithm to identify optimal slicing plans and implements robust performance estimation models to validate these plans. Our experimental evaluation across 

---

## 一句话总结

> 该工作属于 Machine Learning: Inference and Serving 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Inference and Serving 领域贡献新的设计范式或评估框架。
