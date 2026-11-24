---
title: "Cassandra: Efficient Enforcement of Sequential Execution for Cryptographic Programs"
description: "ISCA 2025 · Session 1B · Cassandra: 密码程序顺序执行高效强制"
tags:
  - "ISCA2025"
  - "Session 1B"
  - "Crypto & Fully Homomorphic Encryption"
---

# Cassandra: Efficient Enforcement of Sequential Execution for Cryptographic Programs

**中文标题：** Cassandra: 密码程序顺序执行高效强制

**所属 Session：** [Session 1B](index.md) · [ISCA 2025](../index.md)

**作者：** Ali Hajiabadi, Trevor E. Carlson

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731048) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Constant-time programming is a widely deployed approach to harden cryptographic programs against side channel attacks. However, modern processors often violate the underlying assumptions of standard constant-time policies by transiently executing unintended paths of the program. Despite many solutions proposed, addressing control flow misspeculations in an efficient way without losing performance is an open problem.

In this work, we propose Cassandra, a novel hardware/software mechanism to enforce sequential execution for constant-time cryptographic code in a highly efficient manner. Cassandra explores the radical design point of disabling the branch predictor and recording-and-replaying sequential control flow of the program. Two key insights that enable our design are that (1) the sequential control flow of a constant-time program is mostly static over different runs, and (2) cryptographic programs are loop-intensive and their control flow patterns repeat in a highly compressible way. These insights allow us to perform an upfront branch analysis that significantly compresses control flow traces. We add a small component to a typical processor design, the Branch Trace Unit, to store compressed traces and determine fetch redirections according to the sequential model of the program. Despite providing a strong security guarantee, Cassandra counterintuitively provides an average 1.85% speedup compared to an unsafe baseline processor, mainly due to enforcing near-perfect fetch redirections.

## 中文摘要

常数时间编程是一种广泛部署的方法，用于强化加密程序以抵御侧信道攻击。然而，现代处理器经常通过瞬态执行程序的非预期路径来违反标准常数时间策略的基本假设。尽管提出了许多解决方案，但在不损失性能的情况下以有效的方式解决控制流错误推测仍然是一个悬而未决的问题。在这项工作中，我们提出了 Cassandra，一种新颖的硬件/软件机制，以高效的方式强制执行常数时间加密代码的顺序执行。 Cassandra 探索了禁用分支预测器以及记录和重放程序顺序控制流的根本设计点。支持我们设计的两个关键见解是：(1) 常数时间程序的顺序控制流在不同的运行中大部分是静态的，(2) 加密程序是循环密集型的，它们的控制流模式以高度可压缩的方式重复。

这些见解使我们能够执行前期分支分析，从而显著压缩控制流轨迹。我们在典型的处理器设计中添加了一个小组件，即分支轨迹单元，以存储压缩跟踪并根据程序的顺序模型确定取指重定向。尽管提供了强大的安全保证，但与不安全的基准处理器相比，Cassandra 却提供了平均 1.85% 的加速，这与直觉相反，这主要是由于强制执行近乎完美的取指重定向。

## 英文关键词

Cryptography, constant-time programming, speculative execution, hardware/software co-design

## 中文关键词

密码学, 常量时间编程, 推测执行, 软硬件协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731048)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1B](index.md) · [返回 ISCA 2025](../index.md)
