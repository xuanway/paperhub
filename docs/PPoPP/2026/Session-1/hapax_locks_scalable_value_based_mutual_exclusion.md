---
title: "Hapax Locks: Scalable Value-Based Mutual Exclusion"
description: "PPoPP 2026 Session 1（Concurrency Control）：常数时间入场/解锁与 FIFO 顺序，性能对标最好的 SOTA 锁"
tags:
  - "PPoPP2026"
  - "Session-1"
  - "Concurrency Control"
  - "Mutual Exclusion"
  - "Lock Design"
  - "Scalability"
authors:
  - "Dave Dice"
  - "Alex Kogan"
session: "Session 1: Concurrency Control"
session_number: 1
session_chair: "Madan Musuvathi"
date: "2026-02-02"
time: "10:10–10:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786443"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Hapax Locks: Scalable Value-Based Mutual Exclusion

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Hapax Locks，一个简单、空间高效且提供 FIFO 入场顺序的可扩展互斥锁，到达与解锁路径均为常数时间。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 1: Concurrency Control</p>
</div>

**作者**：Dave Dice and Alex Kogan — Independent, USA; Oracle Labs, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 10:10–10:30 · Session 1: Concurrency Control（主席：Madan Musuvathi）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786443) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

We present Hapax Locks, a novel locking algorithm that is simple, enjoys constant-time arrival and unlock paths, provides FIFO admission order, and which is also space efficient and generates relatively little coherence traffic under contention in the common case. Hapax Locks offer performance (both latency and scalability) that is comparable with the best state of the art locks, while at the same time Hapax Locks impose fewer constraints and dependencies on the ambient runtime environment, making them particularly easy to integrate or retrofit into existing systems or under existing lock application programming interfaces.

## 中文摘要

我们提出 Hapax Locks，一种新颖的锁算法。它简单，具有常数时间的到达路径与解锁路径，提供 FIFO 准入顺序，同时空间高效，并且在常见情形的竞争下产生的缓存一致性流量相对较少。Hapax Locks 的性能（包括延迟与可扩展性）可与最先进的锁相媲美，同时 Hapax Locks 对所处运行时环境的约束与依赖更少，使其特别易于集成或改造到现有系统中，或置于现有锁应用程序编程接口之下。

## 英文关键词

Synchronization; Locks; Mutual Exclusion; Mutex; Scalability; Cache-coherent Shared Memory

## 中文关键词

同步；锁；互斥；互斥锁；可扩展性；缓存一致共享内存

---

## 一句话总结

> 提出 Hapax Locks，一个简单、空间高效且提供 FIFO 入场顺序的可扩展互斥锁，到达与解锁路径均为常数时间。

## 研究问题

高性能锁需要在可扩展性、延迟、空间占用与运行时依赖之间权衡，同时还要易于集成到现有系统或锁 API 中。

## 方法简述

- 常数时间的到达与解锁路径，并提供 FIFO 入场顺序。
- 空间高效的设计，常见竞争下产生较少一致性流量。
- 对运行时环境的约束与依赖更少，便于集成或改造现有系统。

## 主要结果

- 延迟与可扩展性可与当前最好的 SOTA 锁相媲美。
- 更容易在现有系统与锁 API 上集成或改造。

---

> 所属 Session：[Session 1: Concurrency Control](index.md) · 返回 [PPoPP 2026 总览](../index.md)
