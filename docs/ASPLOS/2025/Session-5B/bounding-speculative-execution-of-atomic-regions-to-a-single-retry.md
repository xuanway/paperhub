---
title: "Bounding Speculative Execution of Atomic Regions to a Single Retry"
description: "ASPLOS 2025 · Session 5B · 将原子区域的投机执行限定为单次重试"
tags:
  - "ASPLOS2025"
  - "Session 5B"
  - "Microarchitecture"
---

# Bounding Speculative Execution of Atomic Regions to a Single Retry

**中文标题：** 将原子区域的投机执行限定为单次重试

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Eduardo José Gómez-Hernández (Computer Engineering Department, University of Murcia), Juan M. Cebrian (Computer Engineering Department, University of Murcia), Stefanos Kaxiras (Department of Information Technology, Uppsala University), Alberto Ros (Computer Engineering Department, University of Murcia)

**单位：** Computer Engineering Department, University of Murcia；Department of Information Technology, Uppsala University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674176) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Mutual exclusion has long served as a fundamental construct in parallel programs. Despite a long history of optimizing the lower-level lock and unlock operations used to enforce mutual exclusion, such operations largely dictate performance in parallel programs. Speculative Lock Elision, and more generally Hardware Transactional Memory, allow executing atomic regions (ARs) concurrently and speculatively, and ensure correctness by using conflict detection. However, practical implementations of these ideas are best-effort and, in case of conflicts, the execution of ARs is retried a predetermined number of times before falling back to mutual exclusion. This work explores the opportunities of using cacheline locking to bound the number of retries of speculative solutions. Our key insight is that ARs that access exactly the same set of addresses when re-executing can learn that set in the first execution and execute non-speculatively in the next one by performing an ordered cacheline locking. This way the speculative execution is bounded to a single retry. We first establish the conditions for ARs to be able to re-execute under a cacheline-locked mode. Based on these conditions, we propose cleAR, cacheline-locked executed AR, a novel technique that on the first abort, forces the reexecution to use cacheline locking. The detection and conversion to cacheline-locking mode is transparent to software. Using gem5 running data-structure benchmarks and the STAMP benchmark suite, we show that the average number of ARs that succeed on the first retry grows from 35.4% in our baseline to 64.4% with cleAR, reducing the percentage of fallback (coarse-grain mutual exclusion) execution from 37.2% to 15.4%. These improvements reduce average execution time by 35.0% over a baseline configuration and by 23.3% over more elaborated approaches like PowerTM.

## 中文摘要

互斥长期以来一直是并行程序中的基本构造。尽管针对用于实施互斥的底层 lock 与 unlock 操作的优化由来已久，此类操作仍在很大程度上决定并行程序的性能。投机锁消除（Speculative Lock Elision）以及更一般的硬件事务内存允许并发且投机地执行原子区域（atomic regions, AR），并通过冲突检测保证正确性。然而，这些思想的实际实现都是尽力而为的，一旦发生冲突，AR 的执行会在回退到互斥之前被重试预定的次数。本工作探索利用缓存行锁（cacheline locking）限定投机方案重试次数的机会。我们的关键洞察是：在重新执行时访问完全相同地址集合的 AR，可以在第一次执行中学习该集合，并在下一次执行中通过执行有序的缓存行锁定以非投机方式运行。这样，投机执行就被限定为单次重试。我们首先确立 AR 能够在缓存行锁定模式下重新执行的条件。基于这些条件，我们提出 cleAR（cacheline-locked executed AR），一种在首次中止时强制重执行使用缓存行锁定的新技术。向缓存行锁定模式的检测与转换对软件透明。使用运行数据结构基准与 STAMP 基准套件的 gem5，我们表明首次重试即成功的 AR 平均比例从基线的 35.4% 提升到 cleAR 的 64.4%，回退（粗粒度互斥）执行的比例从 37.2% 降至 15.4%。这些改进使平均执行时间相对基线配置降低 35.0%，相对 PowerTM 等更精细的方案降低 23.3%。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674176)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2025](../index.md)
