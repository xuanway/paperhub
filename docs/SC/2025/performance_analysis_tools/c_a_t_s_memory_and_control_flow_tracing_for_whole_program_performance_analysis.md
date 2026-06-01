---
title: "C.A.T.S.: Memory and Control Flow Tracing for Whole-Program Performance Analysis"
description: "SC 2025 · Performance: Analysis Tools · Philipp Schaad; Tal Ben-Nun; Torsten Hoefler"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# C.A.T.S.: Memory and Control Flow Tracing for Whole-Program Performance Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Philipp Schaad; Tal Ben-Nun; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

Performance engineering often involves localized, bottleneck-based optimization, supported by a plethora of tools. When no apparent bottlenecks exist, engineers resort to coarser whole-program optimization, consisting of data layout, sparsity, allocation strategy, and algorithmic modifications, to name a few. In this work, we aim to codify whole-program optimization by providing three global views based on a single tracing format. The format, called C.A.T.S., captures information necessary for static and runtime analysis of large applications. Instead of call stacks and function annotations, C.A.T.S. uses control flow stacks and memory events to identify common performance anti-patterns and potential optimizations. We develop interactive timeline, dataflow, and access visualizations, and implement compiler analysis passes to extract C.A.T.S. traces statically and in seconds on consumer hardware. The visualizations and analyses are demonstrated on case studies including sparse computati

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
