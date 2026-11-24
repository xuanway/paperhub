---
title: "RAPTOR: Practical Numerical Profiling of Scientific Applications"
description: "SC 2025 · Precision and Real Number Representations · Faveo Hoerold; Ivan Radanov Ivanov; Akash Dhruv; William S. Moses; Anshu Dubey; "
tags:
  - "SC2025"
  - "Precision and Real Number Representations"
---

# RAPTOR: Practical Numerical Profiling of Scientific Applications

**中文标题：** 科学应用的实用数值剖析

**所属 Session：** [Precision and Real Number Representations](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Precision and Real Number Representations。</p>
<p class="paper-seo-summary__tags">SC 2025 · Precision and Real Number Representations</p>
</div>

**作者**：Faveo Hoerold; Ivan Radanov Ivanov; Akash Dhruv; William S. Moses; Anshu Dubey; Mohamed Wahib; Jens Domke

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap330&sess=sess304)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The proliferation of low-precision units in modern high-performance architectures increasingly burdens domain scientists. Historically, the choice in HPC was easy: Can we get away with 32-bit floating-point operations and lower bandwidth requirements, or is FP64 necessary? Driven by artificial intelligence, vendors introduce novel low-precision units for vector and tensor operations, and FP64 capabilities stagnate or are reduced. This forces scientists to re-evaluate their codes, but a trivial search-and-replace approach to go from FP64 to FP16 will not suffice. We introduce RAPTOR: a numerical profiling tool to guide scientists in their search for code regions where precision lowering is feasible. Using LLVM, we transparently replace high-precision computations using low-precision units, or emulate a user-defined precision. RAPTOR is a novel, feature-rich approach—with a focus on ease of use—to change, profile, and reason about numerical requirements and instabilities, which we demons

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
