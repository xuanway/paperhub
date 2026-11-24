---
title: "A Programming Model for Disaggregated Memory over CXL"
description: "ASPLOS 2026 · Session 1D · 面向 CXL 分离式内存的编程模型"
tags:
  - "ASPLOS2026"
  - "Session 1D"
  - "CXL & Memory Fabric"
---

# A Programming Model for Disaggregated Memory over CXL

**中文标题：** 面向 CXL 分离式内存的编程模型

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Gal Assa (Technion), Moritz Lumme (ETH Zürich), Lucas Bürgi (ETH Zürich), Michal Friedman (ETH Zürich), Ori Lahav (Tel Aviv University)

**单位：** Technion；ETH Zürich；Tel Aviv University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790121) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

CXL (Compute Express Link) is an emerging open industry-standard interconnect between processing and memory devices that is expected to revolutionize the way systems are designed. It enables cache-coherent, shared memory pools in a disaggregated fashion at unprecedented scales, allowing algorithms to interact with various storage devices using simple loads and stores. While CXL unleashes unique opportunities, it also introduces challenges of data management and crash consistency. For example, CXL currently lacks an adequate programming model, making it impossible to reason about the correctness and behavior of systems on top. In this work, we present CXL0, the first programming model for concurrent programs over CXL. We propose a high-level abstraction for memory accesses and formally define operational semantics. We demonstrate that CXL0 captures a wide range of current and future CXL setups and perform initial measurements on real hardware. To illustrate the usefulness of CXL0, we present a general transformation that enhances any linearizable concurrent algorithm with durability in a distributed partial-crash setting. We believe that this work will serve as a stepping stone for systems design and programming on top of CXL.

## 中文摘要

CXL（Compute Express Link）是一种新兴的开放行业标准互连技术，用于连接处理设备与内存设备，有望彻底改变系统的设计方式。它以解聚的方式在前所未有的规模上提供缓存一致的共享内存池，使算法能够通过简单的加载和存储操作与各种存储设备交互。尽管 CXL 释放了独特的机遇，但它也带来了数据管理和崩溃一致性方面的挑战。例如，CXL 目前缺乏一个恰当的编程模型，使得人们无法推理其上系统的正确性与行为。在本工作中，我们提出了 CXL0，这是首个面向 CXL 上并发程序的编程模型。我们提出了面向内存访问的高层抽象，并形式化地定义了操作语义。我们证明 CXL0 能够刻画当前和未来广泛的 CXL 配置，并在真实硬件上进行了初步测量。为说明 CXL0 的实用性，我们提出了一种通用变换，可在分布式部分崩溃环境下为任意可线性化的并发算法增强持久性。我们相信，本工作将成为 CXL 之上系统设计与编程的垫脚石。

## 英文关键词

CXL; Programming models; Disaggregated memory

## 中文关键词

CXL；编程模型；分离式内存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790121)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2026](../index.md)
