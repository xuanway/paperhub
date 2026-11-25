---
title: "Binary Compatible Critical Section Delegation"
description: "PPoPP 2026 Session 1（Concurrency Control）：内核代理 + 二进制兼容，现有程序无需改代码即可降低临界区竞争"
tags:
  - "PPoPP2026"
  - "Session-1"
  - "Concurrency Control"
  - "Critical Section"
  - "Delegation"
  - "Futex"
authors:
  - "Junyao Zhang"
  - "Zhuo Wang"
  - "Zhe Zhou"
session: "Session 1: Concurrency Control"
session_number: 1
session_chair: "Madan Musuvathi"
date: "2026-02-02"
time: "09:50–10:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786439"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Award"
---

# Binary Compatible Critical Section Delegation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出二进制兼容的临界区代理机制 BCD：在内核 futex_wake 处接管并代理执行用户态临界区，无需修改二进制即可让现有应用透明受益。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 1: Concurrency Control</p>
</div>

**作者**：Junyao Zhang, Zhuo Wang, and Zhe Zhou — Fudan University, China; Alibaba Cloud Computing, China

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 09:50–10:10 · Session 1: Concurrency Control（主席：Madan Musuvathi）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786439) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Award**

---

## 英文摘要

In high-performance applications, critical sections often become performance bottlenecks due to contention among multiple cores. Critical section delegation mitigates this overhead by consistently executing critical sections on the same core, thereby reducing contention. Traditional delegation techniques, however, typically require manual code refactoring, which limits their practicality and adoption. More recent schemes that integrate with existing lock APIs have lowered this barrier, but delegating unsupported critical sections can still cause undefined behavior, including crashes. To make delegation broadly accessible—even for end-users without access to or knowledge of source code, we introduce BCD, a binary-compatible delegation mechanism. BCD leverages kernel support to delegate userspace critical sections at the point of futex_wake. It employs an in-kernel virtual machine to supervise the execution of delegated userspace instructions, eliminating the need for binary modification. Crucially, BCD can detect and safely exclude unsupported critical sections, preserving correctness. This enables existing applications to transparently benefit from critical section delegation, without requiring developer intervention.

## 中文摘要

在高性能应用中，临界区常常因多个核之间的竞争而成为性能瓶颈。临界区委派（critical section delegation）通过始终在同一个核上执行临界区来缓解这一开销，从而减少竞争。然而，传统的委派技术通常需要手动重构代码，这限制了其实用性与推广。较新的方案通过与现有锁 API 集成降低了这一门槛，但委派不受支持的临界区仍可能导致未定义行为，包括崩溃。为了让委派能够被广泛使用——即使是对无法访问或不了解源代码的最终用户也是如此——我们提出了 BCD，一种二进制兼容的委派机制。BCD 借助内核支持，在 futex_wake 处对用户空间临界区进行委派。它采用内核内虚拟机来监管被委派的用户空间指令的执行，从而无需修改二进制。关键在于，BCD 能够检测并安全地排除不受支持的临界区，从而保持正确性。这使得现有应用无需开发者介入即可透明地受益于临界区委派。

## 英文关键词

Delegation Lock, Cache Thrashing

## 中文关键词

委派锁（Delegation Lock）；缓存抖动（Cache Thrashing）

---

## 一句话总结

> 提出二进制兼容的临界区代理机制 BCD：在内核 futex_wake 处接管并代理执行用户态临界区，无需修改二进制即可让现有应用透明受益。

## 研究问题

传统临界区代理通常需要手工重构代码；基于现有锁 API 的方案虽降低了门槛，但代理不支持的临界区仍可能引发崩溃等未定义行为，普通用户难以直接使用。

## 方法简述

- 在内核的 futex_wake 处拦截并代理 userspace 临界区。
- 用内核内虚拟机监督被代理用户态指令的执行，避免修改二进制。
- 检测并安全排除不支持的临界区，保证程序正确性。

## 主要结果

- 现有应用无需开发者介入或源码知识即可透明获得临界区代理的收益。
- 在保持正确性的同时降低了代理技术的使用门槛。

---

> 所属 Session：[Session 1: Concurrency Control](index.md) · 返回 [PPoPP 2026 总览](../index.md)
