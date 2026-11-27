---
title: "SPARK – Sparsity Aware, Low Area, Energy-Efficient, Near-memory Architecture for Accelerating Linear Programming Problems"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# SPARK – Sparsity Aware, Low Area, Energy-Efficient, Near-memory Architecture for Accelerating Linear Programming Problems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Siddhartha Raman Sundara Raman (The University of Texas at Austin), Lizy Kurian John (UT Austin), Jaydeep Kulkarni (University of Texas, Austin)
**会议**：HPCA 2025

---

## 中文标题

SPARK：面向线性规划问题加速的稀疏感知、小面积、高能效近内存架构

## 英文摘要

Integer Linear Programming (ILP) is an important mathematical approach for solving time-sensitive real-life optimization problems, including network routing, map routing, traffic scheduling, etc. However, the algorithms for solving ILPs are typically sparse and branch-intensive, and not CPU/GPU friendly. In the paper “What could a million cores do to solve Integer programs”, Koch et al. [40] presented data illustrating that Integer Linear Programming (ILP) applications take tens of hours of execution time even on the largest parallel computers. Long execution time is a problem because many real-life applications need a decision in seconds or minutes. The widely used ILP solvers, like Gurobi (optimized for CPUs), perform software-based optimizations to handle the inherent sparsity in ILPs but still do not meet decision threshold because of the limited throughput of CPUs. GPUs are suited for large-sized dot-product compute, however, GPU-based ILP solvers also do not meet decision thresholds as (i) GPU is not sparsity friendly and (ii) GPU incurs thread divergence for branching, resulting in under-utilization of streaming engines and periodic host-GPU interaction. We propose SPARK, a sparsity-aware, reuse-aware, energy-efficient, reconfigurable, near-cache ILP architecture that (i) re-configures the existing L1 cache present in CPUs to perform near-cache acceleration with easy integration into the baseline CPU pipeline with minimal area overhead (∼ 1.4% of a CPU), (ii) performs near-cache sparsity detection and sparsity-aware compute, reducing the number of insignificant computations, and data movement energy overheads, (iii) leverages the computational patterns present in algorithms used for solving ILP to realize a reuse-aware architecture, and (iv) is applicable to solving sparse and dense ILPs and LPs (Linear Programs). We observe 15x/20x, and 152x/740x performance/energy improvement over AMD’s Zen3 CPU, and Nvidia’s Tesla v100 GPU for sparse real-life ILPs in Mixed Integer Programming library (MIPLIB 2017). For sparse LPs (non-integer), SPARK achieves 7-17x/103-250x performance/energy improvement over CPU/ GPU indicating SPARK’s broad applicability.

## 中文摘要

整数线性规划（ILP）是求解网络路由、地图寻路、交通调度等时效性优化问题的重要方法，但求解算法稀疏、分支密集，对 CPU/GPU 不友好。ILP 应用在最大的并行计算机上也需数十小时，现实应用却需秒级决策。Gurobi 等求解器用软件优化处理稀疏性，但受 CPU 吞吐限制；GPU 适合大规模点积，却对稀疏性不友好、因分支发散无法达标。我们提出 SPARK，一种稀疏感知、复用感知、高能效、可重构的近缓存 ILP 架构：它重构 CPU 现有 L1 缓存做近缓存加速，仅需约 1.4% CPU 面积即可融入流水线；它做稀疏性检测与稀疏计算，减少无意义计算与搬运能耗；它利用 ILP 求解算法中的计算模式实现复用，适用于稀疏与稠密 ILP 和 LP。在 MIPLIB 2017 的稀疏真实 ILP 上，相比 AMD Zen3 CPU 与 Nvidia Tesla v100 GPU，性能/能耗提升 15 倍/20 倍与 152 倍/740 倍；对稀疏 LP 提升 7-17 倍/103-250 倍。
