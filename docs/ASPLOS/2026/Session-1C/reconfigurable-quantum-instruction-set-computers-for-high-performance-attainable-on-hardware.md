---
title: "Reconfigurable Quantum Instruction Set Computers for High Performance Attainable on Hardware"
description: "ASPLOS 2026 · Session 1C · 面向硬件上可达成高性能的可重构量子指令集计算机"
tags:
  - "ASPLOS2026"
  - "Session 1C"
  - "Quantum Computing: Compilation"
---

# Reconfigurable Quantum Instruction Set Computers for High Performance Attainable on Hardware

**中文标题：** 面向硬件上可达成高性能的可重构量子指令集计算机

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhaohui Yang (The Hong Kong University of Science and Technology), Dawei Ding (Tsinghua University), Qi Ye (Tsinghua University), Cupjin Huang (Alibaba Group USA), Jianxin Chen (Tsinghua University), Yuan Xie (The Hong Kong University of Science and Technology)

**单位：** The Hong Kong University of Science and Technology；Tsinghua University；Alibaba Group USA

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790208) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Despite remarkable milestones in quantum computing, the performance of current quantum hardware remains limited. One critical path to higher performance is to expand the quantum ISA with basis gates that have higher fidelity and greater synthesis capabilities than the standard CNOT. However, this substantially increases gate calibration overhead and introduces challenges in compiler optimization. Consequently, although more expressive ISAs (even complex, continuous gate sets) have been proposed, they still remain primarily proofs-of-concept and have not been widely adopted. To move beyond these hurdles and unlock the performance gains offered by expressive continuous ISAs, we introduce the concept of “reconfigurable quantum instruction set computers” (ReQISC). It incorporates (1) a unified microarchitecture capable of directly implementing arbitrary 2Q gates equivalently, i.e., SU(4) modulo 1Q rotations, with theoretically optimal gate durations given any 2Q coupling Hamiltonian and (2) a compilation framework tailored to ReQISC primitives for end-to-end synthesis and optimization, comprising a program-aware pass that refines high-level representations, a program-agnostic pass for aggressive circuit-level optimization, and an SU(4)-aware routing pass that minimizes hardware mapping overhead. We detail the hardware implementation to demonstrate the feasibility of this superior gate scheme in terms of both pulse control and calibration. By leveraging the expressivity of SU(4) and the time minimality realized by the underlying microarchitecture, the SU(4)-based ISA achieves remarkable performance, with a 4.97-fold reduction in average pulse duration to implement arbitrary 2Q gates, compared to the usual CNOT/CZ scheme on mainstream flux-tunable transmons. Supported by the end-to-end compiler, ReQISC outperforms the conventional CNOT-based ISA, state-of-the-art compiler, and pulse implementation counterparts by significantly reducing 2Q gate count, circuit depth, pulse duration, qubit mapping overhead, and program fidelity losses. For the first time, ReQISC makes the theoretical benefits of continuous ISAs practically feasible.

## 中文摘要

尽管量子计算已取得显著里程碑，当前量子硬件的性能仍然受限。通向更高性能的一条关键路径是扩展量子 ISA，加入比标准 CNOT 具有更高保真度和更强综合能力的基础门。然而，这大幅增加了门校准开销，并在编译器优化中引入挑战。因此，尽管人们已提出表达能力更强的 ISA（甚至复杂、连续的门集合），它们仍主要停留在概念验证阶段，尚未被广泛采用。为跨越这些障碍并释放富有表现力的连续 ISA 所带来的性能收益，我们引入“可重构量子指令集计算机”（ReQISC）的概念。它包含（1）一个统一的微架构，能够等价地直接实现任意 2Q 门，即在模 1Q 旋转意义下的 SU(4)，并在给定任意 2Q 耦合哈密顿量时具有理论最优的门持续时间；（2）一个面向 ReQISC 原语的编译框架，用于端到端综合与优化，包括一个细化高层表示的程序感知 pass、一个用于激进电路级优化的程序无关 pass，以及一个最小化硬件映射开销的 SU(4) 感知路由 pass。我们详述了硬件实现，以从脉冲控制与校准两方面证明这一优越门方案的可行性。借助 SU(4) 的表达能力以及底层微架构所实现的时间最小性，基于 SU(4) 的 ISA 取得了显著性能：在主流磁通可调 transmon 上，与通常的 CNOT/CZ 方案相比，实现任意 2Q 门的平均脉冲持续时间缩短了 4.97 倍。在端到端编译器的支持下，ReQISC 通过显著降低 2Q 门数量、电路深度、脉冲持续时间、量子比特映射开销和程序保真度损失，超越了传统基于 CNOT 的 ISA、最先进的编译器以及脉冲实现的对标方案。ReQISC 首次使连续 ISA 的理论优势在实践上变得可行。

## 英文关键词

Quantum Computing, Quantum Control, Quantum Compilation, Instruction Set Architecture, Microarchitecture, Compiler, Co-Design

## 中文关键词

量子计算；量子控制；量子编译；指令集架构；微架构；编译器；协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790208)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2026](../index.md)
