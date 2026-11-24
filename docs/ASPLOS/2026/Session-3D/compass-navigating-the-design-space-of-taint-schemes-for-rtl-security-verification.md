---
title: "Compass: Navigating the Design Space of Taint Schemes for RTL Security Verification"
description: "ASPLOS 2026 · Session 3D · Compass：导航 RTL 安全验证的污点方案设计空间"
tags:
  - "ASPLOS2026"
  - "Session 3D"
  - "Trusted Execution Environments"
---

# Compass: Navigating the Design Space of Taint Schemes for RTL Security Verification

**中文标题：** Compass：导航 RTL 安全验证的污点方案设计空间

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yuheng Yang (MIT), Qinhan Tan (Princeton University), Thomas Bourgeat (EPFL), Sharad Malik (Princeton University), Mengjia Yan (MIT)

**单位：** MIT；Princeton University；EPFL

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790144) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hardware information flow tracking (IFT) using taint analysis provides a methodology to check whether a hardware design satisfies certain security properties. Previous work has shown a broad trade-off space between precision and complexity when using different taint analysis schemes. A careful investigation of this space has led to the insight that applying different taint schemes to different components of a hardware design can improve overall efficiency. We present Compass, a systematic framework to guide users in designing appropriate taint schemes that are as lightweight as possible while still sufficient to accomplish their security verification goals. We first establish a unified terminology to comprehensively capture existing taint schemes. We then apply counterexample-guided abstraction refinement (CEGAR) for taint refinement to iteratively improve the taint scheme. We evaluated Compass on a set of open-source RISCV processors to verify the information flow properties for speculative execution vulnerabilities, and demonstrate that Compass significantly improves both simulation speed and formal-verification scalability of taint analysis.

## 中文摘要

使用污点分析的硬件信息流追踪（IFT）提供了一种方法来检查硬件设计是否满足特定的安全性质。先前的工作已经表明，在使用不同的污点分析方案时，精度与复杂度之间存在广阔的权衡空间。对这一空间的仔细研究带来了一个洞见：将不同的污点方案应用于硬件设计的不同组件可以提升整体效率。我们提出 Compass，一个系统化框架，用于指导用户设计尽可能轻量、同时又仍足以完成其安全验证目标的合适污点方案。我们首先建立一套统一的术语体系，以全面刻画现有的污点方案。然后，我们应用反例引导的抽象精化（CEGAR）进行污点精化，以迭代地改进污点方案。我们在若干开源 RISC-V 处理器上评估 Compass，以验证针对推测执行漏洞的信息流性质，并证明 Compass 显著提升了污点分析的仿真速度和形式验证可扩展性。

## 英文关键词

Hardware Information Flow Tracking; Taint Analysis; Counterexample-guided Abstraction Refinement; Speculative Execution Attacks

## 中文关键词

硬件信息流追踪；污点分析；反例引导的抽象精化；推测执行攻击

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790144)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2026](../index.md)
