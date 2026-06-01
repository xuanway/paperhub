---
title: "Make Updates Faster: A Fast Multi-Stripe Updates Framework in Erasure-Coded Storage Clusters"
description: "SC 2025 · System Software and Cloud · Hai Zhou; Dan Feng"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# Make Updates Faster: A Fast Multi-Stripe Updates Framework in Erasure-Coded Storage Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Hai Zhou; Dan Feng

**会议**：SC 2025 · St. Louis, MO

## 摘要

Erasure coding is widely adopted to maintain data reliability, yet it introduces a significant update penalty. We analyze real-world traces and observe several challenges that are not addressed by existing studies, which thereby restrict the performance gains. We propose FastUpdate, an efficient multi-stripe updates framework that assists existing update schemes for fast updates. FastUpdate comprises three key designs: (1) it perceives the update locality and carefully merges multiple update requests accessing the same stripe to reduce the incurred network traffic; (2) it abstracts the existing update schemes into collector selection and tree construction, greedily generates the update solution for each stripe to balance the transmission load across nodes; (3) it dynamically schedules appropriate stripes to update in heterogeneous and dynamic networks to fully saturate the bandwidth resources. Comprehensive evaluations verify the effectiveness of FastUpdate on Alibaba ECS. It can incre

---

## 一句话总结

> 该工作属于 System Software and Cloud 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 System Software and Cloud 领域贡献新的设计范式或评估框架。
