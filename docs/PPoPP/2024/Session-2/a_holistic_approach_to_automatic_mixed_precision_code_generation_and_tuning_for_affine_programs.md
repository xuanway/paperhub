---
title: "A Holistic Approach to Automatic Mixed-Precision Code Generation and Tuning for Affine Programs"
description: "PPoPP 2024 Session Compilers and Runtimes for Parallel Systems：统一参数耦合混合精度代码生成与调优，CPU 上比 LuIs 快 3.28×"
tags:
  - "PPoPP2024"
  - "Session-2"
  - "Compilers and Runtimes for Parallel Systems"
  - "polyhedral model"
  - "autotuning"
  - "mixed precision"
authors:
  - "Jinchen Xu"
  - "Guanghui Song"
  - "Bei Zhou"
  - "Fei Li"
  - "Jiangwei Hao"
  - "Jie Zhao"
session: "Session 2: Compilers and Runtimes for Parallel Systems"
session_number: 2
session_chair: "Mohamed Riyadh Baghdadi"
date: "2024-03-04"
time: "11:50–12:10"
room: "Moorfoot"
doi: "10.1145/3627535.3638484"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# A Holistic Approach to Automatic Mixed-Precision Code Generation and Tuning for Affine Programs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">针对类型转换开销在代码生成前不可知、迫使生成与调优解耦的问题，提出用一个参数统一生成器与调优器的 PrecTuner，CPU 上比 LuIs 快 3.28× 且误差更小。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 2: Compilers and Runtimes for Parallel Systems</p>
</div>

**作者**：Jinchen Xu (Information Engineering University); Guanghui Song (Li Auto Inc.); Bei Zhou, Fei Li, Jiangwei Hao (Information Engineering University); Jie Zhao (Hunan University)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 11:50–12:10 · Session 2: Compilers and Runtimes for Parallel Systems（主席：Mohamed Riyadh Baghdadi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638484) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Reducing floating-point (FP) precision is used to trade the quality degradation of a numerical program’s output for performance, but this optimization coincides with type casting, whose overhead is undisclosed until a mixed-precision code version is generated. This uncertainty enforces the decoupled implementation of mixed-precision code generation and autotuning in prior work. In this paper, we present a holistic approach called PrecTuner that consolidates the mixed-precision code generator and the autotuner by defining one parameter. This parameter is first initialized by some automatically sampled values and used to generate several code variants, with various loop transformations also taken into account. The generated code variants are next profiled to solve a performance model formulated using the aforementioned parameter, possibly under a pre-defined quality degradation budget. The best-performing value of the defined parameter is finally predicted without evaluating all code variants. Experimental results of the PolyBench benchmarks on CPU demonstrate that PrecTuner outperforms LuIs by 3.28× while achieving smaller errors, and we also validate its effectiveness in optimizing a real-life large-scale application. In addition, PrecTuner also obtains a mean speedup of 1.81× and 1.52×-1.73× over Pluto on single-and multi-core CPU, respectively, and 1.71× over PPCG on GPU.

## 中文摘要

降低浮点（FP）精度被用于以数值程序输出的质量下降换取性能，但这一优化同时伴随着类型转换，而类型转换的开销在生成混合精度代码版本之前是不可知的。这种不确定性迫使先前工作将混合精度代码生成与自动调优解耦实现。在本文中，我们提出一种称为 PrecTuner 的整体化方法，它通过定义一个参数将混合精度代码生成器与自动调优器统一起来。该参数首先由一些自动采样的值初始化，并用于生成若干代码变体，生成时也考虑了各种循环变换。随后对生成的代码变体进行性能剖析，以求解用上述参数表述的性能模型，并且可能是在预先定义的质量退化预算之下求解。最后，无需评估所有代码变体即可预测所定义参数的最佳取值。在 CPU 上的 PolyBench 基准实验结果表明，PrecTuner 比 LuIs 快 3.28×，同时误差更小；我们还验证了其在优化一个真实大规模应用中的有效性。此外，PrecTuner 在单核和多核 CPU 上相对 Pluto 分别取得 1.81× 和 1.52×–1.73× 的平均加速，在 GPU 上相对 PPCG 取得 1.71× 的加速。

## 英文关键词

polyhedral model, performance, autotuning

## 中文关键词

多面体模型；性能；自动调优

---

## 一句话总结

> 针对类型转换开销在代码生成前不可知、迫使生成与调优解耦的问题，提出用一个参数统一生成器与调优器的 PrecTuner，CPU 上比 LuIs 快 3.28× 且误差更小。

## 研究问题

降低浮点精度以性能换质量会伴随类型转换，而该开销在生成混合精度代码版本之前无法得知；这种不确定性迫使已有工作把代码生成与自动调优解耦实现。

## 方法简述

- 提出整体化方法 PrecTuner，通过定义一个参数把混合精度代码生成器与自动调优器统一起来
- 用自动采样的值初始化该参数并生成若干代码变体，生成时同时考虑多种循环变换
- 对生成的代码变体进行性能剖析，求解以该参数表述的性能模型，并可在预先定义的质量退化预算下求解
- 无需评估所有代码变体即可预测该参数的最佳取值

## 主要结果

- 在 CPU 上的 PolyBench 基准中，PrecTuner 比 LuIs 快 3.28×，同时误差更小
- 相对 Pluto 在单核与多核 CPU 上分别取得 1.81× 与 1.52×–1.73× 的平均加速，在 GPU 上相对 PPCG 取得 1.71× 加速
- 在真实大规模应用的优化中验证了有效性

---

> 所属 Session：[Session 2: Compilers and Runtimes for Parallel Systems](index.md) · 返回 [PPoPP 2024 总览](../index.md)
