---
title: "Leveraging Phase Polynomials for Quantum Circuit Optimization"
description: "ISCA 2026 · Session 8C · Leveraging Phase Polynomials for Quantum Circuit Optimization"
tags:
  - "ISCA2026"
  - "Session 8C"
  - "Quantum 2"
---

# Leveraging Phase Polynomials for Quantum Circuit Optimization

**中文标题：** 利用相位多项式优化量子电路

**所属 Session：** [Session 8C](index.md) · [ISCA 2026](../index.md)

**作者：** Zihan Chen, Mingkuan Xu, Henry Chen, Vannessa Chan, Yuwei Jin, Won Woo Ro, Enhyeok Jang, Eddy Z. Zhang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Quantum circuits on resource-limited hardware require optimizing regions dominated by {CNOT, Rz}, which account for a large fraction of operations and often dominate execution cost. This optimization can be challenging because phase-polynomial blocks are fragmented by basis-changing gates such as H, and optimizing phase parities alone may increase the cost of downstream basis transformations. Existing phase-polynomial approaches are limited to single-block or phase-only optimization, while subcircuit rewriting approaches are local and scale poorly beyond small rewrite windows. We introduce PhasePoly, a compiler optimization pass that jointly optimizes phase-parity and output-parity networks and employs a cross-block intermediate representation to reuse parities across phase-polynomial block barriers. This approach is effective because its unified parity-matrix representation exposes long-range {CNOT, Rz} structure that local rewriting and single-block methods cannot capture. PhasePoly reduces total gate count by up to 50.00% (34.70% on average) and CNOT count by up to 48.57% (26.83% on average), while scaling to large circuits and improving both fault-tolerant compilation and near-term hardware execution. PhasePoly is available at https://github.com/ruadapt/PhasePoly.

## 中文摘要

资源受限硬件上的量子电路需要优化以 {CNOT, Rz} 为主的区域，这些操作占很大的比例，并常常主导执行成本。这一优化颇具挑战，因为相位多项式块会被 H 等基变换门割裂，而仅优化相位奇偶性可能会增加下游基变换的成本。现有相位多项式方法局限于单块或仅相位优化，而子电路重写方法则是局部的，难以扩展到小重写窗口之外。我们提出 PhasePoly，一种编译器优化 pass，它联合优化相位奇偶性网络与输出奇偶性网络，并采用跨块中间表示，以跨越相位多项式块之间的屏障复用奇偶性。该方法之所以有效，是因为其统一的奇偶性矩阵表示能够揭示局部重写与单块方法无法捕捉的长程 {CNOT, Rz} 结构。PhasePoly 将总门数最多减少 50.00%（平均 34.70%），将 CNOT 数最多减少 48.57%（平均 26.83%），同时可扩展到大型电路，并同时改善容错编译与近期硬件执行。PhasePoly 已在 https://github.com/ruadapt/PhasePoly 提供。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：ruadapt/PhasePoly](https://github.com/ruadapt/PhasePoly)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2026](../index.md)
