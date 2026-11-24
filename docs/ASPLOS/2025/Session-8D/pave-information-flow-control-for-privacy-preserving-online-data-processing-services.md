---
title: "Pave: Information Flow Control for Privacy-preserving Online Data Processing Services"
description: "ASPLOS 2025 · Session 8D · Pave：面向隐私保护在线数据处理服务的信息流控制"
tags:
  - "ASPLOS2025"
  - "Session 8D"
  - "Security"
---

# Pave: Information Flow Control for Privacy-preserving Online Data Processing Services

**中文标题：** Pave：面向隐私保护在线数据处理服务的信息流控制

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Minkyung Park (University of Texas at Dallas), Jaeseung Choi (Sogang University), Hyeonmin Lee (University of Virginia), Taekyoung Kwon (Seoul National University)

**单位：** University of Texas at Dallas；Sogang University；University of Virginia；Seoul National University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716266) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In online data-processing services, a user typically hands over personal data to a remote server beyond the user's control. In such environments, the user cannot be assured that the data is protected from potential leaks. We introduce Pave, a new framework to guarantee data privacy while being processed remotely. Pave provides an arbitrary data-processing program with a sandboxed execution environment. The runtime monitor, PaveBox, intercepts all data flows into and out of the sandbox, allowing them only if they do not compromise user data. At the same time, it guarantees that the benign flows will not be hampered to preserve the program's functionality. As the PaveBox is built on top of Intel SGX, a user can verify the integrity and confidentiality of the PaveBox by remote attestation. We provide a formal model of Pave and prove its security and carry out the quantitative analysis with prototype-based experiments.

## 中文摘要

在在线数据处理服务中，用户通常将个人数据交给其无法控制的远程服务器。在此类环境中，用户无法确保数据不会发生潜在泄漏并得到保护。我们提出 Pave，一个新框架，用于在数据被远程处理时保障其隐私。Pave 为任意数据处理程序提供沙箱化执行环境。运行时监控器 PaveBox 拦截进出沙箱的所有数据流，仅当这些数据流不会危害用户数据时才予以放行。与此同时，它保证良性数据流不会受到阻碍，以维持程序的功能。由于 PaveBox 构建在 Intel SGX 之上，用户可通过远程认证验证 PaveBox 的完整性与机密性。我们给出了 Pave 的形式化模型并证明了其安全性，并通过基于原型的实验开展了定量分析。

## 英文关键词

Privacy-preserving Computation, Intel SGX, Secure Multi-Execution, Software Fault Isolation

## 中文关键词

隐私保护计算；Intel SGX；安全多重执行；软件故障隔离

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716266)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2025](../index.md)
