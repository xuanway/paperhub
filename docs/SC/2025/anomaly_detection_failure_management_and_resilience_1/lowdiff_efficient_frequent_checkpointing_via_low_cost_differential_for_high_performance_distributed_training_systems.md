---
title: "LowDiff: Efficient Frequent Checkpointing via Low-Cost Differential for High-Performance Distributed Training Systems"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Chenxuan Yao; Feifan Liu; Yuchong Hu; Zhengyu Liu; Xinjue Zheng; Wenxiang Zhou"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# LowDiff: Efficient Frequent Checkpointing via Low-Cost Differential for High-Performance Distributed Training Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Chenxuan Yao; Feifan Liu; Yuchong Hu; Zhengyu Liu; Xinjue Zheng; Wenxiang Zhou

**会议**：SC 2025 · St. Louis, MO

## 摘要

Distributed training of large deep-learning models often leads to failures, so checkpointing is commonly employed for recovery. State-of-the-art studies focus on frequent checkpointing for fast recovery from failures. However, it generates numerous checkpoints, incurring substantial costs and thus degrading training performance. Recently, differential checkpointing has been proposed to reduce costs, but it is limited to recommendation systems, so its application to general distributed training systems remains unexplored. This paper proposes LowDiff, an efficient frequent-checkpointing framework that reuses compressed gradients (commonly used in distributed training), serving as differential checkpoints to reduce cost. Furthermore, LowDiff incorporates a batched gradient write optimization to efficiently persist these differentials to storage. It also dynamically tunes both the checkpoint frequency and the batching size to maximize the performance. Experiments on various workloads show 

---

## 一句话总结

> 该工作属于 Anomaly Detection, Failure Management, and Resilience 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Anomaly Detection, Failure Management, and Resilience 1 领域贡献新的设计范式或评估框架。
