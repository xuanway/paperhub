---
title: "TT-LoRA MoE: Using Parameter-Efficient Fine Tuning and Sparse Mixture-of-Experts"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Pradip Kunwar; Minh N. Vu; Maanak Gupta; Mahmoud Abdelsalam; Manish Bhattarai"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# TT-LoRA MoE: Using Parameter-Efficient Fine Tuning and Sparse Mixture-of-Experts

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Pradip Kunwar; Minh N. Vu; Maanak Gupta; Mahmoud Abdelsalam; Manish Bhattarai

**会议**：SC 2025 · St. Louis, MO

## 摘要

We propose Tensor-Trained Low-Rank Adaptation Mixture-of-Experts (TT-LoRA MoE), a novel computational framework integrating parameter-efficient fine-tuning (PEFT) with sparse MoE routing to address scalability challenges in large model deployments. Unlike traditional MoE approaches, which face substantial computational overhead as expert counts grow, TT-LoRA MoE decomposes training into two distinct, optimized stages. First, we independently train lightweight, tensorized low-rank adapters (TT-LoRA experts), each specialized for specific tasks. Subsequently, these expert adapters remain frozen, eliminating inter-task interference and catastrophic forgetting in multi-task settings. A sparse MoE router, trained separately, dynamically leverages base model representations to select exactly one specialized adapter per input at inference time, automating expert selection without explicit task specification. Comprehensive experiments confirm our architecture retains the memory efficiency of l

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
