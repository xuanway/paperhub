---
title: "Million-Atom Ab Initio Electron Dynamics: Discontinuous Galerkin Real-Time Time-Dependent Density Functional Theory"
description: "SC 2025 · Applications: Large-Scale Scientific Simulation · Junwei Feng; Junshi Chen; Xiangyu Zhang; Junhui Liu; Xinming Qin; Lingyun Wan; S"
tags:
  - "SC2025"
  - "Applications: Large-Scale Scientific Simulation"
---

# Million-Atom Ab Initio Electron Dynamics: Discontinuous Galerkin Real-Time Time-Dependent Density Functional Theory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Large-Scale Scientific Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Large-Scale Scientific Simulation</p>
</div>

**作者**：Junwei Feng; Junshi Chen; Xiangyu Zhang; Junhui Liu; Xinming Qin; Lingyun Wan; Sheng Chen; Wentiao Wu; Bingkun Hou; Yexuan Lin; Yihong Zhang; Zechuan Zhang; Yijun Hu; Weile Jia; Hong An; Jinlong Yang; Wei Hu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Over the past decades, first-principles real-time time-dependent density functional theory (RT-TDDFT) simulations have been limited to systems with only thousands of atoms. We propose a novel method based on the discontinuous Galerkin adaptive local basis, significantly reducing global communication in RT-TDDFT. We further introduce a tensor compression technique that leverages basis locality to avoid repeated evaluation of multi-center integrals in hybrid functionals, greatly reducing computational cost. To overcome the projection bottleneck in our basis sets, we design a fused GEMM-Reduce operation that achieves several times higher floating-point efficiency than standard BLAS combination. Our implementation reaches 34.8\% of theoretical peak performance on 524,288 CGs of the New Sunway supercomputer and simulates electronic dynamics of systems with over one million atoms for both local-semi-local and hybrid functionals. This work improves computational scale by two orders of magnitu

---

## 一句话总结

> 该工作属于 Applications: Large-Scale Scientific Simulation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Applications: Large-Scale Scientific Simulation 领域贡献新的设计范式或评估框架。
