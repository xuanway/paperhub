---
title: "Tally: Non-Intrusive Performance Isolation for Concurrent Deep Learning Workloads"
description: "ASPLOS 2025 · Session 6A · Tally：面向并发深度学习工作负载的非侵入式性能隔离"
tags:
  - "ASPLOS2025"
  - "Session 6A"
  - "ML Systems 2"
---

# Tally: Non-Intrusive Performance Isolation for Concurrent Deep Learning Workloads

**中文标题：** Tally：面向并发深度学习工作负载的非侵入式性能隔离

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Wei Zhao (Stanford University,CentML), Anand Jayarajan (University of Toronto,Vector Institute), Gennady Pekhimenko (University of Toronto,Vector Institute)

**单位：** Stanford University,CentML；University of Toronto,Vector Institute

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707282) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

GPU underutilization is a significant concern in many production deep learning clusters, leading to prolonged job queues and increased operational expenses. A promising solution to this inefficiency is GPU sharing, which improves resource utilization by allowing multiple workloads to execute concurrently on a single GPU. However, deploying GPU sharing in production settings faces critical obstacles due to the limitations of existing mechanisms, including high integration costs, inadequate performance isolation, and limited application compatibility. To address these issues, we introduce Tally, a non-intrusive GPU sharing mechanism that provides robust performance isolation and comprehensive workload compatibility. The key to Tally's robust performance isolation capability lies in its fine-grained threadblock-level GPU kernel scheduling strategy, which allows the system to effectively mitigate interference caused by workload co-execution. We evaluate Tally on a diverse range of workloads and show that it incurs an average overhead of only 7.2% on the 99𝑡ℎ-percentile latency of high-priority inference tasks when executed concurrently with best-effort training workloads, compared to 188.9% overhead exhibited by the state-of-the-art GPU sharing systems like TGS, while achieving over 80% of TGS's system throughput.

## 中文摘要

GPU 利用率不足是许多生产环境深度学习集群中的突出问题，会导致作业排队时间延长和运营开销增加。针对这一低效问题，一个有前景的解决方案是 GPU 共享，它允许多个工作负载在单个 GPU 上并发执行，从而提高资源利用率。然而，由于现有机制存在局限——包括集成成本高、性能隔离不足以及应用兼容性有限——在生产环境中部署 GPU 共享面临严峻障碍。为解决这些问题，我们提出 Tally，一种非侵入式的 GPU 共享机制，可提供稳健的性能隔离和全面的工作负载兼容性。Tally 具备稳健性能隔离能力的关键，在于其细粒度的线程块级 GPU 内核调度策略，该策略使系统能够有效缓解工作负载共同执行所造成的干扰。我们在多种多样工作负载上评估了 Tally，结果表明：当高优先级推理任务与尽力而为的训练工作负载并发执行时，Tally 对其第 99 百分位延迟带来的平均开销仅为 7.2%，而 TGS 等最先进的 GPU 共享系统则表现出 188.9% 的开销；同时 Tally 达到了 TGS 系统吞吐量的 80% 以上。

## 英文关键词

GPU sharing, performance isolation, cloud infrastructure, deep learning, systems for machine learning

## 中文关键词

GPU 共享；性能隔离；云基础设施；深度学习；面向机器学习的系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707282)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2025](../index.md)
