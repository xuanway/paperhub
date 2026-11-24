---
title: "HardHarvest: Hardware-Supported Core Harvesting for Microservices"
description: "ISCA 2025 · Session 4C · HardHarvest：面向微服务的硬件支持核心收割"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# HardHarvest: Hardware-Supported Core Harvesting for Microservices

**中文标题：** HardHarvest：面向微服务的硬件支持核心收割

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Jovan Stojkovic, Chunao Liu, Muhammad Shahbaz, Josep Torrellas

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731071) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

In microservice environments, users size their virtual machines (VMs) for peak loads, leaving cores idle much of the time. To im- prove core utilization and overall throughput, it is instructive to con- sider a recently-introduced software technique for environments with relatively long-running monolithic applications: Core Harvest- ing. With this technique, Harvest VMs running batch applications temporarily steal idle cores allocated by Primary VMs running latency-critical applications, and return them on demand. Unfor- tunately, re-assigning cores across VMs has substantial overhead, resulting from hypervisor calls, context switching, and flushing TLBs/caches. While such overhead is acceptable in monolithic ap- plication environments, it would be prohibitive in environments with sub-millisecond microservices. To address this problem, this paper proposes, for the first time, an architecture for core harvesting in hardware. The architecture, called HardHarvest, targets microservices. It aims to: 1) maximize core utilization, 2) minimize impact on Primary VM tail latency, and 3) boost Harvest VM throughput. HardHarvest eliminates software overheads by using in-hardware request scheduling and partition- ing TLBs/caches with a smart replacement algorithm. On average, compared to state-of-the-art software core harvesting, HardHarvest increases core utilization by 1.5×, increases Harvest VM throughput by 1.8×, and reduces Primary VM tail latency by 6.0×.

## 中文摘要

在微服务场景中，用户按照峰值负载配置虚拟机（VM）规格，导致大部分时间核心处于空闲状态。为提升核心利用率与整体吞吐，业界借鉴了一种面向长时单体应用的软件方案：核心资源征用（Core Harvesting）。该方案中，运行批处理任务的征用虚拟机（Harvest VM）临时借用低延迟关键型主虚拟机（Primary VM）闲置的核心，在需要时归还。
但跨虚拟机重新分配核心的开销很大：涉及虚拟化管理程序调用、上下文切换、TLB与缓存冲刷。这类开销在单体应用场景尚可接受，对于亚毫秒级微服务而言则无法承受。

针对该问题，本文首次提出硬件层面的核心征用架构HardHarvest，面向微服务场景，目标：1）最大化核心利用率；2）最小化对主VM长尾延迟的影响；3）提升征用VM的吞吐。HardHarvest通过硬件内请求调度，配合智能替换算法对TLB、缓存进行分区管理，消除软件带来的额外开销。实验表明，对比前沿软件核心征用方案，HardHarvest平均将核心利用率提升至原来的1.5倍，征用VM吞吐提升至1.8倍，主VM长尾延迟降低至原来的1/6。

## 英文关键词

Microservices, cloud computing, core harvesting

## 中文关键词

微服务, 云计算, 核心资源征用

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731071)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
