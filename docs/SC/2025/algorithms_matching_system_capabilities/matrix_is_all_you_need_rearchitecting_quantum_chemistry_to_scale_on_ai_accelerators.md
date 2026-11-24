---
title: "Matrix Is All You Need: Rearchitecting Quantum Chemistry to Scale on AI Accelerators"
description: "SC 2025 · Algorithms: Matching System Capabilities · Haozhi Han; Kun Li; Fusong Ju; Qi Li; Hong An; Yifeng Chen; Yunquan Zhang; Ting "
tags:
  - "SC2025"
  - "Algorithms: Matching System Capabilities"
---

# Matrix Is All You Need: Rearchitecting Quantum Chemistry to Scale on AI Accelerators

**中文标题：** 矩阵就是你所需要的一切：重构量子化学以在 AI 加速器上扩展

**所属 Session：** [Algorithms: Matching System Capabilities](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Matching System Capabilities。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Matching System Capabilities</p>
</div>

**作者**：Haozhi Han; Kun Li; Fusong Ju; Qi Li; Hong An; Yifeng Chen; Yunquan Zhang; Ting Cao; Mao Yang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap462&sess=sess307)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Scientific computing remains misaligned with the execution paradigm of modern AI accelerators, which favor structured, low-precision matrix operations. Quantum chemistry exemplifies this gap, with irregular computations, fragmented utilization, and limited support for high-complexity systems. We present Mako, a matrix-centric system that rearchitects quantum chemistry to scale on AI accelerators. Mako comprises three components: KernelMako reformulates ERI evaluation into composable MatMul pipelines using CUTLASS; QuantMako introduces physics-informed quantization to exploit low-precision potential; and CompilerMako automates kernel fusion and architecture-tuned specialization. Mako achieves up to ~20× speedup on high-angular-momentum basis sets. It sustains over 90% parallel efficiency on a single node and 70% across 64 GPUs, completing the accurate simulation of ubiquitin (1,231 atoms, def2-TZVP) from days to just 58 minutes. Mako demonstrates how scientific workloads can be restruct

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
