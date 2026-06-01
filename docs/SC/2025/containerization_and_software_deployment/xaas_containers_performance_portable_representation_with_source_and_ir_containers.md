---
title: "XaaS Containers: Performance-Portable Representation with Source and IR Containers"
description: "SC 2025 · Containerization and Software Deployment · Marcin Copik; Eiman Alnuaimi; Alok Kamatar; Valerie Hayot-Sasson; Alberto Madonn"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# XaaS Containers: Performance-Portable Representation with Source and IR Containers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Marcin Copik; Eiman Alnuaimi; Alok Kamatar; Valerie Hayot-Sasson; Alberto Madonna; Todd Gamblin; Kyle Chard; Ian Foster; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

HPC systems and cloud data centers are converging, and containers are becoming the default software deployment method. While containers simplify software management, they face significant performance challenges: they must sacrifice hardware-specific optimizations to achieve portability. Although HPC containers can use runtime hooks to access optimized libraries and devices, they are limited by ABI compatibility and cannot reverse the effects of early-stage compilation decisions. XaaS containers proposed a vision of performance-portable containers, and we present a practical realization with Source and Intermediate Representation (IR) containers. We delay performance-critical decisions until the target system specification is known. We analyze specialization mechanisms in HPC software and propose a new LLM-assisted method for their automatic discovery. By examining the compilation pipeline, we develop a methodology to build containers optimized for target architectures at deployment tim

---

## 一句话总结

> 该工作属于 Containerization and Software Deployment 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Containerization and Software Deployment 领域贡献新的设计范式或评估框架。
