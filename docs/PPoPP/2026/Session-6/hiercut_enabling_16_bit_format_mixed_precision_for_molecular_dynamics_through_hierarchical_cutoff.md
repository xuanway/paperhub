---
title: "HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff"
description: "PPoPP 2026 Session 6（Mixed Precision and Quantization）：按截断层分配 16-bit 精度，较 FP64 最高 3.75×"
tags:
  - "PPoPP2026"
  - "Session-6"
  - "Mixed Precision and Quantization"
  - "Mixed Precision"
  - "Molecular Dynamics"
  - "16-bit Format"
authors:
  - "Zeyu Song"
  - "Lin Gan"
  - "Xiaohui Duan"
  - "Zhengrui Li"
  - "Jiayu Fu"
  - "Yinuo Wang"
  - "Guangzhao Li"
  - "Guangwen Yang"
session: "Session 6: Mixed Precision and Quantization"
session_number: 6
session_chair: "Dingwen Tao"
date: "2026-02-03"
time: "12:30–12:50"
room: "Balmoral"
doi: "10.1145/3774934.3786433"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Artifact Award"
---

# HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 HierCut，利用分子动力学的截断方案按截断层为粒子分配不同精度，在 LAMMPS KOKKOS 中引入 16-bit 混合精度，较 FP64 最高加速 3.75×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 6: Mixed Precision and Quantization</p>
</div>

**作者**：Zeyu Song, Lin Gan, Xiaohui Duan, Zhengrui Li, Jiayu Fu, Yinuo Wang, Guangzhao Li, and Guangwen Yang — Tsinghua University, China; Shandong University, China; Institute of Software at Chinese Academy of Sciences, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 12:30–12:50 · Session 6: Mixed Precision and Quantization（主席：Dingwen Tao）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786433) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Artifact Award**

---

## 英文摘要

Mixed-precision methods offer the potential to achieve better performance while maintaining accuracy comparable to that of high-precision formats. However, the adoption of mixed precision—particularly with 16-bit formats—in scientific computing remains limited due to precision truncation. To address this challenge, we propose HierCut, a mixed-precision strategy that leverages cutoff schemes in molecular dynamics (KOKKOS package of LAMMPS) by assigning different precision levels to particles across distinct cutoff layers. We further introduce techniques to improve the performance and accuracy of simulations using 16-bit numerical formats, and develop error analysis methods to guide the configuration of mixed-precision ratios. Our scheme achieves accuracy comparable to high-precision results, delivering a speedup of up to 3.75x over the original FP64 implementation of LAMMPS and up to 1.40x over the optimized FP32 kernels, based on NVIDIA A100 GPUs. Our implementation can be effectively scaled to boost large-scale multi-GPU simulations.

## 中文摘要

混合精度方法有望在保持与高精度格式相当的精度水平的同时取得更好的性能。然而，由于精度截断，混合精度——尤其是 16 比特格式——在科学计算中的应用仍然有限。为应对这一挑战，我们提出 HierCut，一种利用分子动力学中截断方案的混合精度策略（基于 LAMMPS 的 KOKKOS 包），它为不同截断层内的粒子分配不同的精度等级。我们进一步引入利用 16 比特数值格式提升仿真性能与精度的技术，并开发误差分析方法以指导混合精度比例的配置。该方案达到了与高精度结果相当的精度，在 NVIDIA A100 GPU 上相较 LAMMPS 原始 FP64 实现最高取得 3.75 倍加速，相较优化的 FP32 内核最高取得 1.40 倍加速。我们的实现可有效扩展，以提升大规模多 GPU 仿真的性能。

## 英文关键词

Mixed Precision, Molecular Dynamics

## 中文关键词

混合精度；分子动力学

---

## 一句话总结

> 提出 HierCut，利用分子动力学的截断方案按截断层为粒子分配不同精度，在 LAMMPS KOKKOS 中引入 16-bit 混合精度，较 FP64 最高加速 3.75×。

## 研究问题

混合精度（尤其 16-bit 格式）在科学计算中受精度截断限制，难以在保持精度的同时获得性能收益。

## 方法简述

- 将分子动力学的 cutoff 方案建模为分层精度分配，对不同截断层内的粒子使用不同精度。
- 引入提升 16-bit 数值格式仿真性能与精度的技术。
- 开发误差分析方法，用于指导混合精度比例的配置。

## 主要结果

- 精度与高精度结果相当。
- 在 NVIDIA A100 上相对 LAMMPS 原始 FP64 实现最高加速 3.75×，相对优化后的 FP32 核最高加速 1.40×。
- 实现可有效扩展到大规模多 GPU 仿真。

---

> 所属 Session：[Session 6: Mixed Precision and Quantization](index.md) · 返回 [PPoPP 2026 总览](../index.md)
