---
title: "TNIC: A Trusted NIC Architecture"
description: "ASPLOS 2025 · Session 8B · TNIC：一种可信 NIC 架构"
tags:
  - "ASPLOS2025"
  - "Session 8B"
  - "Networking"
---

# TNIC: A Trusted NIC Architecture

**中文标题：** TNIC：一种可信 NIC 架构

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Dimitra Giantsidi (The University of Edinburgh), Julian Pritzi (Technical University of Munich), Felix Gust (Technical University of Munich), Antonios Katsarakis (Huawei Research), Atsushi Koshiba (Technical University of Munich), Pramod Bhatotia (Technical University of Munich)

**单位：** The University of Edinburgh；Technical University of Munich；Huawei Research

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716277) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

We introduce tnic, a trusted NIC architecture for building trustworthy distributed systems deployed in heterogeneous, untrusted (Byzantine) cloud environments. tnic builds a minimal, formally verified, silicon root-of-trust at the network interface level. We strive for three primary design goals: (1) a host CPU-agnostic unified security architecture by providing trustworthy network-level isolation; (2) a minimalistic and verifiable TCB based on a silicon root-of-trust by providing two core properties of transferable authentication and non-equivocation; and (3) a hardware-accelerated trustworthy network stack leveraging SmartNICs. Based on the tnic architecture and associated network stack, we present a generic set of programming APIs and a recipe for building high-performance, trustworthy, distributed systems for Byzantine settings. We formally verify the safety and security properties of our tnic while demonstrating its use by building four trustworthy distributed systems. Our evaluation of tnic shows up to 6× performance improvement compared to CPU-centric TEE systems.

## 中文摘要

我们提出 tnic，一种可信 NIC 架构，用于在异构、不可信（拜占庭）的云环境中构建可信的分布式系统。tnic 在网络接口层构建了一个最小化、经过形式化验证的硅信任根。我们力求实现三个主要设计目标：(1) 通过提供可信的网络级隔离，构建与主机 CPU 无关的统一安全架构；(2) 基于硅信任根构建极简且可验证的 TCB，提供可转移认证（transferable authentication）与不可抵赖（non-equivocation）两项核心属性；(3) 利用 SmartNIC 构建硬件加速的可信网络栈。基于 tnic 架构及相应的网络栈，我们给出了一组通用编程 API，以及一套为拜占庭场景构建高性能可信分布式系统的配方。我们对 tnic 的功能安全（safety）与安全（security）属性进行了形式化验证，并通过构建四个可信分布式系统展示了它的用途。对 tnic 的评估显示，与以 CPU 为中心的 TEE 系统相比，其性能最高提升 6 倍。

## 英文关键词

trusted computing, hardware-software co-design

## 中文关键词

可信计算；软硬件协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716277)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2025](../index.md)
