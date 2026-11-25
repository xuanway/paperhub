---
title: "CARBS: Compiler Autotuning via Randomized Biased Search"
description: "HPDC 2026 · Session 4 — Programming Models, Frameworks & Compilers"
tags:
  - "HPDC2026"
  - "Session 4"
  - "Programming Models, Frameworks & Compilers"
---

# CARBS: Compiler Autotuning via Randomized Biased Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 4</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807592)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#LiGW26](https://dblp.org/db/conf/hpdc/hpdc2026.html#LiGW26)

**作者**：Wei Li, Bin Gao, Weng-Fai Wong

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）

---

## 英文摘要

Performance tuning is a persistent challenge in high-performance computing (HPC), where large codebases, architectural diversity, and limited evaluation budgets make manual optimization impractical. Modern compilers expose hundreds of optimization flags, yielding an enormous configuration space that existing autotuners explore inefficiently, often requiring thousands of costly trials. To address the problem, this paper proposes CARBS, a probability-guided autotuning algorithm that iteratively refines the probability of enabling each flag based on performance feedback, significantly reducing the search cost. Our empirical analysis reveals three exploitable properties of the optimization space: simple randomized strategies can already match sophisticated methods, only a small subset of flags are performance-critical for a given program, and optimization landscapes vary dramatically across programs. Building on these findings, CARBS generates candidate configurations via lightweight probability-guided sampling. To identify the critical flags, CARBS employs an adaptive update that attributes performance differences to differential flags, promoting beneficial optimizations while suppressing harmful ones. To ensure robust convergence across diverse programs and noisy measurements, CARBS incorporates a momentum-based historical update that dampens measurement noise and prevents premature convergence. Extensive experimental results on 133 benchmarks totaling nearly 5M lines of C/C++ code demonstrate that CARBS achieves an average speedup of 18.7% over -O3 on traditional benchmarks and 10% on SPECspeed CPU 2017 workloads, outperforms all 12 state-of-the-art baselines, and reduces search cost by 3×.

## 中文摘要

在高性能计算（HPC）中，性能调优是一个长期挑战：庞大的代码库、架构多样性和有限的评估预算使手工优化不切实际。现代编译器暴露数百个优化标志，形成巨大的配置空间，现有自动调优器探索效率低下，往往需要数千次昂贵的试验。为解决该问题，本文提出 CARBS，一种概率引导的自动调优算法，它根据性能反馈迭代地修正启用每个标志的概率，显著降低搜索成本。我们的实证分析揭示了优化空间的三个可利用特性：简单的随机策略已能匹敌复杂方法；对给定程序而言只有一小部分标志对性能关键；优化景观在不同程序间差异巨大。基于这些发现，CARBS 通过轻量级概率引导采样生成候选配置。为识别关键标志，CARBS 采用自适应更新，将性能差异归因于差异标志，促进有益优化、抑制有害优化。为确保在多样程序和噪声测量下稳健收敛，CARBS 引入基于动量的历史更新，抑制测量噪声并防止过早收敛。在总计近 500 万行 C/C++ 代码的 133 个基准上的大量实验表明，CARBS 在传统基准上相比 -O3 平均加速 18.7%，在 SPECspeed CPU 2017 负载上加速 10%，优于全部 12 个最先进基线，并将搜索成本降低 3 倍。

## 英文关键词

Auto-tuning, Compiler, Optimization

## 中文关键词

自动调优，编译器，优化

---

[← 返回 Session 4 — Programming Models, Frameworks & Compilers](index.md)
