---
title: "Constraint-Driven Auto-Tuning of GEMM-Like Operators for MT-3000 Many-Core Processors"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Xinxin Qi; Jianbin Fang; Peng Zhang; Yonggang Che; Jie Ren"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# Constraint-Driven Auto-Tuning of GEMM-Like Operators for MT-3000 Many-Core Processors

**中文标题：** 面向 MT-3000 众核处理器类 GEMM 算子的约束驱动自动调优

**所属 Session：** [Auto-Tuning, Compilation, and Code Generation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Xinxin Qi; Jianbin Fang; Peng Zhang; Yonggang Che; Jie Ren

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap950&sess=sess290)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Optimizing deep learning (DL) operators, especially GEMM-like operations, on heterogeneous many-core processors such as MT-3000 is difficult due to large search spaces and hardware-specific constraints. Existing methods, including hand-tuned libraries and auto-tuners, are either costly to develop or deliver limited performance. We propose DynaChain, an operator-level optimization framework for MT-3000. DynaChain separates computation and data movement, enabling independent optimization and maximizing data reuse across schedules. To shrink the search space, it employs constraint dependency chains that dynamically prune invalid scheduling choices. For irregular matrix dimensions, DynaChain uses an integer linear programming (ILP) based decomposition to avoid padding and enhance hardware utilization. At the low level, it generates optimized micro-kernels tailored to MT-3000’s VLIW+SIMD architecture, improving register allocation and pipelining for irregular operations. Experiments on repr

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
