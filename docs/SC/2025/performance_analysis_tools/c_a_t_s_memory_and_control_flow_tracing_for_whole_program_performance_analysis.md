---
title: "C.A.T.S.: Memory and Control Flow Tracing for Whole-Program Performance Analysis"
description: "SC 2025 · Performance: Analysis Tools · Philipp Schaad; Tal Ben-Nun; Torsten Hoefler"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# C.A.T.S.: Memory and Control Flow Tracing for Whole-Program Performance Analysis

**中文标题：** 面向全程序性能分析的内存与控制流追踪

**所属 Session：** [Performance: Analysis Tools](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Philipp Schaad; Tal Ben-Nun; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap270&sess=sess342)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Performance engineering often involves localized, bottleneck-based optimization, supported by a plethora of tools. When no apparent bottlenecks exist, engineers resort to coarser whole-program optimization, consisting of data layout, sparsity, allocation strategy, and algorithmic modifications, to name a few. In this work, we aim to codify whole-program optimization by providing three global views based on a single tracing format. The format, called C.A.T.S., captures information necessary for static and runtime analysis of large applications. Instead of call stacks and function annotations, C.A.T.S. uses control flow stacks and memory events to identify common performance anti-patterns and potential optimizations. We develop interactive timeline, dataflow, and access visualizations, and implement compiler analysis passes to extract C.A.T.S. traces statically and in seconds on consumer hardware. The visualizations and analyses are demonstrated on case studies including sparse computati

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
