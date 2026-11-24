---
title: "Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO"
description: "ASPLOS 2026 · Session 2C · 异步与 GPU：以 AGIO 弥合 I/O 中的这一二分对立"
tags:
  - "ASPLOS2026"
  - "Session 2C"
  - "GPU Systems & Scheduling"
---

# Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO

**中文标题：** 异步与 GPU：以 AGIO 弥合 I/O 中的这一二分对立

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jihoon Han (Pennsylvania State University), Anand Sivasubramaniam (Pennsylvania State University), Chia-Hao Chang (Nvidia), Vikram Sharma Mailthody (Nvidia Research), Zaid Qureshi (Nvidia Research), Wen-mei W. Hwu (Nvidia Research)

**单位：** Pennsylvania State University；Nvidia；Nvidia Research

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790130) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

GPUs rely on a largely synchronous programming and execution model. With increasing need to access data residing on SSDs, GPU threads can incur significant latencies for such accesses when using blocking/synchronous I/O mechanisms. There is little hardware/systems support today to perform non-blocking/asynchronous operations from GPU threads directly to tolerate microsecond level latencies incurred in SSD accesses. To fix this dichotomy, this paper presents the design, implementation and evaluation of AGIO, which provides APIs and a runtime environment for GPU threads to directly perform asynchronous I/O operations (fully GPUorchestrated without CPU involvement). AGIO decouples, both in time and space, the I/O initiation from its completion, to allow useful computation in-between, in order to hide much of the I/O latency. This is particularly useful in applications with access patterns known at compile time, where similar to prefetching, AGIO I/Os can be introduced ahead of need, to yield 65% better performance than its synchronous counterpart. A non-intuitive benefit of AGIO, particularly in applications with data dependent accesses, is the ability to allow threads to proceed beyond I/O initiation, towards initiating more I/O, even if there is little compute to overlap. Such pro-active I/O issuance increases the I/O parallelism to more fully utilize underlying bandwidths, yielding 32% better performance than the synchronous alternative in data dependent executions. Decoupling initiation from completion makes AGIO more adaptive to dataset characteristics, with the programmer not needing a priori knowledge of inputs for effective performance. We also show that AGIO can meet (or better) the performance using a GPU with fewer than half the compute engines of its synchronous counterparts.

## 中文摘要

GPU 依赖在很大程度上同步的编程与执行模型。随着访问存放于 SSD 上的数据的需求不断增长，GPU 线程在使用阻塞/同步 I/O 机制进行这类访问时会承受显著的延迟。目前几乎没有硬件/系统支持来让 GPU 线程直接执行非阻塞/异步操作，以容忍 SSD 访问中所产生的微秒级延迟。为消解这一二分对立，本文介绍 AGIO 的设计、实现与评估，它提供 API 和一个运行时环境，使 GPU 线程能够直接执行异步 I/O 操作（完全由 GPU 编排，无 CPU 参与）。AGIO 在时间和空间上将 I/O 的发起与其完成解耦，以允许其间进行有用的计算，从而隐藏大部分 I/O 延迟。这在访问模式在编译期即已知的应用中尤为有用：与预取类似，AGIO 的 I/O 可以提前于需求被引入，从而比其同步对等方案获得 65% 的性能提升。AGIO 的一个非直观优势，尤其是在访问依赖于数据的应用中，是能够让线程越过 I/O 发起继续推进，进而发起更多 I/O，即使几乎没有可重叠的计算。这种主动的 I/O 发起提高了 I/O 并行度，以更充分地利用底层带宽，在数据相关执行中比同步方案获得 32% 的性能提升。将发起与完成解耦使 AGIO 对数据集特征更具适应性，程序员无需事先了解输入即可获得有效性能。我们还表明，AGIO 可以使用计算引擎数量不到其同步对等方案一半的 GPU 来达到（或超过）该性能。

## 英文关键词

GPUs; Storage; SSDs; Asynchrony; GPUDirect; I/O; P2P

## 中文关键词

GPU；存储；SSD；异步性；GPUDirect；I/O；P2P

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790130)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2026](../index.md)
