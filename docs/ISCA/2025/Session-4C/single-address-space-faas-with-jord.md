---
title: "Single-Address-Space FaaS with Jord"
description: "ISCA 2025 · Session 4C · 基于 Jord 的单地址空间 FaaS"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# Single-Address-Space FaaS with Jord

**中文标题：** 基于 Jord 的单地址空间 FaaS

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Yuanlong Li, Atri Bhattacharyya, Madhur Kumar, Abhishek Bhattacharjee, Yoav Etsion, Babak Falsafi, Sanidhya Kashyap, Mathias Payer

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731108) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Function-as-a-Service (FaaS) has emerged as a popular cloud par- adigm that simplifies software development and deployment by providing scalable and event-driven function execution without the burden of managing servers. FaaS was originally created with a function as a function semantics to enable standalone microservices with adequately short execution time to meet microsecond-scale service-level objectives (SLOs). Unfortunately, today’s FaaS systems fundamentally suffer from millisecond-level performance bottle- necks that arise from isolating functions in separate address spaces inside containers or microVMs. Prior work has focused on optimiz- ing FaaS performance, but these systems still fall short of meeting microsecond-level SLOs. In this paper, we present Jord, a FaaS sys- tem that revives the original function-as-a-function vision of FaaS. Jord leverages hardware/software co-design to colocate functions in a single address space with user-level in-process memory iso- lation, extending the capability of traditional virtual memory. By performing memory isolation and management in nanoseconds, Jord enables zero-copy cross-function communication and scalable function dispatch, thereby minimizing FaaS overheads. We demon- strate that Jord can meet microsecond-level SLOs for microservice workloads while performing within 16% of an idealized but insecure baseline and delivering over 2×higher throughput compared to enhanced state-of-the-art systems.

## 中文摘要

函数即服务（FaaS）是主流云范式，提供可扩展、事件驱动的函数执行能力，免去服务器运维负担，简化开发与部署。FaaS最初的设计理念是“函数即独立执行单元”，目标是实现独立微服务，执行时间足够短，满足微秒级服务等级目标（SLO）。但当下FaaS系统受限于容器或微虚拟机（microVM）带来的独立地址空间隔离，存在毫秒级性能瓶颈。已有研究对FaaS进行性能优化，但仍难以达到微秒级SLO。本文提出Jord，一套FaaS系统，回归FaaS最初“函数即独立单元”的设计愿景。Jord采用软硬件协同设计，将多个函数部署在同一个地址空间内，依托用户态进程内内存隔离机制拓展传统虚拟内存能力。Jord可以在纳秒粒度完成内存隔离与管理，支持零拷贝跨函数通信和高扩展的函数调度，大幅削减FaaS开销。实验表明，Jord可以让微服务负载满足微秒级SLO；性能距离无安全保障的理想基线仅相差16%，相比优化后的前沿系统，吞吐量提升2倍以上。

## 英文关键词

Function-as-a-Service, Single-Address-Space, Virtual Memory

## 中文关键词

函数即服务, 单一地址空间, 虚拟内存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731108)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
