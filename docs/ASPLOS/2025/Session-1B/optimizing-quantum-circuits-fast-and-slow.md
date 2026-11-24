---
title: "Optimizing Quantum Circuits, Fast and Slow"
description: "ASPLOS 2025 · Session 1B · 快与慢：量子线路优化"
tags:
  - "ASPLOS2025"
  - "Session 1B"
  - "Quantum Computing"
---

# Optimizing Quantum Circuits, Fast and Slow

**中文标题：** 快与慢：量子线路优化

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Amanda Xu (University of Wisconsin-Madison), Abtin Molavi (University of Wisconsin-Madison), Swamit Tannu (University of Wisconsin-Madison), Aws Albarghouthi (University of Wisconsin-Madison)

**单位：** University of Wisconsin-Madison

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707240) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Optimizing quantum circuits is critical: the number of quantum operations needs to be minimized for a successful evaluation of a circuit on a quantum processor. In this paper we unify two disparate ideas for optimizing quantum circuits, rewrite rules, which are fast standard optimizer passes, and unitary synthesis, which is slow, requiring a search through the space of circuits. We present a clean, unifying framework for thinking of rewriting and resynthesis as abstract circuit transformations. We then present a radically simple algorithm, guoq, for optimizing quantum circuits that exploits the synergies of rewriting and resynthesis. Our extensive evaluation demonstrates the ability of guoq to strongly outperform existing optimizers on a wide range of benchmarks.

## 中文摘要

优化量子线路至关重要：要在量子处理器上成功求值一个线路，必须最小化量子操作的数量。本文统一了两种迥异的量子线路优化思路，即作为快速标准优化器遍（pass）的重写规则，以及作为慢速方法、需要在电路空间中搜索的酉合成。我们给出了一个清晰且统一的框架，将重写与再合成视为抽象的线路变换。随后，我们提出了一个极其简单的量子线路优化算法 guoq，它充分利用了重写与再合成之间的协同效应。我们的大量评估表明，guoq 在广泛的基准测试上能够显著超越现有优化器。

## 英文关键词

quantum-circuit optimization; unitary synthesis; superoptimization; quantum computing

## 中文关键词

量子线路优化；酉合成；超优化；量子计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707240)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2025](../index.md)
