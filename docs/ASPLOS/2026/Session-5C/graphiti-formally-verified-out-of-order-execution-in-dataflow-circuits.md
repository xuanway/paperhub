---
title: "Graphiti: Formally Verified Out-of-Order Execution in Dataflow Circuits"
description: "ASPLOS 2026 · Session 5C · Graphiti：数据流电路中经形式化验证的乱序执行"
tags:
  - "ASPLOS2026"
  - "Session 5C"
  - "Formal Verification"
---

# Graphiti: Formally Verified Out-of-Order Execution in Dataflow Circuits

**中文标题：** Graphiti：数据流电路中经形式化验证的乱序执行

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yann Herklotz (EPFL), Ayatallah Elakhras (EPFL), Martina Camaioni (EPFL), Paolo Ienne (EPFL), Lana Josipovic (ETH Zurich), Thomas Bourgeat (EPFL)

**单位：** EPFL；ETH Zurich

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790166) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

High-level synthesis (HLS) tools automatically synthesise hardware from imperative programs and have seen a significant rise in adoption in both industry and academia. To deliver high-quality hardware designs for increasingly general purpose programs, HLS compilers have to become more aggressive. For the most irregular programs, HLS tools generating dataflow circuits show promising performance by adapting and specializing key ideas from processor architectures, like out-of-order execution and speculation. However, the complexity of these transformations makes them difficult to reason about, increasing the risk of subtle bugs and potentially delaying their adoption in a conservative industry where bugs can be extremely costly. This paper introduces Graphiti, a framework embedded in the Lean 4 proof assistant designed to formally reason about and manipulate dataflow circuits at the core of these HLS tools. We develop a metatheory of graph refinement that allows us to verify a general-purpose dataflow circuit rewriting algorithm. Using this framework, we formally verify a loop rewrite that introduces out-of-order execution into a dataflow circuit. Our evaluation shows that the resulting verified optimization pipeline achieves a 2.1× speedup over the in-order HLS flow and a 5.8× speedup over a verified HLS tool generating a static state machine. We also show that it achieves the same performance compared to an existing unverified approach which introduces out-of-order execution. Graphiti is a step toward a fully-verified HLS flow targeting dataflow circuits. In the interim, it can serve as an extensible, verified, optimizing engine that can be integrated into existing dataflow HLS compilers.

## 中文摘要

高层综合（HLS）工具能够从命令式程序自动生成硬件，其采用率在工业界和学术界均有显著上升。为了给日益通用的程序交付高质量的硬件设计，HLS 编译器必须变得更加激进。对于最不规则的程序，生成数据流电路的 HLS 工具通过改造并特化处理器架构中的关键思想（如乱序执行与推测），展现出可观的性能。然而，这些变换的复杂性使其难以推理，增加了出现微妙缺陷的风险，并可能推迟它们在保守行业中的采用——在那种行业里，缺陷可能代价极高。本文提出 Graphiti，一个嵌入 Lean 4 证明助手的框架，旨在对位于这类 HLS 工具核心的数据流电路进行形式化推理与操控。我们发展了图细化的元理论，使我们能够验证一种通用的数据流电路重写算法。借助该框架，我们形式化验证了一种将乱序执行引入数据流电路的循环重写。我们的评估表明，所得经过验证的优化流水线相比按序 HLS 流程取得 2.1× 的加速，相比生成静态状态机的已验证 HLS 工具取得 5.8× 的加速。我们还表明，与引入乱序执行的现有未验证方法相比，它取得了相同的性能。Graphiti 是迈向面向数据流电路的完全验证 HLS 流程的一步。在此期间，它可作为可扩展的、经过验证的优化引擎，集成到现有的数据流 HLS 编译器中。

## 英文关键词

high-level synthesis; interactive theorem proving; Lean

## 中文关键词

高层综合；交互式定理证明；Lean

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790166)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2026](../index.md)
