---
title: "Pure: Evolving Message Passing To Better Leverage Shared Memory Within Nodes"
description: "PPoPP 2024 Session High Performance Computing：等待消息时窃取工作+节点内无锁消息，CoMD/miniAMR 最高 2.1×"
tags:
  - "PPoPP2024"
  - "Session-3"
  - "High Performance Computing"
  - "task-based parallelism"
  - "lock-free data structures"
  - "runtime systems"
authors:
  - "James Psota"
  - "Armando Solar-Lezama"
session: "Session 3: High Performance Computing"
session_number: 3
session_chair: "Helen Xu"
date: "2024-03-04"
time: "15:20–15:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638503"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Pure: Evolving Message Passing To Better Leverage Shared Memory Within Nodes

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出编程模型与运行时 Pure，在消息传递为主的场景中利用节点内共享内存：等待消息的核可相互窃取工作，并用无锁数据结构实现节点内高性能消息与集合操作，应用最高加速 2.1×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 3: High Performance Computing</p>
</div>

**作者**：James Psota, Armando Solar-Lezama (Massachusetts Institute of Technology)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 15:20–15:40 · Session 3: High Performance Computing（主席：Helen Xu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638503) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Pure is a new programming model and runtime system explicitly designed to take advantage of shared memory within nodes in the context of a mostly message passing interface enhanced with the ability to use tasks to make use of idle cores. Pure leverages shared memory in two ways: (a) by allowing cores to steal work from each other while waiting on messages to arrive, and, (b) by leveraging efficient lock-free data structures in shared memory to achieve high-performance messaging and collective operations between the ranks within nodes. We use microbenchmarks to evaluate Pure’s key messaging and collective features and also show application speedups up to 2.1×on the CoMD molecular dynamics and the miniAMR adaptive mesh refinement applications scaling up to 4,096 cores.

## 中文摘要

Pure 是一种新的编程模型与运行时系统，它被明确设计用于在一种以消息传递接口为主、并增强了使用任务来利用空闲核的能力的场景中，发挥节点内共享内存的优势。Pure 以两种方式利用共享内存：(a) 允许核在等待消息到达期间相互窃取工作；(b) 利用共享内存中高效的无锁数据结构，实现节点内各 rank 之间的高性能消息传递与集合操作。我们使用微基准评测了 Pure 的关键消息传递与集合操作特性，并展示了在 CoMD 分子动力学与 miniAMR 自适应网格细化应用上最高 2.1× 的应用加速，规模扩展至 4096 核。

## 英文关键词

parallel programming models; distributed runtime systems; task-based parallelism; concurrent data structures; lock-free data structures

## 中文关键词

并行编程模型；分布式运行时系统；任务并行；并发数据结构；无锁数据结构

---

## 一句话总结

> 提出编程模型与运行时 Pure，在消息传递为主的场景中利用节点内共享内存：等待消息的核可相互窃取工作，并用无锁数据结构实现节点内高性能消息与集合操作，应用最高加速 2.1×。

## 研究问题

以消息传递为主的并行程序在执行中未能充分利用节点内共享内存，等待消息期间的空闲核与节点内通信开销成为性能瓶颈。

## 方法简述

- 提出 Pure 编程模型与运行时系统，在主要由消息传递接口构成、并以任务利用空闲核的执行模型中显式利用节点内共享内存
- 允许核在等待消息到达期间相互窃取工作（work stealing）
- 利用共享内存中高效的无锁数据结构，实现节点内各 rank 之间的高性能消息传递与集合操作

## 主要结果

- 以微基准评测了 Pure 的关键消息传递与集合操作特性
- 在 CoMD 分子动力学与 miniAMR 自适应网格细化应用上取得最高 2.1× 的应用加速
- 验证规模可扩展至 4096 核

---

> 所属 Session：[Session 3: High Performance Computing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
