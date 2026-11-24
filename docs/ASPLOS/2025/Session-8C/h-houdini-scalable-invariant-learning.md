---
title: "H-Houdini: Scalable Invariant Learning"
description: "ASPLOS 2025 · Session 8C · H-Houdini：可扩展的不变式学习"
tags:
  - "ASPLOS2025"
  - "Session 8C"
  - "Potpourri 2"
---

# H-Houdini: Scalable Invariant Learning

**中文标题：** H-Houdini：可扩展的不变式学习

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sushant Dinesh (University of California, Berkeley), Yongye Zhu (University of California, Berkeley), Christopher W. Fletcher (University of California, Berkeley)

**单位：** University of California, Berkeley

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707263) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Formal verification is a critical task in hardware design today. Yet, while there has been significant progress in improving technique automation and efficiency, scaling to large hardware designs remains a significant challenge. We address this challenge by proposing H-Houdini: a new algorithm for (mostly) push-button inductive invariant learning that scales to large hardware designs. H-Houdini combines the strengths of Machine Learning Inspired Synthesis (MLIS) and SAT-based Incremental Learning. The key advance is a method that replaces the monolithic SMT-style checks made by MLIS with a carefully-constructed hierarchy of smaller, incremental SMT checks that can be parallelized, memoized and reassembled into the original 'monolithic' invariant in a correct-by-construction fashion. We instantiate H-Houdini as VeloCT, a framework that proves hardware security properties by learning relational invariants. We benchmark VeloCT on the 'safe instruction set synthesis' problem in microarchitectural security. Here, VeloCT automatically (with no expert annotations) learns an invariant for the RISC-V Rocketchip in under 10s (2880× faster than state of the art). Further, VeloCT is the first work to scale to the RISC-V out-of-order BOOM and can (mostly automatically) verify all BOOM variants (ranging from Small to Mega) in between 6.95 minutes to 199.1 minutes.

## 中文摘要

形式验证是当今硬件设计中的一项关键任务。然而，尽管在提升技术自动化程度与效率方面已取得显著进展，扩展到大规模硬件设计仍是一项重大挑战。为应对这一挑战，我们提出 H-Houdini：一种（基本）一键式的归纳不变式学习新算法，可扩展到大规模硬件设计。H-Houdini 结合了机器学习启发式综合（MLIS）与基于 SAT 的增量学习二者的优势。其关键进展在于一种方法：用精心构造的、更小且增量的 SMT 检查层次结构，替代 MLIS 所做的单体式 SMT 风格检查，这些检查可被并行化、记忆化，并以构造即正确的方式重组为原始的“单体”不变式。我们将 H-Houdini 实例化为 VeloCT，这是一个通过学习关系不变式来证明硬件安全属性的框架。我们在微体系结构安全中的“安全指令集综合”问题上对 VeloCT 进行基准测试。在此，VeloCT 无需任何专家标注即自动在 10 秒内为 RISC-V Rocketchip 学习到不变式（比最先进技术快 2880 倍）。此外，VeloCT 是首个可扩展到 RISC-V 乱序 BOOM 的工作，并且能够（基本自动地）在 6.95 分钟到 199.1 分钟之间验证所有 BOOM 变体（从 Small 到 Mega）。

## 英文关键词

Hardware Verification; Invariant Learning; Scalable Verification; Formal Verification; Abductive Reasoning; Microarchitectural Security; Constant-Time Programming; Incremental Invariant Learning; Hardware attacks and defenses

## 中文关键词

硬件验证；不变式学习；可扩展验证；形式验证；溯因推理；微体系结构安全；常数时间编程；增量不变式学习；硬件攻击与防御

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707263)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2025](../index.md)
