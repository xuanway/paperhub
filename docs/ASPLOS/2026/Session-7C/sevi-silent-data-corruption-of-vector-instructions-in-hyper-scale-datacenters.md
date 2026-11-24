---
title: "SEVI: Silent Data Corruption of Vector Instructions in Hyper-Scale Datacenters"
description: "ASPLOS 2026 · Session 7C · SEVI：超大规模数据中心中向量指令的静默数据损坏"
tags:
  - "ASPLOS2026"
  - "Session 7C"
  - "Testing & Fuzzing"
---

# SEVI: Silent Data Corruption of Vector Instructions in Hyper-Scale Datacenters

**中文标题：** SEVI：超大规模数据中心中向量指令的静默数据损坏

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yixuan Mei (Carnegie Mellon University), Shreya Varshini (Meta Platforms, Inc.), Harish Dattatraya Dixit (Meta Platforms, Inc.), Sriram Sankar (Meta Platforms, Inc.), Rashmi Vinayak (Carnegie Mellon University)

**单位：** Carnegie Mellon University；Meta Platforms, Inc.

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790217) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Silent Data Corruption (SDC) poses a reliability threat in modern datacenters. These insidious errors evade detections and propagate incorrect results throughout the system. Companies including Google, Meta, and Alibaba have reported SDC incidents affecting their production. In this paper, we present the first comprehensive instruction- and application-level analysis of vector instruction SDCs in hyper-scale datacenters using a two-stage approach. We perform over 78 trillion test rounds in more than 14 billion CPU seconds. Our observations reveal undocumented SDC patterns that provide insights into possible underlying causes and inspire new mitigation strategies. Based on these findings, we propose a low-overhead SDC detection mechanism leveraging in-application algorithm-based fault tolerance. Our method achieves 88% to 100% SDC machine detection rate with a time overhead of only 1.35% even for modestly sized inputs.

## 中文摘要

静默数据损坏（SDC）在现代数据中心构成可靠性威胁。这些隐蔽的错误逃避检测，并在整个系统中传播错误结果。包括 Google、Meta 和阿里巴巴在内的公司已报告了影响其生产环境的 SDC 事件。本文采用两阶段方法，首次对超大规模数据中心中向量指令的 SDC 进行全面、涵盖指令级与应用级的分析。我们执行了超过 78 万亿次测试轮次，耗时超过 140 亿 CPU 秒。我们的观察揭示了此前未记录的 SDC 模式，这些模式为可能的根本原因提供了洞见，并启发了新的缓解策略。基于这些发现，我们提出一种低开销的 SDC 检测机制，利用应用内基于算法的容错。我们的方法实现了 88% 到 100% 的 SDC 机器检测率，即使对规模适中的输入，时间开销也仅为 1.35%。

## 英文关键词

Silent Data Corruption; Datacenter Reliability; Algorithm-Based Fault Tolerance; Vector Instructions; Hardware Faults

## 中文关键词

静默数据损坏；数据中心可靠性；基于算法的容错；向量指令；硬件故障

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790217)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2026](../index.md)
