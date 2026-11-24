---
title: "Protecting Cryptographic Code Against Spectre-RSB"
description: "ASPLOS 2025 · Session 7C · 保护密码代码免受 Spectre-RSB 攻击"
tags:
  - "ASPLOS2025"
  - "Session 7C"
  - "Side Channels"
---

# Protecting Cryptographic Code Against Spectre-RSB

**中文标题：** 保护密码代码免受 Spectre-RSB 攻击

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Santiago Arranz Olmos (MPI-SP), Gilles Barthe (MPI-SP, IMDEA Software Institute), Chitchanok Chuengsatiansup (University of Melbourne), Benjamin Gregoire (Inria), Vincent Laporte (Université de Lorraine, CNRS, Inria, LORIA), Tiago Oliveira (Sandbox AQ), Peter Schwabe (MPI-SP,Radboud University), Yuval Yarom (Ruhr University Bochum), Zhiyuan Zhang (MPI-SP)

**单位：** MPI-SP；MPI-SP, IMDEA Software Institute；University of Melbourne；Inria；Université de Lorraine, CNRS, Inria, LORIA；Sandbox AQ；MPI-SP,Radboud University；Ruhr University Bochum

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716015) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Spectre attacks void the guarantees of constant-time cryptographic code by leaking secrets during speculative execution. Recent research shows that such code can be protected from Spectre-v1 attacks with minimal overhead, but leaves open the question of protecting against other Spectre variants. In this work, we design, validate, implement, and verify a new approach to protect cryptographic code against all known classes of Spectre attacks, in particular Spectre-RSB. Our approach combines a new value-dependent information-flow type system that ensures that no secrets leak even under speculative execution and a compiler transformation that enables it on the generated low-level code. We first prove the soundness of the type system and the correctness of the compiler transformation using the Coq proof assistant. We then implement our approach in the Jasmin framework for high-assurance cryptography and demonstrate that the overhead incurred by all Spectre protections is below 2% for most cryptographic primitives and ost-quantum key-encapsulation mechanism Kyber.

## 中文摘要

Spectre 攻击通过在推测执行期间泄漏机密，使常时（constant-time）密码代码的保证失效。近期研究表明，此类代码可以以极小的开销获得针对 Spectre-v1 攻击的防护，但如何防护其他 Spectre 变体仍是未解问题。在本工作中，我们设计、验证、实现并形式化验证了一种新方法，用于保护密码代码免受所有已知类别的 Spectre 攻击，特别是 Spectre-RSB。我们的方法结合了一个新的值相关信息流类型系统（确保即使在推测执行下也不会泄漏机密）与一个编译器变换（使该类型系统在生成的低层代码上生效）。我们首先使用 Coq 证明助手证明该类型系统的可靠性与该编译器变换的正确性。随后我们在面向高保障密码学的 Jasmin 框架中实现了该方法，并证明对于大多数密码原语以及后量子密钥封装机制 Kyber，所有 Spectre 防护所带来的开销均低于 2%。

## 英文关键词

Spectre-RSB, Type system, Compiler, Speculative execution, Coq

## 中文关键词

Spectre-RSB；类型系统；编译器；推测执行；Coq

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716015)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2025](../index.md)
