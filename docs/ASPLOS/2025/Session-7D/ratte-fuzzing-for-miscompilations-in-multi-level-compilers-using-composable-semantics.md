---
title: "Ratte: Fuzzing for Miscompilations in Multi-Level Compilers Using Composable Semantics"
description: "ASPLOS 2025 · Session 7D · Ratte：基于可组合语义的多级编译器误编译模糊测试"
tags:
  - "ASPLOS2025"
  - "Session 7D"
  - "Fuzz Testing"
---

# Ratte: Fuzzing for Miscompilations in Multi-Level Compilers Using Composable Semantics

**中文标题：** Ratte：基于可组合语义的多级编译器误编译模糊测试

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Pingshi Yu (Imperial College London), Nicolas Wu (Imperial College London), Alastair F. Donaldson (Imperial College London)

**单位：** Imperial College London

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716270) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Multi-level intermediate representation (MLIR) is a rapidly growing compiler framework, with its defining feature being an ecosystem of modular language fragments called dialects. Specifying dialect semantics and validating dialect implementations presents novel challenges, as existing techniques do not cater for the modularity and composability required by MLIR. We present Ratte,1 a framework for specifying composable dialect semantics and modular dialect fuzzers. We introduce a novel technique for the development of semantics and fuzzers for MLIR dialects, enabling a harmonious cycle where the fuzzer validates the semantics via test-case generation, whilst at the same time the semantics allow the generation of high-quality test cases that are free from undefined behaviour. The composability of semantics and fuzzers allows generators to be cheaply derived to test combinations of dialects. We have used Ratte to find 6 previously-unknown miscompilation bugs in the production MLIR implementation. To our knowledge, Ratte is the first MLIR fuzzer capable of finding such bugs. Our work identified several aspects of the MLIR specification that were unclear, for which we proposed fixes that were adopted. Our technique provides composable reference interpreters for important MLIR dialects, validated against the production implementation, which can be used in future compiler development and testing research.

## 中文摘要

多级中间表示（MLIR）是一个快速发展的编译器框架，其标志性特征是被称为 dialect 的模块化语言片段生态系统。描述 dialect 语义并验证 dialect 实现带来了新的挑战，因为现有技术无法满足 MLIR 所要求的模块化与可组合性。我们提出 Ratte,1——一个用于描述可组合 dialect 语义与模块化 dialect 模糊测试器的框架。我们引入一种用于开发 MLIR dialect 语义与模糊测试器的新技术，它形成了协调的循环：模糊测试器通过测试用例生成来验证语义，同时语义又支持生成不含未定义行为的高质量测试用例。语义与模糊测试器的可组合性使得可以低成本地派生出生成器，用以测试各种 dialect 的组合。我们使用 Ratte 在生产级 MLIR 实现中发现了 6 个此前未知的误编译缺陷。据我们所知，Ratte 是首个能够发现此类缺陷的 MLIR 模糊测试器。我们的工作识别出 MLIR 规范中若干不清晰之处，并针对这些问题提出了修改建议且已被采纳。我们的技术为重要的 MLIR dialect 提供了可组合的参考解释器，并已针对生产实现进行验证，可供未来的编译器开发与测试研究使用。

## 英文关键词

Compiler testing; differential testing; fuzzing; composable semantics; MLIR

## 中文关键词

编译器测试；差分测试；模糊测试；可组合语义；MLIR

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716270)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2025](../index.md)
