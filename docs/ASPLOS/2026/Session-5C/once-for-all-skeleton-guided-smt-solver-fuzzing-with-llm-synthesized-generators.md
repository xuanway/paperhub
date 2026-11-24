---
title: "Once-for-All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators"
description: "ASPLOS 2026 · Session 5C · Once-for-All：基于骨架引导、以 LLM 合成生成器驱动的 SMT 求解器模糊测试"
tags:
  - "ASPLOS2026"
  - "Session 5C"
  - "Formal Verification"
---

# Once-for-All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators

**中文标题：** Once-for-All：基于骨架引导、以 LLM 合成生成器驱动的 SMT 求解器模糊测试

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Maolin Sun (Nanjing University), Yibiao Yang (Nanjing University), Yuming Zhou (Nanjing University)

**单位：** Nanjing University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790195) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** Once4All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators

## 英文摘要

Satisfiability Modulo Theory (SMT) solvers are foundational to modern systems and programming languages research, providing the foundation for tasks like symbolic execution and automated verification. Because these solvers sit on the critical path, their correctness is essential, and high-quality test formulas are key to uncovering bugs. However, while prior testing techniques performed well on earlier solver versions, they struggle to keep pace with rapidly evolving features. Recent approaches based on Large Language Models (LLMs) show promise in exploring advanced solver capabilities, but two obstacles remain: nearly half of the generated formulas are syntactically invalid, and iterative interactions with LLMs introduce substantial computational overhead. In this study, we present Once4All, a novel LLM-assisted fuzzing framework that addresses both issues by shifting from direct formula generation to the synthesis of generators for reusable terms (i.e., logical expressions). Specifically, Once4All uses LLMs to (1) automatically extract contextfree grammars (CFGs) for SMT theories, including solver-specific extensions, from documentation, and (2) synthesize composable Boolean term generators that adhere to these grammars. During fuzzing, Once4All populates structural skeletons derived from existing formulas with the terms iteratively produced by the LLM-synthesized generators. This design ensures syntactic validity while promoting semantic diversity. Notably, Once4All requires only one-time LLM interaction investment, dramatically reducing runtime cost. We evaluated Once4All on two leading SMT solvers: Z3 and cvc5. Our experiments show that Once4All has identified 43 confirmed bugs, 40 of which have already been fixed by developers.

## 中文摘要

可满足性模理论（SMT）求解器是现代系统与编程语言研究的基础，为符号执行与自动化验证等任务提供支撑。由于这些求解器处于关键路径之上，其正确性至关重要，而高质量的测试公式是发现缺陷的关键。然而，尽管先前的测试技术在较早的求解器版本上表现良好，它们却难以跟上快速演进的新特性。近期基于大语言模型（LLM）的方法在探索求解器高级能力方面展现出前景，但仍存在两个障碍：生成的公式中有近一半在语法上无效，以及与 LLM 的迭代交互会带来大量计算开销。在本研究中，我们提出 Once4All，一个新颖的 LLM 辅助模糊测试框架，它通过从直接生成公式转向合成可复用项（即逻辑表达式）的生成器来解决这两个问题。具体而言，Once4All 使用 LLM 来：(1) 从文档中自动抽取 SMT 理论的上下文无关文法（CFG），包括求解器特定的扩展；(2) 合成符合这些文法的可组合布尔项生成器。在模糊测试过程中，Once4All 用 LLM 合成的生成器迭代产生的项来填充从现有公式导出的结构骨架。这一设计既保证了语法有效性，又提升了语义多样性。值得注意的是，Once4All 只需一次性的 LLM 交互投入，从而大幅降低运行时开销。我们在两个主流的 SMT 求解器 Z3 与 cvc5 上评估了 Once4All。实验表明，Once4All 已发现 43 个已确认的缺陷，其中 40 个已由开发者修复。

## 英文关键词

SMT solver, Fuzzing, Large Language Models

## 中文关键词

SMT 求解器；模糊测试；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790195)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2026](../index.md)
