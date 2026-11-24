---
title: "Unifying Qubit Routing Across Diverse Quantum ISAs via Canonical Representation"
description: "ISCA 2026 · Session 9C · Unifying Qubit Routing Across Diverse Quantum ISAs via Canonical Representation"
tags:
  - "ISCA2026"
  - "Session 9C"
  - "Quantum 3"
---

# Unifying Qubit Routing Across Diverse Quantum ISAs via Canonical Representation

**中文标题：** 通过规范表示统一跨多样量子 ISA 的量子比特路由

**所属 Session：** [Session 9C](index.md) · [ISCA 2026](../index.md)

**作者：** Zhaohui Yang, Kai Zhang, Xinyang Tian, Xiangyu Ren, Yingjian Liu, Yunfeng Li, Dawei Ding, Jianxin Chen, Yuan Xie

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Qubit mapping/routing is a critical stage in compilation for both near-term and fault-tolerant quantum computers, yet existing scalable methods typically impose several times the routing overhead in terms of circuit depth or duration. This inefficiency stems from a fundamental disconnect: compilers rely on an abstract routing model (e.g., three-CX-unrolled SWAP insertion) that completely ignores the idiosyncrasies of native gates supported by physical devices. Recent hardware breakthroughs have enabled high-precision implementations of diverse instruction set architectures (ISAs) beyond standard CX-based gates. Advanced ISAs involving gates such as √ iSWAP and ZZ(θ) gates offer superior circuit synthesis capabilities and can be realized with higher fidelities. However, systematic compiler optimization strategies tailored to these advanced ISAs are lacking. To address this, we propose CANOPUS, a unified qubit mapping/routing framework applicable to diverse quantum ISAs. Built upon the canonical representation of two-qubit gates, CANOPUS centers on qubit routing to perform deep co-optimization in an ISA-aware approach. CANOPUS leverages the two-qubit canonical representation and the monodromy polytope theory to model the synthesis cost for more intelligent SWAP insertion during qubit routing. We also formalize the commutation relations between two-qubit gates through the canonical form, providing a generalized approach to commutativity-based optimization. Experiments show that CANOPUS consistently reduces routing overhead by 15%-35% compared to state-of-the-art methods across various backend ISAs and device topologies. More broadly, this work establishes a coherent method for co-exploration of program patterns, quantum ISAs, and hardware topologies, yielding concrete guidelines for hardware-software co-design. This is the first practical demonstration of how to efficiently utilize advanced quantum ISAs, opening the door to designing more powerful and synergistic quantum systems.

## 中文摘要

量子比特映射/路由是近期和容错量子计算机编译中的关键阶段，然而现有的可扩展方法通常会在线路深度或时长方面带来数倍的路由开销。这种低效源于一个根本性的脱节：编译器依赖一种抽象的路由模型（例如三个 CX 展开的 SWAP 插入），完全忽略了物理设备所支持的原生门的特性。近期的硬件突破使得超越标准基于 CX 的门之外的各种指令集架构（ISA）得以高精度实现。涉及诸如 √iSWAP 和 ZZ(θ) 门等门的高级 ISA 提供了卓越的线路综合能力，并能够以更高的保真度实现。然而，针对这些高级 ISA 的系统性编译器优化策略仍然缺乏。为此，我们提出 CANOPUS，一个适用于各种量子 ISA 的统一量子比特映射/路由框架。CANOPUS 以两量子比特门的规范表示为基础，以量子比特路由为中心，以 ISA 感知的方式进行深度协同优化。CANOPUS 利用两量子比特规范表示和单值多面体理论来建模综合成本，从而在量子比特路由期间实现更智能的 SWAP 插入。我们还通过规范形式形式化了两量子比特门之间的对易关系，为基于对易性的优化提供了一种通用的方法。实验表明，在各种后端 ISA 和设备拓扑上，CANOPUS 相对于最先进的方法一致地将路由开销降低了 15%-35%。更广泛地说，这项工作建立了一种对程序模式、量子 ISA 和硬件拓扑进行协同探索的连贯方法，为软硬件协同设计提供了具体指导。这是如何高效利用高级量子 ISA 的首次实际演示，为设计更强大、更协同的量子系统打开了大门。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Youngcius/canopus](https://github.com/Youngcius/canopus)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2026](../index.md)
