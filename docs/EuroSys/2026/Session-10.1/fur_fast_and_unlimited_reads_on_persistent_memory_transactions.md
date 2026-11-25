---
title: "FUR: Fast and Unlimited Reads on Persistent Memory Transactions"
description: "EuroSys 2026 · Distributed Systems and Multicore · João Barreto (INESC-ID, IST, Universidade de Lisboa, Portugal), Daniel Castro (I"
tags:
  - "EuroSys2026"
  - "Distributed Systems and Multicore"
---

# FUR: Fast and Unlimited Reads on Persistent Memory Transactions

**中文标题：** FUR：持久内存事务上的快速无限制读

**所属 Session：** [Session 10.1: Distributed Systems and Multicore](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Systems and Multicore。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Systems and Multicore</p>
</div>

**作者**：João Barreto (INESC-ID, IST, Universidade de Lisboa, Portugal), Daniel Castro (INESC-ID, IST, Universidade de Lisboa, Portugal), Paolo Romano (INESC-ID, IST, Universidade de Lisboa, Portugal), Alexandro Baldassin (São Paulo State University (Unesp), Brazil)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769343)

## 英文摘要

Despite the recent improvements in supporting Persistent Hardware Transactions (PHTs) on emerging persistent memories (PM), they have largely overlooked the poor performance of Read-Only (RO) transactions, which suffer from two crucial bottlenecks: i) the considerable post-commit delays required to ensure consistency with concurrent update transactions; and ii) the well-known tight read capacity limits of the commercially available HTM implementations.

We propose FUR, a new design for PHT that eliminates the two most crucial bottlenecks that hinder RO transactions in state-of-the-art PHT. At its core, FUR exploits advanced instructions that some contemporary HTMs provide to suspend (and resume) transactional access tracking.

With the exception of workloads comprised of 100% update transactions, our experimental evaluation with an IBM POWER9 system using the TPC-C benchmark shows that FUR can outperform the state of the art designs for persistent hardware (SPHT) and software memory transactions (Pisces or SpecPMT-based) by up to 6.17×.

## 中文摘要

尽管近期在持久内存（PM）上支持持久硬件事务（PHT）方面已有改进，但这些工作在很大程度上忽视了只读（RO）事务的糟糕性能，后者受制于两个关键瓶颈：i）为确保与并发更新事务的一致性所需的大幅提交后延迟；ii）商用 HTM 实现众所周知的严格读容量限制。

我们提出 FUR，一种新的 PHT 设计，消除了最先进 PHT 中阻碍 RO 事务的两个最关键瓶颈。FUR 的核心是利用某些当代 HTM 所提供的先进指令来暂停（并恢复）事务性访问追踪。

除由 100% 更新事务构成的工作负载外，我们在 IBM POWER9 系统上使用 TPC-C 基准进行的实验评估表明，FUR 相比最先进的持久硬件事务设计（SPHT）和软件内存事务设计（Pisces 或基于 SpecPMT 的方案）最多可快 6.17 倍。

**英文关键词：** Hardware transactional memory, persistent memory transactions, persistent memory

**中文关键词：** 硬件事务内存、持久内存事务、持久内存

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
