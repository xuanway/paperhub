---
title: "A Sample-Free Compilation Framework for Efficient Dynamic Tensor Computation"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Yangjie Zhou; Honglin Zhu; Qian Qiu; Weihao Cui; Zihan Liu; Peng Chen; Mohamed W"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# A Sample-Free Compilation Framework for Efficient Dynamic Tensor Computation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Yangjie Zhou; Honglin Zhu; Qian Qiu; Weihao Cui; Zihan Liu; Peng Chen; Mohamed Wahib; Cong Guo; Siyuan Feng; Jintao Meng; Haidong Lan; Jingwen Leng; Yun Lin; Jin Song Dong; Wenxi Zhu; Minwen Deng

**会议**：SC 2025 · St. Louis, MO

## 摘要

Dynamic-shape tensor computation poses challenges for shape-specific compilation due to variable input dimensions. Existing compilers rely on shape samples, incurring high tuning costs and degraded performance on unseen inputs. We present Helix, a dynamic tensor framework with sample-free and architecture-guided compilation for compilation efficiency and shape-general performance. To avoid shape sampling, Helix constructs shape-agnostic compilation by decomposing computations across architectural layers. A bidirectional strategy combines top-down abstraction, aligning tensor computations with architectural hierarchies, and bottom-up kernel construction, building efficient execution strategies from reusable, architecture-aligned micro-kernels. A hybrid analyzer ensures accuracy through profiling at lower architectural levels, and achieves scalability through architecture-informed modeling at higher levels and runtime. This hierarchical design eliminates shape-specific tuning and enables

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
