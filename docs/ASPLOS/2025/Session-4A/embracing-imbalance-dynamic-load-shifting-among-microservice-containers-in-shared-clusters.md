---
title: "Embracing Imbalance: Dynamic Load Shifting among Microservice Containers in Shared Clusters"
description: "ASPLOS 2025 · Session 4A · 拥抱不均衡：共享集群中微服务容器间的动态负载迁移"
tags:
  - "ASPLOS2025"
  - "Session 4A"
  - "Cloud Computing 2"
---

# Embracing Imbalance: Dynamic Load Shifting among Microservice Containers in Shared Clusters

**中文标题：** 拥抱不均衡：共享集群中微服务容器间的动态负载迁移

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shutian Luo (Yale University), Jianxiong Liao (Sun Yat-sen University,University of Macau), Chenyu Lin (University of Macau), Huanle Xu (University of Macau), Zhi Zhou (Sun Yat-sen University), Chengzhong Xu (University of Macau)

**单位：** Yale University；Sun Yat-sen University,University of Macau；University of Macau；Sun Yat-sen University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716255) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In a unified resource scheduling architecture, containers within the same microservice often encounter temporal and spatial performance imbalance when deployed in large-scale shared clusters. As a result, the commonly employed loadbalancing approach often leads to substantial resource wastage as applications are frequently over-provisioned to meet service level agreements (SLAs). In this paper, we utilize an alternative approach by leveraging load imbalance. The central concept involves the dynamic load shifting across microservice containers with a focus on imbalance awareness. However, achieving seamless integration between load shifting and resource scaling, while accommodating the demands of partial connection between upstream and downstream containers, remains a challenge. To address this challenge, we introduce Imbres—a new microservice system that optimizes load shifting, connection management, and resource scaling in tandem. One significant advantage of Imbres lies in its rapid responsiveness, relying solely on online gradients of latency, eliminating the need for offline profiling. Evaluation using real microservice benchmarks reveals that Imbres reduces resource allocation by up to 62% and decreases SLA violation probability by up to 82%, compared to state-of-the-art systems.

## 中文摘要

在统一的资源调度架构中，同一微服务内的容器在部署到大规模共享集群时常常遭遇时间和空间上的性能不均衡。因此，通常采用的负载均衡方法往往造成大量资源浪费，因为应用经常被过度配置以满足服务等级协议（SLA）。本文采用另一种思路，即利用负载不均衡。其核心思想是围绕不均衡感知，在微服务容器之间进行动态负载迁移。然而，在负载迁移与资源伸缩之间实现无缝集成，同时兼顾上下游容器之间部分连接的需求，仍然是一项挑战。为应对该挑战，我们提出 Imbres——一种新的微服务系统，它协同优化负载迁移、连接管理和资源伸缩。Imbres 的一个显著优势在于其快速响应能力，它仅依赖延迟的在线梯度，无需离线剖析。使用真实微服务基准的评估显示，与最先进的系统相比，Imbres 将资源分配最多降低 62%，并将 SLA 违规概率最多降低 82%。

## 英文关键词

Load Shifting, Microservice Scaling, SLA Guarantees

## 中文关键词

负载迁移；微服务伸缩；SLA 保障

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716255)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2025](../index.md)
