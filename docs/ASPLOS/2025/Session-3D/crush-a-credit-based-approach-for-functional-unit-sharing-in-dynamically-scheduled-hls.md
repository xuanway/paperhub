---
title: "CRUSH: A Credit-Based Approach for Functional Unit Sharing in Dynamically Scheduled HLS"
description: "ASPLOS 2025 · Session 3D · CRUSH：动态调度 HLS 中基于信用的功能单元共享方法"
tags:
  - "ASPLOS2025"
  - "Session 3D"
  - "EDA"
---

# CRUSH: A Credit-Based Approach for Functional Unit Sharing in Dynamically Scheduled HLS

**中文标题：** CRUSH：动态调度 HLS 中基于信用的功能单元共享方法

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiahui Xu (ETH Zurich), Lana Josipović (ETH Zurich)

**单位：** ETH Zurich

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707273) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Dynamically scheduled high-level synthesis (HLS) automatically translates software code (e.g., C/C++) to dataflow circuits—networks of compute units that communicate via handshake signals. These signals schedule the circuit during runtime, allowing them to handle irregular control flow or unpredictable memory accesses efficiently, thus giving them performance merit over statically scheduled circuits produced by standard HLS tools. To make HLS of dataflow circuits attractive and practical, we need various resource-optimization strategies to complement their performance advantage. A crucial technique is resource sharing: scarce and expensive resources (e.g., floating-point arithmetic units) are shared between multiple operations. However, this approach faces unique challenges in dataflow circuits, as an uncareful sharing strategy leads to performance degradation and circuit deadlock. This work presents CRUSH, a strategy that enables efficient functional unit sharing in dynamically scheduled HLS. CRUSH systematically avoids sharing-introduced deadlocks: it decouples interactions of operations in the shared resource to break resource dependencies. CRUSH maintains the benefit of dynamism: it does not constrain circuit execution with a complex deadlock avoidance mechanism and seizes sharing opportunities enabled by out-of-order access to the shared unit. CRUSH is practical: it employs scalable and effective heuristics for sharing decisions. Compared to a prior strategy, CRUSH achieves an average reduction of 12% DSPs, 15% FFs, and 90% optimization runtime. CRUSH has been integrated into the Dynamatic HLS compiler (

## 中文摘要

动态调度的高层综合（HLS）可自动将软件代码（例如 C/C++）转换为数据流电路——即通过握手信号通信的计算单元网络。这些信号在运行时调度电路，使其能够高效处理不规则控制流或不可预测的存储器访问，因而相比标准 HLS 工具生成的静态调度电路具有性能优势。要使数据流电路的 HLS 具有吸引力且实用，我们需要各种资源优化策略来补充其性能优势。一项关键技术是资源共享：稀缺且昂贵的资源（例如浮点算术单元）在多个操作之间共享。然而，这种方法在数据流电路中面临独特挑战，因为不够谨慎的共享策略会导致性能下降和电路死锁。本工作提出 CRUSH，一种能够在动态调度 HLS 中实现高效功能单元共享的策略。CRUSH 系统性地避免共享引入的死锁：它将共享资源中各操作之间的交互解耦，从而打破资源依赖。CRUSH 保持了动态性的优势：它不以复杂的死锁避免机制约束电路执行，并抓住对共享单元的乱序访问所带来的共享机会。CRUSH 具有实用性：它采用可扩展且有效的启发式方法进行共享决策。与先前的策略相比，CRUSH 平均减少 12% 的 DSP、15% 的 FF，并将优化运行时间缩短 90%。CRUSH 已集成到 Dynamatic HLS 编译器中（

## 英文关键词

Dataflow circuits; high-level synthesis; resource sharing

## 中文关键词

数据流电路；高层综合；资源共享

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707273)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2025](../index.md)
