---
title: "DiffMoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching"
description: "SC 2025 · Collective Operations and Communication · Kexin Li; Wenkan Huang; Qinggang Wang; Long Zheng; Xiaofei Liao; Hai Jin; Jingli"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# DiffMoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching

**中文标题：** 利用优先级驱动的差异化专家缓存实现高效批量 MoE 推理

**所属 Session：** [Collective Operations and Communication](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Kexin Li; Wenkan Huang; Qinggang Wang; Long Zheng; Xiaofei Liao; Hai Jin; Jingling Xue

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap990&sess=sess296)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The Mixture-of-Experts (MoE) model reduces the computation of large LLMs by sparsely activating experts, but its massive parameter storage creates severe GPU memory bottlenecks. Existing solutions offload experts to host memory and prefetch them with sophisticated policies, yet they target single-batch inference and suffer from communication bottlenecks at larger batch sizes. We identify two forms of locality in expert activation: a small set of experts are frequently invoked across inference (global locality), while others recur within short decoding bursts (temporal locality). To exploit this, we propose DiffMoE, which introduces a differential cache hierarchy in GPU memory. Globally hot experts reside in per-layer high-priority caches, locally hot ones are dynamically managed in per-layer medium-priority caches under a priority-driven replacement policy, and cold experts are cached temporarily and evicted on demand. Moreover, a lightweight predictor overlaps expert migration with co

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
