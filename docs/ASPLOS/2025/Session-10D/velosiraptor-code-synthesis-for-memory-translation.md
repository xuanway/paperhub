---
title: "Velosiraptor: Code Synthesis for Memory Translation"
description: "ASPLOS 2025 · Session 10D · Velosiraptor：面向内存转换的代码合成"
tags:
  - "ASPLOS2025"
  - "Session 10D"
  - "Memory Management"
---

# Velosiraptor: Code Synthesis for Memory Translation

**中文标题：** Velosiraptor：面向内存转换的代码合成

**所属 Session：** [Session 10D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Reto Achermann (University of British Columbia), Em Chu (JuliaHub), Ryan Mehri (Replit), Ilias Karimalis (University of British Columbia), Margo Seltzer (University of British Columbia)

**单位：** University of British Columbia；JuliaHub；Replit

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3711998) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Security is among the top concerns of operating system (OS) developers. A secure runtime environment relies on the OS to correctly configure the memory hardware on which it runs. This is mission-critical as it provides essential security-relevant features and abstractions that ensure the integrity and isolation of untrusted applications running alongside each other. Configuring a platform's memory hardware is not a one-off effort as designers constantly develop new mechanisms for translation and protection with different features and means of configuration. Adapting the OS code to the new hardware is not only a manual, repetitive and timeconsuming task, it may also introduce subtle, but security-critical bugs that break security and isolation guarantees. We present Velosiraptor, a system that automatically generates correct, low-level OS code that programs the memory hardware of a machine. Velosiraptor leverages software synthesis techniques and exploits the domain specificity of the problem to make the synthesis process efficient. With Velosiraptor, developers write only a high-level description of the memory hardware's mapping behavior and OS environment. The Velosiraptor toolchain transforms this specification into a verified implementation that can be linked directly with the rest of the operating system. Incorporating the OS environment into this process allows porting an OS to new hardware platforms without worrying about writing code to configure the memory hardware. We can also use the same specification to generate hardware components. This enables research in new translation mechanisms, freeing up OS developers from manually writing OS code.

## 中文摘要

安全是操作系统（OS）开发者最为关注的问题之一。安全的运行时环境依赖 OS 正确配置其运行所依托的内存硬件。这属于关键任务，因为它提供了与安全密切相关的必要特性与抽象，确保并行运行的不受信任应用之间的完整性与隔离性。配置平台的内存硬件并非一次性工作，因为设计者不断提出具有不同特性和配置方式的新转换与保护机制。让 OS 代码适配新硬件不仅是手工、重复且耗时的任务，还可能引入隐蔽但关乎安全的缺陷，破坏安全与隔离保证。我们提出 Velosiraptor，一个自动生成正确、底层 OS 代码来编程机器内存硬件的系统。Velosiraptor 利用软件合成技术，并借助问题的领域特性使合成过程高效。使用 Velosiraptor 时，开发者只需编写内存硬件映射行为与 OS 环境的高层描述。Velosiraptor 工具链将该规格说明转换为经过验证的实现，可直接与操作系统其余部分链接。将 OS 环境纳入这一过程，使得把 OS 移植到新硬件平台时无需担心编写配置内存硬件的代码。我们也可以使用同一规格说明生成硬件组件。这为新型转换机制的研究提供了支持，使 OS 开发者从手工编写 OS 代码中解放出来。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3711998)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10D](index.md) · [返回 ASPLOS 2025](../index.md)
