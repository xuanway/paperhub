---
title: "Exo 2: Growing a Scheduling Language"
description: "ASPLOS 2025 · Session 6B · Exo 2：可生长的调度语言"
tags:
  - "ASPLOS2025"
  - "Session 6B"
  - "Compilers & Languages"
---

# Exo 2: Growing a Scheduling Language

**中文标题：** Exo 2：可生长的调度语言

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yuka Ikarashi (MIT CSAIL), Kevin Qian (MIT CSAIL), Samir Droubi (MIT CSAIL), Alex Reinking (Adobe), Gilbert Louis Bernstein (University of Washington), Jonathan Ragan-Kelley (MIT CSAIL)

**单位：** MIT CSAIL；Adobe；University of Washington

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707218) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

User-schedulable languages (USLs) help programmers productively optimize programs by providing safe means of transforming them. Current USLs are designed to give programmers exactly the control they want, while automating all other concerns. However, there is no universal answer for what performance-conscious programmers want to control, how they want to control it, and what they want to automate, even in relatively narrow domains. We claim that USLs should, instead, be designed to grow. We present Exo 2, a scheduling language that enables users to de￿ne new scheduling operations externally to the compiler. By composing a set of trusted, ￿ne-grained primitives, users can safely write their own scheduling library to build up desired automation. We identify actions (ways of modifying code), inspection (ways of interrogating code), and references (ways of pointing to code) as essential for any user-extensible USL. We fuse these ideas into a new mechanism called Cursors that enables the creation of scheduling libraries in user code. We demonstrate libraries that amortize scheduling e￿ort across more than 80 high-performance kernels, reducing total scheduling code by an order of magnitude and delivering performance competitive with state-of-the-art implementations on three di￿erent platforms.

## 中文摘要

用户可调度语言（user-schedulable languages, USL）通过提供安全地变换程序的手段，帮助程序员高效地优化程序。当前的 USL 被设计为恰好给予程序员他们想要的控制权，同时自动化所有其他关注点。然而，即使是在相对狭窄的领域内，对于注重性能的程序员想要控制什么、希望以何种方式控制，以及想要自动化什么，都不存在普适的答案。我们主张，USL 应当被设计为可生长的。我们提出 Exo 2，一种调度语言，使用户能够在编译器之外定义新的调度操作。通过组合一组可信的细粒度原语，用户可以安全地编写自己的调度库，以构建所需的自动化。我们指出，动作（修改代码的方式）、检查（查询代码的方式）以及引用（指向代码的方式）对于任何用户可扩展的 USL 都是必不可少的。我们将这些思想融合为一种称为 Cursors 的新机制，使得在用户代码中创建调度库成为可能。我们展示了这些库可在 80 多个高性能内核上摊销调度开销，将调度代码总量减少一个数量级，并在三个不同平台上取得与最先进实现相竞争的性能。

## 英文关键词

user-schedulable languages, meta-programming, performance engineering, high-performance computing

## 中文关键词

用户可调度语言；元编程；性能工程；高性能计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707218)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2025](../index.md)
