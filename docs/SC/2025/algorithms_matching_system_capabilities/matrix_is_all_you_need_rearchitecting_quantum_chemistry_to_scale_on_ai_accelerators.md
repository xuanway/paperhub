---
title: "Matrix Is All You Need: Rearchitecting Quantum Chemistry to Scale on AI Accelerators"
description: "SC 2025 · Algorithms: Matching System Capabilities · Haozhi Han; Kun Li; Fusong Ju; Qi Li; Hong An; Yifeng Chen; Yunquan Zhang; Ting "
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# Matrix Is All You Need: Rearchitecting Quantum Chemistry to Scale on AI Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Haozhi Han; Kun Li; Fusong Ju; Qi Li; Hong An; Yifeng Chen; Yunquan Zhang; Ting Cao; Mao Yang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Scientific computing remains misaligned with the execution paradigm of modern AI accelerators, which favor structured, low-precision matrix operations. Quantum chemistry exemplifies this gap, with irregular computations, fragmented utilization, and limited support for high-complexity systems. We present Mako, a matrix-centric system that rearchitects quantum chemistry to scale on AI accelerators. Mako comprises three components: KernelMako reformulates ERI evaluation into composable MatMul pipelines using CUTLASS; QuantMako introduces physics-informed quantization to exploit low-precision potential; and CompilerMako automates kernel fusion and architecture-tuned specialization. Mako achieves up to ~20× speedup on high-angular-momentum basis sets. It sustains over 90% parallel efficiency on a single node and 70% across 64 GPUs, completing the accurate simulation of ubiquitin (1,231 atoms, def2-TZVP) from days to just 58 minutes. Mako demonstrates how scientific workloads can be restruct

---

## 一句话总结

> 该工作属于 Algorithms: Matching System Capabilities 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Matching System Capabilities 领域贡献新的设计范式或评估框架。
