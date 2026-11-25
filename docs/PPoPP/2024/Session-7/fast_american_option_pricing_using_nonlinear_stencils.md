---
title: "Fast American Option Pricing using Nonlinear Stencils"
description: "PPoPP 2024 Session Parallel Algorithms：以 FFT 求解非线性 stencil 的期权定价，T≈0.5×10⁶ 时提速超 500×"
tags:
  - "PPoPP2024"
  - "Session-7"
  - "Parallel Algorithms"
  - "American Option Pricing"
  - "Nonlinear Stencil"
  - "Fast Fourier Transform"
authors:
  - "Zafar Ahmad"
  - "Reilly Browne"
  - "Rezaul Chowdhury"
  - "Rathish Das"
  - "Yushen Huang"
  - "Yimin Zhu"
session: "Session 7: Parallel Algorithms"
session_number: 7
session_chair: "Prashant Pandey"
date: "2024-03-05"
time: "15:20–15:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638506"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Fast American Option Pricing using Nonlinear Stencils

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">针对二项式、三项式与 Black-Scholes-Merton 期权定价，提出基于 FFT 的快速并行有限差分算法，首次以 o(T²) 时间求解非线性一维 stencil 计算。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 7: Parallel Algorithms</p>
</div>

**作者**：Zafar Ahmad, Reilly Browne, Rezaul Chowdhury (Stony Brook University); Rathish Das (University of Houston); Yushen Huang, Yimin Zhu (Stony Brook University)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 15:20–15:40 · Session 7: Parallel Algorithms（主席：Prashant Pandey）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638506) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

We study the binomial, trinomial, and Black-Scholes-Merton models of option pricing. We present fast parallel discrete-time finite-difference algorithms for American call option pricing under the binomial and trinomial models and American put option pricing under the Black-Scholes-Merton model. For T-step finite differences, each algorithm runs in O((T log^2 T)/p + T) time under a greedy scheduler on p processing cores, which is a significant improvement over the Θ(T^2/p) + Ω (TlogT) time taken by the corresponding state-of-the-art parallel algorithm. Even when run on a single core, the O(T log^2 T) time taken by our algorithms is asymptotically much smaller than the Θ(T^2) running time of the fastest known serial algorithms. Implementations of our algorithms significantly outperform the fastest implementations of existing algorithms in practice, e.g., when run for T ≈ 1000 steps on a 48-core machine, our algorithm for the binomial model runs at least 15× faster than the fastest existing parallel program for the same model with the speedup factor gradually reaching beyond 500× for T ≈ 0.5 × 10^6. It saves more than 80% energy when T ≈ 4000, and more than 99% energy for T > 60,000. Our algorithms can be viewed as solving a class of nonlinear 1D stencil (i.e., finite-difference) computation problems efficiently using the Fast Fourier Transform (FFT). To our knowledge, ours are the first algorithms to handle such stencils in o(T^2) time. These contributions are of independent interest as stencil computations have a wide range of applications beyond quantitative finance. Full Version: https://arxiv.org/abs/2303.02317.

## 中文摘要

我们研究二项式、三项式和 Black-Scholes-Merton 期权定价模型。我们提出了快速的并行离散时间有限差分算法，用于二项式和三项式模型下的美式看涨期权定价，以及 Black-Scholes-Merton 模型下的美式看跌期权定价。对于 T 步有限差分，在 p 个处理器核上的贪心调度器下，每个算法运行时间为 O((T log²T)/p + T)，相比对应的最先进并行算法所需的 Θ(T²/p) + Ω(T log T) 时间有显著改进。即使在单核上运行，我们的算法所需的 O(T log²T) 时间也渐进地远小于已知最快串行算法的 Θ(T²) 运行时间。我们算法的实现在实际中显著优于现有算法的最快实现，例如，在 48 核机器上以 T ≈ 1000 步运行时，我们的二项式模型算法比同一模型下最快的现有并行程序至少快 15 倍，当 T ≈ 0.5×10^6 时加速比逐渐超过 500 倍。当 T ≈ 4000 时节能 80% 以上，当 T > 60,000 时节能 99% 以上。我们的算法可以看作是利用快速傅里叶变换（FFT）高效求解一类非线性一维 stencil（即有限差分）计算问题。据我们所知，我们的算法是首批能在 o(T²) 时间内处理此类 stencil 的算法。这些贡献具有独立价值，因为 stencil 计算在量化金融之外有广泛的应用。完整版本：https://arxiv.org/abs/2303.02317。

## 英文关键词

American Option Pricing, Binomial Option Pricing Model, Trinomial Option Pricing, Black-Scholes-Merton Option Pricing Model, Nonlinear Stencil, Fast Fourier Transform, Finite-Difference Method

## 中文关键词

美式期权定价；二项式期权定价模型；三项式期权定价；Black-Scholes-Merton 期权定价模型；非线性 stencil 计算；快速傅里叶变换；有限差分法

---

## 一句话总结

> 针对二项式、三项式与 Black-Scholes-Merton 期权定价，提出基于 FFT 的快速并行有限差分算法，首次以 o(T²) 时间求解非线性一维 stencil 计算。

## 研究问题

对应的最先进并行算法需 Θ(T²/p)+Ω(T log T) 时间、已知最快串行算法需 Θ(T²)，对 T 步有限差分而言复杂度过高、实际运行与能耗代价大。

## 方法简述

- 针对二项式与三项式模型下的美式看涨期权、以及 Black-Scholes-Merton 模型下的美式看跌期权，提出快速的并行离散时间有限差分算法
- 将这类非线性一维 stencil（有限差分）计算建模为可用快速傅里叶变换（FFT）高效求解的问题
- 在 p 个处理器核的贪心调度器下将每个算法的时间复杂度设计为 O((T log²T)/p + T)

## 主要结果

- 在 48 核机器上 T≈1000 步时，二项式模型算法比同模型最快的现有并行程序至少快 15 倍；T≈0.5×10^6 时加速比逐步超过 500 倍
- T≈4000 时节省 80% 以上能量，T>60,000 时节省 99% 以上能量
- 单核运行时间为 O(T log²T)，渐进地远小于已知最快串行算法的 Θ(T²)

---

> 所属 Session：[Session 7: Parallel Algorithms](index.md) · 返回 [PPoPP 2024 总览](../index.md)
