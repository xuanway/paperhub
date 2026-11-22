---
title: "VAMOs: Versatile Atomic Memory Operations for High-Performance Many-Core Architectures"
description: "MICRO 2026 · Session 7D · VAMOs：面向高性能众核架构的多功能原子内存操作"
tags:
  - "MICRO2026"
---

# VAMOs: Versatile Atomic Memory Operations for High-Performance Many-Core Architectures

**中文标题：** VAMOs：面向高性能众核架构的多功能原子内存操作

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Joaquín Ferrer, Juan M. Cebrian, Ricardo Fernández-Pascual, Alberto Ros, Manuel E. Acacio

**来源：** MICRO 2026，pp. 2654–2668；[DOI](https://doi.org/10.1109/MICRO67795.2026.00181)

## 英文摘要

Atomic Memory Operations (AMOs) constitute a key mechanism for supporting synchronization in many-core architectures. These operations can be executed near the core (i.e., when the data is at first-level private cache) or far (i.e., at the shared cache). While far AMOs can mitigate coherence bottlenecks under high contention, they are suboptimal in scenarios of low contention and substantial data reuse. Consequently, achieving near-optimal performance requires a prediction-based dynamic adaptation of the execution location of the AMO. Current approaches to dynamic AMO execution address this challenge partially, since they fail to robustly track and respond to changing execution conditions. This work makes two primary observations to improve the near-far execution decision for AMOs. First, the behavior of AMOs can be more consistently determined by using their Program Counter (PC) rather than their target memory address, as currently done in the state of the art. Second, a global, system-level perspective is necessary to effectively determine where to execute each AMO. Building on these insights, we propose Versatile Atomic Memory Operations (VAMOs), a novel dynamic AMO execution approach that (i) employs a per-core, compact, PC-indexed predictor to infer the best location to execute each AMO, (ii) uses both local and global information to update the local predictors, and (iii) bypasses the private cache levels entirely for those AMOs predicted as far. This unique combination enables efficient execution of AMOs and the ability to react rapidly to changes in the sharing patterns. Across diverse benchmarks and applications with varied AMO access and contention patterns, our simulation-based evaluation shows that VAMOs improves average performance by 21.82% and reduces storage requirements by 88.96% over the state-of-the-art DynAMO design.

## 中文摘要

原子内存操作 (AMO) 构成了支持多核架构中同步的关键机制。这些操作可以在核心附近（即，当数据位于一级私有缓存时）或远离核心（即，在共享缓存处）执行。虽然远距离 AMO 可以缓解高争用情况下的一致性瓶颈，但在低争用和大量数据重用的情况下，它们并不是最优的。因此，要实现接近最佳的性能，需要对 AMO 的执行位置进行基于预测的动态调整。当前的动态 AMO 执行方法部分解决了这一挑战，因为它们无法稳健地跟踪和响应不断变化的执行条件。这项工作提出了两个主要观察结果，以改进 AMO 的远近执行决策。首先，AMO 的行为可以通过使用其程序计数器 (PC) 而不是其目标内存地址来更一致地确定，如目前现有技术中所做的那样。其次，必须有全球性、系统级的视角，才能有效地确定在何处执行每个 AMO。基于这些见解，我们提出了通用原子内存操作 (VAMO)，这是一种新颖的动态 AMO 执行方法，该方法 (i) 采用每核、紧凑、PC 索引的预测器来推断执行每个 AMO 的最佳位置，(ii) 使用本地和全局信息来更新本地预测器，以及 (iii) 完全绕过迄今为止预测的 AMO 的私有缓存级别。这种独特的组合可实现 AMO 的高效执行，并能够对共享模式的变化做出快速反应。在具有不同 AMO 访问和争用模式的不同基准和应用程序中，我们基于模拟的评估表明，与最先进的 DynAMO 设计相比，VAMO 将平均性能提高了 21.82%，并将存储要求降低了 88.96%。

## 中文关键词

原子内存操作；微架构；内存子系统；并行架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
