---
title: "täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies"
description: "ISCA 2026 · Session 9A · täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies"
tags:
  - "ISCA2026"
  - "Session 9A"
  - "Verification and Robustness"
---

# täkōFormal: Enabling Robust Software for Programmable Memory Hierarchies

**中文标题：** täkōFormal: 为可编程内存层次结构提供健壮软件支持

**所属 Session：** [Session 9A](index.md) · [ISCA 2026](../index.md)

**作者：** Pranav Srinivasan, Manos Kapritsos, Yatin A. Manerkar

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Accelerators provide large performance and energy-efficiency benefits, but can significantly change the hardware-software interface. The täkō programmable memory hierarchy accelerates data movement by enabling programmers to run user-defined callback functions triggered by cache misses, evictions, and writebacks. However, it also leads to drastically increased complexity and counterintuitive outcomes. In response, we develop an ISA-level memory consistency model (MCM) for täkō that captures the semantics of its operation, and we show how it enables programmers to formally reason about their täkō programs. We also prove the soundness of this ISA-level MCM by constructing a detailed täkō implementation model and verifying that all executions of the implementation model are allowed by our ISA-level MCM. Along the way, we discover useful insights about microarchitectural modeling and verification that are applicable to hardware in general.

## 中文摘要

加速器带来了巨大的性能和能效优势，但可能显著改变硬件-软件接口。täkō 可编程内存层次结构通过使程序员能够运行由缓存未命中、逐出和写回触发的用户定义回调函数来加速数据移动。然而，它也导致复杂性急剧增加和反直觉的结果。作为回应，我们为 täkō 开发了一个 ISA 级内存一致性模型（MCM），该模型捕获了其操作的语义，并展示了它如何使程序员能够对其 täkō 程序进行形式化推理。我们还通过构建详细的 täkō 实现模型并验证该实现模型的所有执行都被我们的 ISA 级 MCM 所允许，证明了该 ISA 级 MCM 的可靠性。在此过程中，我们发现了关于微架构建模和验证的有用见解，这些见解普遍适用于硬件。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：GenericMonkey/takoFormal](https://github.com/GenericMonkey/takoFormal)
- [实验材料归档（Zenodo 19444275）](https://zenodo.org/records/19444275)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2026](../index.md)
