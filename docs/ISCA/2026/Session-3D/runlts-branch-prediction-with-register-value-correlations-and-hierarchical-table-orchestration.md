---
title: "RUNLTS: Branch Prediction with Register-Value Correlations and Hierarchical Table Orchestration"
description: "ISCA 2026 · Session 3D · RUNLTS: Branch Prediction with Register-Value Correlations and Hierarchical Table Orchestration"
tags:
  - "ISCA2026"
  - "Session 3D"
  - "Microarchitexture"
---

# RUNLTS: Branch Prediction with Register-Value Correlations and Hierarchical Table Orchestration

**中文标题：** RUNLTS: 利用寄存器值相关性与分层表编排的分支预测

**所属 Session：** [Session 3D](index.md) · [ISCA 2026](../index.md)

**作者：** Toru Koizumi, Toshiki Maekawa, Masanari Mizuno, Maru Kuroki, Tomoaki Tsumura, Ryota Shioya

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The TAgged GEometric history length predictor (TAGE) and its derivatives are widely regarded as among the most accurate branch predictors. In particular, the TAGE-SC predictor, which combines TAGE with a statistical corrector (SC), achieves state-of-the-art prediction accuracy. In this paper, we propose RUNLTS, a novel branch predictor that augments TAGE-SC with structural refinements and a novel value-correlation-based component, RBias. On the structural side, RUNLTS redesigns the allocation policy, reshapes the history length set, and reorganizes the statistical corrector. RBias is a novel prediction mechanism that directly learns correlations between branch outcomes and register values without explicitly tracking data-dependence chains. It exploits a broad range of value–branch correlations that conventional predictors fail to capture. Our simulation results showed that the RUNLTS predictor significantly outperforms the baseline TAGE-SC in prediction accuracy.

## 中文摘要

带标记的几何历史长度预测器（TAgged GEometric history length predictor, TAGE）及其衍生方案被广泛认为是准确率最高的分支预测器之一。特别是将 TAGE 与统计校正器（statistical corrector, SC）相结合的 TAGE-SC 预测器，实现了最先进的预测准确率。在本文中，我们提出 RUNLTS，一种新颖的分支预测器，它在 TAGE-SC 的基础上加入了结构改进和一个基于值相关性的新组件 RBias。在结构方面，RUNLTS 重新设计了分配策略、重塑了历史长度集合，并重组了统计校正器。RBias 是一种新颖的预测机制，它直接学习分支结果与寄存器值之间的相关性，而无需显式跟踪数据依赖链。它利用了传统预测器无法捕捉的广泛的“值—分支”相关性。我们的仿真结果表明，RUNLTS 预测器在预测准确率上显著优于基线 TAGE-SC。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3D](index.md) · [返回 ISCA 2026](../index.md)
