---
title: "Language-Agnostic Static Deadlock Detection for Futures"
description: "PPoPP 2024 Session Compilers and Runtimes for Parallel Systems：基于图类型的可靠类型系统，实现语言无关的 futures 死锁检测"
tags:
  - "PPoPP2024"
  - "Session-2"
  - "Compilers and Runtimes for Parallel Systems"
  - "deadlock"
  - "futures"
  - "static analysis"
authors:
  - "Stefan K Muller"
session: "Session 2: Compilers and Runtimes for Parallel Systems"
session_number: 2
session_chair: "Mohamed Riyadh Baghdadi"
date: "2024-03-04"
time: "12:10–12:30"
room: "Moorfoot"
doi: "10.1145/3627535.3638487"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Language-Agnostic Static Deadlock Detection for Futures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出并证明作用于图类型的可靠类型系统，以语言无关方式近似依赖图来发现 futures 程序的潜在死锁，纠正原算法依据的错误猜想，并在 OCaml 子集上实现原型。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 2: Compilers and Runtimes for Parallel Systems</p>
</div>

**作者**：Stefan K Muller (Illinois Institute of Technology)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 12:10–12:30 · Session 2: Compilers and Runtimes for Parallel Systems（主席：Mohamed Riyadh Baghdadi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638487) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Deadlocks, in which threads wait on each other in a cyclic fashion and can’t make progress, have plagued parallel programs for decades. In recent years, as the parallel programming mechanism known as futures has gained popularity, interest in preventing deadlocks in programs with futures has increased as well. Various static and dynamic algorithms exist to detect and prevent deadlock in programs with futures, generally by constructing some approximation of the dependency graph of the program but, as far as we are aware, all are specialized to a particular programming language. A recent paper introduced graph types, by which one can statically approximate the dependency graphs of a program in a language-independent fashion. By analyzing the graph type directly instead of the source code, a graph-based program analysis, such as one to detect deadlock, can be made language-independent. Indeed, the paper that proposed graph types also proposed a deadlock detection algorithm. Unfortunately, the algorithm was based on an unproven conjecture which we show to be false. In this paper, we present, and prove sound, a type system for finding possible deadlocks in programs that operates over graph types and can therefore be applied to many different languages. As a proof of concept, we have implemented the algorithm over a subset of the OCaml language extended with built-in futures.

## 中文摘要

死锁——线程以循环方式相互等待、无法取得进展——已困扰并行程序数十年。近年来，随着被称为 futures 的并行编程机制日益流行，人们对防止含 futures 的程序出现死锁的兴趣也随之增长。目前已存在多种静态和动态算法来检测与预防含 futures 程序的死锁，它们通常通过构造程序依赖图的某种近似来实现；但据我们所知，这些算法都专门针对某一特定编程语言。最近一篇论文引入了图类型（graph types），借此可以以语言无关的方式静态近似程序的依赖图。通过直接分析图类型而不是源代码，基于图的程序分析（例如死锁检测）就可以做到语言无关。事实上，提出图类型的那篇论文也提出了一种死锁检测算法。遗憾的是，该算法基于一个未经证明的猜想，而我们证明该猜想是错误的。在本文中，我们提出并证明了一个可靠的类型系统，用于发现程序中可能的死锁；该系统作用于图类型之上，因而可应用于多种不同的语言。作为概念验证，我们在扩展了内置 futures 的 OCaml 语言子集上实现了该算法。

## 英文关键词

Deadlock, futures, graph types, type systems, static analysis

## 中文关键词

死锁；futures；图类型；类型系统；静态分析

---

## 一句话总结

> 提出并证明作用于图类型的可靠类型系统，以语言无关方式近似依赖图来发现 futures 程序的潜在死锁，纠正原算法依据的错误猜想，并在 OCaml 子集上实现原型。

## 研究问题

已有静态与动态的 futures 死锁检测算法通常构造程序依赖图的近似，但都专门针对某一特定编程语言；而图类型论文提出的死锁检测算法基于一个未经证明的猜想，该猜想实际为假。

## 方法简述

- 采用图类型（graph types）以语言无关的方式静态近似程序依赖图，并直接分析图类型而非源代码，使基于图的分析与语言解耦
- 提出一个作用于图类型、用于发现程序中可能死锁的类型系统
- 证明该类型系统的可靠性（sound），并指出此前算法所依赖的猜想为假
- 作为概念验证，在扩展了内置 futures 的 OCaml 语言子集上实现该算法

## 主要结果

- 给出类型系统的可靠性证明，使基于图类型的死锁检测具备可靠基础
- 以反例证明图类型原论文所依据的猜想不成立，修正了此前算法的前提
- 在带内置 futures 的 OCaml 子集上完成原型实现，验证该方法可跨语言应用

---

> 所属 Session：[Session 2: Compilers and Runtimes for Parallel Systems](index.md) · 返回 [PPoPP 2024 总览](../index.md)
