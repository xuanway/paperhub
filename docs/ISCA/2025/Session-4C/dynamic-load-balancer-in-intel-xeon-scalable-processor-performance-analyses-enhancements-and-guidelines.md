---
title: "Dynamic Load Balancer in Intel Xeon Scalable Processor: Performance Analyses, Enhancements, and Guidelines"
description: "ISCA 2025 · Session 4C · 英特尔至强可扩展处理器中的动态负载均衡器：性能分析、增强与指南"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# Dynamic Load Balancer in Intel Xeon Scalable Processor: Performance Analyses, Enhancements, and Guidelines

**中文标题：** 英特尔至强可扩展处理器中的动态负载均衡器：性能分析、增强与指南

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Jiaqi Lou, Srikar Vanavasam, Yifan Yuan, Ren Wang, Nam Sung Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731026) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rapid increase in inter-host networking speed has challenged host processing capabilities, as bursty traffic and uneven load dis- tribution among host CPU cores give rise to excessive queuing delays and service latency variances. To cost-efficiently tackle this challenge, the latest Intel Xeon Scalable Processor has integrated an on-chip accelerator, named Dynamic Load Balancer (DLB). It consists of hardware queues, arbiters, and priority-based Quality of Service (QoS) features to maximize load-balancing performance while minimizing host CPU cycle consumption. In this work, we first compare the performance of DLB against popular software- based load balancers with a microbenchmark suite, demonstrating that DLB significantly outperforms them. Yet, DLB still consumes a significant number of host CPU cycles to prepare and enqueue work descriptors for received packets. Second, to eliminate the consumption of host CPU cycles in load balancing, we propose a system architecture/software co-design solution, AccDirect. Specif- ically, AccDirect leverages the Peer-to-Peer (P2P) communication capability of PCIe devices to enable a direct communication path between DLB and NIC, through which NIC directly enqueues the work descriptors. Our evaluation shows that AccDirect-based DLB offers practically the same performance as conventional DLB while reducing the system-wide power consumption of host CPU by 10%. Compared to the throughput of a commodity hardware-based load balancer for an end-to-end application, that of AccDirect-based DLB is 14–50% higher with comparable p99 latency. Lastly, we provide guidelines to make the best use of DLB, which is riddled with a vast configuration space and advanced features, after conducting a comprehensive evaluation.

## 中文摘要

主机间网络速度的快速提升对主机处理能力提出了挑战，突发流量和主机CPU核心之间的负载分配不均匀导致过多的排队延迟和服务延迟差异。为了经济高效地应对这一挑战，最新的英特尔至强可扩展处理器集成了一个名为动态负载均衡器 (DLB) 的片上加速器。它由硬件队列、仲裁器和基于优先级的服务质量 (QoS) 功能组成，可最大限度地提高负载平衡性能，同时最大限度地减少主机 CPU 周期消耗。在这项工作中，我们首先使用微基准套件将 DLB 与流行的基于软件的负载均衡器的性能进行比较，证明 DLB 显著优于它们。然而，DLB 仍然消耗大量主机 CPU 周期来为接收到的数据包准备和排队工作描述符。 其次，为了消除负载平衡中主机CPU周期的消耗，我们提出了系统架构/软件协同设计解决方案AccDirect。具体来说，AccDirect利用PCIe设备的点对点（P2P）通信能力来实现DLB和NIC之间的直接通信路径，NIC通过该路径直接将工作描述符入队。我们的评估表明，基于 AccDirect 的 DLB 提供与传统 DLB 几乎相同的性能，同时将主机 CPU 的系统功耗降低了 10%。与用于端到端应用程序的基于商品硬件的负载均衡器的吞吐量相比，基于 AccDirect 的 DLB 的吞吐量高出 14-50%，且 p99 延迟相当。 最后，我们在进行全面评估后，提供了如何充分利用DLB的指南，DLB拥有广阔的配置空间和先进的功能。

## 英文关键词

Dynamic Load Balancer (DLB), On-chip Accelerator, Accelerator Chaining, P2P Communication

## 中文关键词

动态负载均衡器 (DLB), 片上加速器, 加速器链接, P2P 通信

## 代码与研究制品

- [代码仓库](https://github.com/ece-fast-lab/ISCA-2025-DLB)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731026)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
