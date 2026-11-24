---
title: "HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC"
description: "ISCA 2026 · Session 2B · HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC"
tags:
  - "ISCA2026"
  - "Session 2B"
  - "Memory Systems and PIM/PNM"
---

# HBM-CASO: A Coordinated Approach to HBM System-Level and On-Die ECC

**中文标题：** HBM-CASO: HBM 系统级与片上 ECC 的协同方法

**所属 Session：** [Session 2B](index.md) · [ISCA 2026](../index.md)

**作者：** Ruizhi Zhu, Yanan Guo, Huize Li, Weidong Cao, Qian Lou, Xin Xin

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

HBM (High-Bandwidth Memory) has progressively strengthened its reliability by employing more advanced ECC (Error Correction Code) techniques, such as Reed-Solomon (RS) codes, to meet the increasing reliability challenges raised from continued technology scaling. Over time, the protection paradigm has shifted from a system-centric approach (i.e., system ECC), where the processor primarily manages error correction, to a memory-centric approach (i.e., on-die ECC), where HBM handles errors independently. Although this shift generally reduces the ECC burden on the processor side, it constrains the flexibility to implement stronger protection schemes, particularly when the processor is capable of supporting more advanced ECC. To address this problem, we propose HBM-CASO, a new protection mode designed to accommodate advanced system ECC. It strategically reorganizes the on-die ECC resources to generate a stronger on-die codeword as a supplement to the system ECC. Furthermore, due to limited on-die computing resources, HBM cannot directly verify the advanced system ECC. HBM-CASO therefore introduces a delayed verification strategy, which accumulates on-die parity across a batch of writes, rather than verifying each write individually, and validates the entire batch as a whole. Our extensive evaluation results demonstrate that HBM-CASO has effectively enhanced error correction capability, allowing the system to correct a broader range of error patterns with minimal performance and bandwidth overhead.

## 中文摘要

高带宽存储器（HBM）通过采用更先进的纠错码（ECC）技术（如里德-所罗门码）不断增强其可靠性，以应对持续工艺缩放带来的日益严峻的可靠性挑战。长期以来，保护范式已从以处理器为中心的方法（即系统ECC，处理器主要负责纠错）转变为以存储器为中心的方法（即片上ECC，HBM独立处理错误）。尽管这种转变通常减轻了处理器侧的ECC负担，但它限制了实施更强保护方案的灵活性，尤其是在处理器能够支持更高级ECC的情况下。为解决这一问题，我们提出HBM-CASO，一种旨在适配高级系统ECC的新型保护模式。它战略性地重组片上ECC资源，生成更强的片上码字作为系统ECC的补充。此外，由于片上计算资源有限，HBM无法直接验证高级系统ECC。因此，HBM-CASO引入了一种延迟验证策略，该策略累积一批写操作的片上校验信息，而非逐个验证，并对整个批次进行整体校验。大量评估结果表明，HBM-CASO有效增强了纠错能力，使系统能够以最小的性能和带宽开销纠正更广泛的错误模式。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2B](index.md) · [返回 ISCA 2026](../index.md)
