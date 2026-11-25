---
title: "Avicenna: Masking Slowdowns in Replicated State Machines with Counterfactual Evaluation"
description: "EuroSys 2026 · Security · Christopher Hodsdon (Databricks), Zijian Qin (Princeton University), Khiem Ngo ("
tags:
  - "EuroSys2026"
  - "Security"
---

# Avicenna: Masking Slowdowns in Replicated State Machines with Counterfactual Evaluation

**中文标题：** Avicenna：利用反事实评估屏蔽复制状态机中的性能降速

**所属 Session：** [Session 6.1: Security](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security</p>
</div>

**作者**：Christopher Hodsdon (Databricks), Zijian Qin (Princeton University), Khiem Ngo (Datadog), Siddhartha Sen (Microsoft Research), Ethan Katz-Bassett (Columbia University), Wyatt Lloyd (Princeton University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803615)

**获奖：** 最佳论文（[官方获奖名单](https://2026.eurosys.org/eurosys-awards.html)）

## 英文摘要

Geo-distributed replicated state machines (RSMs) are at the heart of many production distributed systems, offering linearizability and fault tolerance via consensus protocols. Most existing protocols target crash fault tolerance, however, and are vulnerable to fail-slow faults, where a single slow replica can significantly degrade system latency. Existing protocols that tolerate fail-slow faults do so with much higher normal-case latency in geo-distributed settings.

This paper presents Avicenna, the first consensus protocol for geo-distributed RSMs that maintains low normal-case latency while tolerating a single fail-slow replica. Avicenna uses a single leader to order commands, naturally tolerating a fail-slow follower. To tolerate a fail-slow leader, Avicenna compares the current latency with the counterfactual latency clients would experience if a different replica, the shadow leader, were the leader. When that comparison indicates the current leader might be slow, Avicenna quickly promotes the shadow leader with a fast leader rotation protocol. Our evaluation shows Avicenna has the same normal-case latency as Multi-Paxos while tolerating fail-slow faults.

## 中文摘要

地理分布式复制状态机（RSM）是许多生产级分布式系统的核心，通过共识协议提供线性一致性与容错能力。然而，大多数现有协议针对的是崩溃容错，对慢故障较为脆弱——单个变慢的副本即可显著恶化系统延迟。能够容忍慢故障的现有协议在地理分布式场景下需要付出高得多的正常路径延迟。

本文提出 Avicenna，这是首个面向地理分布式 RSM 的共识协议，在容忍单个慢副本的同时保持较低的正常路径延迟。Avicenna 使用单一领导者对命令排序，天然容忍变慢的跟随者。为容忍变慢的领导者，Avicenna 将当前延迟与客户端在另一副本（影子领导者）担任领导者时所将经历的反事实延迟进行比较。当该比较表明当前领导者可能变慢时，Avicenna 通过快速的领导者轮换协议迅速提升影子领导者。我们的评测表明，Avicenna 在容忍慢故障的同时，其正常路径延迟与 Multi-Paxos 相同。

**英文关键词：** distributed system, replicated state machines, fault tolerance

**中文关键词：** 分布式系统、复制状态机、容错

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
