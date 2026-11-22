---
title: "Catalyst-Length Instruction Fusion Prediction"
description: "MICRO 2026 · Session 3A · Catalyst-Length 指令融合预测"
tags:
  - "MICRO2026"
---

# Catalyst-Length Instruction Fusion Prediction

**中文标题：** Catalyst-Length 指令融合预测

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Sebastian S. Kim, Sawan Singh, Alberto Ros

**来源：** MICRO 2026，pp. 975–988；[DOI](https://doi.org/10.1109/MICRO67795.2026.00078)

## 英文摘要

Instruction fusion is a microarchitectural technique that increases processor efficiency by treating multiple dependent instructions as a single internal operation. In commercial processors, existing fusion support is limited to short, consecutive memory instruction sequences, leaving longer-range fusion opportunities unexploited. In academia, Helios has overcome this limitation by enabling fusion of non-consecutive instructions. This work reveals that Helios relies on complex microarchitectural decisions, with its large tournament predictor falling far short of optimality, and models a more practical fusion architecture. Then, it proposes Catalyst-Length Instruction Fusion prediction (CLIF) for non-consecutive fusion. CLIF implements a lightweight yet accurate predictor that identifies non-consecutive memory instructions likely to benefit from a fused execution. The predictor uses multiple history lengths to discover fusible pairs of instructions but, different from branch predictors, it always trains a given fusible pair using the same context: the branch history comprehended between the two fused instructions. Our simulation results show that, compared to Helios, CLIF obtains average speedups of 2.05% and 3.16% on the SPEC CPU 2017 and MiBench benchmark suites, respectively, while reducing MPKI by 95.31% with less than half of Helios' budget.

## 中文摘要

指令融合是一种微体系结构技术，通过将多个相关指令视为单个内部操作来提高处理器效率。在商用处理器中，现有的融合支持仅限于短的连续内存指令序列，而无法利用更远距离的融合机会。在学术界，Helios 通过融合非连续指令克服了这一限制。这项工作揭示了 Helios 依赖于复杂的微架构决策，其大型锦标赛预测器远远达不到最优性，并模拟了更实用的融合架构。然后，它提出了用于非连续融合的催化剂长度指令融合预测（CLIF）。 CLIF 实现了一个轻量级但准确的预测器，可以识别可能受益于融合执行的非连续内存指令。预测器使用多个历史长度来发现可融合指令对，但与分支预测器不同，它始终使用相同的上下文来训练给定的可融合指令对：两个融合指令之间理解的分支历史记录。我们的仿真结果表明，与 Helios 相比，CLIF 在 SPEC CPU 2017 和 MiBench 基准套件上分别获得了 2.05% 和 3.16% 的平均加速，同时将 MPKI 降低了 95.31%，而预算不到 Helios 的一半。

## 中文关键词

指令融合；硬件预测器；微架构；指令级并行性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
