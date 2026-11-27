---
title: "Sassy: SmartNIC-Assisted Notification Delivery for μs-scale RDMA Workloads"
description: "HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing"
tags:
  - "HPCA2026"
  - "FPGA, SmartNIC, and Reconfigurable Computing"
---

# Sassy: SmartNIC-Assisted Notification Delivery for μs-scale RDMA Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: FPGA, SmartNIC, and Reconfigurable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing</p>
</div>

**论文链接**：
**作者**：Hamed Seyedroudbari Georgia Tech , Alexandros Daglis Georgia Tech
**会议**：HPCA 2026

---

## 中文标题

Sassy：面向 μs 级 RDMA 负载的 SmartNIC 辅助通知投递

## 英文摘要

RDMA is the preferred ultra-low-latency transport in modern datacenters. As services decompose into latency-critical microservices, servers maintain hundreds to thousands of connections across tiers. However, RDMA’s polling-based RPC notification struggles at high core and connection counts, forcing a tradeoff between idle polling, inter-core synchronization costs, and load imbalance—each limiting throughput for μs-scale services. We introduce Sassy, a smartNIC-based notification mechanism that breaks this tradeoff, optimizing the performance and scalability of servicing μs-scale RPCs over high connection counts. Sassy eliminates performance overheads stemming from idle polling and inter-core synchronization, while balancing the load of active RDMA connections across available cores. We implement Sassy on an FPGA-enhanced NIC and evaluate it on a range of traffic patterns, as well as a high-performance key-value store. For deployment scenarios with high connection counts, Sassy improves throughput under SLO by up to 2.3×.

## 中文摘要

RDMA 是现代数据中心首选的超低时延传输方式。随着服务拆分为时延敏感的微服务，服务器在各层次间需维持数百到数千条连接。然而 RDMA 基于轮询的 RPC 通知在高核心数与高连接数下举步维艰，不得不在空闲轮询、核间同步开销与负载不均衡之间权衡，而这三者都会限制 μs 级服务的吞吐。本文提出 Sassy，一种基于 SmartNIC 的通知机制，打破上述权衡，优化在高连接数下服务 μs 级 RPC 的性能与可扩展性。Sassy 消除了空闲轮询与核间同步带来的性能开销，同时在可用核心间均衡活跃 RDMA 连接的负载。我们在 FPGA 增强的网卡上实现 Sassy，并在多种流量模式以及一个高性能键值存储上进行评估。在高连接数的部署场景下，Sassy 将满足 SLO 的吞吐提升最高 2.3 倍。
