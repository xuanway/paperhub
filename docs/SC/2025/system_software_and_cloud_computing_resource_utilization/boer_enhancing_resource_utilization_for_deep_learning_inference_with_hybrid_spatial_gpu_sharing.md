---
title: "BOER: Enhancing Resource Utilization for Deep Learning Inference with Hybrid Spatial GPU Sharing"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Bowen Zhang; Yuhang Wang; Zhuozhao Li"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# BOER: Enhancing Resource Utilization for Deep Learning Inference with Hybrid Spatial GPU Sharing

**中文标题：** 通过混合空间 GPU 共享提高深度学习推理的资源利用率

**所属 Session：** [System Software and Cloud Computing: Resource Utilization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Bowen Zhang; Yuhang Wang; Zhuozhao Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap641&sess=sess370)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Many inference systems leverage spatial multiplexing technologies, such as Multi-Process Service (MPS) and Multi-Instance GPU (MIG), to serve deep learning models concurrently on a single GPU. However, existing solutions suffer from interference under MPS and rigid partition sizes in MIG. To address these limitations, we propose BOER, a system that combines MPS atop MIG partitions to reduce interference and enhance GPU utilization. BOER identifies key challenges in integrating MPS with MIG and introduces a hierarchical scheduling framework that jointly determines model colocation, workload distribution, MIG partitioning, and MPS configurations, while minimizing resource fragmentation and MIG reconfiguration overhead. Since MPS interference is difficult to predict accurately, BOER avoids performance models and instead employs a Bayesian optimization with tailored acceleration strategies to efficiently explore the MPS configuration space. Evaluation on a real testbed demonstrates that BO

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
