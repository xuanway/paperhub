---
title: "A Distributed Matrix-Block-Vector Multiplication in Presence of System Performance Variability"
description: "PPoPP 2026 Session 13（Matrix and Linear Algebra Algorithms）：1D 流水线 + 静态调度，较 COSMA 1.85×、ScaLAPACK 17×"
tags:
  - "PPoPP2026"
  - "Session-13"
  - "Matrix and Linear Algebra Algorithms"
  - "Distributed Linear Algebra"
  - "Load Balancing"
  - "Performance Modeling"
authors:
  - "Yuchen Ma"
  - "Bin Ren"
  - "Andreas Stathopoulos"
session: "Session 13: Matrix and Linear Algebra Algorithms"
session_number: 13
session_chair: "William S. Moses"
date: "2026-02-04"
time: "10:30–10:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786453"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# A Distributed Matrix-Block-Vector Multiplication in Presence of System Performance Variability

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 SMatVec 库，用 1D 流水线 Matvec 结合即时核矩阵生成与四项优化容忍系统波动，较 COSMA 最高 1.85×、较 ScaLAPACK 17× 加速。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 13: Matrix and Linear Algebra Algorithms</p>
</div>

**作者**：Yuchen Ma, Bin Ren, and Andreas Stathopoulos — College of William & Mary, USA

**会议**：PPoPP 2026 · 2026 年 2 月 4 日 10:30–10:50 · Session 13: Matrix and Linear Algebra Algorithms（主席：William S. Moses）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786453) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Distributed matrix-block-vector multiplication (Matvec) algorithm is a critical component of many applications, but can be computationally challenging for dense matrices of dimension 𝑂(106–107) and blocks of 𝑂(10–100) vectors. We present performance analysis, implementation, and optimization of our SMatVec library for Matvec under the effect of system variability. Our modeling shows that 1D pipelining Matvec is as efficient as 2D algorithms at small to medium clusters, which are sufficient for these problem sizes. We develop a performance tracing framework and a simulator that reveal pipeline bubbles caused by modest ~5% system variability. To tolerate such variability, our SMatVec library, which combines on-the-fly kernel matrix generation and Matvec, integrates four optimizations: inter-process data preloading, unconventional static thread scheduling, cache-aware tiling, and multi-version unrolling. In our benchmarks on 𝑂(105) Matvec problems, SMatVec achieves up to 1.85× speedup over COSMA and 17× over ScaLAPACK. For 𝑂(106) problems, where COSMA and ScaLAPACK exceed memory capacity, SMatVec maintains linear strong scaling and achieves peak performance of 75% FMA Flop/s. Its static scheduling policy has a 2.27× speedup compared to the conventional work-stealing dynamic scheduler, and is predicted to withstand up to 108% performance variability under exponential distributed variability simulation.

## 中文摘要

分布式矩阵-块-向量乘法（Matvec）算法是许多应用的关键组成部分，但对于维度为 O(10^6–10^7)、块包含 O(10–100) 个向量的稠密矩阵，其计算颇具挑战。我们给出了在系统性能波动影响下 SMatVec 库用于 Matvec 的性能分析、实现与优化。我们的建模表明，在中小规模集群上，一维流水线 Matvec 与二维算法同样高效，而这些集群足以应对此类问题规模。我们开发了一个性能追踪框架与一个模拟器，揭示了由约 5% 的适度系统波动所引起的流水线气泡。为容忍这种波动，我们的 SMatVec 库将即时（on-the-fly）核矩阵生成与 Matvec 相结合，并集成四项优化：进程间数据预加载、非常规静态线程调度、缓存感知分块以及多版本展开。在 O(10^5) 规模的 Matvec 问题基准测试中，SMatVec 相对 COSMA 最高取得 1.85× 的加速，相对 ScaLAPACK 取得 17× 的加速。对于 O(10^6) 的问题——此时 COSMA 与 ScaLAPACK 已超出内存容量——SMatVec 保持线性强扩展性，并达到 75% FMA Flop/s 的峰值性能。其静态调度策略相比传统的工作窃取动态调度器有 2.27× 的加速，并被预测在指数分布波动模拟下可承受高达 108% 的性能波动。

## 英文关键词

Matrix-Block-Vector Multiplication, Performance Variability, Scalability

## 中文关键词

矩阵-块-向量乘法；性能波动；可扩展性

---

## 一句话总结

> 提出 SMatVec 库，用 1D 流水线 Matvec 结合即时核矩阵生成与四项优化容忍系统波动，较 COSMA 最高 1.85×、较 ScaLAPACK 17× 加速。

## 研究问题

分布式矩阵-块-向量乘法（Matvec）需处理 O(10^6–10^7) 维稠密矩阵与 O(10–100) 个向量块，计算挑战大；系统性能波动还会在流水线中引入气泡，而现有库缺乏针对性的容忍手段。

## 方法简述

- 通过建模分析表明，在小到中等规模集群上 1D 流水线 Matvec 与 2D 算法效率相当，且足以覆盖此类问题规模。
- 开发性能追踪框架与模拟器，揭示仅约 5% 的系统波动即可造成流水线气泡。
- SMatVec 库将核矩阵即时生成与 Matvec 结合，并集成进程间数据预加载、非常规静态线程调度、缓存感知分块与多版本展开四项优化以容忍波动。

## 主要结果

- 在 O(10^5) 规模的 Matvec 问题上，相对 COSMA 最高 1.85×、相对 ScaLAPACK 17× 加速。
- 对 O(10^6) 问题（COSMA 与 ScaLAPACK 已超出内存容量），SMatVec 保持线性强扩展，峰值性能达 75% FMA Flop/s。
- 其静态调度策略比常规 work-stealing 动态调度快 2.27×；在指数分布波动模拟下，可承受最高 108% 的性能波动。

---

> 所属 Session：[Session 13: Matrix and Linear Algebra Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
