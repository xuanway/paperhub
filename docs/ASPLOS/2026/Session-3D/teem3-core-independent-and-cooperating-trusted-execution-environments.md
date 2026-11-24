---
title: "TEEM³: Core-Independent and Cooperating Trusted Execution Environments"
description: "ASPLOS 2026 · Session 3D · TEEM³：核无关且可协作的可信执行环境"
tags:
  - "ASPLOS2026"
  - "Session 3D"
  - "Trusted Execution Environments"
---

# TEEM³: Core-Independent and Cooperating Trusted Execution Environments

**中文标题：** TEEM³：核无关且可协作的可信执行环境

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Nils Asmussen (Barkhausen Institut), Sebastian Haas (Barkhausen Institut), Carsten Weinhold (Barkhausen Institut), Nicholas Gordon (Barkhausen Institut), Stephan Gerhold (TU Dresden), Friedrich Pauls (Barkhausen Institut), Nilanjana Das (Barkhausen Institut), Michael Roitzsch (Barkhausen Institut)

**单位：** Barkhausen Institut；TU Dresden

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790232) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Trusted Execution Environments (TEEs) enable secure code execution on machines that are not fully trusted by the user who runs the workload. However, existing TEE solutions mostly target CPUs and are typically tied to one specific instruction set architecture. Although some accelerators also provide support for TEEs, this leads to multiple, different TEE implementations on the same system, increasing its complexity and trusted computing base (TCB). This challenge becomes particularly apparent when workloads span heterogeneous processing units, because the diversity of TEE implementations complicates the creation of secure communication channels between the individual TEEs. In this paper, we present TeeM3, a trusted execution architecture with discrete, out-of-core enforcement, which is core-independent and better-suited to heterogeneous systems than existing approaches. We build upon M3 and extend both the hardware platform and operating system (OS). On the OS side, we add a root of trust (RoT) for remote attestation and a unikernel-like library for TEEs. On the hardware side, we add two lightweight isolation mechanisms to protect both TEEs and the RoT from other components in the system. Furthermore, TeeM3 inherits uniform communication channels from M3 and protects them to support communicating groups of TEEs. We show in the evaluation that our approach has low performance overhead, modest additional hardware costs, and reduces the hardware TCB by a factor of 1.8 and the software TCB by a factor of 3.42.

## 中文摘要

可信执行环境（TEE）使得在并非完全被运行工作负载的用户所信任的机器上安全地执行代码成为可能。然而，现有的 TEE 方案大多针对 CPU，并且通常绑定于某一种特定的指令集架构。尽管一些加速器也提供对 TEE 的支持，但这导致同一系统上出现多个不同的 TEE 实现，增加了系统的复杂性和可信计算基（TCB）。当工作负载跨越异构处理单元时，这一挑战尤为明显，因为 TEE 实现的多样性使得在各个 TEE 之间创建安全通信通道变得复杂。在本文中，我们提出 TeeM3，一种采用离散式核外强制机制的可信执行架构，它独立于核，并且比现有方法更适合异构系统。我们基于 M3 构建，并同时扩展硬件平台和操作系统（OS）。在 OS 侧，我们为远程证明添加了可信根（RoT），并为 TEE 添加了一个类 unikernel 的库。在硬件侧，我们添加了两种轻量级隔离机制，以保护 TEE 和 RoT 免受系统中其他组件的影响。此外，TeeM3 继承了 M3 的统一通信通道并对其加以保护，以支持相互通信的 TEE 组。我们在评估中表明，我们的方法性能开销低、额外硬件成本适中，并将硬件 TCB 缩减了 1.8 倍、软件 TCB 缩减了 3.42 倍。

## 英文关键词

Trusted Execution Environments, Operating Systems, Hardware-Software Co-Design, Accelerators

## 中文关键词

可信执行环境；操作系统；软硬件协同设计；加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790232)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2026](../index.md)
