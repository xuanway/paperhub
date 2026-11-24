---
title: "Extended User Interrupts (xUI): Fast and Flexible Notification without Polling"
description: "ASPLOS 2025 · Session 8C · 扩展用户中断（xUI）：无需轮询的快速灵活通知"
tags:
  - "ASPLOS2025"
  - "Session 8C"
  - "Potpourri 2"
---

# Extended User Interrupts (xUI): Fast and Flexible Notification without Polling

**中文标题：** 扩展用户中断（xUI）：无需轮询的快速灵活通知

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Berk Aydogmus (Purdue University), Linsong Guo (UC San Diego), Danial Zuberi (UC San Diego), Tal Garfinkel (UC San Diego), Dean Tullsen (UC San Diego), Amy Ousterhout (UC San Diego), Kazem Taram (Purdue University)

**单位：** Purdue University；UC San Diego

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716028) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Extended user interrupts (xUI) is a set of processor extensions that builds on Intel's UIPI model of user interrupts, for enhanced performance and flexibility. This paper deconstructs Intel's current UIPI design through analysis and measurement, and uses this to develop an accurate model of its timing. It then introduces four novel enhancements to user interrupts: tracked interrupts, hardware safepoints, a kernel bypass timer, and interrupt forwarding. xUI is modeled in gem5 simulation and evaluated on three use cases – preemption in a high-performance user-level runtime, IO notification in a layer3 router using DPDK, and IO notification in a synthetic workload with a streaming accelerator modeled after Intel's Data Streaming Accelerator. This work shows that xUI offers the performance of shared memory polling with the efficiency of asynchronous notification.

## 中文摘要

扩展用户中断（xUI）是一组处理器扩展，它构建在 Intel 的用户中断 UIPI 模型之上，以获得更高的性能与灵活性。本文通过分析与测量对 Intel 当前的 UIPI 设计进行解构，并据此建立其时序的精确模型。随后，本文为用户中断引入四项新增强：可跟踪中断（tracked interrupts）、硬件安全点（hardware safepoints）、内核旁路定时器（kernel bypass timer）以及中断转发（interrupt forwarding）。xUI 在 gem5 模拟器中建模，并在三个用例上进行评估——高性能用户级运行时中的抢占、使用 DPDK 的三层路由器中的 IO 通知，以及一个带有仿照 Intel 数据流加速器（Data Streaming Accelerator）建模的流式加速器的合成负载中的 IO 通知。该工作表明，xUI 以异步通知的效率提供了共享内存轮询的性能。

## 英文关键词

Interrupt, User Space, Preemption, Processor Architecture

## 中文关键词

中断；用户态；抢占；处理器体系结构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716028)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2025](../index.md)
