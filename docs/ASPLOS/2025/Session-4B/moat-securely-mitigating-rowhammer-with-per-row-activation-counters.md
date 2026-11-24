---
title: "MOAT: Securely Mitigating Rowhammer with Per-Row Activation Counters"
description: "ASPLOS 2025 · Session 4B · MOAT：利用逐行激活计数器安全地缓解 Rowhammer"
tags:
  - "ASPLOS2025"
  - "Session 4B"
  - "Memory & Storage"
---

# MOAT: Securely Mitigating Rowhammer with Per-Row Activation Counters

**中文标题：** MOAT：利用逐行激活计数器安全地缓解 Rowhammer

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Moinuddin Qureshi (Georgia Institute of Technology), Salman Qazi (Google)

**单位：** Georgia Institute of Technology；Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707278) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Rowhammer has worsened over the last decade. Existing in-DRAM solutions, such as TRR, were broken with simple patterns. In response, the DDR5 specifications have been extended to support Per-Row Activation Counting (PRAC), with counters inlined with each row, and ALERT-Back-Off (ABO) to stop the memory controller if the DRAM needs more time to mitigate. Although PRAC+ABO represents a strong advance in Rowhammer protection, they are just a framework, and the actual security is dependent on the implementation. In this paper, we first show that a prior work, Panopticon (which formed the basis for PRAC+ABO), is insecure, as our Jailbreak pattern can cause 1150 activations on an attack row for Panopticon configured for a threshold of 128. We then propose MOAT, a provably secure design, which uses two internal thresholds: ETH, an Eligibility Threshold for mitigating a row, and ATH, an ALERT Threshold for initiating an ABO. As JEDEC specifications permit a few activations between consecutive ALERTs, we also study how an attacker can exploit such activations to inflict more activations than ATH on an attack row and thus increase the tolerated Rowhammer threshold. Our analysis shows that MOAT configured with ATH=64 can safely tolerate a Rowhammer threshold of 99. Finally, we also study performance attacks and denialof-service due to ALERTs. Our evaluations, with SPEC and GAP workloads, show that MOAT with ATH=64 incurs an average slowdown of 0.27% and 7 bytes of SRAM per bank.

## 中文摘要

过去十年间 Rowhammer 问题不断恶化。现有的 DRAM 内解决方案（如 TRR）已被简单的访存模式攻破。作为应对，DDR5 规范已扩展支持逐行激活计数（Per-Row Activation Counting，PRAC），将计数器内联在每一行中，并支持 ALERT-Back-Off（ABO）：当 DRAM 需要更多时间进行缓解时暂停内存控制器。尽管 PRAC+ABO 代表了 Rowhammer 防护的一项重大进步，但它们只是一个框架，实际安全性取决于具体实现。本文首先表明，先前工作 Panopticon（它构成了 PRAC+ABO 的基础）是不安全的：对于阈值配置为 128 的 Panopticon，我们的 Jailbreak 模式可以在一条攻击行上造成 1150 次激活。随后我们提出 MOAT，一种可证明安全的设计，它使用两个内部阈值：ETH，即用于缓解某一行的资格阈值（Eligibility Threshold），以及 ATH，即用于发起 ABO 的 ALERT 阈值。由于 JEDEC 规范允许在连续两次 ALERT 之间存在少量激活，我们还研究了攻击者如何利用这些激活，在一条攻击行上造成超过 ATH 的激活次数，从而提高可容忍的 Rowhammer 阈值。我们的分析表明，配置 ATH=64 的 MOAT 可以安全地容忍 99 的 Rowhammer 阈值。最后，我们还研究了性能攻击以及由 ALERT 引起的拒绝服务问题。我们使用 SPEC 和 GAP 工作负载的评估表明，配置 ATH=64 的 MOAT 平均仅带来 0.27% 的性能下降，并且每个 bank 仅需 7 字节 SRAM。

## 英文关键词

DRAM, Rowhammer, Security, PRAC, ABO, DOS

## 中文关键词

DRAM；Rowhammer；安全性；PRAC；ABO；DOS

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707278)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2025](../index.md)
