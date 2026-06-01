---
title: "Balanced and Elastic End-to-End Training of Dynamic LLMs"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Mohamed Wahib; Muhammed Abdullah Soyturk; Didem Unat"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# Balanced and Elastic End-to-End Training of Dynamic LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Mohamed Wahib; Muhammed Abdullah Soyturk; Didem Unat

**会议**：SC 2025 · St. Louis, MO

## 摘要

To reduce computational and memory costs in large language models (LLMs), dynamic workload reduction schemes like Mixture of Experts (MoEs), parameter pruning, layer freezing, sparse attention, early token exit, and Mixture of Depths (MoDs) have emerged. However, these methods introduce severe workload imbalances, limiting their practicality for large-scale distributed training. We propose DynMo, an autonomous dynamic load-balancing solution that ensures optimal compute distribution when using pipeline parallelism in training dynamic models. DynMo adaptively balances workloads, dynamically packs tasks into fewer workers to free idle resources, and supports both multi-GPU single-node and multi-node systems. Compared to static training methods (Megatron-LM, DeepSpeed), DynMo accelerates training by up to 1.23x (MoEs), 3.18x (pruning), 2.23x (layer freezing), 4.02x (sparse attention), 4.52x (early exit), and 1.17x (MoDs).

---

## 一句话总结

> 该工作属于 Machine Learning: Training at Scale 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Training at Scale 1 领域贡献新的设计范式或评估框架。
