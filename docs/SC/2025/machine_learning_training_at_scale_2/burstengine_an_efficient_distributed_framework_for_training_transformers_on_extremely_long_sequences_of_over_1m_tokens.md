---
title: "BurstEngine: An Efficient Distributed Framework for Training Transformers on Extremely Long Sequences of Over 1M Tokens"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Ao Sun; Weilin Zhao; Xu Han; Cheng Yang; Zhiyuan Liu; Chuan Shi; Maosong Sun"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# BurstEngine: An Efficient Distributed Framework for Training Transformers on Extremely Long Sequences of Over 1M Tokens

**中文标题：** 面向超过百万 token 超长序列 Transformer 训练的高效分布式框架

**所属 Session：** [Machine Learning: Training at Scale 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Ao Sun; Weilin Zhao; Xu Han; Cheng Yang; Zhiyuan Liu; Chuan Shi; Maosong Sun

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap290&sess=sess167)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Existing methods for training large language models (LLMs) on long-sequence data, such as tensor parallelism and context parallelism, exhibit low model FLOPs utilization (MFU) as sequence lengths and number of GPUs increase, especially when sequence lengths exceed 1M tokens. To address these challenges, we propose BurstEngine, an efficient framework designed to train LLMs on long-sequence data. BurstEngine introduces BurstAttention, an optimized distributed attention with lower communication cost than RingAttention. BurstAttention leverages topology-aware ring communication to fully utilize network bandwidth and incorporates fine-grained communication-computation overlap to minimize communication cost. Furthermore, BurstEngine introduces sequence-level selective checkpointing and fuses the language modeling head with the loss function to reduce memory cost. Additionally, BurstEngine introduces workload balance optimization for various types of attention masking. By integrating these op

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
