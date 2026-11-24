---
title: "DejaVuzz: Disclosing Transient Execution Bugs with Dynamic Swappable Memory and Differential Information Flow Tracking assisted Processor Fuzzing"
description: "ASPLOS 2026 · Session 7C · DejaVuzz：借助动态可交换内存与差分信息流追踪的处理器模糊测试揭示瞬态执行缺陷"
tags:
  - "ASPLOS2026"
  - "Session 7C"
  - "Testing & Fuzzing"
---

# DejaVuzz: Disclosing Transient Execution Bugs with Dynamic Swappable Memory and Differential Information Flow Tracking assisted Processor Fuzzing

**中文标题：** DejaVuzz：借助动态可交换内存与差分信息流追踪的处理器模糊测试揭示瞬态执行缺陷

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jinyan Xu (Zhejiang University), Yangye Zhou (Zhejiang University), Xingzhi Zhang (Zhejiang University), Yinshuai Li (Southern University of Science and Technology), Qinhan Tan (Princeton University), Yinqian Zhang (Southern University of Science and Technology (SUSTech)), Yajin Zhou (Zhejiang University & BlockSec), Rui Chang (Zhejiang University), Wenbo Shen (Zhejiang University)

**单位：** Zhejiang University；Southern University of Science and Technology；Princeton University；Southern University of Science and Technology (SUSTech)；Zhejiang University & BlockSec

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736115) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Transient execution vulnerabilities have emerged as a critical threat to modern processors. Hardware fuzzing testing techniques have recently shown promising results in discovering transient execution bugs in large-scale out-of-order processor designs. However, their poor microarchitectural controllability and observability prevent them from effectively and efficiently detecting transient execution vulnerabilities. This paper proposes DejaVuzz, a novel pre-silicon stage processor transient execution bug fuzzer. DejaVuzz utilizes two innovative operating primitives: dynamic swappable memory and differential information flow tracking, enabling more effective and efficient transient execution vulnerability detection. The dynamic swappable memory enables the isolation of different instruction streams within the same address space. Leveraging this capability, DejaVuzz generates targeted training for arbitrary transient windows and eliminates ineffective training, enabling efficient triggering of diverse transient windows. The differential information flow tracking aids in observing the propagation of sensitive data across the microarchitecture. Based on taints, DejaVuzz designs the taint coverage matrix to guide mutation and uses taint liveness annotations to identify exploitable leakages. Our evaluation shows that DejaVuzz outperforms the state-of-the-art fuzzer SpecDoctor, triggering more comprehensive transient windows with lower training overhead and achieving a 4.7× coverage improvement. And DejaVuzz also mitigates control flow over-tainting with acceptable overhead and identifies 5 previously undiscovered transient execution vulnerabilities (with 6 CVEs assigned) on BOOM and XiangShan.

## 中文摘要

瞬态执行漏洞已成为现代处理器面临的关键威胁。硬件模糊测试技术近来在大规模乱序处理器设计中发现瞬态执行缺陷方面展现出良好前景。然而，其微架构可控性与可观测性较差，使其无法有效且高效地检测瞬态执行漏洞。本文提出 DejaVuzz，一种新颖的硅前阶段处理器瞬态执行缺陷模糊测试器。DejaVuzz 利用两种创新的操作原语：动态可交换内存与差分信息流追踪，从而实现更有效、更高效的瞬态执行漏洞检测。动态可交换内存能够在同一地址空间内隔离不同的指令流。借助这一能力，DejaVuzz 为任意瞬态窗口生成有针对性的训练，并消除无效训练，从而高效触发多种瞬态窗口。差分信息流追踪有助于观察敏感数据在微架构中的传播。基于污点，DejaVuzz 设计污点覆盖矩阵以指导变异，并利用污点活跃性标注来识别可利用的泄漏。我们的评估表明，DejaVuzz 优于最先进的模糊测试器 SpecDoctor，能够以更低的训练开销触发更全面的瞬态窗口，并实现 4.7× 的覆盖率提升。此外，DejaVuzz 还能以可接受的开销缓解控制流过度污点化，并在 BOOM 与 XiangShan 上识别出 5 个此前未被发现的瞬态执行漏洞（分配了 6 个 CVE）。

## 英文关键词

transient execution bug; hardware fuzzing; processor fuzzing; information flow tracking

## 中文关键词

瞬态执行缺陷；硬件模糊测试；处理器模糊测试；信息流追踪

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736115)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 7C](index.md) · [返回 ASPLOS 2026](../index.md)
