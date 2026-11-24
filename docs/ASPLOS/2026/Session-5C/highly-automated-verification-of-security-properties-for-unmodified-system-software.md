---
title: "Highly Automated Verification of Security Properties for Unmodified System Software"
description: "ASPLOS 2026 · Session 5C · 面向未经修改的系统软件的安全属性高度自动化验证"
tags:
  - "ASPLOS2026"
  - "Session 5C"
  - "Formal Verification"
---

# Highly Automated Verification of Security Properties for Unmodified System Software

**中文标题：** 面向未经修改的系统软件的安全属性高度自动化验证

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ganxiang Yang (Columbia University), Wei Qiang (Columbia University), Yi Rong (Columbia University), Xuheng Li (Columbia University), Fanqi Yu (Columbia University), Jason Nieh (Columbia University), Ronghui Gu (Columbia University)

**单位：** Columbia University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790171) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

System software is often complex and hides exploitable security vulnerabilities. Formal verification promises bug-free software but comes with a prohibitive proof cost. We present Spoq2, the first verification framework to highly automate security verification of unmodified system software. Spoq2 is based on the observation that many security properties, such as noninterference, can be reduced to establishing inductive invariants on individual transitions of a transition system that models system software. However, directly verifying such invariants for real system code overwhelms existing SMT solvers. Spoq2 makes this possible by automatically reducing verification complexity. It decomposes transitions into individual execution paths, extends cone-of-influence analysis to the individual transition level, and eliminates irrelevant machine states, clauses, and control-flow paths before invoking the SMT solver. Spoq2 further optimizes how pointer operations are modeled and verified through pointer abstractions that eliminate expensive bit-wise operations from SMT queries. We demonstrate the effectiveness of Spoq2 by verifying security properties of four unmodified, real-world system codebases with minimal manual effort.

## 中文摘要

系统软件往往十分复杂，并隐藏着可被利用的安全漏洞。形式化验证承诺无缺陷的软件，但伴随着高昂得令人却步的证明成本。我们提出 Spoq2，这是首个能够高度自动化地对未经修改的系统软件进行安全验证的验证框架。Spoq2 基于这样一个观察：许多安全属性（如非干涉性）都可归约为在建模系统软件的迁移系统的各个迁移上建立归纳不变式。然而，直接对真实系统代码验证此类不变式会让现有的 SMT 求解器不堪重负。Spoq2 通过自动降低验证复杂度使这一点成为可能。它将迁移分解为单条执行路径，将影响锥分析扩展到单条迁移的层面，并在调用 SMT 求解器之前消除无关的机器状态、子句和控制流路径。Spoq2 还通过指针抽象消除 SMT 查询中昂贵的位级运算，从而进一步优化指针操作的建模与验证方式。我们通过以极少的人工投入验证四个未经修改的真实系统代码库的安全属性，展示了 Spoq2 的有效性。

## 英文关键词

Formal verification, system software, automated verification, security properties, SMT solvers

## 中文关键词

形式化验证；系统软件；自动化验证；安全属性；SMT 求解器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790171)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2026](../index.md)
