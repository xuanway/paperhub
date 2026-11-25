---
title: "FaaSKeeper: Learning from Building Serverless Services with ZooKeeper as an Example"
description: "HPDC 2024 · Session 3 — Serverless Computing"
tags:
  - "HPDC2024"
  - "Session 3"
  - "Serverless Computing"
---

# FaaSKeeper: Learning from Building Serverless Services with ZooKeeper as an Example

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 3</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658661)

**作者**：Marcin Copik, Alexandru Calotoiu, Pengyu Zhou, Konstantin Taranov, Torsten Hoefler

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）

---

## 英文摘要

FaaS (Function-as-a-Service) revolutionized cloud computing by replacing persistent virtual machines with dynamically allocated resources. This shift trades locality and statefulness for a pay-as-you-go model more suited to variable and infrequent workloads. However, the main challenge is to adapt services to the serverless paradigm while meeting functional, performance, and consistency requirements. In this work, we push the boundaries of FaaS computing by designing a serverless variant of ZooKeeper, a centralized coordination service with a safe and wait-free consensus mechanism. We define synchronization primitives to extend the capabilities of scalable cloud storage and outline a set of requirements for efficient computing with serverless. In FaaSKeeper, the first coordination service built on serverless functions and cloud-native services, we explore the limitations of serverless offerings and propose improvements essential for complex and latency-sensitive applications. We share serverless design lessons based on our experiences of implementing a ZooKeeper model deployable to clouds today. FaaSKeeper maintains the same consistency guarantees and interface as ZooKeeper, with a serverless price model that lowers costs up to 110-719x on infrequent workloads.

## 中文摘要

FaaS（函数即服务）通过用动态分配的资源取代持久虚拟机，彻底变革了云计算。这种转变以局部性和有状态性为代价，换取了更适合多变、低频负载的按需付费模式。然而，主要挑战在于使服务适配无服务器范式，同时满足功能、性能与一致性要求。在本工作中，我们通过设计 ZooKeeper（一个具有安全且无等待共识机制的集中式协调服务）的无服务器变体，拓展了 FaaS 计算的边界。我们定义同步原语以扩展可扩展云存储的能力，并勾勒出用无服务器进行高效计算的一组需求。在 FaaSKeeper——首个基于无服务器函数与云原生服务构建的协调服务——中，我们探究了无服务器供给的局限，并提出对复杂且延迟敏感应用至关重要的改进。基于我们实现可部署到当今云上的 ZooKeeper 模型的经验，我们分享了无服务器设计经验。FaaSKeeper 保持与 ZooKeeper 相同的一致性保证与接口，其无服务器价格模型在低频负载下将成本降低达 110–719 倍。

## 英文关键词

serverless, function-as-a-service, faas, cloud computing, zookeeper

## 中文关键词

无服务器，函数即服务，FaaS，云计算，ZooKeeper

---

[← 返回 Session 3 — Serverless Computing](index.md)
