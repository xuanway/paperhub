---
title: "PropHunt: Automated Optimization of Quantum Syndrome Measurement Circuits"
description: "ASPLOS 2026 · Session 4C · PropHunt：量子校验子测量电路的自动化优化"
tags:
  - "ASPLOS2026"
  - "Session 4C"
  - "Quantum Error Correction"
---

# PropHunt: Automated Optimization of Quantum Syndrome Measurement Circuits

**中文标题：** PropHunt：量子校验子测量电路的自动化优化

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Joshua Viszlai (University of Chicago), Satvik Maurya (University of Wisconsin-Madison), Swamit Tannu (University of Wisconsin-Madison), Margaret R. Martonosi (Princeton University), Fred Chong (University of Chicago)

**单位：** University of Chicago；University of Wisconsin-Madison；Princeton University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790205) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fault-Tolerant Quantum Computing (FTQC) relies on Quantum Error Correction (QEC) codes to reach error rates necessary for large scale quantum applications. At a physical level, QEC codes perform parity checks on data qubits, producing syndrome information, through Syndrome Measurement (SM) circuits. These circuits define a code's logical error rate and must be run repeatedly throughout the entire program. The performance of SM circuits is therefore critical to the success of a FTQC system. While ultimately implemented as physical circuits, SM circuits have challenges that are not addressed by existing circuit optimization tools. Importantly, inside SM circuits themselves errors are expected to occur, and how errors propagate through SM circuits directly impacts which errors are detectable and correctable, defining the code's logical error rate. This is not modeled in NISQ-era tools, which instead optimize for targets such as gate depth or gate count to mitigate the chance that any error occurs. This gap leaves key questions unanswered about the expected real-world effectiveness of QEC codes. In this work we address this gap and present PropHunt, an automated tool for optimizing SM circuits for CSS codes. We evaluate PropHunt on a suite of relevant QEC codes and demonstrate PropHunt's ability to iteratively improve performance and recover existing hand-designed circuits automatically. We also propose a near-term QEC application, Hook-ZNE, which leverages PropHunt's fine-grained control over logical error rate to improve Zero-Noise Extrapolation (ZNE), a promising error mitigation strategy.

## 中文摘要

容错量子计算（FTQC）依赖量子纠错（QEC）码来达到大规模量子应用所需的错误率。在物理层面，QEC 码通过校验子测量（Syndrome Measurement，SM）电路对数据量子比特执行奇偶校验，产生校验子信息。这些电路决定了码的逻辑错误率，并且必须在整个程序运行过程中被反复执行。因此，SM 电路的性能对 FTQC 系统的成功至关重要。SM 电路最终虽然以物理电路的形式实现，但它们面临的挑战并未被现有的电路优化工具所解决。重要的是，错误被预期会发生在 SM 电路内部，而错误如何在 SM 电路中传播，直接影响到哪些错误可被检测和纠正，从而定义了码的逻辑错误率。NISQ 时代的工具并未对此建模，它们转而针对门深度或门数量等目标进行优化，以降低任何错误发生的几率。这一空白使得关于 QEC 码在真实世界中预期有效性的关键问题仍未得到解答。在本工作中，我们填补了这一空白，提出 PropHunt，一个用于为 CSS 码优化 SM 电路的自动化工具。我们在若干相关 QEC 码上评估 PropHunt，并展示了 PropHunt 迭代提升性能以及自动重现现有手工设计电路的能力。我们还提出了一种近期 QEC 应用 Hook-ZNE，它利用 PropHunt 对逻辑错误率的细粒度控制来改进零噪声外推（Zero-Noise Extrapolation，ZNE）——一种颇具前景的错误缓解策略。

## 英文关键词

Quantum Computing; Quantum Error Correction; Syndrome Measurement Circuit; Error Mitigation

## 中文关键词

量子计算；量子纠错；校验子测量电路；错误缓解

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790205)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2026](../index.md)
