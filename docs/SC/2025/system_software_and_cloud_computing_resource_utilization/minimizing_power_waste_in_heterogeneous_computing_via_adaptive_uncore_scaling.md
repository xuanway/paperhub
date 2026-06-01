---
title: "Minimizing Power Waste in Heterogeneous Computing via Adaptive Uncore Scaling"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Zhong Zheng; Seyfal Sultanov; Michael Papka; Zhiling Lan"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# Minimizing Power Waste in Heterogeneous Computing via Adaptive Uncore Scaling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Zhong Zheng; Seyfal Sultanov; Michael Papka; Zhiling Lan

**会议**：SC 2025 · St. Louis, MO

## 摘要

High performance computing (HPC) systems are essential for scientific discovery and engineering innovation. However, their growing power demands pose significant challenges, particularly as systems scale to the exascale level. Prior uncore frequency tuning studies primarily focused on conventional HPC workloads on homogeneous systems. As HPC advances toward heterogeneous computing, integrating diverse GPU workloads on heterogeneous systems, it is crucial to revisit and enhance uncore scaling. Our investigation reveals that uncore frequency decreases only when CPU power approaches its TDP (thermal design power)—an uncommon scenario in GPU-dominant applications—resulting in power waste. To address this, we present MAGUS, a user-transparent uncore scaling runtime for heterogeneous computing. Effective uncore tuning is complex, requiring dynamic detection of application execution phases that affect uncore utilization. Moreover, an efficient runtime should introduce minimal overhead. MAGUS 

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
