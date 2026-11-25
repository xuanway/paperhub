---
title: "Rose: Reproducing External-Fault-Induced Failures in Distributed Systems with Lightweight Instrumentation"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Sebastião Amaro (INESC-ID), Miguel Matos (IST Lisbon & INESC-ID), Pedro Fonseca "
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# Rose: Reproducing External-Fault-Induced Failures in Distributed Systems with Lightweight Instrumentation

**中文标题：** Rose：借助轻量级插桩复现分布式系统中外部故障引发的失效

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Sebastião Amaro (INESC-ID), Miguel Matos (IST Lisbon & INESC-ID), Pedro Fonseca (Purdue University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803625)

## 英文摘要

Distributed systems form the backbone of critical infrastructures, yet remain vulnerable to external-fault-induced bugs that manifest only when specific external events occur during specific application states. Existing approaches to reproducing these bugs require fine-grained information about the application, which might not be available in production, and operate within a limited fault model. Rose is a novel approach that collects traces from production and systematically generates fault schedules that reproduce these bugs. By leveraging the insight that external faults are observable through system interfaces, Rose uses lightweight tracing (2.6% overhead) to capture essential application-environment interactions. Then, it identifies the application states when faults must occur to trigger bugs, and generates schedules that consistently reproduce these bugs. Rose reproduced 20 bugs across eight production systems implemented in diverse languages (C, C++, Java, Go, Scala), including widely-used systems such as Zookeeper, MongoDB, and HBase.

## 中文摘要

分布式系统构成了关键基础设施的骨干，却仍易受外部故障引发的缺陷影响，这类缺陷仅在特定应用状态期间发生特定外部事件时才会显现。现有复现这些缺陷的方法需要应用的细粒度信息，而这些信息在生产环境中可能并不具备，并且只能在有限的故障模型内工作。Rose 是一种新颖的方法，它从生产环境采集轨迹，并系统性地生成能够复现这些缺陷的故障调度。基于外部故障可通过系统接口观测这一洞见，Rose 使用轻量级追踪（开销 2.6%）捕获关键的应用与环境交互。随后，它识别出必须发生故障才能触发缺陷的应用状态，并生成可稳定复现这些缺陷的调度。Rose 在八个生产系统上复现了 20 个缺陷，这些系统由多种语言实现（C、C++、Java、Go、Scala），其中包括 ZooKeeper、MongoDB 和 HBase 等广泛使用的系统。

**英文关键词：** Bug Reproduction, Fault Injection, Distributed Systems

**中文关键词：** 缺陷复现、故障注入、分布式系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
