---
title: "TAOPT: Tool-Agnostic Optimization of Parallelized Automated Mobile UI Testing"
description: "ASPLOS 2025 · Session 6D · TAOPT：并行化自动化移动 UI 测试的工具无关优化"
tags:
  - "ASPLOS2025"
  - "Session 6D"
  - "Testing"
---

# TAOPT: Tool-Agnostic Optimization of Parallelized Automated Mobile UI Testing

**中文标题：** TAOPT：并行化自动化移动 UI 测试的工具无关优化

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Dezhi Ran (Key Lab of HCST (PKU), MOE; SCS, Peking University), Zihe Song (University of Texas at Dallas), Wenyu Wang (University of Illinois at Urbana-Champaign), Wei Yang (University of Texas at Dallas), Tao Xie (Key Lab of HCST (PKU), MOE; SCS, Peking University)

**单位：** PKU；University of Texas at Dallas；University of Illinois at Urbana-Champaign

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716282) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The emergence of modern testing clouds, equipped with a vast array of real testing devices and high-fidelity emulators, has significantly increased the need for parallel automated mobile testing to optimally utilize the resources of testing clouds. Parallel testing aligns perfectly with the characteristic of rapid iteration cycles for mobile app development, where testing time is limited. While numerous tools have been proposed for optimizing the testing effectiveness on a single testing device, it remains an open problem to optimize the parallelization of automated mobile UI testing in terms of resource and time utilization. To optimize the parallelization of automated mobile UI testing, in this paper, we propose TaOPT, a fully automated, tool-agnostic approach, which improves the parallelization effectiveness of any given testing tool without modifying the tool's internal workflow. In particular, TaOPT conducts online analysis to infer loosely coupled UI subspaces in the App Under Test (AUT). TaOPT then manages access to these subspaces across various testing devices, guiding automated UI testing toward distinct subspaces on different devices without knowing the testing tool's internal workflow. We apply TaOPT on 18 highly popular mobile apps with three state-of-the-art automated UI testing tools for Android. Evaluation results show that TaOPT helps the tools reach comparable code coverage using 60% less testing duration and 62% less machine time than the baseline on average. In addition, TaOPT consistently enhances automated UI testing tools to detect 1.2 to 2.1 times more unique crashes given the same testing resources.

## 中文摘要

现代测试云配备了大量的真实测试设备与高保真模拟器，其兴起显著提升了对并行自动化移动测试的需求，以便最优地利用测试云的资源。并行测试与移动应用开发快速迭代周期的特点高度契合，在这一周期中测试时间十分有限。尽管已有众多工具被提出用于优化单个测试设备上的测试有效性，但如何在资源与时间利用方面优化自动化移动 UI 测试的并行化仍是一个开放问题。为优化自动化移动 UI 测试的并行化，本文提出 TaOPT，一种全自动、工具无关的方法，它能在不修改测试工具内部工作流的前提下提升任意给定测试工具的并行化效果。具体而言，TaOPT 通过在线分析推断被测应用（AUT）中松耦合的 UI 子空间。随后 TaOPT 在多个测试设备之间管理对这些子空间的访问，在不知道测试工具内部工作流的情况下，引导不同设备上的自动化 UI 测试走向不同的子空间。我们将 TaOPT 应用于 18 个高度流行的移动应用，并搭配三款面向 Android 的最先进自动化 UI 测试工具。评估结果表明，相比基线，TaOPT 平均帮助这些工具以少 60% 的测试时长和少 62% 的机器时间达到相当的代码覆盖率。此外，在相同测试资源下，TaOPT 稳定地使自动化 UI 测试工具多检测到 1.2 到 2.1 倍的唯一崩溃。

## 英文关键词

UI Testing, Mobile Testing, Parallel Testing, Android, Parallelization, Graph Partition, Online Algorithm

## 中文关键词

UI 测试；移动测试；并行测试；Android；并行化；图划分；在线算法

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716282)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2025](../index.md)
