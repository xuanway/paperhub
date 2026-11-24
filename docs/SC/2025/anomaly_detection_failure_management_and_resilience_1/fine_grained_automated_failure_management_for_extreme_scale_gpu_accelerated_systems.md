---
title: "Fine-Grained Automated Failure Management for Extreme-Scale GPU-Accelerated Systems"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Yonatan Levitt; Richard Barella; Sam Zeltner; Tom Musta; Lance Cheney; Gustavo E"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# Fine-Grained Automated Failure Management for Extreme-Scale GPU-Accelerated Systems

**中文标题：** 面向超大规模 GPU 加速系统的细粒度自动故障管理

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Yonatan Levitt; Richard Barella; Sam Zeltner; Tom Musta; Lance Cheney; Gustavo Espinosa; Olivier Franza; Balazs Gerofi

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap809&sess=sess289)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

As high performance computing (HPC) systems scale in size, system-wide hardware failure rates increase. Historical data from previous large-scale HPC installations illustrate this trend, with the mean time between failures (MTBF) decreasing steadily over the past decade. Recent studies from artificial intelligence and machine learning (AI/ML) training extrapolate MTBF declining even further for future GPU-accelerated systems. As MTBF decreases, mean time to repair (MTTR) becomes more pronounced, highlighting the need for efficient recovery strategies. This paper presents an automated failure management system that addresses this issue by minimizing MTTR through real-time decision-making based on failure statistics. Our key contributions include a centralized meta-database for event history analysis including correlated events, fine-grained multi-strike repair policies, and an automated recovery framework. Deployed on the Aurora supercomputer, the proposed system has reduced MTTR by up

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
