---
title: "Themis: Improving Performance and Fairness in Multi-Stream NVMe SSDs"
description: "MICRO 2026 · Session 6B · Themis：提高多流 NVMe SSD 的性能与公平性"
tags:
  - "MICRO2026"
  - "Storage"
---

# Themis: Improving Performance and Fairness in Multi-Stream NVMe SSDs

**中文标题：** Themis：提高多流 NVMe SSD 的性能与公平性

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Jiaojiao Wu, Lieven Eeckhout, Qiyu Liu, Zhigang Cai, François Trahay, Yuanquan Shi, Jim Woodcock, Jianwei Liao

**来源：** MICRO 2026，pp. 1983–1997；[DOI](https://doi.org/10.1109/MICRO67795.2026.00139)

## 英文摘要

NAND flash-based SSDs are widely adopted for their performance, with the NVMe interface further enhancing I/O throughput by providing multi-stream support. However, streams with high intensity and/or strong locality can monopolize shared resources, degrading fairness and performance of concurrent streams. Existing fairness-oriented approaches rely on a slowdown-based metric, which suffers from practical measurement challenges and limited accuracy, while neglecting request-level dynamics. Consequently, they optimize inter-stream fairness but overlook intra-stream variations. This paper introduces the Request IneQuality (RIQ) score, a request-level fairness metric based on the Lorenz curve computed from per-request Normalized Completion Round (NCR) scores. Subsequently, we design a flash I/O scheduling mechanism called Themis, which monitors the NCRs of requests and applies a two-step scheduling strategy to improve both inter-stream and intra-stream fairness, thereby enhancing I/O service quality. Trace-driven simulation experiments using a variety of production multi-stream mixes show that Themis significantly improves request-level and stream-level fairness while reducing average I/O response time and tail latency compared to state-of-the-art I/O schedulers.

## 中文摘要

基于 NAND 闪存的 SSD 因其性能而被广泛采用，NVMe 接口通过提供多流支持进一步提高 I/O 吞吐量。然而，具有高强度和/或强局部性的流可能会独占共享资源，从而降低并发流的公平性和性能。现有的面向公平的方法依赖于基于减速的度量，该度量面临着实际测量挑战和有限的准确性，同时忽略了请求级别的动态。因此，它们优化了流间公平性，但忽略了流内变化。本文介绍了请求 IneQuality (RIQ) 分数，这是一种请求级别的公平性度量，基于根据每个请求归一化完成回合 (NCR) 分数计算得出的洛伦兹曲线。随后，我们设计了一种称为Themis的闪存I/O调度机制，它监控请求的NCR并应用两步调度策略来提高流间和流内的公平性，从而提高I/O服务质量。使用各种生产多流混合的跟踪驱动模拟实验表明，与最先进的 I/O 调度程序相比，Themis 显着提高了请求级别和流级别的公平性，同时减少了平均 I/O 响应时间和尾部时延。

## 中文关键词

多流 NVMe 固态硬盘；性能与公平性；存储调度；资源管理

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
