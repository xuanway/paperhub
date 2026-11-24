---
title: "Sequential Specifications for Precise Hardware Exceptions"
description: "ASPLOS 2026 · Session 6B · 精确硬件异常的串行规范"
tags:
  - "ASPLOS2026"
  - "Session 6B"
  - "Hardware Design Languages"
---

# Sequential Specifications for Precise Hardware Exceptions

**中文标题：** 精确硬件异常的串行规范

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yulun Yao (Cornell University), Drew Zagieboylo (NVIDIA), G. Edward Suh (Cornell University / NVIDIA), Andrew Myers (Cornell University)

**单位：** Cornell University；NVIDIA；Cornell University / NVIDIA

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762233) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern processors are difficult to implement because pipelining makes them inherently parallel. A promising new approach, demonstrated in the PDL hardware description language, is to compile a high-level sequential specification into an efficient pipelined implementation. This high-level approach makes design-space exploration and reasoning easier. However, previous work on this approach does not support features needed for operating systems: hardware exceptions like traps and interrupts. The inherently non-sequential nature of these features makes it challenging to give them a sequential specification. They often require flushing the pipeline, writing to control state registers (CSRs), or resetting pipeline state. In this work, we develop XPDL, which extends PDL to support hardware exceptions. With this extension, logic for precise exceptions can be synthesized from a high-level specification, while maintaining the appealing properties of PDL. Using RISC-V processor designs, we demonstrate that XPDL flexibly supports exceptions with no impact on CPI (Cycles per Instructions), and minor overhead over frequency and area, and argue that the implementation preserves the oneinstruction-at-a-time semantics of PDL.

## 中文摘要

现代处理器难以实现，因为流水线使其本质上是并行的。一种有前景的新方法（在 PDL 硬件描述语言中得到展示）是将高层串行规范编译为高效的流水线实现。这种高层方法使设计空间探索与推理更加容易。然而，此前关于该方法的工作并不支持操作系统所需的功能：诸如陷阱（trap）和中断（interrupt）之类的硬件异常。这些功能本质上非串行的性质，使得为它们给出串行规范颇具挑战。它们常常需要冲刷流水线、写入控制状态寄存器（CSR）或重置流水线状态。在本工作中，我们开发了 XPDL，它扩展 PDL 以支持硬件异常。借助这一扩展，精确异常的逻辑可以从高层规范合成，同时保持 PDL 的优良特性。我们使用 RISC-V 处理器设计证明，XPDL 能灵活支持异常，且对 CPI（每指令周期数）没有影响，在频率和面积上只有很小的开销，并论证该实现保留了 PDL 一次一条指令（one-instruction-at-a-time）的语义。

## 英文关键词

Pipelining, Interrupts, Exception Handling

## 中文关键词

流水线；中断；异常处理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762233)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2026](../index.md)
