---
title: "RTeAAL Sim: Using Tensor Algebra to Represent and Accelerate RTL Simulation"
description: "ASPLOS 2026 · Session 6B · RTeAAL Sim：使用张量代数表示并加速 RTL 仿真"
tags:
  - "ASPLOS2026"
  - "Session 6B"
  - "Hardware Design Languages"
---

# RTeAAL Sim: Using Tensor Algebra to Represent and Accelerate RTL Simulation

**中文标题：** RTeAAL Sim：使用张量代数表示并加速 RTL 仿真

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yan Zhu (University of California, Berkeley), Boru Chen (University of California, Berkeley), Christopher W. Fletcher (University of California, Berkeley), Nandeeka Nayak (University of California, Berkeley)

**单位：** University of California, Berkeley

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790214) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

RTL simulation on CPUs remains a persistent bottleneck in hardware design. State-of-the-art simulators embed the circuit directly into the simulation binary, resulting in long compilation times and execution that is fundamentally CPU frontend-bound, with severe instruction-cache pressure. This work proposes RTeAAL Sim, which reformulates RTL simulation as a sparse tensor algebra problem. By representing RTL circuits as tensors and simulation as a sparse tensor algebra kernel, RTeAAL Sim decouples simulation behavior from binary size and makes RTL simulation amenable to wellstudied tensor algebra optimizations. We demonstrate that a prototype of our tensor-based simulator, even with a subset of these optimizations, already mitigates the compilation overhead and frontend pressure and achieves performance competitive with the highly optimized Verilator simulator across multiple CPUs and ISAs.

## 中文摘要

在 CPU 上进行 RTL 仿真是硬件设计中一个长期存在的瓶颈。最先进的仿真器将电路直接嵌入仿真二进制中，导致编译时间长，并且执行在根本上受限于 CPU 前端，伴随严重的指令缓存压力。本工作提出 RTeAAL Sim，它将 RTL 仿真重新表述为稀疏张量代数问题。通过将 RTL 电路表示为张量、将仿真表示为稀疏张量代数内核，RTeAAL Sim 将仿真行为与二进制大小解耦，并使 RTL 仿真能够受益于已被充分研究的张量代数优化。我们证明，基于张量的仿真器原型即便只采用这些优化的一部分，也已经缓解了编译开销和前端压力，并在多种 CPU 和 ISA 上达到与高度优化的 Verilator 仿真器相竞争的性能。

## 英文关键词

RTL simulation; Tensor algebra

## 中文关键词

RTL 仿真；张量代数

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790214)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2026](../index.md)
