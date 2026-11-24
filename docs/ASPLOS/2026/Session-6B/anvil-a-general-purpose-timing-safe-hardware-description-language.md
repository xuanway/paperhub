---
title: "Anvil: A General-Purpose Timing-Safe Hardware Description Language"
description: "ASPLOS 2026 · Session 6B · Anvil：一种通用的定时安全硬件描述语言"
tags:
  - "ASPLOS2026"
  - "Session 6B"
  - "Hardware Design Languages"
---

# Anvil: A General-Purpose Timing-Safe Hardware Description Language

**中文标题：** Anvil：一种通用的定时安全硬件描述语言

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jason Zhijingcheng Yu (National University of Singapore), Aditya Ranjan Jha (National University of Singapore), Umang Mathur (National University of Singapore), Trevor E. Carlson (National University of Singapore), Prateek Saxena (National University of Singapore)

**单位：** National University of Singapore

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790125) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Expressing hardware designs using hardware description languages (HDLs) routinely involves using stateless signals whose values change according to their underlying registers. Unintended behaviours can arise when the stored values in these underlying registers are mutated while their dependent signals are expected to remain constant across multiple cycles. Such timing hazards are common because, with a few exceptions, existing HDLs lack abstractions for values that remain unchanged over multiple clock cycles, delegating this responsibility to hardware designers. Designers must then carefully decide whether a value should remain unchanged, sometimes even across hardware modules. This paper proposes Anvil, an HDL which statically prevents timing hazards with a novel type system. Anvil is the only HDL we know of that guarantees timing safety, i.e., absence of timing hazards, without sacrificing expressiveness for cyclelevel timing control or dynamic timing behaviours. Unlike many HLS languages that abstract away the differences between registers and signals, Anvil's type system exposes them fully while capturing the timing relationships between register value mutations and signal usages to enforce timing safety. This, in turn, enables safe composition of communicating hardware modules by static enforcement of timing contracts that encode timing constraints on shared signals. Such timing contracts can be specified parametric on abstract time points that can vary during run-time, allowing the type system to statically express dynamic timing behaviour. We have implemented Anvil and successfully used it to implement key timing-sensitive modules, comparing them against open-source SystemVerilog counterparts to demonstrate the practicality and expressiveness of the generated hardware.

## 中文摘要

使用硬件描述语言（HDL）表达硬件设计，通常都涉及使用无状态信号，其值根据其底层寄存器而变化。当其底层寄存器中存储的值在依赖它们的信号预期要在多个周期内保持恒定时被改变，就可能出现非预期的行为。此类定时风险（timing hazard）很常见，因为除少数例外，现有 HDL 缺乏对在多个时钟周期内保持不变的值的抽象，而是将这一责任交给硬件设计者。设计者随后必须仔细判断某个值是否应保持不变，有时甚至要跨硬件模块进行判断。本文提出 Anvil，一种 HDL，它通过新颖的类型系统静态地防止定时风险。据我们所知，Anvil 是唯一在不牺牲周期级（cycle-level）定时控制或动态定时行为表达力的情况下保证定时安全（即不存在定时风险）的 HDL。与许多将寄存器与信号之间的差异抽象掉的 HLS 语言不同，Anvil 的类型系统完全暴露这些差异，同时捕获寄存器值变更与信号使用之间的定时关系以强制定时安全。这反过来通过静态强制执行定时契约（这些契约对共享信号编码定时约束），实现了通信硬件模块的安全组合。此类定时契约可以针对抽象时间点进行参数化指定，而这些时间点可在运行时变化，从而使类型系统能够静态表达动态定时行为。我们已实现 Anvil，并成功地用它实现了关键的定时敏感模块，将它们与开源 SystemVerilog 对应实现进行比较，以证明所生成硬件的实用性与表达力。

## 英文关键词

Hardware description languages; Type systems; Concurrency safety

## 中文关键词

硬件描述语言；类型系统；并发安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790125)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2026](../index.md)
