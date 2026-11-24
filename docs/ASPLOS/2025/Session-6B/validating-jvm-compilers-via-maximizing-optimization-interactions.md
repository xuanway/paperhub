---
title: "Validating JVM Compilers via Maximizing Optimization Interactions"
description: "ASPLOS 2025 · Session 6B · 通过最大化优化交互来验证 JVM 编译器"
tags:
  - "ASPLOS2025"
  - "Session 6B"
  - "Compilers & Languages"
---

# Validating JVM Compilers via Maximizing Optimization Interactions

**中文标题：** 通过最大化优化交互来验证 JVM 编译器

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zifan Xie (Huazhong University of Science and Technology), Ming Wen (Huazhong University of Science and Technology), Shiyu Qiu (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

**单位：** Huazhong University of Science and Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674188) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

This paper introduces the concept of optimization interaction, which refers to the practice in modern compilers where multiple optimization phases, such as inlining, loop unrolling, and dead code elimination, are not completed in a one-off sequential order while being interacted instead. Therefore, while optimizing a certain phase, the compiler needs to ensure that the results of other optimization phases will not be disrupted, as this could lead to compiler crashes or unpredictable results. To verify whether compilers can correctly handle the optimization process across various phases, we propose MopFuzzer, which aims at maximizing runtime optimization interactions during fuzzing. Specifically, it encourages the JVM to perform multi-stage optimizations and verifies the correctness of the compiler's optimized code through differential testing. Currently, MopFuzzer has implemented 13 mutators, and each is intended to trigger a certain optimization behavior. Such mutators are applied iteratively to the same program point, aiming to maximize ∗National Engineering Research Center for Big Data Technology and System, Services Computing Technology and System Lab, Huazhong University of Science and Technology (HUST), Wuhan, 430074, China †Hubei Engineering Research Center on Big Data Security, Hubei Key Laboratory of Distributed System Security, School of Cyber Science and Engineering, HUST, Wuhan, 430074, China ‡Corresponding author §Cluster and Grid Computing Lab, School of Computer Science and Technology, HUST, Wuhan, 430074, China optimization interactions. Subsequently, the testing process is guided by a novel method based on profile data, which records the optimization behaviors performed by the compiler. The guidance enables MopFuzzer to generate mutants that are able to maximize optimization behaviors and their interactions. Our evaluation has led to 59 bug reports for widely used production JVMs, OpenJDK and OpenJ9.

## 中文摘要

本文引入优化交互（optimization interaction）的概念，它指现代编译器中的多个优化阶段——例如内联、循环展开和死代码消除——并非按一次性的顺序完成，而是相互交互地进行。因此，在优化某一特定阶段时，编译器需要确保其他优化阶段的结果不会被破坏，因为否则可能导致编译器崩溃或不可预期的结果。为了验证编译器能否正确处理跨多个阶段的优化过程，我们提出 MopFuzzer，其目标是在模糊测试过程中最大化运行时的优化交互。具体而言，它促使 JVM 执行多阶段优化，并通过差分测试验证编译器优化后代码的正确性。目前，MopFuzzer 已实现 13 个变异器（mutator），每一个都旨在触发某种特定的优化行为。这些变异器被迭代地应用于同一程序点，旨在最大化（原文此处插入作者单位脚注：∗National Engineering Research Center for Big Data Technology and System, Services Computing Technology and System Lab, Huazhong University of Science and Technology (HUST), Wuhan, 430074, China †Hubei Engineering Research Center on Big Data Security, Hubei Key Laboratory of Distributed System Security, School of Cyber Science and Engineering, HUST, Wuhan, 430074, China ‡Corresponding author §Cluster and Grid Computing Lab, School of Computer Science and Technology, HUST, Wuhan, 430074, China）优化交互。随后，测试过程由一种基于 profile 数据的新方法引导，该数据记录了编译器所执行的优化行为。这种引导使 MopFuzzer 能够生成可最大化优化行为及其交互的变异体。我们的评估为广泛使用的生产级 JVM——OpenJDK 与 OpenJ9——提交了 59 个缺陷报告。

## 英文关键词

JVM, JIT Compiler, Optimization

## 中文关键词

JVM；JIT 编译器；优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674188)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2025](../index.md)
