---
title: "Acyclic Cost-Effective Requester-Stalls Hardware Transactional Memory"
description: "MICRO 2026 · Session 7D · 无环且低成本的请求方停顿式硬件事务内存"
tags:
  - "MICRO2026"
---

# Acyclic Cost-Effective Requester-Stalls Hardware Transactional Memory

**中文标题：** 无环且低成本的请求方停顿式硬件事务内存

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Víctor Nicolás-Conesa, Rubén Titos-Gil, Ricardo Fernández-Pascual, Manuel E. Acacio, Alberto Ros

**来源：** MICRO 2026，pp. 2608–2624；[DOI](https://doi.org/10.1109/MICRO67795.2026.00178)

## 英文摘要

Conflict resolution remains a central challenge in best-effort Hardware Transactional Memory (HTM). Commercial implementations favor requester-wins for its simplicity but suffer from excessive squashed work due to transaction aborts and cannot guarantee progress under contention. Requester-stalls alternatives avoid many of these aborts, yet existing designs face a fundamental burden: cyclic dependencies between stalled transactions. In state-of-the-art requester-stalls policies, conservative cycle detection frequently leads to futile stalls. This work presents HighwayTM, a requester-stalls conflict resolution policy that can guarantee progress under contention whilst avoiding cyclic dependencies and futile stalls. Our key insight is that combining a lightweight dynamic priority (which we call a lane) with the static, yet simple and already available CoreID yields both cycle freedom and dependency awareness at negligible hardware cost. Lanes are assigned at conflict time and elevate transactions already part of a dependency chain over newcomers, effectively addressing the inherent problems from dynamically established dependencies. The entire mechanism fits in a 7-bit register per core with no centralized clock or global state. Evaluated in gem5 full-system simulation with a variety of benchmarks on a 16-core system, HighwayTM can reduce execution time by 22% and 15% over commercial-like requester-wins and state-of-the-art requester-stalls policies, respectively, while halving futile stalled cycles and reducing stalled transactions to under a third, with consistent results on additional concurrent data structures and in-memory applications.

## 中文摘要

冲突解决仍然是尽力硬件事务内存 (HTM) 中的一个核心挑战。商业实现因其简单性而有利于请求者获胜，但由于事务中止而导致工作过度压缩，并且无法保证争用下的进展。请求者停滞替代方案避免了许多此类中止，但现有设计面临着一个基本负担：停滞事务之间的循环依赖性。在最先进的请求者停顿策略中，保守的周期检测经常导致徒劳的停顿。这项工作提出了 HighwayTM，一种请求者拖延冲突解决策略，可以保证争用下的进展，同时避免循环依赖和无效的拖延。我们的主要见解是将轻量级动态优先级（我们称之为通道）与静态但简单且可用的 CoreID 相结合，以可忽略的硬件成本实现循环自由和依赖性感知。通道在冲突时分配，并将已经属于依赖链一部分的事务提升到新来者之上，从而有效解决动态建立依赖关系的固有问题。整个机制适合每个内核的 7 位寄存器，没有集中时钟或全局状态。在 gem5 全系统模拟中，在 16 核系统上使用各种基准进行评估，HighwayTM 可以比商业类请求者获胜和最先进的请求者停止策略分别减少 22% 和 15% 的执行时间，同时将无用的停滞周期减半并将停滞事务减少到三分之一以下，在额外的并发数据结构和内存应用程序上获得一致的结果。

## 中文关键词

多核；共享内存系统；并行与分布式架构；硬件事务内存；无环冲突管理

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22303584](https://doi.org/10.5281/zenodo.22303584)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
