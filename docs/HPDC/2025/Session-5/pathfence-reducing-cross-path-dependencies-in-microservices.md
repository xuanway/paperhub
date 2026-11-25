---
title: "PathFence: Reducing Cross-Path Dependencies in Microservices"
description: "HPDC 2025 · Session 5 — Clouds and FaaS"
tags:
  - "HPDC2025"
  - "Session 5"
  - "Clouds and FaaS"
---

# PathFence: Reducing Cross-Path Dependencies in Microservices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 5</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731583) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/gu.pdf)

**作者**：Xuhang Gu, Qingyang Wang

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）

---

## 英文摘要

Maintaining low and consistent response times is crucial for mission-critical, user-facing applications (e.g., e-commerce sites and social media platforms) that are built on microservices architectures. However, through extensive benchmarking of microservice applications in cloud environments, we find that response time stability in microservices applications is fragile, with delays ranging from milliseconds to seconds, even under moderate CPU utilization level (e.g., 60%). An important cause of this instability is cross-path dependency, where multiple execution paths, triggered by different user requests, share certain common component microservices. As a result, a slowdown in one execution path (e.g., due to a transient bottleneck) can propagate and degrade the performance of other execution paths that share the same microservices. To address this challenge, we propose PathFence, a novel approach that reduces the impact of cross-path dependencies in microservices applications by isolating workloads from different execution paths at shared microservices. By dynamically allocating software resources (e.g., thread and connection pools) with the awareness of execution path and optimizing concurrency level on shared microservices, PathFence significantly improves response time stability. Based on three real-world workload traces and three representative microservices benchmarks, we show that PathFence reduces the 99th percentile response time by up to 80% and decreases the number of dropped requests by over 90%.

## 中文摘要

对构建在微服务架构上的关键任务、面向用户的应用（如电商网站与社交媒体平台）而言，保持低且一致的响应时间至关重要。然而，通过对云环境中微服务应用的广泛基准测试，我们发现微服务应用的响应时间稳定性十分脆弱：即便在中等 CPU 利用率（如 60%）下，延迟也会从毫秒级波动到秒级。造成这种不稳定的一个重要原因是跨路径依赖：由不同用户请求触发的多条执行路径共享某些公共组件微服务。因此，某条执行路径的变慢（例如由于瞬时瓶颈）会传播并劣化共享同一微服务的其他执行路径的性能。为应对这一挑战，我们提出 PathFence，一种通过在共享微服务处隔离来自不同执行路径的负载，来降低跨路径依赖影响的新方法。PathFence 以执行路径感知的方式动态分配软件资源（如线程池与连接池），并优化共享微服务上的并发级别，从而显著提升响应时间稳定性。基于三种真实负载轨迹和三种代表性微服务基准，我们表明 PathFence 将第 99 百分位响应时间最高降低 80%，并将被丢弃请求数减少 90% 以上。

## 英文关键词

Microservices, Dependency, Resource Scheduling, Scalability

## 中文关键词

微服务，依赖，资源调度，可扩展性

---

[← 返回 Session 5 — Clouds and FaaS](index.md)
