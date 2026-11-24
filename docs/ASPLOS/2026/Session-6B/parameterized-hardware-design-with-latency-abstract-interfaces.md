---
title: "Parameterized Hardware Design with Latency-Abstract Interfaces"
description: "ASPLOS 2026 · Session 6B · 带延迟抽象接口的参数化硬件设计"
tags:
  - "ASPLOS2026"
  - "Session 6B"
  - "Hardware Design Languages"
---

# Parameterized Hardware Design with Latency-Abstract Interfaces

**中文标题：** 带延迟抽象接口的参数化硬件设计

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Rachit Nigam (Massachusetts Institute of Technology), Edmund Lam (Cornell University), Ethan Gabizon (Cornell University), Carolyn Zech (Massachusetts Institute of Technology), Jonathan Balkind (UC Santa Barbara), Adrian Sampson (Cornell University)

**单位：** Massachusetts Institute of Technology；Cornell University；UC Santa Barbara

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790199) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hardware designs must use latency-insensitive (LI) interfaces when timing is input-dependent. When timing is input-independent, designs should use latency-sensitive (LS) interfaces for maximum performance. However, designs commonly use LI interfaces to integrate with externally generated LS modules–from, e.g., IP generators, high-level synthesis, or domain specific languages. In every fully integrated design, such uses of LI represent pure overhead. The challenge is that generators can dramatically change timing interfaces of the modules to meet performance objectives, and LI interfaces act as a useful design abstraction and enable timing adaptation. We define latency-abstract (LA) interfaces, a new design abstraction, which provide the timing adaptability of LI interfaces at design-time and the efficient integration of LS interfaces. LA interfaces use output parameters, a novel compile-time mechanism for child modules to return values parent modules, to abstract and encapsulate timing behaviors at design time. During design elaboration, LA interfaces are compiled into efficient LS interfaces based on parameter values. While an attractive option, LA interfaces inherit the complexities of parameterized hardware design: the user must reason how parameters influence timing behaviors of modules and ensure that designs adapt to interface changes. To address this challenge and demonstrate the utility of LA interfaces, we design Lilac, a parameterized HDL that uses a type system track the influence of parameters on timing behaviors and formally guarantee that every parameterization o hazards. We demonstrate Lilac's efficacy by using it to implement parameterized designs and integrate designs generated from external tools. We show that LA designs use 26– 33% fewer chip resources and achieve 6.8% better maximum frequencies than comparable LI implementations.

## 中文摘要

当定时（timing）依赖于输入时，硬件设计必须使用延迟不敏感（latency-insensitive，LI）接口。当定时与输入无关时，设计应使用延迟敏感（latency-sensitive，LS）接口以获得最高性能。然而，设计常常使用 LI 接口来与外部生成的 LS 模块集成——这些模块来自例如 IP 生成器、高层综合或领域特定语言。在任何完全集成的设计中，这种对 LI 的使用都是纯粹的开销。挑战在于，生成器可以大幅改变模块的定时接口以满足性能目标，而 LI 接口则充当一种有用的设计抽象并支持定时适配。我们定义了延迟抽象（latency-abstract，LA）接口，这是一种新的设计抽象，它在设计时提供 LI 接口的定时可适应性，并具备 LS 接口的高效集成能力。LA 接口使用输出参数——一种新颖的编译期机制，使子模块能够向父模块返回值——来在设计时抽象并封装定时行为。在设计精化（elaboration）期间，LA 接口根据参数值被编译为高效的 LS 接口。LA 接口虽然是一个有吸引力的选项，但它继承了参数化硬件设计的复杂性：用户必须推理参数如何影响模块的定时行为，并确保设计能够适应接口变化。为应对这一挑战并展示 LA 接口的实用性，我们设计了 Lilac，一种参数化 HDL，它使用类型系统追踪参数对定时行为的影响，并形式化地保证每个参数化 o hazards。我们通过使用 Lilac 实现参数化设计并集成由外部工具生成的设计，展示了 Lilac 的效用。我们表明，LA 设计与可比的 LI 实现相比使用少 26–33% 的芯片资源，并达到高 6.8% 的最大频率。

## 英文关键词

Safe Hardware Description Languages; Hardware Design; Type Systems

## 中文关键词

安全硬件描述语言；硬件设计；类型系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790199)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2026](../index.md)
