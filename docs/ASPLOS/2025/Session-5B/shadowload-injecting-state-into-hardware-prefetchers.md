---
title: "ShadowLoad: Injecting State into Hardware Prefetchers"
description: "ASPLOS 2025 · Session 5B · ShadowLoad：向硬件预取器注入状态"
tags:
  - "ASPLOS2025"
  - "Session 5B"
  - "Microarchitecture"
---

# ShadowLoad: Injecting State into Hardware Prefetchers

**中文标题：** ShadowLoad：向硬件预取器注入状态

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Lorenz Hetterich (CISPA Helmholtz Center for Information Security), Fabian Thomas (CISPA Helmholtz Center for Information Security), Lukas Gerlach (CISPA Helmholtz Center for Information Security), Ruiyi Zhang (CISPA Helmholtz Center for Information Security), Nils Bernsdorf (CISPA Helmholtz Center for Information Security), Eduard Ebert (CISPA Helmholtz Center for Information Security), Michael Schwarz (CISPA Helmholtz Center for Information Security)

**单位：** CISPA Helmholtz Center for Information Security

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716020) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Hardware prefetchers are an optimization in modern CPUs that predict memory accesses and preemptively load the corresponding value into the cache. Previous work showed that the internal state of hardware prefetchers can act as a side channel, leaking information across security boundaries such as processes, user and kernel space, and even trusted execution environments. In this paper, we present ShadowLoad, a new attack primitive to bring inaccessible victim data into the cache by injecting state into the hardware prefetcher. ShadowLoad relies on the inner workings of the hardware stride prefetchers, which we automatically reverse-engineer using our tool StrideRE. We illustrate how ShadowLoad extends the attack surface of existing microarchitectural attacks such as Meltdown and software-based power analysis attacks like Collide+Power and how it can partially bypass L1TF mitigations on clouds, such as AWS. We further demonstrate FetchProbe, a stride prefetcher side-channel attack leaking offsets of memory accesses with sub-cache-line granularity, extending previous work on control-flow leakage. We demonstrate FetchProbe on the side-channel hardened Base64 implementation of WolfSSL, showing that even real-world side-channelhardened implementations can be attacked with our new attack.

## 中文摘要

硬件预取器是现代 CPU 中的一种优化机制，它预测内存访问并抢先将被访问的值加载到缓存中。已有研究表明，硬件预取器的内部状态可以作为侧信道，跨进程、用户态与内核态，甚至跨可信执行环境等安全边界泄漏信息。本文提出 ShadowLoad，一种新的攻击原语，通过向硬件预取器注入状态，将原本无法访问的受害者数据带入缓存。ShadowLoad 依赖硬件步长预取器的内部工作机制，我们使用工具 StrideRE 对其进行了自动化逆向工程。我们说明 ShadowLoad 如何扩展 Meltdown 等已有微体系结构攻击以及 Collide+Power 等基于软件功耗分析攻击的攻击面，以及它如何部分绕过云环境（如 AWS）上的 L1TF 缓解措施。我们进一步展示 FetchProbe，一种步长预取器侧信道攻击，能够以低于缓存行的粒度泄漏内存访问的偏移量，扩展了此前关于控制流泄漏的工作。我们在 WolfSSL 经过侧信道加固的 Base64 实现上演示了 FetchProbe，表明即使是真实世界中经过侧信道加固的实现，也可能被我们的新攻击攻破。

## 英文关键词

microarchitecture, prefetcher, side channel

## 中文关键词

微体系结构；预取器；侧信道

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716020)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2025](../index.md)
