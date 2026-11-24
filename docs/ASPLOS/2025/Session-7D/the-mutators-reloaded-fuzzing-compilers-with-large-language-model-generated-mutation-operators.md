---
title: "The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators"
description: "ASPLOS 2025 · Session 7D · 变异器重装上阵：用大语言模型生成的变异算子对编译器进行模糊测试"
tags:
  - "ASPLOS2025"
  - "Session 7D"
  - "Fuzz Testing"
---

# The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators

**中文标题：** 变异器重装上阵：用大语言模型生成的变异算子对编译器进行模糊测试

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xianfei Ou (Nanjing University), Cong Li (Ant Group,Zhejiang University), Yanyan Jiang (Nanjing University), Chang Xu (Nanjing University)

**单位：** Nanjing University；Ant Group,Zhejiang University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674171) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for compiler fuzzing. It integrates our compilerdomain knowledge into prompts and processes that can best harness the capabilities of a large language model. With MetaMut, we have successfully created 118 semantic-aware mutators at approximately $0.5 each, with only moderate human effort. With these mutators, our fuzzer uncovered 131 bugs in GCC and Clang, 129 of which were confirmed or fixed. The success of MetaMut suggests that the integration of AI into software and system engineering tasks traditionally thought to require expert human intervention could be a promising research direction.

## 中文摘要

构造高质量的变异器——它是基于变异的模糊测试的核心，决定了搜索空间——极具挑战性。这需要人类的专业知识与创造力，其实现还要求掌握编译器内部机理。本文提出 MetaMut 框架，用于为编译器模糊测试开发新的、有用的变异器。它将我们的编译器领域知识融入提示与流程之中，从而最大程度地发挥大语言模型的能力。借助 MetaMut，我们仅投入适度人力，就以每个约 0.5 美元的成本成功创建了 118 个语义感知的变异器。利用这些变异器，我们的模糊测试器在 GCC 和 Clang 中发现了 131 个缺陷，其中 129 个已获确认或修复。MetaMut 的成功表明，将 AI 融入传统上被认为需要人类专家介入的软件与系统工程任务，可能是一个富有前景的研究方向。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674171)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2025](../index.md)
