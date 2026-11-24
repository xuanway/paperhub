---
title: "Optimizer-Friendly Instrumentation for Event Quantification with PRUE Algorithm"
description: "ASPLOS 2026 · Session 2D · 基于 PRUE 算法的事件量化优化器友好插桩"
tags:
  - "ASPLOS2026"
  - "Session 2D"
  - "DRAM Reliability & Security"
---

# Optimizer-Friendly Instrumentation for Event Quantification with PRUE Algorithm

**中文标题：** 基于 PRUE 算法的事件量化优化器友好插桩

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hao Ling (The Hong Kong University of Science and Technology), Yiyuan Guo (The Hong Kong University of Science and Technology), Charles Zhang (The Hong Kong University of Science and Technology)

**单位：** The Hong Kong University of Science and Technology

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790196) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Event quantification provides frequency information for runtime events and is widely used to build fast, secure, and reliable software and systems. It is usually achieved through instrumentation that introduces new instructions into programs but has significant runtime overhead. A key challenge in developing efficient instrumentation is that the instrumentation can barely benefit from modern compiler optimizations because the additional instructions introduce side effects that complicate the optimization process. One intuitive idea to mitigate the side effect issue is to use local counters with transparent lifetimes and scopes instead of relying on global counters. Optimizations are more likely to succeed on instructions that manipulate local variables rather than global ones. However, this idea is not fully adequate, as local counters are unobservable to external users of the quantification data. Therefore, global counters are still necessary, and it is essential to determine when to update them based on the local counters. The challenge is that these updates also introduce side effects that hinder optimizations. We address this update decision problem with the Partially Redundant Update Elimination (PRUE). We present Zircon, the first optimizer-friendly instrumentation to quantify runtime events. With the help of local counters, Zircon separates the event occurrence and the quantification by moving the instructions with side effects outside the scope where the optimizers apply. However, this separation introduces redundant instructions; the additional instructions would still be executed even without event occurrence. In other words, the lifetime control of the local counters challenges the efficiency of instrumentation. PRUE transforms the program and prunes away paths with redundant updates based on static analysis. The evaluation on the SPEC CPU 2017 shows that Zircon is up to 149% faster than state-of-the-art work, including SanCov and Nisse. Unlike existing efforts, Zircon does n harnesses the power of compilation optimizers and delivers automatic performance gains.

## 中文摘要

事件量化提供运行时事件的频率信息，被广泛用于构建快速、安全且可靠的软件与系统。它通常通过插桩实现，插桩会向程序中引入新指令，但会带来显著的运行时开销。开发高效插桩的一个关键挑战在于，插桩几乎无法受益于现代编译器优化，因为额外指令会引入副作用，使优化过程变得复杂。缓解副作用问题的一个直观想法是使用具有透明生存期和作用域的局部计数器，而不是依赖全局计数器。相比操作全局变量的指令，优化更有可能在操作局部变量的指令上成功。然而，这一想法并不完全充分，因为局部计数器对量化数据的外部使用者不可见。因此，全局计数器仍然必要，并且必须确定何时根据局部计数器更新它们。挑战在于，这些更新同样会引入阻碍优化的副作用。我们通过部分冗余更新消除（Partially Redundant Update Elimination，PRUE）来解决这一更新决策问题。我们提出 Zircon，这是首个对优化器友好的运行时事件量化插桩。借助局部计数器，Zircon 将带副作用的指令移到优化器作用的范围之外，从而把事件发生与事件量化分离。然而，这种分离会引入冗余指令；即使事件未发生，这些额外指令仍会被执行。换言之，局部计数器的生存期控制对插桩效率构成了挑战。PRUE 基于静态分析对程序进行变换，并剪除包含冗余更新的路径。在 SPEC CPU 2017 上的评估表明，Zircon 比包括 SanCov 和 Nisse 在内的现有先进工作最多快 149%。与现有工作不同，Zircon 充分借助编译优化器的能力，并带来自动的性能提升。

## 英文关键词

Event Quantification; Instrumentation

## 中文关键词

事件量化；插桩

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790196)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2026](../index.md)
