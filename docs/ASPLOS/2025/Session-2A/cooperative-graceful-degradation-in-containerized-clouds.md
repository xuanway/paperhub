---
title: "Cooperative Graceful Degradation in Containerized Clouds"
description: "ASPLOS 2025 · Session 2A · 容器化云中的协同优雅降级"
tags:
  - "ASPLOS2025"
  - "Session 2A"
  - "Cloud Computing 1"
---

# Cooperative Graceful Degradation in Containerized Clouds

**中文标题：** 容器化云中的协同优雅降级

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Kapil Agrawal (University of California, Irvine), Sangeetha Abdu Jyothi (University of California, Irvine and VMware Research)

**单位：** University of California, Irvine；University of California, Irvine and VMware Research

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707244) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Cloud resilience is crucial for cloud operators and the myriad of applications that rely on the cloud. Today, we lack a mechanism that enables cloud operators to perform graceful degradation of applications while satisfying the application's availability requirements. In this paper, we put forward a vision for automated cloud resilience management with cooperative graceful degradation between applications and cloud operators. First, we investigate techniques for graceful degradation and identify an opportunity for cooperative graceful degradation in public clouds. Second, leveraging criticality tags on containers, we propose diagonal scaling—turning off non-critical containers during capacity crunch scenarios—to maximize the availability of critical services. Third, we design Phoenix, an automated cloud resilience management system that maximizes critical service availability of applications while also considering operator objectives, thereby improving the overall resilience of the infrastructure during failures. We experimentally show that the Phoenix controller running atop Kubernetes can improve critical service availability by up to 2× during large-scale failures. Phoenix can handle failures in a cluster of 100,000 nodes within 10 seconds. We also develop AdaptLab, an open-source resilience benchmarking framework that can emulate realistic cloud environments with real-world application dependency graphs.

## 中文摘要

云韧性对云运营商以及大量依赖云的应用至关重要。当前，我们缺乏一种机制，使云运营商能够在满足应用可用性需求的同时对应用执行优雅降级。本文提出一种自动化云韧性管理的愿景，即在应用与云运营商之间实现协同优雅降级。首先，我们研究优雅降级的各类技术，并识别出公有云中协同优雅降级的机会。其次，借助容器上的关键性标签，我们提出对角扩缩（diagonal scaling）——在容量紧缺场景下关闭非关键容器——以最大化关键服务的可用性。第三，我们设计 Phoenix，一个自动化云韧性管理系统，它最大化应用的关键服务可用性，同时兼顾运营商的目标，从而在故障期间提升基础设施的整体韧性。我们通过实验表明，运行在 Kubernetes 之上的 Phoenix 控制器在大规模故障期间可将关键服务可用性提升至多 2 倍。Phoenix 可在 10 秒内处理拥有 100,000 个节点的集群中的故障。我们还开发了 AdaptLab，一个开源的韧性基准测试框架，能够利用真实的应用依赖图来模拟真实的云环境。

## 英文关键词

Cloud resilience; graceful degradation; Service Level Objectives (SLOs)

## 中文关键词

云韧性；优雅降级；服务等级目标（SLO）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707244)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2025](../index.md)
