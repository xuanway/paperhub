---
title: "Snowplow: Effective Kernel Fuzzing with a Learned White-box Test Mutator"
description: "ASPLOS 2025 · Session 7D · Snowplow：借助学习式白盒测试变异器实现高效内核模糊测试"
tags:
  - "ASPLOS2025"
  - "Session 7D"
  - "Fuzz Testing"
---

# Snowplow: Effective Kernel Fuzzing with a Learned White-box Test Mutator

**中文标题：** Snowplow：借助学习式白盒测试变异器实现高效内核模糊测试

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sishuai Gong (Purdue University), Wang Rui (Purdue University), Deniz Altinbüken (Google DeepMind), Pedro Fonseca (Purdue University), Petros Maniatis (Google DeepMind)

**单位：** Purdue University；Google DeepMind

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716019) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Kernel fuzzers rely heavily on program mutation to automatically generate new test programs based on existing ones. In particular, program mutation can alter the test's control and data flow inside the kernel by inserting new system calls, changing the values of call arguments, or performing other program mutations. However, due to the complexity of the kernel code and its user-space interface, finding the effective mutation that can lead to the desired outcome such as increasing the coverage and reaching a target code location is extremely difficult, even with the widespread use of manually-crafted heuristics. This work proposes Snowplow, a kernel fuzzer that uses a learned white-box test mutator to enhance test mutation. The core of Snowplow is an efficient machine learning model that can learn to predict promising mutations given the test program to mutate, its kernel code coverage, and the desired coverage. Snowplow is demonstrated on argument mutations of the kernel tests, and evaluated on recent Linux kernel releases. When fuzzing the kernels for 24 hours, Snowplow shows a significant speedup of discovering new coverage (4.8×∼5.2×) and achieves higher overall coverage (7.0%∼8.6%). In a 7-day fuzzing campaign, Snowplow discovers 86 previously-unknown crashes. Furthermore, the learned mutator is shown to accelerate directed kernel fuzzing by reaching 19 target code locations 8.5× faster and two additional locations that are missed by the state-of-the-art directed kernel fuzzer.

## 中文摘要

内核模糊测试器高度依赖程序变异，在已有测试程序的基础上自动生成新的测试程序。具体而言，程序变异可以通过插入新的系统调用、修改调用参数的取值或执行其他程序变异，改变测试程序在内核中的控制流与数据流。然而，由于内核代码及其用户态接口的复杂性，即便手工构造的启发式规则已被广泛使用，要找到能够带来预期结果（例如提高覆盖率、到达目标代码位置）的有效变异仍然极其困难。本文提出 Snowplow，一种使用学习式白盒测试变异器来增强测试变异的内核模糊测试器。Snowplow 的核心是一个高效的机器学习模型，它能够根据待变异的测试程序、其内核代码覆盖率以及期望达到的覆盖率，学习预测有前景的变异。Snowplow 在内核测试的参数变异上进行了演示，并在近期的 Linux 内核版本上进行了评估。在对内核进行 24 小时模糊测试时，Snowplow 在发现新覆盖率方面展现出显著加速（4.8×∼5.2×），并取得更高的总体覆盖率（7.0%∼8.6%）。在为期 7 天的模糊测试活动中，Snowplow 发现了 86 个此前未知的崩溃。此外，学习式变异器还被证明能加速定向内核模糊测试：它以快 8.5 倍的速度到达 19 个目标代码位置，并额外到达了最先进的定向内核模糊测试器所遗漏的两个位置。

## 英文关键词

Kernel fuzzing, Operating systems reliability and security, Software testing and debugging

## 中文关键词

内核模糊测试；操作系统可靠性与安全；软件测试与调试

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716019)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2025](../index.md)
