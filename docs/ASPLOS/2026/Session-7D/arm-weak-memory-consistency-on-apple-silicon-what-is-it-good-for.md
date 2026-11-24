---
title: "Arm Weak Memory Consistency on Apple Silicon: What Is It Good For?"
description: "ASPLOS 2026 · Session 7D · Apple Silicon 上的 Arm 弱内存一致性：它有什么用？"
tags:
  - "ASPLOS2026"
  - "Session 7D"
  - "Processor Microarchitecture"
---

# Arm Weak Memory Consistency on Apple Silicon: What Is It Good For?

**中文标题：** Apple Silicon 上的 Arm 弱内存一致性：它有什么用？

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yossi Khayet (Tel Aviv University), Adam Morrison (Tel Aviv University)

**单位：** Tel Aviv University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790129) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Weak memory models such as the Arm model are perceived as enabling higher performance than strong models such as TSO. We critically test this perception on Apple silicon CPUs, whose runtime-configurable TSO mode enables a direct comparison with native Arm mode. We find that Apple silicon TSO mode preserves Arm weak-memory optimizations, typically yielding execution times within 3% of Arm mode across modern applications and classic benchmarks. Although some applications experience higher TSO slowdowns, we trace these to artifacts of Apple's TSO implementation rather than inherent TSO ordering constraints. Our results challenge the perception that the Arm memory model offers a significant performance advantage over TSO in Apple silicon.

## 中文摘要

Arm 模型等弱内存模型被认为相比 TSO 等强模型能够带来更高性能。我们在 Apple silicon CPU 上批判性地检验这一认知，其运行时可配置的 TSO 模式使得与原生 Arm 模式的直接比较成为可能。我们发现 Apple silicon 的 TSO 模式保留了 Arm 弱内存优化，在现代应用和经典基准上通常产生与 Arm 模式相差 3% 以内的执行时间。尽管部分应用经历了更高的 TSO 减速，我们将这些减速追溯为 Apple 的 TSO 实现所带来的人为产物，而非 TSO 固有的排序约束。我们的结果挑战了如下认知：在 Apple silicon 上，Arm 内存模型相对 TSO 具有显著的性能优势。

## 英文关键词

Weak memory models; x86-TSO; Arm

## 中文关键词

弱内存模型；x86-TSO；Arm

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790129)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2026](../index.md)
