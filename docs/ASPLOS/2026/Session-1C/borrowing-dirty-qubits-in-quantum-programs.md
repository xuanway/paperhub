---
title: "Borrowing Dirty Qubits in Quantum Programs"
description: "ASPLOS 2026 · Session 1C · 在量子程序中借用脏量子比特"
tags:
  - "ASPLOS2026"
  - "Session 1C"
  - "Quantum Computing: Compilation"
---

# Borrowing Dirty Qubits in Quantum Programs

**中文标题：** 在量子程序中借用脏量子比特

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Bonan Su (Department of Computer Science and Technology, Tsinghua University), Li Zhou (Institute of Software, Chinese Academy of Sciences), Yuan Feng (Tsinghua University), Mingsheng Ying (University of Technology, Sydney)

**单位：** Department of Computer Science and Technology, Tsinghua University；Institute of Software, Chinese Academy of Sciences；Tsinghua University；University of Technology, Sydney

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790134) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Dirty qubits are ancillary qubits that can be borrowed from idle parts of a computation, enabling qubit reuse and reducing the demand for fresh, clean qubits—a resource that is typically scarce in practice. For such reuse to be valid, the initial states of the dirty qubits must not affect the functionality of the quantum circuits in which they are employed. Moreover, their original states, including any entanglement they possess, must be fully restored after use—a requirement commonly known as safe uncomputation. In this paper, we formally define the semantics of dirtyqubit borrowing as a feature in quantum programming languages, and introduce a notion of safe uncomputation for dirty qubits in quantum programs. We also present an efficient algorithm, along with experimental results, for verifying safe uncomputation of dirty qubits in certain quantum circuits.

## 中文摘要

脏量子比特（dirty qubits）是可以从计算的空闲部分借用的辅助量子比特，它能够实现量子比特复用，并降低对全新、干净量子比特——这一在实践中通常稀缺的资源——的需求。要使这种复用成立，脏量子比特的初始状态不得影响使用它们的量子电路的功能。此外，它们原有的状态，包括其所具有的任何纠缠，必须在用完后被完全恢复——这一要求通常称为安全反计算（safe uncomputation）。在本文中，我们将脏量子比特借用作为量子编程语言中的一项特性，对其语义进行形式化定义，并提出量子程序中脏量子比特的安全反计算概念。我们还提出了一种高效算法及实验结果，用于验证某些量子电路中脏量子比特的安全反计算。

## 英文关键词

dirty qubits; quantum programming; safe uncomputation; formal verification; SAT solving

## 中文关键词

脏量子比特；量子编程；安全反计算；形式化验证；SAT 求解

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790134)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2026](../index.md)
