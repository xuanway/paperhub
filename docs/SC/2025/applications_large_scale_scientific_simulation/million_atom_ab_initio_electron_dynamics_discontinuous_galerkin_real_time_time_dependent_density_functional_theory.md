---
title: "Million-Atom Ab Initio Electron Dynamics: Discontinuous Galerkin Real-Time Time-Dependent Density Functional Theory"
description: "SC 2025 · Applications: Large-Scale Scientific Simulation · Junwei Feng; Junshi Chen; Xiangyu Zhang; Junhui Liu; Xinming Qin; Lingyun Wan; S"
tags:
  - "SC2025"
  - "Applications: Large-Scale Scientific Simulation"
---

# Million-Atom Ab Initio Electron Dynamics: Discontinuous Galerkin Real-Time Time-Dependent Density Functional Theory

**中文标题：** 百万原子从头算电子动力学：间断伽辽金实时含时密度泛函理论

**所属 Session：** [Applications: Large-Scale Scientific Simulation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Large-Scale Scientific Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Large-Scale Scientific Simulation</p>
</div>

**作者**：Junwei Feng; Junshi Chen; Xiangyu Zhang; Junhui Liu; Xinming Qin; Lingyun Wan; Sheng Chen; Wentiao Wu; Bingkun Hou; Yexuan Lin; Yihong Zhang; Zechuan Zhang; Yijun Hu; Weile Jia; Hong An; Jinlong Yang; Wei Hu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap364&sess=sess177)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Over the past decades, first-principles real-time time-dependent density functional theory (RT-TDDFT) simulations have been limited to systems with only thousands of atoms. We propose a novel method based on the discontinuous Galerkin adaptive local basis, significantly reducing global communication in RT-TDDFT. We further introduce a tensor compression technique that leverages basis locality to avoid repeated evaluation of multi-center integrals in hybrid functionals, greatly reducing computational cost. To overcome the projection bottleneck in our basis sets, we design a fused GEMM-Reduce operation that achieves several times higher floating-point efficiency than standard BLAS combination. Our implementation reaches 34.8\% of theoretical peak performance on 524,288 CGs of the New Sunway supercomputer and simulates electronic dynamics of systems with over one million atoms for both local-semi-local and hybrid functionals. This work improves computational scale by two orders of magnitu

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
