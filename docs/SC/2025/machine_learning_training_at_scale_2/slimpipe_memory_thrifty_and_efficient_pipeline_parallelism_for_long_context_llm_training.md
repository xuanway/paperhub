---
title: "SlimPipe: Memory-Thrifty and Efficient Pipeline Parallelism for Long-Context LLM Training"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Zhouyang Li; Yuliang Liu; Wei Zhang; Tailing Yuan; Bin Chen; Chengru Song"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# SlimPipe: Memory-Thrifty and Efficient Pipeline Parallelism for Long-Context LLM Training

**中文标题：** 面向长上下文大语言模型训练的节省内存高效流水线并行

**所属 Session：** [Machine Learning: Training at Scale 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Zhouyang Li; Yuliang Liu; Wei Zhang; Tailing Yuan; Bin Chen; Chengru Song

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap626&sess=sess167)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Pipeline parallelism serves as a crucial technique for training large language models, owing to its capability to alleviate memory pressure from model states with low communication overhead. However, in long-context scenarios, existing pipeline parallelism methods fail to address the substantial activation memory pressure, due to the peak memory consumption resulting from the accumulation of activations across multiple microbatches. Moreover, these approaches inevitably introduce considerable pipeline bubbles, further hindering efficiency. To tackle these challenges, we propose SlimPipe, a novel approach to fine-grained pipeline parallelism that employs uniform sequence slicing coupled with one-forward-one-backward scheduling. It reduces the accumulated activations from several microbatches to just one, which is split into several slices. Although the slices are evenly partitioned, the computation cost is not equal across slices due to causal self-attention. We develop a sophisticated

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
