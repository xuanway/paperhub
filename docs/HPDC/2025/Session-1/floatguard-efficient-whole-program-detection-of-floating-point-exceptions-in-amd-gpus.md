---
title: "FloatGuard: Efficient Whole-Program Detection of Floating-Point Exceptions in AMD GPUs"
description: "HPDC 2025 · Session 1 — Numerical Methods"
tags:
  - "HPDC2025"
  - "Session 1"
  - "Numerical Methods"
---

# FloatGuard: Efficient Whole-Program Detection of Floating-Point Exceptions in AMD GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 1</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731586) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/miao.pdf)

**作者**：Dolores Miao, Ignacio Laguna, Cindy Rubio-González

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

Porting scientific applications across different GPU architectures introduces floating-point arithmetic variations that can affect reproducibility, making efficient detection and mitigation of exceptions like NaNs and infinities crucial. While NVIDIA has dominated the GPU market, AMD GPUs are increasingly used in HPC systems as well, yet existing floating-point exception detection frameworks focus on NVIDIA, leaving a gap for AMD GPUs. We present FloatGuard, the first framework for efficiently detecting floating-point exceptions in HIP programs running on AMD GPUs. FloatGuard leverages AMD GPU hardware registers to detect floating-point exceptions, overcoming the limitations of AMD’s built-in trapping mechanisms through a novel algorithm that combines assembly-and source-level instrumentation with debugger-guided execution. We evaluate FloatGuard on 565 HIP programs, detecting floating-point exceptions in 507 cases with a slowdown ratio that increases at most linearly with the number of exceptions discovered. Furthermore, we analyze the impact of compiler optimizations on exceptions trapped, and compare FloatGuard with the state-of-the-art tool for detecting floating-point exceptions in CUDA programs, which further reveals key differences between AMD and NVIDIA’s floating-point exception behaviors.

## 中文摘要

将科学应用移植到不同的 GPU 架构会引入浮点算术差异，影响可复现性，因此高效检测并缓解 NaN 与无穷等异常至关重要。尽管 NVIDIA 主导 GPU 市场，AMD GPU 在 HPC 系统中也日益普及，但现有浮点异常检测框架主要面向 NVIDIA，AMD GPU 仍存在空白。我们提出 FloatGuard，首个用于在 AMD GPU 上运行的 HIP 程序中高效检测浮点异常的框架。FloatGuard 利用 AMD GPU 硬件寄存器检测浮点异常，通过一种将汇编级与源码级插桩及调试器引导执行相结合的新算法，克服了 AMD 内置陷阱机制的局限。我们在 565 个 HIP 程序上评估 FloatGuard，在 507 个案例中检测到浮点异常，其减速比最多随发现的异常数量线性增长。此外，我们分析了编译器优化对陷阱捕获的影响，并将 FloatGuard 与最先进的 CUDA 程序浮点异常检测工具进行比较，进一步揭示了 AMD 与 NVIDIA 在浮点异常行为上的关键差异。

## 英文关键词

floating-point exception detection, high-performance computing, heterogeneous computing, compiler optimization, numerical reproducibility, program portability

## 中文关键词

浮点异常检测，高性能计算，异构计算，编译器优化，数值可复现性，程序可移植性

---

[← 返回 Session 1 — Numerical Methods](index.md)
