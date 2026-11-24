---
title: "RingX: Scalable Parallel Attention for Long-Context Learning on HPC"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Junqi Yin; Mijanur Palash; Mallikarjun Shankar; Feiyi Wang"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# RingX: Scalable Parallel Attention for Long-Context Learning on HPC

**中文标题：** 面向 HPC 长上下文学习的可扩展并行注意力

**所属 Session：** [Machine Learning: Training at Scale 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Junqi Yin; Mijanur Palash; Mallikarjun Shankar; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap651&sess=sess167)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The attention mechanism has become foundational to remarkable AI breakthroughs since the introduction of the Transformer, driving the demand for increasingly longer context to power AI frontier models. However, its quadratic computational and memory complexities pose a major challenge. Here, we propose RingX, a set of scalable parallel attention methods, optimized for HPC. Through better workload partitioning, communication scheme, and load balancing, we achieve up to 3.4X speedup compared to the current state-of-the-art on the Frontier supercomputer. RingX is specifically optimized for both bi-directional and casual attention, and its performance and validity are demonstrated by training of both a Vision Transformer (ViT) and a Generative Pre-trained Transformer (GPT), respectively. An end-to-end speedup of about 1.5X is obtained in both applications. To our knowledge, the achieved 38% model FLOPs utilization (MFU) for training Llama3-8B on a 1M-token sequence length using 4,096 GPUs

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
