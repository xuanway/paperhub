---
title: "Rethinking Java Performance Analysis"
description: "ASPLOS 2025 · Session 3A · 重新思考 Java 性能分析"
tags:
  - "ASPLOS2025"
  - "Session 3A"
  - "Performance Analysis & Tracing"
---

# Rethinking Java Performance Analysis

**中文标题：** 重新思考 Java 性能分析

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Stephen M. Blackburn (Google,Australian National University), Zixian Cai (Australian National University), Rui Chen (Unaffiliated-Independent), Xi Yang (IOP Systems), John Zhang (Canva), John Zigman (The University of Sydney)

**单位：** Google,Australian National University；Australian National University；Unaffiliated-Independent；IOP Systems；Canva；The University of Sydney

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707217) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Representative workloads and principled methodologies are the foundation of performance analysis, which in turn provides the empirical grounding for much of the innovation in systems research. However, benchmarks are hard to maintain, methodologies are hard to develop, and our field moves fast. The tension between our fast-moving fields and their need to maintain their methodological foundations is a serious challenge. This paper explores that challenge through the lens of Java performance analysis. Lessons we draw extend to other languages and other fields of computer science. In this paper we: i) introduce a complete overhaul of the DaCapo benchmark suite [6], characterizing 22 new and/or refreshed workloads across 47 dimensions, using principal components analysis to demonstrate their diversity, ii) demonstrate new methodologies and how they are integrated into an easy to use framework, iii) use this framework to conduct an analysis of the state of the art in production Java performance, and iv) motivate the need to invest in renewed methodologies and workloads, using as an example a review of contemporary production garbage collector performance. We highlight the danger of allowing methodologies to lag innovation and respond with a suite and new methodologies that nudge forward some of our field's methodological foundations. We offer guidance on maintaining the empirical rigor we need to encourage profitable research directions and quickly identify unprofitable ones.

## 中文摘要

具有代表性的工作负载与有原则的方法论是性能分析的基础，而性能分析又为系统研究中的大量创新提供了实证依据。然而，基准测试难以维护，方法论难以构建，而我们的领域发展迅速。快速发展的领域与其维护方法论基础的需求之间的张力，是一项严峻的挑战。本文以 Java 性能分析为视角探讨这一挑战。我们得出的经验也适用于其他语言以及计算机科学的其他领域。在本文中我们：i) 对 DaCapo 基准测试套件 [6] 进行全面重构，在 47 个维度上刻画 22 个新增和/或更新的工作负载，并用主成分分析展示其多样性；ii) 展示新的方法论以及它们如何被集成到一个易于使用的框架中；iii) 使用该框架对生产环境中 Java 性能的最先进水平进行分析；以及 iv) 以对当代生产环境垃圾收集器性能的评述为例，说明有必要投入于更新方法论与工作负载。我们强调了放任方法论滞后于创新所带来的危险，并以一个套件和新的方法论作为回应，推动本领域部分方法论基础向前发展。我们就如何保持所需的实证严谨性给出了指导，以鼓励有价值的研究方向并快速识别无价值的方向。

## 英文关键词

Performance Analysis; Java; Garbage Collection

## 中文关键词

性能分析；Java；垃圾收集

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707217)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2025](../index.md)
