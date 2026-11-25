---
title: "FPBOXer: Efficient Input-Generation for Targeting Floating-Point Exceptions in GPU Programs"
description: "HPDC 2024 · Session 2 — Resilience"
tags:
  - "HPDC2024"
  - "Session 2"
  - "Resilience"
---

# FPBOXer: Efficient Input-Generation for Targeting Floating-Point Exceptions in GPU Programs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 2</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658660)

**作者**：Anh Tran, Ignacio Laguna, Ganesh Gopalakrishnan

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）

---

## 英文摘要

Numerical programs that generate floating-point exceptions, such as NaNs, are inherently unreliable, as these programs can produce meaningless outputs or affect control flow. When these programs run on GPUs, one cannot rely on hardware traps to handle the exceptions, as most GPUs do not support them. Unfortunately, we must also employ black-box testing for many such GPU programs, as they are supplied as binary code only. While previous work has shown that black-box testing for triggering floating-point exceptions can be approached using Bayesian Optimization, their approach cannot handle programs with more than three inputs. We contribute a new tool, FPBOXer, which pushes up the capabilities of BO to handle over 20 inputs—this makes our contribution capable of handling realistic HPC program functions. In addition to delivering an overall 90x speedup over the previous methods, FPBOXer does not suffer from “self-inflicted” exceptions that are caused by the BO algorithm itself—something that previous tools did. This is achieved through parallel deployments of asynchronous BO searches, which has the beneficial side-effect of improving the GPU-utilization. By using FPBOXer, developers can, for the first time, find exception-causing inputs in realistic HPC programs, as we demonstrate when we apply FPBOXer to NAS, Lampps, CFD, ExaMiniMD, HPCCG, MiniFE, and BDCSVD.

## 中文摘要

产生 NaN 等浮点异常的数值程序本质上不可靠，因为这些程序可能产生无意义的输出或影响控制流。当这些程序在 GPU 上运行时，不能依赖硬件陷阱来处理异常，因为大多数 GPU 不支持。不幸的是，对于许多此类 GPU 程序我们只能采用黑盒测试，因为它们仅以二进制代码提供。尽管先前工作表明，可用贝叶斯优化（BO）来开展触发浮点异常的黑盒测试，但其方法无法处理输入超过三个的程序。我们贡献了新工具 FPBOXer，将 BO 的能力推进到可处理 20 个以上输入——这使我们的贡献能够应对真实的 HPC 程序函数。除了比先前方法整体快 90 倍之外，FPBOXer 不会出现由 BO 算法本身造成的“自伤式”异常——而先前工具存在这一问题。这通过并行部署异步 BO 搜索实现，还带来了提升 GPU 利用率的有利副作用。借助 FPBOXer，开发者首次能够在真实 HPC 程序中找到引发异常的输入，我们将 FPBOXer 应用于 NAS、Lampps、CFD、ExaMiniMD、HPCCG、MiniFE 和 BDCSVD 时展示了这一点。

## 英文关键词

Floating-point Arithmetic, Exceptions, Bayesian Optimization, High-Performance Computing

## 中文关键词

浮点算术，异常，贝叶斯优化，高性能计算

---

[← 返回 Session 2 — Resilience](index.md)
