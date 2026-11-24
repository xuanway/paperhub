---
title: "RESCQ: Realtime Scheduling for Continuous Angle Quantum Error Correction Architectures"
description: "ASPLOS 2025 · Session 7B · RESCQ：面向连续角度量子纠错架构的实时调度"
tags:
  - "ASPLOS2025"
  - "Session 7B"
  - "Quantum Error Correction"
---

# RESCQ: Realtime Scheduling for Continuous Angle Quantum Error Correction Architectures

**中文标题：** RESCQ：面向连续角度量子纠错架构的实时调度

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sayam Sethi (Department of Electrical and Computer Engineering, The University of Texas at Austin), Jonathan Mark Baker (Department of Electrical and Computer Engineering, The University of Texas at Austin)

**单位：** Department of Electrical and Computer Engineering, The University of Texas at Austin

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716018) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In order to realize large scale quantum error correction (QEC), resource states, such as |𝑇⟩, must be prepared which is expensive in both space and time. In order to circumvent this problem, alternatives have been proposed, such as the production of continuous angle rotation states [1, 6, 34]. However, the production of these states is non-deterministic and may require multiple repetitions to succeed. The original proposals suggest architectures which do not account for realtime (or dynamic) management of resources to minimize total execution time. Without a realtime scheduler, a statically generated schedule will be unnecessarily expensive. We propose RESCQ (pronounced rescue), a realtime scheduler for programs compiled onto these continuous angle systems. Our scheme actively minimizes total cycle count by on-demand redistribution of resources based on expected production rates. Depending on the underlying hardware, this can cause excessive classical control overhead. We further address this by dynamically selecting the frequency of our recomputation. RESCQ improves over baseline proposals by an average of 2× in cycle count.

## 中文摘要

为了实现大规模量子纠错（QEC），必须制备资源态，例如 |𝑇⟩，而这在空间和时间上都是昂贵的。为规避该问题，已有替代方案被提出，例如产生连续角度旋转态 [1, 6, 34]。然而，这些态的产生是非确定性的，可能需要多次重复才能成功。最初的提议所给出的架构并未考虑对资源进行实时（或动态）管理以最小化总执行时间。在没有实时调度器的情况下，静态生成的调度将不必要地昂贵。我们提出 RESCQ（发音为 rescue），一种用于编译到这类连续角度系统上的程序的实时调度器。我们的方案通过基于预期产生速率按需重新分配资源，主动最小化总周期数。取决于底层硬件，这可能导致过多的经典控制开销。我们进一步通过动态选择重计算的频率来解决该问题。RESCQ 在周期数上相比基线方案平均提升 2×。

## 英文关键词

quantum computing; quantum error correction; surface codes; realtime scheduling

## 中文关键词

量子计算；量子纠错；表面码；实时调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716018)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2025](../index.md)
