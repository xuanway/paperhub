---
title: "AccelFlow: Orchestrating an On-Package Ensemble of Fine-Grained Accelerators for Microservices"
description: "HPCA 2026 · Efficient Serving and Resource Management"
tags:
  - "HPCA2026"
  - "Efficient Serving and Resource Management"
---

# AccelFlow: Orchestrating an On-Package Ensemble of Fine-Grained Accelerators for Microservices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient Serving and Resource Management。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient Serving and Resource Management</p>
</div>

**论文链接**：
**作者**：Jovan Stojkovic University of Illinois at Urbana-Champaign , Abraham Farrell University of Illinois Urbana-Champaign , Zhangxiaowen Gong Intel , Christopher J. Hughes Intel , Josep Torrellas University of Illinois at Urbana-Champaign
**会议**：HPCA 2026

---

## 中文标题

AccelFlow：面向微服务的封装内细粒度加速器集合编排

## 英文摘要

Microservices suffer from the execution of auxiliary operations known as datacenter tax, such as RPC and TCP processing, and data (de)serialization, (de)encryption, and (de)compression. To minimize this tax, multiple hardware accelerators have been proposed. However, it is unclear how these accelerators should be orchestrated. Past work has focused only on orchestrating accelerators in coarse-grained environments with monolithic applications. In this paper, we characterize the needs of orchestrating an ensemble of on-package accelerators in microservice environments. We observe that orchestration frameworks need to be highly dynamic and nimble. The basic operations to be accelerated are fine grained, potentially taking only tens of µs. Moreover, the sequence of accelerators to use is often affected by “branch conditions” whose real-time resolution determines the set of subsequent accelerators needed. To address these challenges, we present AccelFlow, the first orchestration framework for on-package accelerators of microservices. In AccelFlow, CPU cores build software structures called Traces that contain sequences of accelerators to call. A core enqueues a trace in an accelerator in user mode and, from then on, the accelerators in the trace execute in sequence without CPU involvement. A trace can include branch conditions whose outcomes determine the trace control flow. Compared to state-of-the-art accelerator orchestrators, AccelFlow on average reduces P99 tail latency by 70%, reduces average latency by 38%, and increases throughput by 120%.

## 中文摘要

微服务需要执行被称为数据中心税（datacenter tax）的辅助操作，如 RPC 与 TCP 处理，以及数据（反）序列化、（解）密与（解）压缩。为最小化这一税负，已有多种硬件加速器被提出。然而如何编排这些加速器尚不明确。以往工作仅关注单体应用等粗粒度环境下的加速器编排。本文刻画了在微服务环境中编排封装内加速器集合的需求。我们观察到，编排框架需要高度动态且敏捷：待加速的基本操作是细粒度的，可能仅耗时数十微秒；此外，要使用的加速器序列常受“分支条件”影响，其实时结果决定了后续所需的加速器集合。为应对这些挑战，我们提出 AccelFlow，首个面向微服务封装内加速器的编排框架。在 AccelFlow 中，CPU 核心构建称为 Trace 的软件结构，其中包含要调用的加速器序列。核心在用户态将 Trace 入队到某个加速器，此后该 Trace 中的加速器按序执行而无需 CPU 参与。Trace 可包含分支条件，其结果决定 Trace 的控制流。与最先进的加速器编排器相比，AccelFlow 平均将 P99 尾时延降低 70%，平均时延降低 38%，吞吐提升 120%。
