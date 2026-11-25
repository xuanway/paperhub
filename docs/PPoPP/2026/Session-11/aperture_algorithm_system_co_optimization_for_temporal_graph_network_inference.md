---
title: "APERTURE: Algorithm-System Co-optimization for Temporal Graph Network Inference"
description: "PPoPP 2026 Session 11（Graphs and Graph Neural Networks）：解耦记忆更新与聚合，较 SOTA 最高加速 59.3×"
tags:
  - "PPoPP2026"
  - "Session-11"
  - "Graphs and Graph Neural Networks"
  - "Temporal Graph Networks"
  - "Inference"
  - "Graph Transformation"
authors:
  - "Yiqing Wang"
  - "Hailong Yang"
  - "Enze Yu"
  - "Qingxiao Sun"
  - "Kejie Ma"
  - "Kaige Zhang"
  - "Chenhao Xie"
  - "Depei Qian"
session: "Session 11: Graphs and Graph Neural Networks"
session_number: 11
session_chair: "Ali Jannesari"
date: "2026-02-03"
time: "16:10–16:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786450"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# APERTURE: Algorithm-System Co-optimization for Temporal Graph Network Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 APERTURE，解耦时间图网络推理中的记忆更新与聚合以释放细粒度并行，用计算图变换、依赖感知更新重建与解析建模选粒度，最高加速 59.3×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 11: Graphs and Graph Neural Networks</p>
</div>

**作者**：Yiqing Wang, Hailong Yang, Enze Yu, Qingxiao Sun, Kejie Ma, Kaige Zhang, Chenhao Xie, and Depei Qian — Beihang University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:10–16:30 · Session 11: Graphs and Graph Neural Networks（主席：Ali Jannesari）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786450) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Temporal Graph Networks (TGNs) are widely used to model evolving relationships in dynamic graphs. However, existing inference systems enforce a step-wise paradigm: processing each temporal graph sequentially with a memory update followed by aggregation. We break this dependency by decoupling memory updates from aggregation while preserving prediction accuracy, thereby enabling a global view for fine-grained parallelism control. This design unlocks new optimization opportunities but introduces three system-level challenges: managing intermediate multi-state representations, curbing memory-bound update overheads, and selecting a safe yet efficient aggregation granularity. We present APERTURE, a TGN inference framework that bridges algorithmic semantics and system design. To address the above challenges, APERTURE (1) jointly aggregates temporal states via computation graph transformation, (2) minimizes redundant memory traffic through dependency-aware update reconstruction; (3) selects the optimal granularity by analytically modeling. The experimental results show that APERTURE achieves up to 59.3× speedup over state-of-the-art baselines without compromising accuracy.

## 中文摘要

时序图网络（Temporal Graph Networks，TGN）被广泛用于建模动态图中不断演化的关系。然而，现有的推理系统强加了一种逐步（step-wise）范式：顺序处理每个时序图，先进行内存更新，再进行聚合。我们在保持预测精度的前提下，将内存更新与聚合解耦，从而打破这一依赖关系，使得以全局视角进行细粒度并行控制成为可能。该设计释放了新的优化机会，但也带来了三个系统级挑战：管理中间的多状态表示、抑制受限于内存的更新开销，以及选取既安全又高效的聚合粒度。我们提出 APERTURE，一个连接算法语义与系统设计的 TGN 推理框架。为应对上述挑战，APERTURE（1）通过计算图变换对时序状态进行联合聚合；（2）通过依赖感知的更新重构，最小化冗余内存流量；（3）通过解析建模选取最优粒度。实验结果表明，在不牺牲精度的前提下，APERTURE 相比最先进的基线最高取得 59.3× 的加速。

## 英文关键词

Temporal Graph Networks, Inference System, Parallel Execution, Memory Efficiency

## 中文关键词

时序图网络；推理系统；并行执行；内存效率

---

## 一句话总结

> 提出 APERTURE，解耦时间图网络推理中的记忆更新与聚合以释放细粒度并行，用计算图变换、依赖感知更新重建与解析建模选粒度，最高加速 59.3×。

## 研究问题

现有 TGN 推理系统采用逐步范式，按时间顺序逐图处理并先更新记忆再聚合，把计算强制串行化，限制了并行度与推理效率。

## 方法简述

- 在保持预测精度的前提下解耦记忆更新与聚合，从而获得可做细粒度并行控制的全局视图。
- 针对中间多状态表示的管理问题，通过计算图变换联合聚合时间状态。
- 通过依赖感知的更新重建减少冗余内存流量，降低访存受限的更新开销。
- 对聚合粒度进行解析建模，选择既安全又高效的聚合粒度。

## 主要结果

- 相比最先进基线最高加速 59.3×。
- 在取得该加速的同时不损失预测精度。

---

> 所属 Session：[Session 11: Graphs and Graph Neural Networks](index.md) · 返回 [PPoPP 2026 总览](../index.md)
