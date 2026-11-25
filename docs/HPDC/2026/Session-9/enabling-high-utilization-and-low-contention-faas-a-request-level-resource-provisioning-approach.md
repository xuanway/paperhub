---
title: "Enabling High-Utilization and Low-Contention FaaS: A Request-Level Resource Provisioning Approach"
description: "HPDC 2026 · Session 9 — Cloud, Serverless & Microservices"
tags:
  - "HPDC2026"
  - "Session 9"
  - "Cloud, Serverless & Microservices"
---

# Enabling High-Utilization and Low-Contention FaaS: A Request-Level Resource Provisioning Approach

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 9</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807810)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#LiYWPSX26](https://dblp.org/db/conf/hpdc/hpdc2026.html#LiYWPSX26)

**作者**：Runfu Li, Zishu Yu, Yifan Wang, Xiaohui Peng, Ninghui Sun, Zhiwei Xu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）

---

## 英文摘要

Function-as-a-Service offers cost efficiency but often suffers from resource underutilization. This underutilization stems from the instance-level resource provisioning pattern, an issue that existing optimizations have failed to resolve fundamentally. The core problem is that static coarse-grained instance-level resource allocation cannot match the millisecond-level burstiness of dynamic requests. Consequently, it is difficult for current systems to achieve high resource utilization while maintaining high quality of service (QoS) guarantees. To address the problem, this paper advocates a shift to request-level resource provisioning, which redefines the individual request as the atomic unit for scheduling and resource management. We implement this approach in RRP, a scalable FaaS platform that enables efficient per-request resource allocation and release. RRP unifies instance placement and request routing with low-overhead, millisecond-level global visibility. Our evaluation shows that RRP significantly outperforms state-of-the-art instance-level platforms and algorithms. By matching resources to each request’s needs and isolating them from contention, RRP achieves low latency and high utilization. Specifically, on real-world Azure traces, RRP achieves speedups of 1.33×–30.15× for average end-to-end latency and 1.37×–61.46× for P99 latency, and raises CPU utilization from 44.80%–56.32% to 72.49% under bursty loads.

## 中文摘要

函数即服务（FaaS）具有成本效益，但常常存在资源利用率不足的问题。这种利用率不足源于实例级资源配置模式，现有优化未能从根本上解决该问题。核心问题在于，静态粗粒度的实例级资源分配无法匹配动态请求的毫秒级突发性。因此，当前系统难以在保持高服务质量（QoS）保证的同时实现高资源利用率。为解决该问题，本文主张转向请求级资源配置，将单个请求重新定义为调度与资源管理的原子单元。我们在 RRP 中实现了该方法，这是一个可扩展的 FaaS 平台，支持高效的逐请求资源分配与释放。RRP 以低开销、毫秒级的全局可见性统一了实例放置与请求路由。我们的评估表明，RRP 显著优于最先进的实例级平台与算法。通过让资源匹配每个请求的需求并将其与争用隔离，RRP 实现了低延迟与高利用率。具体而言，在真实 Azure 轨迹上，RRP 将平均端到端延迟加速 1.33–30.15 倍，P99 延迟加速 1.37–61.46 倍，并在突发负载下将 CPU 利用率从 44.80%–56.32% 提升至 72.49%。

## 英文关键词

Cloud Computing, Serverless, Function as a Service, Resource Management, Request-Level Provision

## 中文关键词

云计算，无服务器，函数即服务，资源管理，请求级资源配置

---

[← 返回 Session 9 — Cloud, Serverless & Microservices](index.md)
