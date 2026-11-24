---
title: "HawkSet: Automatic, Application-Agnostic, and Efficient Concurrent PM Bug Detection"
description: "EuroSys 2025 · Bug finding · João Oliveira (INESC-ID, IST), João Gonçalves (INESC-ID & IST U. Lisboa), Miguel"
tags:
  - "EuroSys2025"
  - "Bug finding"
---

# HawkSet: Automatic, Application-Agnostic, and Efficient Concurrent PM Bug Detection

**中文标题：** 自动、应用无关且高效的持久内存并发缺陷检测

**所属 Session：** [Session 8.1: Bug finding](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Bug finding。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Bug finding</p>
</div>

**作者**：João Oliveira (INESC-ID, IST), João Gonçalves (INESC-ID & IST U. Lisboa), Miguel Matos (IST Lisbon)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717477)

**获奖：** Gilles Muller 最佳研究制品（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

Persistent Memory (PM) enables the development of fast, persistent applications without employing costly HDD/SSD-based I/O operations. Since caches are volatile and CPUs may reorder and stall memory accesses for performance, developers must use low-level instructions to ensure a consistent state in case of a crash. Failure to do so can result in data corruption, data loss, or undefined behavior. In concurrent executions, this exposes a new class of bugs.

HawkSet is an automatic, application-agnostic, and efficient tool to detect concurrent PM bugs. HawkSet uses lockset analysis, and automatic binary instrumentation to find all the bugs detected by the state-of-the-art tools and 7 previously unknown bugs. This is achieved without requiring application-specific knowledge or models, nor specialized debugging artifacts or guided executions. Compared to the state-of-the-art, HawkSet offers up to a 159× speedup, and consistently detects harder-to-reach bugs, where a rare interleaving is required.

## 中文摘要

持久内存（PM）使开发快速的持久化应用成为可能，而无需使用昂贵的基于 HDD/SSD 的 I/O 操作。由于缓存是易失的，且 CPU 可能出于性能考虑重排和延迟内存访问，开发者必须使用低级指令来确保崩溃时的状态一致。未能这样做可能导致数据损坏、数据丢失或未定义行为。在并发执行中，这暴露出一类新的缺陷。

HawkSet 是一个自动、应用无关且高效的工具，用于检测并发 PM 缺陷。HawkSet 使用锁集分析和自动二进制插桩，找出了最先进工具能检测到的所有缺陷以及 7 个此前未知的缺陷。这一成果无需应用特定的知识或模型，也无需专门的调试产物或引导执行。与最先进方案相比，HawkSet 最高提供 159 倍加速，并能持续检测到需要罕见交错才能触发的、更难发现的缺陷。

**英文关键词：** Persistent Memory, Concurrency, Bug Detection

**中文关键词：** 持久内存、并发、缺陷检测

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
