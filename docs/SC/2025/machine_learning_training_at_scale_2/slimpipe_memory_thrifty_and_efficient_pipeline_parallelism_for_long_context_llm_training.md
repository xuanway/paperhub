---
title: "SlimPipe: Memory-Thrifty and Efficient Pipeline Parallelism for Long-Context LLM Training"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Zhouyang Li; Yuliang Liu; Wei Zhang; Tailing Yuan; Bin Chen; Chengru Song"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# SlimPipe: Memory-Thrifty and Efficient Pipeline Parallelism for Long-Context LLM Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Zhouyang Li; Yuliang Liu; Wei Zhang; Tailing Yuan; Bin Chen; Chengru Song

**会议**：SC 2025 · St. Louis, MO

## 摘要

Pipeline parallelism serves as a crucial technique for training large language models, owing to its capability to alleviate memory pressure from model states with low communication overhead. However, in long-context scenarios, existing pipeline parallelism methods fail to address the substantial activation memory pressure, due to the peak memory consumption resulting from the accumulation of activations across multiple microbatches. Moreover, these approaches inevitably introduce considerable pipeline bubbles, further hindering efficiency. To tackle these challenges, we propose SlimPipe, a novel approach to fine-grained pipeline parallelism that employs uniform sequence slicing coupled with one-forward-one-backward scheduling. It reduces the accumulated activations from several microbatches to just one, which is split into several slices. Although the slices are evenly partitioned, the computation cost is not equal across slices due to causal self-attention. We develop a sophisticated 

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
