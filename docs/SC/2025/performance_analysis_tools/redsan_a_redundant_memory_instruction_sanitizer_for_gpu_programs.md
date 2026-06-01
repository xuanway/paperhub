---
title: "RedSan: A Redundant Memory Instruction Sanitizer for GPU Programs"
description: "SC 2025 · Performance: Analysis Tools · Yanbo Zhao; Yueming Hao; Zecheng Li; Shuyin Jiao; Xu Liu; Jiajia Li"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# RedSan: A Redundant Memory Instruction Sanitizer for GPU Programs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Yanbo Zhao; Yueming Hao; Zecheng Li; Shuyin Jiao; Xu Liu; Jiajia Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

CUDA is the de facto programming model for GPUs, widely used in the domains of HPC and AI. To obtain bare-metal performance, vendors and academics develop various profiling tools to guide optimization. However, most existing tools focus on hotspot analysis with limited capabilities in identifying actionable opportunities. To complement existing tools, we present RedSan, a novel profiling tool that leverages binary instrumentation to identify redundant instructions in fully optimized CUDA programs. Guided by RedSan, we are able to optimize programs such as PolybenchGPU, Rodinia, PASTA, DARKNET, and LULESH, yielding up to a 6.27× speedup and 3.00× reduction in memory instructions.

---

## 一句话总结

> 该工作属于 Performance: Analysis Tools 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Analysis Tools 领域贡献新的设计范式或评估框架。
