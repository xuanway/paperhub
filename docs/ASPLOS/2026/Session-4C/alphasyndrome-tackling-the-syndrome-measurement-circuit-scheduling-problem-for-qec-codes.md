---
title: "AlphaSyndrome: Tackling the Syndrome Measurement Circuit Scheduling Problem for QEC Codes"
description: "ASPLOS 2026 · Session 4C · AlphaSyndrome：应对 QEC 码的校验子测量电路调度问题"
tags:
  - "ASPLOS2026"
  - "Session 4C"
  - "Quantum Error Correction"
---

# AlphaSyndrome: Tackling the Syndrome Measurement Circuit Scheduling Problem for QEC Codes

**中文标题：** AlphaSyndrome：应对 QEC 码的校验子测量电路调度问题

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yuhao Liu (University of Pennsylvania), Shuohao Ping (University of Pennsylvania), Junyu Zhou (University of Pennsylvania), Ethan Decker (University of Pennsylvania), Justin Kalloor (University of California, Berkeley), Mathias Weiden (University of California, Berkeley), Kean Chen (University of Pennsylvania), Yunong Shi (Amazon Quantum Technologies), Ali Javadi-Abhari (IBM Research), Costin Iancu (Lawrence Berkeley National Laboratory), Gushu Li (University of Pennsylvania)

**单位：** University of Pennsylvania；University of California, Berkeley；Amazon Quantum Technologies；IBM Research；Lawrence Berkeley National Laboratory

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790123) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Quantum error correction (QEC) is essential for scalable quantum computing, yet repeated syndrome-measurement cycles dominate its spacetime and hardware cost. Although stabilizers commute and admit many valid execution orders, different schedules induce distinct error-propagation paths under realistic noise, leading to large variations in logical error rate. Outside of surface codes, effective syndrome-measurement scheduling remains largely unexplored. We present AlphaSyndrome, an automated synthesis framework for scheduling syndrome-measurement circuits in general commuting-stabilizer codes under minimal assumptions: mutually commuting stabilizers and a heuristic decoder. AlphaSyndrome formulates scheduling as an optimization problem that shapes error propagation to (i) avoid patterns close to logical operators and (ii) remain within the decoder's correctable region. The framework uses Monte Carlo Tree Search (MCTS) to explore ordering and parallelism, guided by code structure and decoder feedback. Across diverse code families, sizes, and decoders, AlphaSyndrome reduces logical error rates by 80.6% on average (up to 96.2%) relative to depth-optimal baselines, matches Google's hand-crafted surface-code schedules, and outperforms IBM's schedule for the Bivariate Bicycle code.

## 中文摘要

量子纠错（QEC）对于可扩展量子计算至关重要，然而反复进行的校验子测量周期主导了其时空开销与硬件成本。尽管稳定子彼此对易并允许许多合法的执行顺序，但在真实噪声下，不同的调度会引发不同的错误传播路径，从而导致逻辑错误率出现很大差异。在表面码之外，有效的校验子测量调度在很大程度上仍未被探索。我们提出 AlphaSyndrome，一个在最小假设下（相互对易的稳定子以及一个启发式解码器）为通用对易稳定子码调度校验子测量电路的自动化综合框架。AlphaSyndrome 将调度建模为一个优化问题，通过塑造错误传播来 (i) 避免接近逻辑算符的模式，以及 (ii) 保持在解码器的可纠正区域内。该框架使用蒙特卡洛树搜索（MCTS）来探索顺序与并行性，并由码结构与解码器反馈引导。在多种码族、规模和解码器上，AlphaSyndrome 相对深度最优基线将逻辑错误率平均降低 80.6%（最高 96.2%），与 Google 手工设计的表面码调度相当，并优于 IBM 针对 Bivariate Bicycle 码的调度。

## 英文关键词

Quantum Computing; Quantum Error Correction; Syndrome Measurement

## 中文关键词

量子计算；量子纠错；校验子测量

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790123)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2026](../index.md)
