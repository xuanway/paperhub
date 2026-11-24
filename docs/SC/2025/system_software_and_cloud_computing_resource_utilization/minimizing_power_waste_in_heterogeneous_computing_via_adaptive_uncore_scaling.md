---
title: "Minimizing Power Waste in Heterogeneous Computing via Adaptive Uncore Scaling"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Zhong Zheng; Seyfal Sultanov; Michael Papka; Zhiling Lan"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# Minimizing Power Waste in Heterogeneous Computing via Adaptive Uncore Scaling

**中文标题：** 通过自适应非核心频率调整减少异构计算的功率浪费

**所属 Session：** [System Software and Cloud Computing: Resource Utilization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Zhong Zheng; Seyfal Sultanov; Michael Papka; Zhiling Lan

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap772&sess=sess370)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

High performance computing (HPC) systems are essential for scientific discovery and engineering innovation. However, their growing power demands pose significant challenges, particularly as systems scale to the exascale level. Prior uncore frequency tuning studies primarily focused on conventional HPC workloads on homogeneous systems. As HPC advances toward heterogeneous computing, integrating diverse GPU workloads on heterogeneous systems, it is crucial to revisit and enhance uncore scaling. Our investigation reveals that uncore frequency decreases only when CPU power approaches its TDP (thermal design power)—an uncommon scenario in GPU-dominant applications—resulting in power waste. To address this, we present MAGUS, a user-transparent uncore scaling runtime for heterogeneous computing. Effective uncore tuning is complex, requiring dynamic detection of application execution phases that affect uncore utilization. Moreover, an efficient runtime should introduce minimal overhead. MAGUS

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
