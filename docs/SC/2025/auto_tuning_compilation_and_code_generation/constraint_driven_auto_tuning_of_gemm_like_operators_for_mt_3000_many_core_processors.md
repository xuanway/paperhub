---
title: "Constraint-Driven Auto-Tuning of GEMM-Like Operators for MT-3000 Many-Core Processors"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Xinxin Qi; Jianbin Fang; Peng Zhang; Yonggang Che; Jie Ren"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# Constraint-Driven Auto-Tuning of GEMM-Like Operators for MT-3000 Many-Core Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Xinxin Qi; Jianbin Fang; Peng Zhang; Yonggang Che; Jie Ren

**会议**：SC 2025 · St. Louis, MO

## 摘要

Optimizing deep learning (DL) operators, especially GEMM-like operations, on heterogeneous many-core processors such as MT-3000 is difficult due to large search spaces and hardware-specific constraints. Existing methods, including hand-tuned libraries and auto-tuners, are either costly to develop or deliver limited performance. We propose DynaChain, an operator-level optimization framework for MT-3000. DynaChain separates computation and data movement, enabling independent optimization and maximizing data reuse across schedules. To shrink the search space, it employs constraint dependency chains that dynamically prune invalid scheduling choices. For irregular matrix dimensions, DynaChain uses an integer linear programming (ILP) based decomposition to avoid padding and enhance hardware utilization. At the low level, it generates optimized micro-kernels tailored to MT-3000’s VLIW+SIMD architecture, improving register allocation and pipelining for irregular operations. Experiments on repr

---

## 一句话总结

> 该工作属于 Auto-Tuning, Compilation, and Code Generation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Auto-Tuning, Compilation, and Code Generation 领域贡献新的设计范式或评估框架。
