---
title: "TreeVQA: A Tree-Structured Execution Framework for Shot Reduction in Variational Quantum Algorithms"
description: "ASPLOS 2026 · Session 9B · TreeVQA：一种用于减少变分量子算法采样次数的树状执行框架"
tags:
  - "ASPLOS2026"
  - "Session 9B"
  - "Quantum & Emerging Computing"
---

# TreeVQA: A Tree-Structured Execution Framework for Shot Reduction in Variational Quantum Algorithms

**中文标题：** TreeVQA：一种用于减少变分量子算法采样次数的树状执行框架

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yuewen Hou (University of Michigan), Dhanvi Bharadwaj (University of Michigan), Gokul Ravi (University of Michigan)

**单位：** University of Michigan

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790239) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Variational Quantum Algorithms (VQAs) are promising for near- and intermediate-term quantum computing, but their execution cost is substantial. Each task requires many iterations and numerous circuits per iteration, and real-world applications often involve multiple tasks, scaling with the precision needed to explore the application's energy landscape. This demands an enormous number of execution shots, making practical use prohibitively expensive. We observe that VQA costs can be significantly reduced by exploiting execution similarities across an application's tasks. Based on this insight, we propose TreeVQA, a treebased execution framework that begins by executing tasks jointly and progressively branches only as their quantum executions diverge. Implemented as a VQA wrapper, TreeVQA integrates with typical VQA applications. Evaluations on scientific and combinatorial benchmarks show shot count reductions of 25.9× on average and over 100× for large-scale problems at the same target accuracy. The benefits grow further with increasing problem size and precision requirements.

## 中文摘要

变分量子算法（VQA）在近期与中期量子计算中颇具前景，但其执行成本很高。每个任务都需要多次迭代，且每次迭代需要大量电路，而真实应用往往涉及多个任务，并随探索应用能量景观所需精度的提高而扩展。这要求极其庞大的执行采样次数，使实际应用成本高得难以承受。我们观察到，通过利用一个应用中各任务之间的执行相似性，可以显著降低 VQA 成本。基于这一洞见，我们提出 TreeVQA，一种基于树的执行框架，它首先联合执行各任务，并仅在各任务的量子执行出现分歧时逐步分支。TreeVQA 以 VQA 封装器的形式实现，可与典型的 VQA 应用集成。在科学与组合优化基准上的评估显示，在相同目标精度下，采样次数平均减少 25.9×，对于大规模问题超过 100×。随着问题规模和精度要求的提高，收益进一步增大。

## 英文关键词

Quantum Computing, Variational Quantum Algorithms, Quantum Resource Optimization

## 中文关键词

量子计算；变分量子算法；量子资源优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790239)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2026](../index.md)
