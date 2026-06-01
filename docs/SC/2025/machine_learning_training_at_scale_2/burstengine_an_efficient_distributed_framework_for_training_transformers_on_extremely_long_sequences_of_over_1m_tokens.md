---
title: "BurstEngine: An Efficient Distributed Framework for Training Transformers on Extremely Long Sequences of Over 1M Tokens"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Ao Sun; Weilin Zhao; Xu Han; Cheng Yang; Zhiyuan Liu; Chuan Shi; Maosong Sun"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# BurstEngine: An Efficient Distributed Framework for Training Transformers on Extremely Long Sequences of Over 1M Tokens

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Ao Sun; Weilin Zhao; Xu Han; Cheng Yang; Zhiyuan Liu; Chuan Shi; Maosong Sun

**会议**：SC 2025 · St. Louis, MO

## 摘要

Existing methods for training large language models (LLMs) on long-sequence data, such as tensor parallelism and context parallelism, exhibit low model FLOPs utilization (MFU) as sequence lengths and number of GPUs increase, especially when sequence lengths exceed 1M tokens. To address these challenges, we propose BurstEngine, an efficient framework designed to train LLMs on long-sequence data. BurstEngine introduces BurstAttention, an optimized distributed attention with lower communication cost than RingAttention. BurstAttention leverages topology-aware ring communication to fully utilize network bandwidth and incorporates fine-grained communication-computation overlap to minimize communication cost. Furthermore, BurstEngine introduces sequence-level selective checkpointing and fuses the language modeling head with the loss function to reduce memory cost. Additionally, BurstEngine introduces workload balance optimization for various types of attention masking. By integrating these op

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
