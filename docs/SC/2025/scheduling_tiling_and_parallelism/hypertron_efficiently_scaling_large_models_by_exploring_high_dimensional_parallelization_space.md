---
title: "Hypertron: Efficiently Scaling Large Models by Exploring High-Dimensional Parallelization Space"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Shigang Li; Jingkun Dong; Jihao Chen; Zhi Ma; Zhongzhe Hu"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# Hypertron: Efficiently Scaling Large Models by Exploring High-Dimensional Parallelization Space

**中文标题：** 通过探索高维并行化空间高效扩展大模型

**所属 Session：** [Scheduling, Tiling, and Parallelism](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Shigang Li; Jingkun Dong; Jihao Chen; Zhi Ma; Zhongzhe Hu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap175&sess=sess286)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Large models are evolving towards massive scale, diverse model architectures (dense and sparse), and long-context processing, which makes it very challenging to efficiently scale large models on parallel machines. The current widely-used parallelization strategies are often sub-optimal due to their limited parallelization strategy space. Therefore, we propose Hypertron, a scalable parallel large-model training framework which incorporates an unprecedented high-dimensional (up to 7D) parallelization space, a holistic scheme for efficient dimension fusion, and a comprehensive performance model to guide the high-dimensional exploration. By exploiting the high-dimensional space to discover the optimal strategy not supported by existing frameworks, Hypertron significantly reduces memory and communication cost while improving parallel scalability. Extensive evaluations demonstrate that Hypertron achieves up to 56.7% Model FLOPs Utilization (MFU) on 2,048 new-generation Ascend NPU accelerator

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
