---
title: "Addressing Reproducibility Challenges in HPC with Continuous Integration"
description: "SC 2025 · State of the Practice · Valérie Hayot-Sasson; Nathaniel Hudson; André Bauer; Maxime Gonthier; Ian Foster"
tags:
  - "SC2025"
  - "State of the Practice"
---

# Addressing Reproducibility Challenges in HPC with Continuous Integration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：State of the Practice。</p>
<p class="paper-seo-summary__tags">SC 2025 · State of the Practice</p>
</div>

**作者**：Valérie Hayot-Sasson; Nathaniel Hudson; André Bauer; Maxime Gonthier; Ian Foster; Kyle Chard

**会议**：SC 2025 · St. Louis, MO

## 摘要

The high performance computing (HPC) community has adopted incentive structures to motivate reproducible research, with major conferences awarding badges to papers that meet reproducibility requirements. Yet, many papers do not meet such requirements. The uniqueness of HPC infrastructure and software, coupled with strict access requirements, may limit opportunities for reproducibility. In the absence of resource access, we believe that regular documented testing, through continuous integration (CI), coupled with complete provenance information, can be used as a substitute. Here, we argue that better HPC-compliant CI solutions will improve reproducibility of applications. We present a survey of reproducibility initiatives and describe the barriers to reproducibility in HPC. To address existing limitations, we present a GitHub Action, CORRECT, that enables secure execution of tests on remote HPC resources. We evaluate CORRECT's usability across three different types of HPC applications, 

---

## 一句话总结

> 该工作属于 State of the Practice 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 State of the Practice 领域贡献新的设计范式或评估框架。
