---
title: "Rage Against the State Machine: Type-Stated Hardware Peripherals for Increased Driver Correctness"
description: "ASPLOS 2026 · Session 6B · 怒斥状态机：以类型陈述的硬件外设提升驱动程序正确性"
tags:
  - "ASPLOS2026"
  - "Session 6B"
  - "Hardware Design Languages"
---

# Rage Against the State Machine: Type-Stated Hardware Peripherals for Increased Driver Correctness

**中文标题：** 怒斥状态机：以类型陈述的硬件外设提升驱动程序正确性

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tyler Potyondy (UC San Diego), Anthony Tarbinian (UC San Diego), Leon Schuermann (Princeton University), Eric Mugnier (UC San Diego), Adin Ackerman (UC San Diego), Amit Levy (Princeton University), Pat Pannuto (UC San Diego)

**单位：** UC San Diego；Princeton University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790207) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hardware provides driver authors both a strict specification of the operations a driver is allowed to do, and a highly permissive interface full of operations a driver can do. Authoring drivers that adhere to the provided hardware device protocol is challenged by dynamic definitions of what a driver should do based on the hardware's state. This is further complicated by increasingly capable hardware which may transition between states concurrently and independently from the software driver. We present Abacus, a framework that statically prevents drivers from violating device protocols. Abacus refines typestates to model hardware-software concurrency and presents a formalization of hardware states into two families: stable and transient states. The Abacus framework provides a domain specific language for developers to encode device protocol invariants in tens of lines of code, and, using the generated Abacus type-states, statically prevents device protocol bugs. We demonstrate the Abacus framework's practicality by integrating it into drivers in two Rust OSes. We find that Abacus imposes minimal to no overhead in code-size and runtime performance, statically detects device protocol violations, and enables the usage of hardware features that would otherwise be prohibitively complex.

## 中文摘要

硬件既为驱动作者提供了驱动程序被允许执行哪些操作的严格规范，也提供了一个高度宽松、充满驱动程序可以执行的操作的接口。编写遵循所提供硬件设备协议的驱动程序，其困难在于驱动程序应当做什么是由硬件状态动态定义的。而能力日益增强的硬件可能并发地、独立于软件驱动程序地在状态之间转换，这使其更加复杂。我们提出 Abacus，一个静态防止驱动程序违反设备协议的框架。Abacus 对类型状态（typestate）进行精化以建模硬件与软件之间的并发，并给出将硬件状态划分为两个族的形式化：稳定状态与瞬态状态。Abacus 框架为开发者提供一种领域特定语言，使其能在数十行代码中编码设备协议不变量，并利用生成的 Abacus 类型状态静态防止设备协议缺陷。我们通过将 Abacus 框架集成到两个 Rust 操作系统中的驱动程序，展示了该框架的实用性。我们发现 Abacus 在代码大小和运行时性能上带来极小到没有的开销，能静态检测设备协议违规，并使那些否则会复杂到难以使用的硬件特性得以被使用。

## 英文关键词

Device Driver Bugs; Type-State Programming

## 中文关键词

设备驱动缺陷；类型状态编程

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790207)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2026](../index.md)
