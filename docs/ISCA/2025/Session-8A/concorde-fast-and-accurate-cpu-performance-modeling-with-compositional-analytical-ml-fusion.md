---
title: "Concorde: Fast and Accurate CPU Performance Modeling with Compositional Analytical-ML Fusion"
description: "ISCA 2025 · Session 8A · Concorde：基于组合式分析—机器学习融合的快速精准 CPU 性能建模"
tags:
  - "ISCA2025"
  - "Session 8A"
  - "Performance and Modeling"
---

# Concorde: Fast and Accurate CPU Performance Modeling with Compositional Analytical-ML Fusion

**中文标题：** Concorde：基于组合式分析—机器学习融合的快速精准 CPU 性能建模

**所属 Session：** [Session 8A](index.md) · [ISCA 2025](../index.md)

**作者：** Arash Nasr-Esfahany, Mohammad Alizadeh, Victor Lee, Hanna Alam, Brett W. Coon, David Culler, Vidushi Dadu, Martin Dixon, Henry M. Levy, Santosh Pandey, Parthasarathy Ranganathan, Amir Yazdanbakhsh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731037) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Cycle-level simulators such as gem5 are widely used in microarchi- tecture design, but they are prohibitively slow for large-scale design space explorations. We present Concorde, a new methodology for learning fast and accurate performance models of microarchitectures. Unlike existing simulators and learning approaches that emulate each instruction, Concorde predicts the behavior of a program based on compact performance distributions that capture the impact of dif- ferent microarchitectural components. It derives these performance distributions using simple analytical models that estimate bounds on performance induced by each microarchitectural component, pro- viding a simple yet rich representation of a program’s performance characteristics across a large space of microarchitectural parameters. Experiments show that Concorde is more than five orders of mag- nitude faster than a reference cycle-level simulator, with about 2% average Cycles-Per-Instruction (CPI) prediction error across a range of SPEC, open-source, and proprietary benchmarks. This enables rapid design-space exploration and performance sensitivity analyses that are currently infeasible, e.g., in about an hour, we conducted a first-of-its-kind fine-grained performance attribution to different microarchitectural components across a diverse set of programs, requiring nearly 150 million CPI evaluations.

## 中文摘要

gem5这类周期级仿真器广泛用于微架构设计，但在大规模设计空间探索时速度极慢。本文提出Concorde，一种用于学习快速、精准微架构性能模型的新方法。
现有仿真器与学习方法需要逐条模拟指令；与之不同，Concorde依托紧凑的性能分布来预测程序行为，该分布刻画了各个微架构组件带来的影响。它借助简单解析模型得到这些性能分布，估算每个微架构组件带来的性能上下界，从而用简洁且信息丰富的方式，表征程序在大范围微架构参数下的性能特征。

实验表明：Concorde比基准周期级仿真器快五个数量级以上，在SPEC、开源以及私有测试集上，每指令周期数（CPI）平均预测误差约2%。这使得原本难以实现的快速设计空间探索与性能敏感度分析成为可能。例如，我们在约一小时内完成了首例细粒度性能归因实验，针对多款不同程序，量化各个微架构组件的贡献，该实验需要近1.5亿次CPI评估。

## 英文关键词

CPU performance modeling, microarchitectural bottleneck analysis, analytical–ML fusion, design space exploration, performance attribu- tion, Shapley value analysis, machine learning for microarchitecture

## 中文关键词

CPU性能建模, 微架构瓶颈分析, 解析模型-机器学习融合, 设计空间探索, 性能归因, Shapley 值分析, 微架构机器学习

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731037)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2025](../index.md)
