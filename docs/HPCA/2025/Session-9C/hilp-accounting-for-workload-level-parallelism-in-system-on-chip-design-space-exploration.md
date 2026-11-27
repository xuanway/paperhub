---
title: "HILP: Accounting for Workload-Level Parallelism in System-on-Chip Design Space Exploration"
description: "HPCA 2025 · Finding the Best Table"
tags:
  - "HPCA2025"
  - "Finding the Best Table"
---

# HILP: Accounting for Workload-Level Parallelism in System-on-Chip Design Space Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Finding the Best Table。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Finding the Best Table</p>
</div>

**论文链接**：
**作者**：Joseph Rogers (Norwegian University of Science and Technology (NTNU)), Lieven Eeckhout (Ghent University), Magnus Jahre (Norwegian University of Science and Technology (NTNU))
**会议**：HPCA 2025

---

## 中文标题

HILP：在片上系统设计空间探索中考量负载级并行性

## 英文摘要

High-performance System-on-Chip (SoC) architectures are becoming increasingly complex and heterogeneous, and the days when a single application could utilize all of an SoC’s hardware resources are all but over. The SoC’s workload, i.e., the set of independent applications that the SoC typically executes, therefore has a significant impact on its efficiency. Accounting for Workload-Level Parallelism (WLP) in early-stage design space exploration is thus critical as later-stage analysis steps must focus on favorable design points to yield optimal results. Unfortunately, state-of-the-art MultiAmdahl and Gables fall short because they only model the extremes of minimal and maximal WLP. We hence propose HILP, the first early-stage design space exploration approach for heterogeneous SoCs that fully accounts for WLP. Our key observation is that scheduling a workload of independent multi-phase applications on a heterogeneous SoC is an instance of the classic job-shop scheduling optimization problem and thus can be solved using integer linear programming. HILP therefore uses a high-performance integer linear programming solver to find a near-optimal schedule that minimizes the overall execution time of the workload, i.e., it schedules the dependent phases of all applications in the workload on the cores and accelerators of the target SoC to maximize performance while respecting power consumption and memory bandwidth constraints. We validate HILP by demonstrating that it captures the performance effects of Amdahl’s law, the memory wall, and dark silicon, and then use it to explore the impact of WLP across a large SoC design space, yielding multiple insights. The key takeaway is that modeling WLP is necessary to ensure that more detailed, later-stage design tasks focus on the most favorable parts of the vast design space of heterogeneous SoCs.

## 中文摘要

高性能片上系统（SoC）架构日益复杂且异构，单个应用即可利用 SoC 全部硬件资源的时代基本已经结束。因此，SoC 的负载，即它通常执行的一组相互独立的应用，对其效率有重大影响。在早期设计空间探索中考量负载级并行性（WLP）因而至关重要，因为后续阶段的分析必须聚焦于有利的设计点才能得到最优结果。遗憾的是，最先进的 MultiAmdahl 与 Gables 方法存在不足，因为它们只对最小与最大 WLP 两种极端情况建模。为此我们提出 HILP，这是首个充分考虑 WLP 的异构 SoC 早期设计空间探索方法。我们的关键观察是：在异构 SoC 上调度由独立多阶段应用组成的负载，是经典作业车间调度优化问题的一个实例，因而可用整数线性规划求解。因此，HILP 使用高性能整数线性规划求解器寻找近似最优调度，以最小化负载的整体执行时间，即在遵守功耗与内存带宽约束的前提下，将负载中所有应用的相互依赖阶段调度到目标 SoC 的核心与加速器上以最大化性能。我们通过证明 HILP 能刻画 Amdahl 定律、内存墙与暗硅的性能效应来验证它，随后用它在大规模 SoC 设计空间中探索 WLP 的影响，得出多项洞察。关键的结论是：对 WLP 建模是必要的，可确保更细致的后续设计任务聚焦于异构 SoC 庞大设计空间中最为有利的部分。
