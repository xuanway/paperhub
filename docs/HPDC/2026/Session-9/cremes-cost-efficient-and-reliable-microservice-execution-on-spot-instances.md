---
title: "Cremes: Cost-Efficient and Reliable Microservice Execution on Spot Instances"
description: "HPDC 2026 · Session 9 — Cloud, Serverless & Microservices"
tags:
  - "HPDC2026"
  - "Session 9"
  - "Cloud, Serverless & Microservices"
---

# Cremes: Cost-Efficient and Reliable Microservice Execution on Spot Instances

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 9</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807817)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenLCLXX26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenLCLXX26)

**作者**：Liao Chen, Chenyu Lin, Junlin Chen, Shutian Luo, Huanle Xu, ChengZhong Xu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）

---

## 英文摘要

While spot instances offer a cost-effective alternative to on-demand cloud resources, they introduce reliability challenges for latency-sensitive microservices due to preemption risks and unpredictable provisioning delays. Conventional resource management systems, which often rely on assumptions of immediate instance availability, fail to account for these operational realities—resulting in increased risk of SLO violations when deployed in spot-based environments. In this paper, we propose Cremes, an adaptive and cost-efficient scaling framework that ensures microservice recovery within the spot instance grace period. Cremes explicitly models both instance waiting time and microservice startup latency, leverages cloud-exposed availability metrics, and applies lightweight machine learning for end-to-end latency prediction. By integrating these components into a multi-dimensional optimization engine, Cremes minimizes cost while satisfying recovery and performance constraints. Evaluations on AWS instances using DeathStarBench, TrainTicket, and Alibaba trace-driven experiments show that Cremes reduces infrastructure cost by up to 37.1% and maintains SLO violation rates under preemptible environments below 6.7%.

## 中文摘要

尽管竞价实例为按需云资源提供了高性价比的替代方案，但由于抢占风险和不可预测的供应延迟，它们给延迟敏感的微服务带来可靠性挑战。传统资源管理系统往往基于实例立即可用的假设，未能考虑这些实际运行情况——在竞价实例环境中部署时会导致 SLO 违规风险上升。本文提出 Cremes，一个自适应且高性价比的伸缩框架，确保微服务在竞价实例宽限期内完成恢复。Cremes 显式建模实例等待时间与微服务启动延迟，利用云平台暴露的可用性指标，并应用轻量级机器学习进行端到端延迟预测。通过将这些组件集成到多维优化引擎中，Cremes 在满足恢复与性能约束的同时最小化成本。在 AWS 实例上使用 DeathStarBench、TrainTicket 和阿里巴巴轨迹驱动的实验表明，Cremes 将基础设施成本最高降低 37.1%，并将可抢占环境下的 SLO 违规率保持在 6.7% 以下。

## 英文关键词

Microservice scaling, Spot instance, SLO requirement

## 中文关键词

微服务伸缩，竞价实例，SLO 要求

---

[← 返回 Session 9 — Cloud, Serverless & Microservices](index.md)
