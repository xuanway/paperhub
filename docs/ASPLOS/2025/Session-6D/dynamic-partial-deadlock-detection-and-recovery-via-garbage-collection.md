---
title: "Dynamic Partial Deadlock Detection and Recovery via Garbage Collection"
description: "ASPLOS 2025 · Session 6D · 基于垃圾回收的动态部分死锁检测与恢复"
tags:
  - "ASPLOS2025"
  - "Session 6D"
  - "Testing"
---

# Dynamic Partial Deadlock Detection and Recovery via Garbage Collection

**中文标题：** 基于垃圾回收的动态部分死锁检测与恢复

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Georgian-Vlad Saioc (Aarhus University,Programming Systems Group, Uber Technologies, Inc.), I-Ting Angelina Lee (Washington University in St. Louis), Anders Møller (Aarhus University), Milind Chabbi (Programming Systems Group, Uber Technologies, Inc.)

**单位：** Aarhus University,Programming Systems Group, Uber Technologies, Inc.；Washington University in St. Louis；Aarhus University；Programming Systems Group, Uber Technologies, Inc.

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715990) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

A challenge of writing concurrent message-passing programs is ensuring the absence of partial deadlocks, which can cause severe memory leaks in long-running systems. The Go programming language is particularly susceptible to this problem due to its support of message passing and ease of lightweight concurrency creation. We propose a novel dynamic technique to detect partial deadlocks by soundly approximating liveness using the garbage collector's marking phase. The approach allows systems to not only detect, but also automatically redress partial deadlocks and alleviate their impact on memory. We implement the approach in the tool Golf, as an extension to the garbage collector of the Go runtime system and evaluate its effectiveness in a series of experiments. Preliminary results show that the approach is effective at detecting 94% and 50% of partial deadlocks in a series of microbenchmarks and the test suites of a large-scale industrial codebase, respectively. Furthermore, we deployed Golf on a real service used by Uber, and over a period of 24 hours, effectively detected 252 partial deadlocks caused by three programming errors.

## 中文摘要

编写并发消息传递程序的一项挑战是确保不存在部分死锁，部分死锁会在长期运行系统中造成严重的内存泄漏。Go 编程语言由于支持消息传递且易于创建轻量级并发，尤其容易受到这一问题的影响。我们提出一种新颖的动态技术，利用垃圾回收器的标记阶段对活性进行可靠近似，从而检测部分死锁。该方法使系统不仅能够检测，还能自动修复部分死锁并减轻其对内存的影响。我们在工具 Golf 中实现了该方法，作为 Go 运行时系统垃圾回收器的扩展，并通过一系列实验评估其有效性。初步结果表明，该方法在一系列微基准测试与一个大规模工业代码库的测试套件中分别能有效检测出 94% 与 50% 的部分死锁。此外，我们将 Golf 部署在 Uber 使用的一项真实服务上，在 24 小时内有效检测到由三个编程错误引起的 252 个部分死锁。

## 英文关键词

Go, message passing concurrency, channels, blocking errors, dynamic analysis

## 中文关键词

Go；消息传递并发；通道；阻塞错误；动态分析

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715990)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2025](../index.md)
