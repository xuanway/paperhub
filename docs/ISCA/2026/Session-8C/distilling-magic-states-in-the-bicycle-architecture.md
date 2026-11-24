---
title: "Distilling Magic States in the Bicycle Architecture"
description: "ISCA 2026 · Session 8C · Distilling Magic States in the Bicycle Architecture"
tags:
  - "ISCA2026"
  - "Session 8C"
  - "Quantum 2"
---

# Distilling Magic States in the Bicycle Architecture

**中文标题：** Bicycle 架构中的魔法态蒸馏

**所属 Session：** [Session 8C](index.md) · [ISCA 2026](../index.md)

**作者：** Shifan Xu, Kun Liu, Patrick Rall, Zhiyang He, Yongshan Ding

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Magic State Distillation is considered to be one of the promising methods for supplying the non-Clifford resources required to achieve universal fault tolerance. Conventional MSD protocols implemented in surface codes often require multiple code blocks and lattice surgery rounds, resulting in substantial qubit overhead, especially at low target error rates. In this work, we present practical magic state distillation factories on Bivariate Bicycle (BB) codes that execute Pauli-measurement-based Clifford circuits inside a single BB code block. We formulate distillation circuit design as a joint optimization of logical qubit mapping, gate scheduling, measurement nativization, and protocol compression via qubit recycling. Based on detailed resource analysis and simulations, our BB factories have space-time volume comparable to that of leading distillation factories while delivering lower target error at a smaller qubit footprint, and are particularly compelling as second-round distillers following magic state cultivations.

## 中文摘要

魔法态蒸馏（Magic State Distillation, MSD）被认为是为实现通用容错计算提供所需非 Clifford 资源的有前景方法之一。在表面码中实现的传统 MSD 协议通常需要多个码块与多次格点手术轮次，导致大量量子比特开销，尤其在目标错误率较低时更为突出。在本工作中，我们提出基于双变量自行车（Bivariate Bicycle, BB）码的实用魔法态蒸馏工厂，它在单个 BB 码块内执行基于 Pauli 测量的 Clifford 电路。我们将蒸馏电路设计表述为逻辑量子比特映射、门调度、测量原生化以及通过量子比特回收进行协议压缩的联合优化。基于详细的资源分析与模拟，我们的 BB 工厂具有与领先蒸馏工厂相当的时空体积，同时在更小的量子比特占用下实现更低的目标错误率，并且作为魔法态培养之后的第二轮蒸馏器尤其具有吸引力。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：kunliu7/bb-code-magic-state-distillation](https://github.com/kunliu7/bb-code-magic-state-distillation)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2026](../index.md)
