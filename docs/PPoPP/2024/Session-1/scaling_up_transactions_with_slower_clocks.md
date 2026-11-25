---
title: "Scaling Up Transactions with Slower Clocks"
description: "PPoPP 2024 Session Synchronization and Concurrency Control I：DCTL/DCOTL 让不相交事务不递增中央时钟，高核数下可扩展"
tags:
  - "PPoPP2024"
  - "Session-1"
  - "Synchronization and Concurrency Control I"
  - "concurrency control"
  - "software transactional memory"
  - "scalability"
authors:
  - "Pedro Ramalhete"
  - "Andreia Correia"
session: "Session 1: Synchronization and Concurrency Control I"
session_number: 1
session_chair: "Michael Scott"
date: "2024-03-04"
time: "10:00–10:20"
room: "Moorfoot"
doi: "10.1145/3627535.3638472"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Scaling Up Transactions with Slower Clocks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出延迟时钟事务锁定 DCTL 及变体 DCOTL，让连续不相交乃至写访问重叠的事务提交时不再递增中央时钟，降低时钟心跳，在高核数下可扩展并匹配或超越现有最优算法。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 1: Synchronization and Concurrency Control I</p>
</div>

**作者**：Pedro Ramalhete (Cisco Systems); Andreia Correia (University of Neuchatel)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 10:00–10:20 · Session 1: Synchronization and Concurrency Control I（主席：Michael Scott）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638472) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Concurrency controls with optimistic read accesses and pessimistic write accesses are among the fastest in the literature. However, during write transactions these algorithms need to increment an atomic variable, the central clock, limiting parallelism and preventing scalability at high core counts. In this paper, we propose a new concurrency control, Deferred Clock Transactional Locking (DCTL), which significantly reduces the heartbeat of the central clock, thus increasing scalability. DCTL will not increment the clock for consecutive disjoint transactions. An optimized variant, named DCOTL, allows for consecutive transactions with non-disjoint write-accesses to commit without incrementing the clock. Moreover, we show variants of these two algorithms with starvation-free transactions. Transactions in DCTL are opaque, which means it can be applied to concurrent data structures, Database Management Systems, Software Transactional Memory, and Persistent Transactional Memory. Our experiments show that these DCTL algorithms match or surpass the current state of the art for most workloads. We adapted both algorithms using an existing durability technique and implemented a fully transactional DBMS with disk persistence, whose scalability in write transactions exceeds the current state of the art.

## 中文摘要

具有乐观读取与悲观写入的并发控制是文献中最快的算法之一。然而，在写事务期间，这些算法需要递增一个原子变量——中央时钟，这限制了并行性，并使其在高核数下无法扩展。在本文中，我们提出一种新的并发控制算法——延迟时钟事务锁定（Deferred Clock Transactional Locking，DCTL），它显著降低了中央时钟的心跳频率，从而提升可扩展性。DCTL 不会为连续的不相交事务递增时钟。一个名为 DCOTL 的优化变体允许具有非不相交写访问的连续事务在不递增时钟的情况下提交。此外，我们展示了这两种算法的无饥饿事务变体。DCTL 中的事务是不透明的（opaque），这意味着它可以应用于并发数据结构、数据库管理系统、软件事务内存以及持久事务内存。我们的实验表明，这些 DCTL 算法在大多数工作负载上达到或超过当前的最先进水平。我们使用一种现有的持久化技术对这两种算法进行了改造，并实现了一个具有磁盘持久性的全事务型 DBMS，其写事务的可扩展性超过了当前的最先进水平。

## 英文关键词

concurrency control, starvation-freedom, software transactional memory

## 中文关键词

并发控制；无饥饿；软件事务内存

---

## 一句话总结

> 提出延迟时钟事务锁定 DCTL 及变体 DCOTL，让连续不相交乃至写访问重叠的事务提交时不再递增中央时钟，降低时钟心跳，在高核数下可扩展并匹配或超越现有最优算法。

## 研究问题

现有乐观读、悲观写并发控制在写事务期间必须递增中央时钟这一原子变量，形成串行瓶颈，限制并行度，使其在高核数下无法扩展。

## 方法简述

- 提出延迟时钟事务锁定（DCTL），仅在必要时推进中央时钟，连续的不相交事务不再递增时钟，从而大幅降低时钟心跳频率
- 设计优化变体 DCOTL，使写访问非不相交的连续事务也能在不递增时钟的情况下提交
- 提出两种算法的无饥饿（starvation-free）事务变体，并保证 DCTL 事务的不透明性（opacity），使其可用于并发数据结构、DBMS、STM 与持久事务内存
- 采用现有持久化技术改造两种算法，实现带磁盘持久化的全事务型 DBMS

## 主要结果

- 实验表明 DCTL 系列算法在大多数工作负载上匹配或超越当前最先进方法
- 基于持久化技术实现的带磁盘持久化全事务型 DBMS，其写事务可扩展性超过当前最先进水平
- 提供无饥饿变体，扩展了算法在需保证事务进展的场景下的可用性

---

> 所属 Session：[Session 1: Synchronization and Concurrency Control I](index.md) · 返回 [PPoPP 2024 总览](../index.md)
