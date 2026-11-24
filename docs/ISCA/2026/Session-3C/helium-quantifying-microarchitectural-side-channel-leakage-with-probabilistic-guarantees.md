---
title: "Helium: Quantifying Microarchitectural Side-Channel Leakage with Probabilistic Guarantees"
description: "ISCA 2026 · Session 3C · Helium: Quantifying Microarchitectural Side-Channel Leakage with Probabilistic Guarantees"
tags:
  - "ISCA2026"
  - "Session 3C"
  - "Security"
---

# Helium: Quantifying Microarchitectural Side-Channel Leakage with Probabilistic Guarantees

**中文标题：** Helium: 以概率性保证量化微架构侧信道泄漏

**所属 Session：** [Session 3C](index.md) · [ISCA 2026](../index.md)

**作者：** Samantha Archer, Mohammad Rahmani Fadiheh, Caroline Trippel

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Constant-time programming ensures zero leakage of program secrets via hardware side channels by preventing secrets from being passed to unsafe instructions. However, as microarchitectures employ more data-dependent optimizations to boost performance, more instructions become unsafe, and constant-time code incurs high performance cost. A promising alternative is bounding leakage according to application-specific requirements, but principled methods for doing so remain elusive. We present Helium, a three-part framework for quantifying hardware side-channel leakage of program secrets on specific microarchitectures. First, it leverages a new metric for expressing probabilistic privacy guarantees. Second, it employs a novel formalism for encoding how arbitrary hardware side channels give rise to attacker observations. Third, it provides two analysis techniques—symbolic (precise) and simulation (conservatively approximate)—to determine whether high-leakage observations occur with sufficiently low probability for a given victim program, secret input, microarchitecture, and attacker model. Through four case studies spanning cryptographic and image processing applications, Helium demonstrates the necessity of considering both program and microarchitecture when assessing security-performance trade-offs. In one case, improved performance does not imply worse security; in another, accepting small leakage risk enables significant performance overhead reduction compared to a recent zero-leakage software side-channel defense.

## 中文摘要

常量时间编程通过阻止秘密被传入不安全的指令，确保程序秘密不会经由硬件侧信道发生任何泄漏。然而，随着微架构采用越来越多数据相关的优化来提升性能，不安全指令的数量不断增加，常量时间代码也因此承受高昂的性能代价。一种有前景的替代方案是根据应用特定需求来限定泄漏，但为此提供有原则的方法仍然难以实现。我们提出 Helium，一个由三部分组成的框架，用于量化特定微架构上程序秘密的硬件侧信道泄漏。首先，它利用一种新指标来表达概率性隐私保证。其次，它采用一种新颖的形式化方法，刻画任意硬件侧信道如何产生攻击者观测。第三，它提供两种分析技术——符号化分析（精确）与仿真（保守近似）——以判定对于给定的受害者程序、秘密输入、微架构和攻击者模型，高泄漏观测是否以足够低的概率出现。通过涵盖密码学与图像处理应用的四个案例研究，Helium 表明在评估安全与性能权衡时必须同时考虑程序与微架构。在其中一个案例中，性能提升并不意味着安全性变差；在另一个案例中，与近期一种零泄漏的软件侧信道防御相比，接受较小的泄漏风险可以显著降低性能开销。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：samanthaarcher0/Helium-Artifact](https://github.com/samanthaarcher0/Helium-Artifact)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2026](../index.md)
