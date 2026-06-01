---
title: "DiffMoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching"
description: "SC 2025 · Collective Operations and Communication · Kexin Li; Wenkan Huang; Qinggang Wang; Long Zheng; Xiaofei Liao; Hai Jin; Jingli"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# DiffMoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Kexin Li; Wenkan Huang; Qinggang Wang; Long Zheng; Xiaofei Liao; Hai Jin; Jingling Xue

**会议**：SC 2025 · St. Louis, MO

## 摘要

The Mixture-of-Experts (MoE) model reduces the computation of large LLMs by sparsely activating experts, but its massive parameter storage creates severe GPU memory bottlenecks. Existing solutions offload experts to host memory and prefetch them with sophisticated policies, yet they target single-batch inference and suffer from communication bottlenecks at larger batch sizes. We identify two forms of locality in expert activation: a small set of experts are frequently invoked across inference (global locality), while others recur within short decoding bursts (temporal locality). To exploit this, we propose DiffMoE, which introduces a differential cache hierarchy in GPU memory. Globally hot experts reside in per-layer high-priority caches, locally hot ones are dynamically managed in per-layer medium-priority caches under a priority-driven replacement policy, and cold experts are cached temporarily and evicted on demand. Moreover, a lightweight predictor overlaps expert migration with co

---

## 一句话总结

> 该工作属于 Collective Operations and Communication 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Collective Operations and Communication 领域贡献新的设计范式或评估框架。
