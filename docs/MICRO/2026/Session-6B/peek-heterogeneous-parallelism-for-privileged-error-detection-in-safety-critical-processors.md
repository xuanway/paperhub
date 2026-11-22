---
title: "PEEK: Heterogeneous Parallelism for Privileged Error Detection in Safety-Critical Processors"
description: "MICRO 2026 · Session 6B · PEEK：面向安全关键处理器中特权错误检测的异构并行机制"
tags:
  - "MICRO2026"
---

# PEEK: Heterogeneous Parallelism for Privileged Error Detection in Safety-Critical Processors

**中文标题：** PEEK：面向安全关键处理器中特权错误检测的异构并行机制

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Tinglue Wang, Zhenghui Guo, Bing Guo, Jiapeng Guan, Renshuang Jiang, Jie Zhang, Jing Li, Xin Si, Sam Ainsworth, Zhe Jiang

**来源：** MICRO 2026，pp. 2015–2031；[DOI](https://doi.org/10.1109/MICRO67795.2026.00141)

## 英文摘要

Heterogeneous parallel error detection architecture has been widely researched for safeguarding OoO superscalar processors in safety-critical systems, as it achieves significantly lower hardware overhead compared to traditional LockStep, by exploiting the parallelism that exists in a secondary execution. However, previous works do not cover the protection of privileged-mode execution, impeding their effectiveness in real-world deployment. Moreover, naive extension to privileged-mode can cause a litany of issues, from abysmal performance due to high synchronization costs, to full deadlocks. Here, we present PEEK, the first privileged parallel error detection architecture. Based on a deep analysis of privileged execution, we redesign the verification pipeline, addressing all the bottlenecks and bugs identified in privileged-mode protection. Evaluated using various metrics on an RTL-level full system running Linux, PEEK achieves full-privilege protection on Linux with negligible performance slowdown and affordable hardware overhead. PEEK has been taped out using a 28nm process, and its source is available at https: anonymous.4open.science/r/PEEK-3000.

## 中文摘要

异构并行错误检测架构已被广泛研究，用于保护安全关键系统中的 OoO 超标量处理器，因为与传统的 LockStep 相比，它通过利用辅助执行中存在的并行性，实现了显着降低的硬件开销。然而，以前的工作没有涵盖特权模式执行的保护，阻碍了它们在实际部署中的有效性。此外，对特权模式的简单扩展可能会导致一系列问题，从高同步成本导致的糟糕性能到完全死锁。在这里，我们提出 PEEK，第一个特权并行错误检测架构。基于对特权执行的深入分析，我们重新设计了验证管道，解决了特权模式保护中发现的所有瓶颈和错误。在运行 Linux 的 RTL 级完整系统上使用各种指标进行评估后，PEEK 在 Linux 上实现了完全权限保护，性能下降可以忽略不计，硬件开销也可承受。 PEEK 已采用 28nm 工艺流片，其来源可在 https://anonymous.4open.science/r/PEEK-3000 获取。

## 中文关键词

硬件容错；安全关键系统；全系统；异构并行；错误检测

## 代码与研究制品

- 代码仓库：[https://anonymous.4open.science/r/PEEK-3000](https://anonymous.4open.science/r/PEEK-3000)（本次访问需授权，HTTP 401）

以上入口来自论文正文或 Artifact 附录。

## 来源核对说明

论文提供匿名代码入口；本次请求返回 HTTP 401，尚未确认可公开访问。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
