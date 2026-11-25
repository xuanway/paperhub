---
title: "Locks as a Resource: Fairly Scheduling Lock Occupation with CFL"
description: "PPoPP 2024 Session Synchronization and Concurrency Control I：CFL 把锁占用当作可调度资源，按优先级与 cgroup 公平分配"
tags:
  - "PPoPP2024"
  - "Session-1"
  - "Synchronization and Concurrency Control I"
  - "lock"
  - "synchronization primitives"
  - "resource sharing"
authors:
  - "Jonggyu Park"
  - "Young Ik Eom"
session: "Session 1: Synchronization and Concurrency Control I"
session_number: 1
session_chair: "Michael Scott"
date: "2024-03-04"
time: "10:20–10:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638477"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Locks as a Resource: Fairly Scheduling Lock Occupation with CFL

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">指出现有锁在多容器环境中缺乏调度导致性能不公平与干扰，提出内嵌调度能力的完全公平锁 CFL，按优先级与 cgroup 分配锁占用时间并考虑 NUMA 拓扑，兼顾公平性与性能。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 1: Synchronization and Concurrency Control I</p>
</div>

**作者**：Jonggyu Park (University of Washington); Young Ik Eom (Dept. of Electrical and Computer Engineering / College of Computing and Informatics, Sungkyunkwan University)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 10:20–10:40 · Session 1: Synchronization and Concurrency Control I（主席：Michael Scott）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638477) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

In multi-container environments, applications oftentimes experience unexpected performance fluctuations due to undesirable interference among applications. Synchronization such as locks has been targeted as one of the reasons but still remains an uncontrolled resource while a large set of locks are still shared across applications. In this paper, we demonstrate that this lack of lock scheduling incurs significant real-world problems including performance unfairness and interference among applications. To address this problem, we propose a new synchronization design with an embedded scheduling capability, called CFL (Completely Fair Locking). CFL fairly distributes a fair amount of lock occupation time to applications considering their priorities and cgroup information. For scalability, CFL also considers the NUMA topology in the case of NUMA machines. Experimental results demonstrate that CFL significantly improves performance fairness while achieving comparable or sometimes even superior performance to state-of-the-art locks.

## 中文摘要

在多容器环境中，应用常常因应用之间不期望的相互干扰而遭遇意外的性能波动。同步机制（如锁）一直被视为原因之一，但在大量锁仍被多个应用共享的情况下，它仍然是一种未受控制的资源。在本文中，我们表明，这种锁调度的缺失会造成现实中的严重问题，包括应用之间的性能不公平与相互干扰。为解决该问题，我们提出了一种内嵌调度能力的新型同步设计，称为 CFL（Completely Fair Locking，完全公平锁）。CFL 依据应用的优先级与 cgroup 信息，向应用公平地分配适量的锁占用时间。为了可扩展性，CFL 在 NUMA 机器上还会考虑 NUMA 拓扑。实验结果表明，CFL 显著改善了性能公平性，同时取得与最先进锁相当、有时甚至更优的性能。

## 英文关键词

synchronization primitives, lock, scalability, resource sharing

## 中文关键词

同步原语；锁；可扩展性；资源共享

---

## 一句话总结

> 指出现有锁在多容器环境中缺乏调度导致性能不公平与干扰，提出内嵌调度能力的完全公平锁 CFL，按优先级与 cgroup 分配锁占用时间并考虑 NUMA 拓扑，兼顾公平性与性能。

## 研究问题

多容器环境中应用间的干扰造成性能波动，而锁在被大量应用共享的同时始终是一种不受控制的资源；这种锁调度的缺失带来性能不公平与相互干扰等实际问题。

## 方法简述

- 提出完全公平锁 CFL（Completely Fair Locking），在同步设计中内嵌调度能力，把锁占用视为可调度的资源
- 依据应用的优先级与 cgroup 信息，向各应用公平地分配适量的锁占用时间
- 在 NUMA 机器上进一步考虑 NUMA 拓扑，以保证 CFL 的可扩展性

## 主要结果

- 实验结果表明 CFL 显著改善了性能公平性
- CFL 取得与最先进锁相当、有时甚至更优的性能
- 在多容器与 NUMA 环境下同时兼顾公平性与可扩展性

---

> 所属 Session：[Session 1: Synchronization and Concurrency Control I](index.md) · 返回 [PPoPP 2024 总览](../index.md)
