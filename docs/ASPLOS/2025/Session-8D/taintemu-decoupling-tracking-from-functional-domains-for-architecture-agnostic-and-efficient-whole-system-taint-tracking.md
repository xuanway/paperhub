---
title: "TaintEMU: Decoupling Tracking from Functional Domains for Architecture-Agnostic and Efficient Whole-System Taint Tracking"
description: "ASPLOS 2025 · Session 8D · TaintEMU：解耦跟踪域与功能域，实现架构无关且高效的全系统污点跟踪"
tags:
  - "ASPLOS2025"
  - "Session 8D"
  - "Security"
---

# TaintEMU: Decoupling Tracking from Functional Domains for Architecture-Agnostic and Efficient Whole-System Taint Tracking

**中文标题：** TaintEMU：解耦跟踪域与功能域，实现架构无关且高效的全系统污点跟踪

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Lei Cui (Guangxi Normal University), Youquan Xian (Guangxi Normal University), Peng Liu (Guangxi Normal University), Longjin Lu (Independent Researcher)

**单位：** Guangxi Normal University；Independent Researcher

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716023) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Whole-system taint tracking is vital for security analysis. However, existing methods suffer from limited architecture compatibility and significant performance overhead, mainly due to the tight coupling between the functional and tracking domains. This paper introduces TaintEMU, an architecture-agnostic and efficient solution by fully decoupling the two domains. It separates functional and tracking logic at the QEMU TCG layer, mapping shadow registers to host instead of guest registers, ensuring compatibility across guest CPU architectures. At the host layer, it physically isolates the two domains: general-purpose instructions and registers serve the functional domain, while vector resources are dedicated to tracking, avoiding host resource reuse and enhancing tracking performance. Furthermore, it directly generates tracking instructions from TCG operations on the host, bypassing additional translation and further reducing overhead. We implement TaintEMU on an AMD64 host on QEMU 8.2.2. It supports a wide range of guest architectures (x86, MIPS, ARM, AMD, RISC-V, PPC), reduces performance overhead from 301% (DECAF++) to 101% and successfully detects all vulnerabilities in tests with 8 CVEs across 7 applications.

## 中文摘要

全系统污点跟踪对安全分析至关重要。然而，现有方法受限于架构兼容性不足和显著的性能开销，其主要原因在于功能域与跟踪域之间的紧密耦合。本文提出 TaintEMU，通过完全解耦这两个域，实现了一种架构无关且高效的解决方案。它在 QEMU TCG 层将功能逻辑与跟踪逻辑分离，将影子寄存器映射到宿主机而非客户机寄存器，从而确保跨客户机 CPU 架构的兼容性。在宿主机层，它从物理上隔离这两个域：通用指令和寄存器服务于功能域，而向量资源专用于跟踪，从而避免宿主机资源复用并提升跟踪性能。此外，它直接在宿主机上从 TCG 操作生成跟踪指令，绕过额外的翻译，进一步降低开销。我们在 QEMU 8.2.2 的 AMD64 宿主机上实现了 TaintEMU。它支持广泛的客户机架构（x86、MIPS、ARM、AMD、RISC-V、PPC），将性能开销从 301%（DECAF++）降低到 101%，并成功检测出测试中横跨 7 个应用、8 个 CVE 的所有漏洞。

## 英文关键词

Taint Tracking; Decoupling; Cross architecture

## 中文关键词

污点跟踪；解耦；跨架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716023)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2025](../index.md)
