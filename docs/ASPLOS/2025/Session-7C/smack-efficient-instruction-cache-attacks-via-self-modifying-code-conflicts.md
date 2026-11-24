---
title: "SMaCk: Efficient Instruction Cache Attacks via Self-Modifying Code Conflicts"
description: "ASPLOS 2025 · Session 7C · SMaCk：利用自修改代码冲突的高效指令缓存攻击"
tags:
  - "ASPLOS2025"
  - "Session 7C"
  - "Side Channels"
---

# SMaCk: Efficient Instruction Cache Attacks via Self-Modifying Code Conflicts

**中文标题：** SMaCk：利用自修改代码冲突的高效指令缓存攻击

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Seonghun Son (Iowa State University), Daniel Moghimi (Google), Berk Gulmezoglu (Iowa State University)

**单位：** Iowa State University；Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716274) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Self-modifying code (SMC) allows programs to alter their own instructions, optimizing performance and functionality on x86 processors. Despite its benefits, SMC introduces unique microarchitectural behaviors that can be exploited for malicious purposes. In this paper, we explore the security implications of SMC by examining how specific x86 instructions affecting instruction cache lines lead to measurable timing discrepancies between cache hits and misses. These discrepancies facilitate refined cache attacks, making them less noisy and more effective. We introduce novel attack techniques that leverage these timing variations to enhance existing methods such as Prime+Probe and Flush+Reload. Our advanced techniques allow adversaries to more precisely attack cryptographic keys and create covert channels akin to Spectre across various x86 platforms. Finally, we propose a dynamic detection methodology utilizing hardware performance counters to mitigate these enhanced threats.

## 中文摘要

自修改代码（SMC）允许程序修改自身的指令，从而在 x86 处理器上优化性能与功能。尽管有其益处，SMC 引入了独特的微架构行为，可被用于恶意目的。本文中，我们通过考察影响指令缓存行的特定 x86 指令如何在缓存命中与缺失之间导致可测量的时序差异，探讨了 SMC 的安全影响。这些差异促成了更精细的缓存攻击，使其噪声更低、更加有效。我们引入了新的攻击技术，利用这些时序变化来增强 Prime+Probe 与 Flush+Reload 等现有方法。我们的进阶技术使攻击者能够在多种 x86 平台上更精确地攻击密码密钥，并构建类似 Spectre 的隐蔽信道。最后，我们提出了一种利用硬件性能计数器进行动态检测的方法，以缓解这些增强的威胁。

## 英文关键词

Side-channel Attack; Hardware Security; Selfmodifying Code

## 中文关键词

侧信道攻击；硬件安全；自修改代码

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716274)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2025](../index.md)
