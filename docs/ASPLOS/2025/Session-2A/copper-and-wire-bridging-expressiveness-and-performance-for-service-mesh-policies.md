---
title: "Copper and Wire: Bridging Expressiveness and Performance for Service Mesh Policies"
description: "ASPLOS 2025 · Session 2A · Copper and Wire：弥合服务网格策略在表达力与性能之间的鸿沟"
tags:
  - "ASPLOS2025"
  - "Session 2A"
  - "Cloud Computing 1"
---

# Copper and Wire: Bridging Expressiveness and Performance for Service Mesh Policies

**中文标题：** Copper and Wire：弥合服务网格策略在表达力与性能之间的鸿沟

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Divyanshu Saxena (The University of Texas at Austin), William Zhang (The University of Texas at Austin), Shankara Pailoor (The University of Texas at Austin), Isil Dillig (The University of Texas at Austin), Aditya Akella (The University of Texas at Austin)

**单位：** The University of Texas at Austin

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707257) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Distributed microservice applications require a convenient means of controlling L7 communication between services. Service meshes have emerged as a popular approach to achieving this. However, current service mesh frameworks are difficult to use – they burden developers in realizing even simple communication policies, lack compatibility with diverse dataplanes, and introduce performance and resource overheads. We identify the root causes of these drawbacks and propose a ground-up new mesh architecture that overcomes them. We develop novel abstractions for mesh communication, a new mesh policy language centered on these abstractions to enable expressive policies, and a novel control plane that enables using minimal dataplane resources for policy enforcement. We develop the precise semantics of our language abstractions and demonstrate how our control plane can use them to execute policies correctly and optimally. We build and evaluate a prototype on realistic workloads and policies and open-source production traces. Our results show that complex policies can be specified in up to 6.75× fewer lines, enforced with up to 2.6× smaller tail latencies and up to 39% fewer CPU resources than today.

## 中文摘要

分布式微服务应用需要一种便捷的手段来控制服务之间的 L7 通信。服务网格已成为实现这一目标的流行方案。然而，当前的服务网格框架难以使用——即使实现简单的通信策略也会给开发者带来负担，缺乏与多种数据平面的兼容性，并引入性能与资源开销。我们找出这些缺陷的根本原因，并提出一种从零开始重新设计的网格架构来克服它们。我们为网格通信设计了新颖的抽象，围绕这些抽象设计了一种新的网格策略语言以支持富有表达力的策略，并提出一种新颖的控制平面，使策略执行只需占用最少的数据平面资源。我们给出语言抽象的精确语义，并展示我们的控制平面如何利用这些语义正确且最优地执行策略。我们基于真实的工作负载与策略以及开源生产轨迹构建并评估了一个原型。结果表明，相比当前方案，复杂策略的代码行数最多可减少到原来的 1/6.75，执行时的尾延迟最多可降低到原来的 1/2.6，CPU 资源最多可减少 39%。

## 英文关键词

Service Mesh, Microservices, Cloud Computing

## 中文关键词

服务网格；微服务；云计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707257)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2025](../index.md)
