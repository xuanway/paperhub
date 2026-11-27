---
title: "MASCOT: Predicting Memory Dependencies and Opportunities for Speculative Memory Bypassing"
description: "HPCA 2025 · Speculating in Vegas"
tags:
  - "HPCA2025"
  - "Speculating in Vegas"
---

# MASCOT: Predicting Memory Dependencies and Opportunities for Speculative Memory Bypassing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Speculating in Vegas。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Speculating in Vegas</p>
</div>

**论文链接**：
**作者**：Karl H. Mose (University of Cambridge), Sebastian S. Kim (University of Murcia), Alberto Ros (University of Murcia), Timothy M. Jones (University of Cambridge), Robert Mullins (University of Cambridge)
**会议**：HPCA 2025

---

## 中文标题

MASCOT：预测内存依赖与推测内存旁路的机会

## 英文摘要

Memory-dependence prediction (MDP) increases instruction-level parallelism (ILP) by allowing load instructions to be issued even when addresses in the store queue are unknown. The predictor determines whether a load will alias with a prior store, delaying issue when a dependence is predicted. Speculative memory bypassing (SMB) further enhances ILP by short-circuiting a predicted dependence to forward the value written by a store to a load that is predicted to depend on it, without their addresses necessarily being known. This breaks data dependencies on the load and store addresses, allowing loads to obtain their values much earlier than they normally would. To obtain benefits, dependencies must be predicted with high accuracy. Furthermore, the benefits are skewed, with false negatives being more costly for performance than false positives for MDP, since the former requires squashing when the misprediction is identified, whereas the latter only delays the issue of independent loads. For SMB, on the other hand, false positives are very costly, as they require squashing, whereas false negatives have little impact in the presence of an accurate memory dependence predictor. Due to these differing requirements, the designs of predictors for these mechanisms have diverged. In this paper, we propose MASCOT, a novel predictor capable of performing both MDP and SMB. MASCOT is inspired by the TAGE predictor, widely used in branch prediction. Although TAGE has proven effective as a universal predictor structure, we demonstrate how prior TAGE-based MDP or SMB predictors suffer from inaccuracy due to not learning patterns of nondependence. By learning the context for dependencies as well as non-dependencies, MASCOT achieves sufficiently low false negatives and false positives to perform MDP and SMB, while at the same time uses less space than existing designs that only perform MDP or SMB. Our simulation results show that for SPEC CPU 2017, MASCOT used for MDP alone yields an IPC gain of 0.4 % over the previous state-of-the-art predictor, on average, at the same size. When used for both MDP and SMB, it yields an increase in IPC of 1.9 % on average, with peak gains of 26 %. A compacted version of MASCOT, MASCOT-OPT, achieves similar numbers within 0.1 % while using just 10.1 KiB of space.

## 中文摘要

内存依赖预测（MDP）允许在存储队列地址未知时发射加载，从而提升指令级并行（ILP）：预测器判断加载是否与先前存储别名，若预测有依赖则延迟发射。推测内存旁路（SMB）进一步把预测到的依赖短路，将存储写入的值转发给预测依赖它的加载，二者地址无需已知，由此打破地址上的数据依赖，使加载远早于常规获得数值。要获益必须高准确率预测依赖，且代价不对称：对 MDP，漏报比误报更伤性能，因为漏报在发现预测错误时要冲刷，而误报只延迟独立加载的发射；对 SMB 相反，误报代价很高需要冲刷，在有准确预测器时漏报影响很小。由于需求不同，两类机制的预测器设计已分化。本文提出 MASCOT，能同时完成 MDP 与 SMB，灵感来自分支预测中广泛使用的 TAGE。尽管 TAGE 是通用预测器结构，我们表明基于 TAGE 的 MDP 或 SMB 预测器因未学习非依赖模式而不准确。通过学习依赖与非依赖的上下文，MASCOT 的漏报与误报都足够低，且比仅做 MDP 或 SMB 的现有设计占用更少空间。仿真显示，在 SPEC CPU 2017 上，同等容量时仅用于 MDP 平均提升 0.4% 的 IPC；同时用于两者时平均提升 1.9%，峰值 26%。精简版 MASCOT-OPT 仅占 10.1 KiB，差距在 0.1% 以内。
