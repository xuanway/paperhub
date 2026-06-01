---
title: "RAPTOR: Practical Numerical Profiling of Scientific Applications"
description: "SC 2025 · Precision and Real Number Representations · Faveo Hoerold; Ivan Radanov Ivanov; Akash Dhruv; William S. Moses; Anshu Dubey; "
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# RAPTOR: Practical Numerical Profiling of Scientific Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Faveo Hoerold; Ivan Radanov Ivanov; Akash Dhruv; William S. Moses; Anshu Dubey; Mohamed Wahib; Jens Domke

**会议**：SC 2025 · St. Louis, MO

## 摘要

The proliferation of low-precision units in modern high-performance architectures increasingly burdens domain scientists. Historically, the choice in HPC was easy: Can we get away with 32-bit floating-point operations and lower bandwidth requirements, or is FP64 necessary? Driven by artificial intelligence, vendors introduce novel low-precision units for vector and tensor operations, and FP64 capabilities stagnate or are reduced. This forces scientists to re-evaluate their codes, but a trivial search-and-replace approach to go from FP64 to FP16 will not suffice. We introduce RAPTOR: a numerical profiling tool to guide scientists in their search for code regions where precision lowering is feasible. Using LLVM, we transparently replace high-precision computations using low-precision units, or emulate a user-defined precision. RAPTOR is a novel, feature-rich approach—with a focus on ease of use—to change, profile, and reason about numerical requirements and instabilities, which we demons

---

## 一句话总结

> 该工作属于 Precision and Real Number Representations 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Precision and Real Number Representations 领域贡献新的设计范式或评估框架。
