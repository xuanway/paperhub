---
title: "Multiverse: Transactional Memory with Dynamic Multiversioning"
description: "PPoPP 2026 Session 1（Concurrency Control）：有版本/无版本事务并发，长读负载吞吐高几个数量级"
tags:
  - "PPoPP2026"
  - "Session-1"
  - "Concurrency Control"
  - "Transactional Memory"
  - "Multiversioning"
  - "Concurrency"
authors:
  - "Gaetano Coccimiglio"
  - "Trevor Brown"
  - "Srivatsan Ravi"
session: "Session 1: Concurrency Control"
session_number: 1
session_chair: "Madan Musuvathi"
date: "2026-02-02"
time: "10:50–11:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786436"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Multiverse: Transactional Memory with Dynamic Multiversioning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Multiverse，一种同时支持有版本与无版本事务并发执行的软件事务内存，在无长读时保持 SOTA 性能，在有长读且频繁更新时显著优于现有 STM。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 1: Concurrency Control</p>
</div>

**作者**：Gaetano Coccimiglio, Trevor Brown, and Srivatsan Ravi — University of Waterloo, Canada; University of Southern California, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 10:50–11:10 · Session 1: Concurrency Control（主席：Madan Musuvathi）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786436) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Software transactional memory (STM) allows programmers to easily implement concurrent data structures. STMs simplify atomicity. Recent STMs can achieve good performance for some workloads but they have some limitations. In particular, STMs typically cannot support long-running reads which access a large number of addresses that are frequently updated. Multiversioning is a common approach used to support this type of workload. However, multiversioning is often expensive and can reduce the performance of transactions where versioning is not necessary. In this work we present Multiverse, a new STM that combines the best of both unversioned TM and multiversioning. Multiverse features versioned and unversioned transactions which can execute concurrently. A main goal of Multiverse is to ensure that unversioned transactions achieve performance comparable to the state of the art unversioned STM while still supporting fast versioned transactions needed to enable long running reads. We implement Multiverse and compare it against several STMs. Our experiments demonstrate that Multiverse achieves comparable or better performance for common case workloads where there are no long running reads. For workloads with long running reads and frequent updates Multiverse significantly outperforms existing STMS. In several cases for these workloads the throughput of Multiverse is several orders of magnitude faster than other STMs.

## 中文摘要

软件事务内存（software transactional memory，STM）使程序员能够轻松实现并发数据结构。STM 简化了原子性。近期的 STM 在某些工作负载上可以取得良好性能，但它们仍存在一些局限。特别是，STM 通常无法支持长时间运行的读操作，这类读操作会访问大量频繁更新的地址。多版本化是支持此类工作负载的常用方法。然而，多版本化往往开销高昂，并且可能降低那些并不需要版本化的事务的性能。在本工作中，我们提出 Multiverse，一种融合了无版本 TM 与多版本化两者之长的新型 STM。Multiverse 具备可并发执行的有版本事务与无版本事务。Multiverse 的一个主要目标是确保无版本事务达到与最先进的无版本 STM 相当的性能，同时仍支持实现长时间运行读操作所需的快速有版本事务。我们实现了 Multiverse，并将其与若干 STM 进行比较。实验表明，对于没有长时间运行读操作的常见情形工作负载，Multiverse 取得了相当或更好的性能。对于包含长时间运行读操作与频繁更新的工作负载，Multiverse 显著优于现有 STM。在这些工作负载的若干情形中，Multiverse 的吞吐量比其他 STM 快若干数量级。

## 英文关键词

Transaction Memory, Software Transaction Memory, Multiversioning, Multiversion Concurrency Control

## 中文关键词

事务内存（Transactional Memory）；软件事务内存（Software Transactional Memory）；多版本化（multiversioning）；多版本并发控制（Multiversion Concurrency Control）

---

## 一句话总结

> 提出 Multiverse，一种同时支持有版本与无版本事务并发执行的软件事务内存，在无长读时保持 SOTA 性能，在有长读且频繁更新时显著优于现有 STM。

## 研究问题

现有 STM 难以支持访问大量频繁更新地址的长事务读；多版本化虽能支持这类负载，但开销大，会拖慢不需要版本化的事务。

## 方法简述

- 支持有版本与无版本事务并发执行。
- 在保持无版本事务达到 SOTA 无版本 STM 性能的同时，提供长读所需的快速版本化事务。

## 主要结果

- 在无长读的常见负载上性能与现有 STM 相当或更好。
- 在有长读且频繁更新的负载上显著优于现有 STM，部分场景吞吐高出几个数量级。

---

> 所属 Session：[Session 1: Concurrency Control](index.md) · 返回 [PPoPP 2026 总览](../index.md)
