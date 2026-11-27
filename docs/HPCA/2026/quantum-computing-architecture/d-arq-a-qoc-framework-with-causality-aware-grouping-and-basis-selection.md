---
title: "d'ArQ: A QOC Framework with Causality-Aware Grouping and Basis Selection"
description: "HPCA 2026 · Quantum Computing Architecture"
tags:
  - "HPCA2026"
  - "Quantum Computing Architecture"
---

# d'ArQ: A QOC Framework with Causality-Aware Grouping and Basis Selection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Computing Architecture。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Computing Architecture</p>
</div>

**论文链接**：
**作者**：Changheon Lee Yonsei University , Hyungseok Kim Yonsei University , Seungwoo Choi Yonsei University , Youngmin Kim Yonsei University , Won Woo Ro Yonsei University
**会议**：HPCA 2026

---

## 中文标题

d'ArQ：具备因果感知分组与基选择的量子最优控制框架

## 英文摘要

Quantum Optimal Control (QOC) frameworks are powerful tools for compiling quantum circuits into low-latency hardware control pulses, but recent studies suffer from two critical limitations: lengthy compilation times and potential logical inconsistencies from flawed gate grouping strategies. In this work, we introduce d’ArQ, a novel QOC framework that solves these challenges. (i) We identify and resolve the causality problem, a flaw in greedy partitioning that can produce invalid schedules, by introducing a DAG-based grouping algorithm with assigning mergeability to each group so that it guarantees logical correctness. (ii) To mitigate compilation times, we use a pre-computed library of pulses derived from random unitary matrices to provide a high-quality random initialization for pulse optimization. (iii) Diverging from prior work based on GRAPE, d’ArQ is built on the GOAT algorithm. We demonstrate that the choice of analytic basis is a critical hyperparameter and introduce a heuristic cost model to dynamically select the optimal basis for each synthesis task, improving pulse performance. When evaluated against the state-of-the-art baseline PAQOC on a realistic, inhomogeneous hardware model, d’ArQ demonstrates superior performance. Notably, d’ArQ reduces circuit latency up to 22.8% and compilation time up to 56.8%, establishing a more robust and physically realistic path for circuit compilation.

## 中文摘要

量子最优控制（QOC）框架是将量子线路编译为低时延硬件控制脉冲的强大工具，但近期研究受两个关键局限困扰：编译时间冗长，以及有缺陷的门分组策略可能带来逻辑不一致。本文提出 d'ArQ，一个解决这些挑战的新型 QOC 框架。(i) 我们识别并解决因果性问题——贪心划分中的一种缺陷，可能产生无效调度——为此引入基于 DAG 的分组算法，为每个分组赋予可合并性，从而保证逻辑正确性。(ii) 为缓解编译时间，我们使用由随机酉矩阵导出的预计算脉冲库，为脉冲优化提供高质量的随机初始化。(iii) 与基于 GRAPE 的先前工作不同，d'ArQ 构建在 GOAT 算法之上。我们证明解析基的选择是一个关键超参数，并引入启发式代价模型为每个综合任务动态选择最优基，从而提升脉冲性能。在与最先进基线 PAQOC 于真实非均匀硬件模型上的对比中，d'ArQ 展现出更优性能：线路时延最多降低 22.8%，编译时间最多缩短 56.8%，为线路编译建立了更稳健且更符合物理实际的路径。
