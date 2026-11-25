---
title: "WaterWise: Co-optimizing Carbon- and Water-Footprint Toward Environmentally Sustainable Cloud Computing"
description: "PPoPP 2025 Session 7（Scheduling and Resource Management）：揭示碳/水目标冲突，并给出二者协同的作业调度器"
tags:
  - "PPoPP2025"
  - "Session-7"
  - "Scheduling and Resource Management"
  - "Sustainable Computing"
  - "Job Scheduling"
  - "Carbon Footprint"
authors:
  - "Yankai Jiang"
  - "Rohan Basu Roy"
  - "Raghavendra Kanakagiri"
  - "Devesh Tiwari"
session: "Session 7: Scheduling and Resource Management"
session_number: 7
session_chair: "Jie Ren"
date: "2025-03-04"
time: "12:00–12:20"
room: "Acacia D"
doi: "10.1145/3710848.3710891"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# WaterWise: Co-optimizing Carbon- and Water-Footprint Toward Environmentally Sustainable Cloud Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向地理分布式数据中心的作业调度器 WaterWise，在碳足迹与水足迹两个可持续性目标之间做协同优化。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 7: Scheduling and Resource Management</p>
</div>

**作者**：Yankai Jiang (Northeastern University); Rohan Basu Roy (University of Utah); Raghavendra Kanakagiri (IIT Tirupati); Devesh Tiwari (Northeastern University)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 12:00–12:20 · Session 7: Scheduling and Resource Management（主席：Jie Ren）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710891) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向地理分布式数据中心的作业调度器 WaterWise，在碳足迹与水足迹两个可持续性目标之间做协同优化。

## 研究问题

大规模计算系统的碳足迹与水足迹构成严重的环境可持续性风险；而研究发现碳与水的可持续性目标彼此冲突，只优化其中一个会损害另一个。

## 方法简述

- 面向并行负载设计作业调度器，把碳足迹与水足迹同时纳入调度决策。
- 在地理分布式数据中心之间协调作业放置，以改善整体可持续性。

## 主要结果

- 实证揭示了碳与水的可持续性目标之间存在权衡冲突。
- 提出可同时考虑两类足迹的协同调度方案（论文摘要未给出具体量化指标）。

<details>
<summary>原文摘要（英文）</summary>

The carbon and water footprint of large-scale computing systems poses serious environmental sustainability risks. In this study, we discover that, unfortunately, carbon and water sustainability are at odds with each other – and, optimizing one alone hurts the other. Toward that goal, we introduce, WaterWise, a novel job scheduler for parallel workloads that intelligently co-optimizes carbon and water footprint to improve the sustainability of geographically distributed data centers.

</details>

---

> 所属 Session：[Session 7: Scheduling and Resource Management](index.md) · 返回 [PPoPP 2025 总览](../index.md)
