---
title: "QED: Scalable Consistency Verification of Memory Instruction Reordering in Hardware"
description: "ISCA 2026 · Session 9A · QED: Scalable Consistency Verification of Memory Instruction Reordering in Hardware"
tags:
  - "ISCA2026"
  - "Session 9A"
  - "Verification and Robustness"
---

# QED: Scalable Consistency Verification of Memory Instruction Reordering in Hardware

**中文标题：** QED: 硬件中内存指令重排的可扩展一致性验证

**所属 Session：** [Session 9A](index.md) · [ISCA 2026](../index.md)

**作者：** Gokulan Ravi, Xiaokang Qiu, Mithuna Thottethodi, T. N. Vijaykumar

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory consistency models (MCMs) in out-of-order-issue microprocessor-based shared-memory systems are notoriously non-intuitive and a source of hardware design bugs. Previous hardware verification work is limited to (1) in-order-issue processors, (2) proving the correctness only for some test cases, or (3) bounded verification that does not scale in practice beyond 7 instructions across all threads. Because cache coherence (i.e., write serialization and (non-)multi-copy write atomicity) and pipeline front-end verification and testing are well-studied, we focus on memory instruction ordering in the load-store queue (LSQ) of an out-of-order-issue processor. We show that our approach, called QED, needs to consider (1) only a small subset of instruction pairs and not all in-flight instructions, and (2) only one external event from other cores at a time per instruction of a pair (e.g., an invalidation), where only the events’ ordering matters but not their originating cores. We call these results as two+two. Exhaustively exploring all pairs of instruction types and all types of event pairs intervening between each instruction pair, QED checks whether each of a reordered pair’s execution trace leads to a cycle, which is well known to indicate an MCM violation. The MCM-violating execution traces in each instruction pair’s exploration result in a decision tree of simple, narrowly-defined predicates to be evaluated in the RTL implementation. Our two+two result proves that the number of predicates for all MCMs is independent of program length and of the numbers of in-flight memory instructions and cores. Nevertheless, each predicate must explore all of the LSQ’s RTL state. To combat RTL state space explosion, QED employs novel, empirical state space reduction, which itself is verified, to remain scalable for practical design sizes. In our experiments, we automatically generate the decision trees for SC, TSO, and RISC-V WMO, and verify the LSQ of BOOMv3 RTL with 128 loads/64 stores against RISC-V WMO using Jaspergold, where we found two correctness bugs and a performance bug (though not our goal). We fully verify the corrected implementation in under ten days. This unbounded RTL verification of a modern out-of-order-issue processor’s LSQ against an MCM is the first in the literature.

## 中文摘要

基于乱序发射微处理器的共享内存系统中的内存一致性模型（MCM）出了名地不直观，并且是硬件设计缺陷的来源。以往的硬件验证工作局限于（1）顺序发射处理器，（2）仅对某些测试用例证明正确性，或（3）有界验证，该方法在实践中无法扩展到所有线程中超过 7 条指令。由于缓存一致性（即写串行化和（非）多副本写原子性）以及流水线前端验证和测试已得到充分研究，我们将重点放在乱序发射处理器中加载-存储队列（LSQ）的内存指令排序上。我们表明，我们称为 QED 的方法只需考虑（1）指令对的一个小子集而非所有在途指令，以及（2）对于一对指令中的每条指令，一次只考虑来自其他核心的一个外部事件（例如失效），其中只有事件的顺序重要，而发起事件的核心并不重要。我们将这些结果称为 two+two。QED 穷尽探索所有指令类型对以及介入每对指令之间的所有事件对类型，检查重排对的每条执行迹是否导致环，这众所周知表示 MCM 违例。每对指令探索中导致 MCM 违例的执行迹会形成一棵由简单、定义狭窄的谓词组成的决策树，供在 RTL 实现中求值。我们的 two+two 结果证明，所有 MCM 的谓词数量与程序长度以及所有在途内存指令和核心的数量无关。然而，每个谓词必须探索 LSQ 的全部 RTL 状态。为应对 RTL 状态空间爆炸，QED 采用了新颖的、经验性的状态空间缩减（其本身也经过验证），以在实际设计规模下保持可扩展性。在我们的实验中，我们自动生成 SC、TSO 和 RISC-V WMO 的决策树，并使用 Jaspergold 针对 RISC-V WMO 验证了具有 128 个加载/64 个存储的 BOOMv3 RTL 的 LSQ，期间发现了两个正确性缺陷和一个性能缺陷（尽管这并非我们的目标）。我们在不到十天的时间内完全验证了修正后的实现。这种针对 MCM 对现代乱序发射处理器 LSQ 的无界 RTL 验证在文献中尚属首次。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2026](../index.md)
