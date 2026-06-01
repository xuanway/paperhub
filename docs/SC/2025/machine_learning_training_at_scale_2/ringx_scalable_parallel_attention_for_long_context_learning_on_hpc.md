---
title: "RingX: Scalable Parallel Attention for Long-Context Learning on HPC"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Junqi Yin; Mijanur Palash; Mallikarjun Shankar; Feiyi Wang"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# RingX: Scalable Parallel Attention for Long-Context Learning on HPC

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Junqi Yin; Mijanur Palash; Mallikarjun Shankar; Feiyi Wang

**会议**：SC 2025 · St. Louis, MO

## 摘要

The attention mechanism has become foundational to remarkable AI breakthroughs since the introduction of the Transformer, driving the demand for increasingly longer context to power AI frontier models. However, its quadratic computational and memory complexities pose a major challenge. Here, we propose RingX, a set of scalable parallel attention methods, optimized for HPC. Through better workload partitioning, communication scheme, and load balancing, we achieve up to 3.4X speedup compared to the current state-of-the-art on the Frontier supercomputer. RingX is specifically optimized for both bi-directional and casual attention, and its performance and validity are demonstrated by training of both a Vision Transformer (ViT) and a Generative Pre-trained Transformer (GPT), respectively. An end-to-end speedup of about 1.5X is obtained in both applications. To our knowledge, the achieved 38% model FLOPs utilization (MFU) for training Llama3-8B on a 1M-token sequence length using 4,096 GPUs 

---

## 一句话总结

> 该工作属于 Machine Learning: Training at Scale 2 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Training at Scale 2 领域贡献新的设计范式或评估框架。
