---
title: "OsirisBFT: Say No to Task Replication for Scalable Byzantine Fault Tolerant Analytics"
description: "PPoPP 2024 Session High Performance Computing：以验证替代任务复制，容错规模与预期故障数解耦，吞吐与可扩展性更优"
tags:
  - "PPoPP2024"
  - "Session-3"
  - "High Performance Computing"
  - "Byzantine fault tolerance"
  - "distributed computing"
  - "resilient systems"
authors:
  - "Kasra Jamshidi"
  - "Keval Vora"
session: "Session 3: High Performance Computing"
session_number: 3
session_chair: "Helen Xu"
date: "2024-03-04"
time: "14:20–14:40"
room: "Moorfoot"
doi: "10.1145/3627535.3638468"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# OsirisBFT: Say No to Task Replication for Scalable Byzantine Fault Tolerant Analytics

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出基于验证的拜占庭容错系统 OsirisBFT，区分计算任务与状态更新任务，用通用验证算子与轻量验证策略，使应用可独立于预期故障数扩展，吞吐与可扩展性优于复制式处理。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 3: High Performance Computing</p>
</div>

**作者**：Kasra Jamshidi, Keval Vora (Simon Fraser University)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 14:20–14:40 · Session 3: High Performance Computing（主席：Helen Xu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638468) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

We present a verification-based Byzantine Fault Tolerant processing system, called OsirisBFT, for distributed task-parallel applications. OsirisBFT treats computation tasks differently from state update tasks, allowing the application to scale independently from number of expected failures. OsirisBFT captures application-specific verification semantics via generic verification operators and employs lightweight verification strategies with little coordination during graceful execution. Evaluation across multiple applications and workloads shows that OsirisBFT delivers high processing throughput and scalability compared to replicated processing. Importantly, the scalable nature of OsirisBFT enables it to reduce the performance gap compared to baseline with no fault tolerance by simply scaling out.

## 中文摘要

我们提出一种基于验证的拜占庭容错处理系统 OsirisBFT，面向分布式任务并行应用。OsirisBFT 将计算任务与状态更新任务区别对待，使应用能够独立于预期故障数量进行扩展。OsirisBFT 通过通用验证算子捕获应用特定的验证语义，并采用轻量级验证策略，在无故障（graceful）执行期间只需很少的协调。跨多种应用与工作负载的评估表明，与复制式处理相比，OsirisBFT 提供了高处理吞吐与可扩展性。重要的是，OsirisBFT 的可扩展特性使其能够仅通过横向扩展就缩小与无容错基线的性能差距。

## 英文关键词

Distributed Computing, Byzantine Fault Tolerance, Data Processing Systems, Resilient Systems

## 中文关键词

分布式计算；拜占庭容错；数据处理系统；弹性系统

---

## 一句话总结

> 提出基于验证的拜占庭容错系统 OsirisBFT，区分计算任务与状态更新任务，用通用验证算子与轻量验证策略，使应用可独立于预期故障数扩展，吞吐与可扩展性优于复制式处理。

## 研究问题

分布式任务并行应用的拜占庭容错通常依赖任务复制，容错规模与预期故障数耦合，应用难以扩展；需要不靠复制即可容错的处理方式。

## 方法简述

- 提出基于验证的拜占庭容错系统 OsirisBFT，将计算任务与状态更新任务区别对待
- 通过通用验证算子（generic verification operators）刻画应用特定的验证语义
- 采用轻量级验证策略，在无故障（graceful）执行期间只需极少协调即可完成验证

## 主要结果

- 在多种应用与工作负载上，OsirisBFT 相比复制式处理提供了更高的处理吞吐与可扩展性
- 其可扩展特性使系统仅通过横向扩展即可缩小与无容错基线的性能差距
- 使应用能够独立于预期故障数量进行扩展

---

> 所属 Session：[Session 3: High Performance Computing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
