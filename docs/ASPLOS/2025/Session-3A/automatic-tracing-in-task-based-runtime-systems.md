---
title: "Automatic Tracing in Task-Based Runtime Systems"
description: "ASPLOS 2025 · Session 3A · 基于任务制运行时系统的自动追踪"
tags:
  - "ASPLOS2025"
  - "Session 3A"
  - "Performance Analysis & Tracing"
---

# Automatic Tracing in Task-Based Runtime Systems

**中文标题：** 基于任务制运行时系统的自动追踪

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Rohan Yadav (Stanford University), Michael Bauer (NVIDIA), David Broman (KTH Royal Institute of Technology), Michael Garland (NVIDIA), Alex Aiken (Stanford University), Fredrik Kjolstad (Stanford University)

**单位：** Stanford University；NVIDIA；KTH Royal Institute of Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707237) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Implicitly parallel task-based runtime systems often perform dynamic analysis to discover dependencies in and extract parallelism from sequential programs. Dependence analysis becomes expensive as task granularity drops below a threshold. Tracing techniques have been developed where programmers annotate repeated program fragments (traces) issued by the application, and the runtime system memoizes the dependence analysis for those fragments, greatly reducing overhead when the fragments are executed again. However, manual trace annotation can be brittle and not easily applicable to complex programs built through the composition of independent components. We introduce Apophenia, a system that automatically traces the dependence analysis of task-based runtime systems, removing the burden of manual annotations from programmers and enabling new and complex programs to be traced. Apophenia identifies traces dynamically through a series of dynamic string analyses, which find repeated program fragments in the stream of tasks issued to the runtime system. We show that Apophenia is able to come between 0.92x–1.03x the performance of manually traced programs, and is able to effectively trace previously untraced programs to yield speedups of between 0.91x–2.82x on the Perlmutter and Eos supercomputers.

## 中文摘要

隐式并行的任务制运行时系统通常执行动态分析，以发现顺序程序中的依赖关系并从中提取并行性。当任务粒度低于某一阈值时，依赖分析会变得开销高昂。已有追踪技术要求程序员标注应用所发出的重复程序片段（trace），运行时系统则对这些片段的依赖分析进行记忆化，从而在片段被再次执行时大幅降低开销。然而，手工标注 trace 往往脆弱，且难以适用于由独立组件组合而成的复杂程序。我们提出 Apophenia，一个自动对任务制运行时系统的依赖分析进行追踪的系统，它免除了程序员手工标注的负担，并使新的复杂程序也能被追踪。Apophenia 通过一系列动态字符串分析来动态识别 trace，这些分析可在提交给运行时系统的任务流中发现重复的程序片段。我们表明，Apophenia 的性能可达手工追踪程序的 0.92 倍至 1.03 倍，并且能够有效追踪此前未被追踪的程序，在 Perlmutter 与 Eos 超级计算机上带来 0.91 倍至 2.82 倍的加速。

## 英文关键词

Dynamic Analysis; Runtime Systems; Tracing

## 中文关键词

动态分析；运行时系统；追踪

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707237)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2025](../index.md)
