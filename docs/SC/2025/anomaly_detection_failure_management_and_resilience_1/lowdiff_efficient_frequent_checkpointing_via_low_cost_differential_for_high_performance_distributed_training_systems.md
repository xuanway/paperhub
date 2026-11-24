---
title: "LowDiff: Efficient Frequent Checkpointing via Low-Cost Differential for High-Performance Distributed Training Systems"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Chenxuan Yao; Feifan Liu; Yuchong Hu; Zhengyu Liu; Xinjue Zheng; Wenxiang Zhou"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# LowDiff: Efficient Frequent Checkpointing via Low-Cost Differential for High-Performance Distributed Training Systems

**中文标题：** 利用低成本差分为高性能分布式训练系统提供高效高频检查点

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Chenxuan Yao; Feifan Liu; Yuchong Hu; Zhengyu Liu; Xinjue Zheng; Wenxiang Zhou

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap886&sess=sess289)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Distributed training of large deep-learning models often leads to failures, so checkpointing is commonly employed for recovery. State-of-the-art studies focus on frequent checkpointing for fast recovery from failures. However, it generates numerous checkpoints, incurring substantial costs and thus degrading training performance. Recently, differential checkpointing has been proposed to reduce costs, but it is limited to recommendation systems, so its application to general distributed training systems remains unexplored. This paper proposes LowDiff, an efficient frequent-checkpointing framework that reuses compressed gradients (commonly used in distributed training), serving as differential checkpoints to reduce cost. Furthermore, LowDiff incorporates a batched gradient write optimization to efficiently persist these differentials to storage. It also dynamically tunes both the checkpoint frequency and the batching size to maximize the performance. Experiments on various workloads show

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
