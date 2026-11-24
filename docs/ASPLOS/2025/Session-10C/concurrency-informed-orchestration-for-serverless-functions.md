---
title: "Concurrency-Informed Orchestration for Serverless Functions"
description: "ASPLOS 2025 · Session 10C · 并发感知的 Serverless 函数编排"
tags:
  - "ASPLOS2025"
  - "Session 10C"
  - "Serverless Computing"
---

# Concurrency-Informed Orchestration for Serverless Functions

**中文标题：** 并发感知的 Serverless 函数编排

**所属 Session：** [Session 10C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Qichang Liu (University of Virginia), Yue Cheng (University of Virginia), Haiying Shen (University of Virginia), Ao Wang (Alibaba Group), Bharathan Balaji (Amazon)

**单位：** University of Virginia；Alibaba Group；Amazon

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716253) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Cold start delays are a main pain point for today's FaaS (Function-as-a-Service) platforms. A widely used mitigation strategy is keeping recently invoked function containers alive in memory to enable warm starts with minimal overhead. This paper identifies new challenges that state-of-theart FaaS keep-alive policies neglect. These challenges are caused by concurrent function invocations, a common FaaS workload behavior. First, concurrent requests present a tradeoff between reusing busy containers (delayed warm starts) versus cold-starting containers. Second, concurrent requests cause imbalanced evictions of containers that will be reused shortly thereafter. To tackle the challenges, we propose a novel serverless function container orchestration algorithm called CIDRE. CIDRE makes informed decisions to speculatively choose between a delayed warm start and a cold start under concurrency-driven function scaling. CIDRE uses both fine-grained container-level and coarse-grained concurrency information to make balanced eviction decisions. We evaluate CIDRE extensively using two production FaaS workloads. Results show that CIDRE reduces the cold start ratio and the average invocation overhead by up to 75.1% and 39.3% compared to state-of-the-art function keep-alive policies.

## 中文摘要

冷启动延迟是当今 FaaS（Function-as-a-Service，函数即服务）平台的主要痛点。一种广泛采用的缓解策略是将最近被调用的函数容器保留在内存中，从而以最小开销实现热启动。本文指出了现有最先进（state-of-the-art）FaaS 保活（keep-alive）策略所忽视的新挑战。这些挑战由并发的函数调用引起，而并发调用是 FaaS 工作负载中常见的行为。首先，并发请求在复用繁忙容器（延迟的热启动）与冷启动新容器之间形成权衡。其次，并发请求会导致容器被不均衡地驱逐，而这些容器随后不久就会被再次复用。为应对这些挑战，我们提出一种新颖的 Serverless 函数容器编排算法 CIDRE。CIDRE 在并发驱动的函数伸缩下做出有依据的决策，以推测性地在延迟的热启动与冷启动之间进行选择。CIDRE 同时利用细粒度的容器级信息与粗粒度的并发信息来做出均衡的驱逐决策。我们使用两个生产环境的 FaaS 工作负载对 CIDRE 进行了广泛评估。结果表明，与最先进的函数保活策略相比，CIDRE 将冷启动比例和平均调用开销分别降低最多 75.1% 和 39.3%。

## 英文关键词

Cloud Computing; Serverless Computing; Functionas-a-Service; Autoscaling; Container Orchestration; Caching

## 中文关键词

云计算；Serverless 计算；函数即服务；自动伸缩；容器编排；缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716253)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10C](index.md) · [返回 ASPLOS 2025](../index.md)
