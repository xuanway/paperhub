---
title: "Breaking the System Noise Barrier at Exascale"
description: "SC 2025 · State of the Practice · Edgar A. Leon; Joseph Glenski; Mark Stock; Kim McMahon; William Loewe; Clark Sny"
tags:
  - "SC2025"
  - "State of the Practice"
---

# Breaking the System Noise Barrier at Exascale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：State of the Practice。</p>
<p class="paper-seo-summary__tags">SC 2025 · State of the Practice</p>
</div>

**作者**：Edgar A. Leon; Joseph Glenski; Mark Stock; Kim McMahon; William Loewe; Clark Snyder; Larry Kaplan; Srinath Vadlamani; Timothy I. Mattox; Trent D'Hooge; Brian Behlendorf; Nathan Hanford; Ramesh Pankajakshan; Matthew L. Leininger

**会议**：SC 2025 · St. Louis, MO

## 摘要

To meet the increasing demands of parallel scientific applications, supercomputers continue to grow in both scale and complexity. The fastest supercomputer in the world, El Capitan, features over a million CPU cores and tens of thousands of GPUs. Applications running on such large-scale systems are particularly susceptible to system noise or interference caused by the operating system (OS) and other services running on the same compute nodes as the application. In this paper, we address this critical performance and scalability challenge on El Capitan, enabling scientific applications to better leverage the benefits of the world's fastest supercomputer. Our strategy comprises two key components: (1) isolating system services from applications and (2) applying OS-level tuning to maintain minimal application interference. As part of this effort, we provide a distribution-independent tuning guide applicable to any Linux system, and we propose and evaluate general strategies for isolating 

---

## 一句话总结

> 该工作属于 State of the Practice 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 State of the Practice 领域贡献新的设计范式或评估框架。
