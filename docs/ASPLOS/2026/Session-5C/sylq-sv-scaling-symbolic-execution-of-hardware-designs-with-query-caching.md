---
title: "SylQ-SV: Scaling Symbolic Execution of Hardware Designs with Query Caching"
description: "ASPLOS 2026 · Session 5C · SylQ-SV：利用查询缓存扩展硬件设计的符号执行"
tags:
  - "ASPLOS2026"
  - "Session 5C"
  - "Formal Verification"
---

# SylQ-SV: Scaling Symbolic Execution of Hardware Designs with Query Caching

**中文标题：** SylQ-SV：利用查询缓存扩展硬件设计的符号执行

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Kaki Ryan (University of North Carolina at Chapel Hill), Cynthia Sturton (University of North Carolina at Chapel Hill)

**单位：** University of North Carolina at Chapel Hill

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736123) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Symbolic execution of hardware designs is a path-based analysis that can deliver high quality coverage and security verification results. Unfortunately, the technique has historically struggled with the path explosion problem and, despite recent advances, remains expensive. We present SylQ-SV, a dedicated SystemVerilog symbolic execution engine that uses SMT query caching to improve execution times, reducing run time by up to 17% over the state of the art. SylQ-SV provides language support for all necessary SystemVerilog constructs, including SystemVerilog Assertions, to provide end-to-end verification workflows of the open-source designs most commonly appearing in the literature. We evaluate SylQ-SV on the OR1200 CPU, the OpenTitan SoC with Ibex core, and two SoC designs from the HACK@DAC competitions (with PULPissimo core and CVA6 core, respectively). We make the SylQ-SV source code and all data used in the evaluation publicly available.

## 中文摘要

对硬件设计的符号执行是一种基于路径的分析，能够交付高质量的覆盖率与安全验证结果。遗憾的是，该技术长期以来一直受困于路径爆炸问题，尽管近来有所进展，其开销依然高昂。我们提出 SylQ-SV，一个专用的 SystemVerilog 符号执行引擎，它使用 SMT 查询缓存来改善执行时间，相比当前最优水平将运行时间最多降低 17%。SylQ-SV 对包括 SystemVerilog 断言在内的所有必要 SystemVerilog 构造提供语言支持，从而为文献中最常见的开源设计提供端到端的验证流程。我们在 OR1200 CPU、搭载 Ibex 核的 OpenTitan SoC，以及来自 HACK@DAC 竞赛的两个 SoC 设计（分别搭载 PULPissimo 核与 CVA6 核）上评估了 SylQ-SV。我们公开了 SylQ-SV 的源代码以及评估中使用的全部数据。

## 英文关键词

symbolic execution, query caching, hardware security

## 中文关键词

符号执行；查询缓存；硬件安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736123)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 5C](index.md) · [返回 ASPLOS 2026](../index.md)
