---
title: "TT-LoRA MoE: Using Parameter-Efficient Fine Tuning and Sparse Mixture-of-Experts"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Pradip Kunwar; Minh N. Vu; Maanak Gupta; Mahmoud Abdelsalam; Manish Bhattarai"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# TT-LoRA MoE: Using Parameter-Efficient Fine Tuning and Sparse Mixture-of-Experts

**中文标题：** 使用参数高效微调与稀疏混合专家

**所属 Session：** [Machine Learning: Training at Scale 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Pradip Kunwar; Minh N. Vu; Maanak Gupta; Mahmoud Abdelsalam; Manish Bhattarai

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap864&sess=sess302)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

We propose Tensor-Trained Low-Rank Adaptation Mixture-of-Experts (TT-LoRA MoE), a novel computational framework integrating parameter-efficient fine-tuning (PEFT) with sparse MoE routing to address scalability challenges in large model deployments. Unlike traditional MoE approaches, which face substantial computational overhead as expert counts grow, TT-LoRA MoE decomposes training into two distinct, optimized stages. First, we independently train lightweight, tensorized low-rank adapters (TT-LoRA experts), each specialized for specific tasks. Subsequently, these expert adapters remain frozen, eliminating inter-task interference and catastrophic forgetting in multi-task settings. A sparse MoE router, trained separately, dynamically leverages base model representations to select exactly one specialized adapter per input at inference time, automating expert selection without explicit task specification. Comprehensive experiments confirm our architecture retains the memory efficiency of l

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
