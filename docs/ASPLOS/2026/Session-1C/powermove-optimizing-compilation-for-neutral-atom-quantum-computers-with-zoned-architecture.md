---
title: "PowerMove: Optimizing Compilation for Neutral Atom Quantum Computers with Zoned Architecture"
description: "ASPLOS 2026 · Session 1C · PowerMove：面向分区架构中性原子量子计算机的优化编译"
tags:
  - "ASPLOS2026"
  - "Session 1C"
  - "Quantum Computing: Compilation"
---

# PowerMove: Optimizing Compilation for Neutral Atom Quantum Computers with Zoned Architecture

**中文标题：** PowerMove：面向分区架构中性原子量子计算机的优化编译

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jixuan Ruan (University of California San Diego), Xiang Fang (University of California, San Diego), Hezi Zhang (University of California San Diego), Ang Li (PNNL and UW), Travis Humble (Quantum Science Center, Oak Ridge National Laboratory), Yufei Ding (UCSD)

**单位：** University of California San Diego；University of California, San Diego；PNNL and UW；Quantum Science Center, Oak Ridge National Laboratory；UCSD

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736128) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Neutral atom quantum computers (NAQCs) have emerged as promising candidates for scalable quantum computing, thanks to their advanced hardware capabilities, particularly qubit movement and the Zoned Architecture (ZA). However, fully harnessing these features presents significant compilation challenges, requiring careful coordination across gate scheduling, qubit positioning, atom movement, and interzone communication. In this paper, we propose PowerMove, an efficient compiler for NAQCs that unlocks new optimization opportunities, significantly improving qubit movement strategies while seamlessly integrating ZA. Our evaluation demonstrates orders-of-magnitude fidelity improvements over state-of-the-art methods, with execution time reduced by up to 3.76× and compilation time accelerated by up to 216.9× across various NISQ applications. Furthermore, PowerMove extends naturally to the fault-tolerant quantum computing (FTQC) setting, where physical qubits are replaced by logical qubits encoded in QEC codes, achieving a 4.78× reduction in execution time. These results highlight PowerMove's impact on both near-term NISQ applications and long-term FTQC implementations. We have open-sourced our codes at to facilitate further research and collaboration within the community.

## 中文摘要

中性原子量子计算机（NAQC）凭借其先进的硬件能力，特别是量子比特移动与分区架构（ZA），已成为可扩展量子计算的有前景的候选方案。然而，要充分驾驭这些特性带来了显著的编译挑战，需要在门调度、量子比特布局、原子移动与区间间通信之间进行细致的协调。在本文中，我们提出 PowerMove，一种面向 NAQC 的高效编译器，它解锁了新的优化机会，显著改进了量子比特移动策略，同时无缝集成 ZA。我们的评估表明，相比最先进方法，保真度提升达数个数量级，在各类 NISQ 应用中执行时间最多缩短 3.76×，编译时间最多加速 216.9×。此外，PowerMove 自然地扩展到容错量子计算（FTQC）场景，其中物理量子比特被替换为编码在 QEC 码中的逻辑量子比特，实现了 4.78× 的执行时间缩减。这些结果凸显了 PowerMove 对近期 NISQ 应用与长期 FTQC 实现的影响。我们已将我们的代码开源，以促进社区内的进一步研究与协作。

## 英文关键词

neutral atom quantum computing (NAQC), zoned architecture (ZA), compiler

## 中文关键词

中性原子量子计算（NAQC）；分区架构（ZA）；编译器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736128)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 1C](index.md) · [返回 ASPLOS 2026](../index.md)
