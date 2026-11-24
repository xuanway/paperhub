---
title: "Debugger Toolchain Validation via Cross-Level Debugging"
description: "ASPLOS 2025 · Session 6D · 基于跨层级调试的调试器工具链验证"
tags:
  - "ASPLOS2025"
  - "Session 6D"
  - "Testing"
---

# Debugger Toolchain Validation via Cross-Level Debugging

**中文标题：** 基于跨层级调试的调试器工具链验证

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yibiao Yang (State Key Laboratory for Novel Software Technology, Nanjing University), Maolin Sun (State Key Laboratory for Novel Software Technology, Nanjing University), Jiangchang Wu (State Key Laboratory for Novel Software Technology, Nanjing University), Qingyang Li (State Key Laboratory for Novel Software Technology, Nanjing University), Yuming Zhou (State Key Laboratory for Novel Software Technology, Nanjing University)

**单位：** State Key Laboratory for Novel Software Technology, Nanjing University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707271) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Ensuring the correctness of debugger toolchains is of paramount importance, as they play a vital role in understanding and resolving programming errors during software development. Bugs hidden within these toolchains can significantly mislead developers. Unfortunately, comprehensive testing of debugger toolchains is lacking due to the absence of effective test oracles. Existing studies on debugger toolchain validation have primarily focused on validating the debug information within optimized executables by comparing the traces between debugging optimized and unoptimized executables (i.e., different executables) in the debugger, under the assumption that the traces obtained from debugging unoptimized executables serve as a reliable oracle. However, these techniques suffer from inherent limitations, as compiler optimizations can drastically alter source code elements, variable representations, and instruction order, rendering the traces obtained from debugging different executables incomparable and failing to uncover bugs in debugger toolchains when debugging unoptimized executables. To address these limitations, we propose a novel concept called Cross-Level Debugging (CLD) for validating the debugger toolchain. CLD compares the traces obtained from debugging the same executable using source-level and instruction-level strategies within the same debugger. The core insight of CLD is that the execution traces obtained from different debugging levels for the same executable should adhere to specific relationships, regardless of whether the executable Attribution International 4.0 License.. We formulate three key relations in CLD: reachability preservation of program locations, order preservation for reachable program locations, and value consistency at program locations, which apply to traces at different debugging levels. We implement Devil, a practical framework that employs these relations for debugger toolchain validation. We evaluate the effectiveness of Devil using two widely used production debugger toolchains, GDB and LLDB. Ultimately, Devil successfully identified 27 new bug reports, of which 18 have been confirmed and 12 have been fixed by developers.

## 中文摘要

确保调试器工具链的正确性至关重要，因为它们在软件开发过程中理解和排查程序错误方面发挥着关键作用。隐藏在这些工具链中的缺陷会严重误导开发者。遗憾的是，由于缺乏有效的测试预言，调试器工具链的全面测试仍然不足。已有关于调试器工具链验证的研究主要关注验证优化后可执行文件中的调试信息，其做法是在调试器中比较优化与未优化可执行文件（即不同的可执行文件）之间的轨迹，并假设从未优化可执行文件调试得到的轨迹可作为可靠的预言。然而，这些技术存在固有局限：编译器优化会大幅改变源代码元素、变量表示与指令顺序，使得从不同可执行文件调试得到的轨迹无法比较，并且无法在调试未优化可执行文件时发现调试器工具链中的缺陷。为克服这些局限，我们提出一种用于验证调试器工具链的新概念——跨层级调试（CLD）。CLD 在同一调试器内使用源码级与指令级策略调试同一可执行文件，并比较所得的轨迹。CLD 的核心洞见在于：对同一可执行文件从不同调试层级获得的执行轨迹应当遵循特定关系，无论该可执行文件是否经过优化。我们在 CLD 中形式化了三条关键关系：程序位置的可达性保持、可达程序位置的顺序保持，以及程序位置处的取值一致性，这些关系适用于不同调试层级的轨迹。我们实现了 Devil——一个利用这些关系进行调试器工具链验证的实用框架。我们使用两款广泛使用的生产级调试器工具链 GDB 与 LLDB 评估了 Devil 的有效性。最终，Devil 成功识别出 27 个新的缺陷报告，其中 18 个已得到确认，12 个已被开发者修复。

## 英文关键词

Debugger, Validation, Cross-Level Debugging

## 中文关键词

调试器；验证；跨层级调试

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707271)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2025](../index.md)
