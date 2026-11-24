---
title: "NetCrafter: Tailoring Network Traffic for Non-Uniform Bandwidth Multi-GPU Systems"
description: "ISCA 2025 · Session 6B · NetCrafter：为非均匀带宽多 GPU 系统定制网络流量"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# NetCrafter: Tailoring Network Traffic for Non-Uniform Bandwidth Multi-GPU Systems

**中文标题：** NetCrafter：为非均匀带宽多 GPU 系统定制网络流量

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Amel Fatima, Yang Yang, Yifan Sun, Rachata Ausavarungnirun, Adwait Jog

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731040) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Multiple Graphics Processing Units (GPUs) are being integrated into systems to meet the computing demands of emerging workloads. To continuously support more GPUs in a system, it is important to connect them efficiently and effectively. To this end, emerging multi-GPU systems are adopting a hierarchical approach – a group of GPUs with high affinity are connected with higher-bandwidth networks, while multiple groups of GPUs are connected with lower- bandwidth networks to support the scaling of GPUs. Unfortunately, such a non-uniform bandwidth configuration leads to significant performance bottlenecks, especially across lower-bandwidth net- works. We present NetCrafter, a combination of novel approaches to deal with the network traffic. NetCrafter is based on three observations: a) not all flits in the network fully utilize the network bandwidth, b) not all requested flits are even necessary – they are requested in the hope that their data might be useful later, c) some flits are more latency-sensitive than others and must be prioritized in the network. NetCrafter leverages these observations to re- duce the network traffic by stitching compatible flits that are partly filled, and trimming the number of flits by not fetching flits that are unnecessary. NetCrafter also effectively manages network traffic by sequencing flits such that latency-sensitive flits reach their destinations faster. Although our proposed techniques are generic and can be applied to any network, they are especially useful in alleviating the bottlenecks presented by lower-bandwidth networks connecting multiple groups of GPUs. Overall, NetCrafter signifi- cantly improves multi-GPU performance, thereby contributing to efficient scaling of GPU-based systems.

## 中文摘要

为满足新兴负载的算力需求，系统中集成了多块GPU。为在单台机器内接入更多GPU，GPU之间高效互联至关重要。为此，新一代多GPU系统采用分层互联思路：通信紧密的一组GPU之间使用高带宽网络，而不同GPU组之间依靠低带宽网络互联，以此实现GPU规模扩展。
但这种带宽非均匀配置会带来显著性能瓶颈，跨低带宽网络的通信尤为突出。本文提出NetCrafter，一套全新机制用于处理网络流量。NetCrafter基于三点观察：（1）网络中的部分微片并没有占满带宽；（2）部分被请求的微片本身并非必需，只是提前预取，期望后续数据可能用到；（3）不同微片对延迟敏感度不同，需要在网络中区分优先级。

NetCrafter利用上述结论削减网络流量：把未填满的兼容微片拼接在一起，同时舍弃不必要的微片请求，减少传输数量；并且对微片重新排序，让延迟敏感的微片优先送达目的地。该技术通用性强，可适配各类互联网络，尤其适合缓解GPU组间低带宽链路带来的瓶颈。总的来说，NetCrafter大幅提升多GPU性能，助力GPU集群高效扩展。

## 英文关键词

GPUs, Virtual Memory, Bandwidth, Performance

## 中文关键词

GPU, 虚拟内存, 带宽, 性能

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731040)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
