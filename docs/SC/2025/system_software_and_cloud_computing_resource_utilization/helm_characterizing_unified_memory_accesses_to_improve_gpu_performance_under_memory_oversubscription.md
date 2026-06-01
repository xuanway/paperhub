---
title: "HELM: Characterizing Unified Memory Accesses to Improve GPU Performance Under Memory Oversubscription"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Nathan Jones; Tyler Allen; Rong Ge"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# HELM: Characterizing Unified Memory Accesses to Improve GPU Performance Under Memory Oversubscription

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Nathan Jones; Tyler Allen; Rong Ge

**会议**：SC 2025 · St. Louis, MO

## 摘要

Unified memory (UM) technologies simplify memory management across CPU and GPU domains in GPU-accelerated heterogeneous architectures through transparent data migration. However, the default migration mechanism can severely degrade performance when applications oversubscribe GPU memory. Existing approaches to mitigating this performance degradation often fail to generalize, as they target specific application types, require specialized hardware, or integrate opaque classification methods. We introduce HEterogeneous Locality Metrics (HELM), a novel set of semantically meaningful metrics designed to characterize UM access patterns across diverse applications. These metrics are quantified using readily accessible UM driver telemetry data, providing users with tractable and interpretable UM memory characterizations. Such insight is critical for selecting optimal UM migration and placement policies under oversubscription. We demonstrate HELM’s accuracy and interpretability through access pa

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
