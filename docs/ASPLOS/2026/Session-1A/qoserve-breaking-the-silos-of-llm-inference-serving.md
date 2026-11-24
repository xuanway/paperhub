---
title: "QoServe: Breaking the Silos of LLM Inference Serving"
description: "ASPLOS 2026 · Session 1A · QoServe：打破 LLM 推理服务的孤岛"
tags:
  - "ASPLOS2026"
  - "Session 1A"
  - "LLM Serving: Throughput Optimization"
---

# QoServe: Breaking the Silos of LLM Inference Serving

**中文标题：** QoServe：打破 LLM 推理服务的孤岛

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Kanishk Goel (Microsoft Research India), Jayashree Mohan (Microsoft Research India), Nipun Kwatra (Microsoft Research India), Ravi Anupindi (Microsoft Research India), Ram Ramjee (Microsoft Research India)

**单位：** Microsoft Research India

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790206) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The widespread adoption of Large Language Models (LLMs) has enabled diverse applications with very different latency requirements. Existing LLM serving frameworks rely on siloed infrastructure with coarse-grained workload segregation — interactive and batch — leading to inefficient resource utilization and limited support for fine-grained Quality-of-Service (QoS) differentiation. We present QoServe, a novel QoS-driven inference serving system that enables efficient co-scheduling of diverse workloads on shared infrastructure. QoServe introduces fine-grained QoS classification allowing applications to specify precise latency requirements, and dynamically adapts scheduling decisions based on real-time system state. Leveraging the predictable execution characteristics of LLM inference, QoServe implements dynamic chunking to improve overall throughput while maintaining strict QoS guarantees. Additionally, QoServe introduces hybrid prioritization to balance fairness and efficiency, and employs selective request relegation for graceful service degradation during overloads. Our evaluation demonstrates that QoServe increases serving capacity by 23% compared to current siloed deployments, while maintaining QoS guarantees on an A100 cluster, and improves per-replica goodput by up to 2.4x compared to Sarathi on a shared cluster. Notably, under extreme load, our system reduces SLO violations by an order of magnitude compared to current strategies.

## 中文摘要

大语言模型（LLM）的广泛应用催生了延迟需求差异极大的多样化应用。现有 LLM 服务框架依赖孤岛式（siloed）基础设施，以"交互式/批处理"的粗粒度方式隔离工作负载，导致资源利用效率低下，且对细粒度服务质量（QoS）差异化的支持有限。我们提出 QoServe，一种新颖的由 QoS 驱动的推理服务系统，可在共享基础设施上对多样化工作负载进行高效协同调度。QoServe 引入细粒度 QoS 分类，使应用能够指定精确的延迟需求，并依据实时系统状态动态调整调度决策。借助 LLM 推理可预测的执行特征，QoServe 实现动态分块（dynamic chunking），在保持严格 QoS 保障的同时提升整体吞吐。此外，QoServe 引入混合优先级机制以平衡公平性与效率，并采用选择性请求降级（selective request relegation），在过载时实现服务的优雅降级。我们的评估表明，与当前孤岛式部署相比，QoServe 在 A100 集群上将服务容量提升 23%，同时保持 QoS 保障；在共享集群上，与 Sarathi 相比，每副本有效吞吐最高提升 2.4×。值得注意的是，在极端负载下，本系统相比现有策略将 SLO 违反次数降低了一个数量级。

## 英文关键词

Large Language Models; Quality of Service; Inference serving; Scheduling; Reliability

## 中文关键词

大语言模型；服务质量；推理服务；调度；可靠性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790206)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2026](../index.md)
