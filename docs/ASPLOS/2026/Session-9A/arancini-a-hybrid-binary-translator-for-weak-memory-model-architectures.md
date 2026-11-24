---
title: "Arancini: A Hybrid Binary Translator for Weak Memory Model Architectures"
description: "ASPLOS 2026 · Session 9A · Arancini：面向弱内存模型架构的混合二进制翻译器"
tags:
  - "ASPLOS2026"
  - "Session 9A"
  - "Systems Profiling & Optimization"
---

# Arancini: A Hybrid Binary Translator for Weak Memory Model Architectures

**中文标题：** Arancini：面向弱内存模型架构的混合二进制翻译器

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Sebastian Reimers (Technical University of Munich (TUM)), Dennis Sprokholt (TU Delft), Martin Fink (TU Munich), Theofilos Augoustis (Technical University of Munich (TUM)), Simon Kammermeier (Technical University of Munich), Rodrigo C. O. Rocha (Huawei), Tom Spink (University of St Andrews, United Kingdom), Redha Gouicem (RWTH Aachen University), Soham Chakraborty (TU Delft), Pramod Bhatotia (TU Munich)

**单位：** Technical University of Munich (TUM)；TU Delft；TU Munich；Technical University of Munich；Huawei；University of St Andrews, United Kingdom；RWTH Aachen University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790127) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Binary translation is a powerful approach to support cross-architecture emulation of unmodified binaries in increasingly heterogeneous computing environments. However, binary translation systems face correctness issues, due to the strong-on-weak memory model mismatch (e.g., from x86-64 to Arm/RISC-V) for concurrent programs. Besides, the current landscape of binary translation systems is fundamentally limited in terms of completeness for static systems and performance for dynamic ones. To address these limitations, we propose Arancini, a hybrid binary translator system designed and implemented from the ground up that strives for correct, complete, and efficient emulation for weak memory model architectures. Our system makes three foundational contributions to achieve these design goals: ArancinIR, a unified intermediate representation for static and dynamic binary translators; a formalization of ArancinIR's memory model and formally verified mapping schemes from x86-64 to Arm and RISC-V, to ensure strong-on-weak correctness; and Arancini, a complete ‡Work done while the author was at the University of Edinburgh. §Jointly led the project. and performant hybrid binary translator, implementing the verified mapping schemes for correctness. We evaluate Arancini using a multi-threaded benchmark suite with two backends (Arm and RISC-V), and show that Arancini can be up to 5× faster than QEMU-based translators while ensuring correctness and completeness. To our knowledge, Arancini is the first hybrid binary translator whose implementation is guided by formal proofs, to ensure correct execution of strong memory guests on weak memory hosts. It is also the first translator to address mixed-sized accesses for Arm targets.

## 中文摘要

二进制翻译是一种强大的方法，用于在日益异构的计算环境中支持对未经修改的二进制文件进行跨架构模拟。然而，由于强内存模型到弱内存模型的不匹配（例如从 x86-64 到 Arm/RISC-V），二进制翻译系统在并发程序上面临正确性问题。此外，当前二进制翻译系统的格局在静态系统的完备性与动态系统的性能方面都存在根本性局限。为解决这些局限，我们提出 Arancini，一个从零开始设计与实现的混合二进制翻译系统，力求为弱内存模型架构提供正确、完备且高效的模拟。为实现这些设计目标，我们的系统做出三项基础性贡献：ArancinIR，一种面向静态与动态二进制翻译器的统一中间表示；ArancinIR 内存模型的形式化，以及从 x86-64 到 Arm 和 RISC-V 的经形式化验证的映射方案，以保证强到弱的正确性；以及 Arancini，一个完备且高性能的混合二进制翻译器，实现了经形式验证的映射方案以保证正确性。我们使用多线程基准测试套件并以两种后端（Arm 和 RISC-V）对 Arancini 进行评估，结果表明 Arancini 在保证正确性与完备性的同时，相比基于 QEMU 的翻译器最高可快 5 倍。据我们所知，Arancini 是首个实现过程由形式化证明指导的混合二进制翻译器，以确保强内存模型客户机在弱内存模型主机上的正确执行。它也是首个针对 Arm 目标处理混合大小访问的翻译器。

## 英文关键词

Binary translation; Memory models; Formal verification

## 中文关键词

二进制翻译；内存模型；形式化验证

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790127)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2026](../index.md)
