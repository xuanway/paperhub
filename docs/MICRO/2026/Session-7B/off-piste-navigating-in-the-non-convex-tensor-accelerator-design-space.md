---
title: "Off-Piste: Navigating in the Non-Convex Tensor Accelerator Design Space"
description: "MICRO 2026 · Session 7B · Off-Piste：探索非凸张量加速器设计空间"
tags:
  - "MICRO2026"
---

# Off-Piste: Navigating in the Non-Convex Tensor Accelerator Design Space

**中文标题：** Off-Piste：探索非凸张量加速器设计空间

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Zhongdi Luo, Dong Chen, Yang Shi

**来源：** MICRO 2026，pp. 2423–2437；[DOI](https://doi.org/10.1109/MICRO67795.2026.00166)

## 英文摘要

Joint hardware-software design space exploration (DSE) for tensor accelerators is fundamentally bottlenecked by the space's extreme non-convexity. Standard black-box optimizations fail by probabilistically guessing deterministic architectural constraints, wasting evaluation budgets on infeasible designs and stalling at local optima. In typical deep neural network (DNN) workloads, 46% of configurations exhibit abrupt >2× performance cliffs, rendering existing unguided search methods highly inefficient and prone to convergence failures on large-scale workloads. In this paper, we present Off-Piste, a single-loop DSE framework that exploits a fundamental architectural asymmetry: while performance objectives are complex black boxes, physical hardware boundaries (e.g., SRAM capacities and array dimensions) are deterministic white-box tensor algebra. Off-Piste transforms blind search into directed architectural navigation through three mechanisms: (1) analytical feasibility projection that deterministically repairs constraint-violating configurations without evaluating them; (2) architecture-aware feature augmentation that linearizes implicit performance cliffs (e.g., capacity saturation) for surrogate models; and (3) analytical soft-feasibility multipliers that eliminate the artificial suppression of high-utilization boundary points inherent in standard Bayesian approaches. Evaluated across 12 representative DNN workloads, Off-Piste achieves strong sample efficiency and competitive EDP. On massive Transformer workloads where standard probabilistic baselines suffer near-zero feasibility, Off-Piste uniquely sustains a 70% valid exploration rate. Our work demonstrates that exposing structural hardware constraints directly to the surrogate model is essential for efficiently navigating accelerator design spaces and discovering high-quality, EDP-efficient designs.

## 中文摘要

张量加速器的联合硬件-软件设计空间探索（DSE）从根本上受到空间的极端非凸性的瓶颈。标准黑盒优化会因概率猜测确定性架构约束、在不可行的设计上浪费评估预算以及停滞在局部最优而失败。在典型的深度神经网络 (DNN) 工作负载中，46% 的配置表现出突然的 >2 倍性能悬崖，使得现有的无引导搜索方法效率极低，并且在大规模工作负载上容易出现收敛失败。在本文中，我们提出了 Off-Piste，这是一种单环 DSE 框架，它利用了基本的架构不对称性：虽然性能目标是复杂的黑匣子，但物理硬件边界（例如 SRAM 容量和阵列维度）是确定性的白盒张量代数。 Off-Piste 通过三种机制将盲目搜索转变为定向建筑导航：（1）分析可行性预测，确定性地修复违反约束的配置而不对其进行评估； (2) 架构感知的特征增强，使代理模型的隐式性能悬崖（例如容量饱和）线性化； (3) 分析软可行性乘数，消除标准贝叶斯方法中固有的高利用率边界点的人为抑制。经过 12 个代表性 DNN 工作负载的评估，Off-Piste 实现了强大的样本效率和具有竞争力的 EDP。在标准概率基线的可行性接近于零的大量 Transformer 工作负载上，Off-Piste 独特地维持了 70% 的有效探索率。我们的工作表明，直接向替代模型暴露结构硬件约束对于有效导航加速器设计空间和发现高质量、EDP 高效的设计至关重要。

## 中文关键词

张量加速器；设计空间探索；代理建模；非凸优化

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/abnerhexu/micro2026ae-off-piste](https://github.com/abnerhexu/micro2026ae-off-piste)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21482136](https://doi.org/10.5281/zenodo.21482136)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
