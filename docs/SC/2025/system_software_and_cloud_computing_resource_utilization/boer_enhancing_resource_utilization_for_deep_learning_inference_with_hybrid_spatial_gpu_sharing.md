---
title: "BOER: Enhancing Resource Utilization for Deep Learning Inference with Hybrid Spatial GPU Sharing"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Bowen Zhang; Yuhang Wang; Zhuozhao Li"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# BOER: Enhancing Resource Utilization for Deep Learning Inference with Hybrid Spatial GPU Sharing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Bowen Zhang; Yuhang Wang; Zhuozhao Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

Many inference systems leverage spatial multiplexing technologies, such as Multi-Process Service (MPS) and Multi-Instance GPU (MIG), to serve deep learning models concurrently on a single GPU. However, existing solutions suffer from interference under MPS and rigid partition sizes in MIG. To address these limitations, we propose BOER, a system that combines MPS atop MIG partitions to reduce interference and enhance GPU utilization. BOER identifies key challenges in integrating MPS with MIG and introduces a hierarchical scheduling framework that jointly determines model colocation, workload distribution, MIG partitioning, and MPS configurations, while minimizing resource fragmentation and MIG reconfiguration overhead. Since MPS interference is difficult to predict accurately, BOER avoids performance models and instead employs a Bayesian optimization with tailored acceleration strategies to efficiently explore the MPS configuration space. Evaluation on a real testbed demonstrates that BO

---

## 一句话总结

> 该工作属于 System Software and Cloud Computing: Resource Utilization 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 System Software and Cloud Computing: Resource Utilization 领域贡献新的设计范式或评估框架。
