---
title: "UltraAttn: Efficiently Parallelizing Attention Through Hierarchical Context-Tiling"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Haoyu Yang; Zan Zong; Yuyang Jin; Kinman Lei; Jiaao He; Qigang Yang; Jidong Zhai"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# UltraAttn: Efficiently Parallelizing Attention Through Hierarchical Context-Tiling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Haoyu Yang; Zan Zong; Yuyang Jin; Kinman Lei; Jiaao He; Qigang Yang; Jidong Zhai

**会议**：SC 2025 · St. Louis, MO

## 摘要

Long-context comprehension is a crucial capability for LLM. Context parallelism and irregular block sparse attention are two key technologies to accelerate long contextual training and inference. Existing context parallelism techniques for attention suffer from poor scalability, owing to their common characteristics: the striped-like partition pattern. The striped-like partition pattern causes high communication traffic and inflexible kernel granularity, which in turn results in low single-kernel device utilization. To address these problems, we propose UltraAttn, a novel context parallelism solution for irregular attention. UltraAttn hierarchically tiles the context to reduce communication cost. UltraAttn also performs context-tiling at the kernel level to adjust the granularity of kernels to trade off between kernel overlap and single-kernel device utilization. UltraAttn executes distributed attention with an ILP-based runtime to optimize latency. We evaluate UltraAttn on 64 GPUs. Ul

---

## 一句话总结

> 该工作属于 Scheduling, Tiling, and Parallelism 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Scheduling, Tiling, and Parallelism 领域贡献新的设计范式或评估框架。
