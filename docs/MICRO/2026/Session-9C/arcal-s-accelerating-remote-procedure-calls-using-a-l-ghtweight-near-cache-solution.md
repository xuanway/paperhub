---
title: "Arcalís: Accelerating Remote Procedure Calls Using a Líghtweight Near-Cache Solution"
description: "MICRO 2026 · Session 9C · Arcalís：利用轻量级近缓存方案加速远程过程调用"
tags:
  - "MICRO2026"
  - "Cache"
---

# Arcalís: Accelerating Remote Procedure Calls Using a Líghtweight Near-Cache Solution

**中文标题：** Arcalís：利用轻量级近缓存方案加速远程过程调用

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Johnson Umeike, Pongstorn Maidee, Bahar Asgari

**来源：** MICRO 2026，pp. 3443–3460；[DOI](https://doi.org/10.1109/MICRO67795.2026.00230)

## 英文摘要

Modern microservices increasingly depend on high-performance remote procedure calls (RPCs) to coordinate fine-grained, distributed computation. As network bandwidths continue to scale, the CPU overhead associated with RPC processing, particularly serialization, deserialization, and protocol handling, has become a critical bottleneck. This challenge is exacerbated by fast user-space networking stacks such as DPDK, which expose RPC processing as the dominant performance limiter. While prior hardware accelerators have explored NIC-attached and FPGA-based offloads, these approaches remain farther from the cache hierarchy, so the frequent data accesses during RPC processing each pay an extra interconnect traversal cost that inflates RPC time. Therefore, RPC handling should occur as close as possible to the cache; however, a near-cache solution must be small, hence practical and deployable. Our key insight to enable such a solution is to take advantage of a reconfigurable accelerator that can be configured specifically for the services currently running on the CPUs. We present Arcalis, a near-cache RPC accelerator that positions a lightweight hardware engine adjacent to the last-level cache (LLC). Arcalis offloads RPC processing to dedicated microengines that operate with cache-line latency while preserving programmability. By decoupling RPC processing logic, enabling microservice-specific execution, and positioning itself near the LLC, Arcalis achieves a 1.72-4.91× end-to-end speedup compared to the CPU baseline, significantly reduces microarchitectural overhead by up to 88%, and achieves up to a 1.62× higher throughput than prior solutions. These results highlight the potential of near-cache RPC acceleration as a practical solution for high-performance microservice deployment.

## 中文摘要

现代微服务越来越依赖高性能远程过程调用 (RPC) 来协调细粒度的分布式计算。随着网络带宽不断扩展，与 RPC 处理（特别是序列化、反序列化和协议处理）相关的 CPU 开销已成为关键瓶颈。 DPDK 等快速用户空间网络堆栈加剧了这一挑战，这些堆栈将 RPC 处理暴露为主要的性能限制因素。虽然之前的硬件加速器已经探索了连接 NIC 和基于 FPGA 的卸载，但这些方法仍然远离缓存层次结构，因此 RPC 处理期间的频繁数据访问都会付出额外的互连遍历成本，从而增加 RPC 时间。因此，RPC 处理应该尽可能靠近缓存进行；然而，近缓存解决方案必须很小，因此实用且可部署。我们实现此类解决方案的关键见解是利用可重新配置的加速器，该加速器可以专门针对当前在 CPU 上运行的服务进行配置。我们推出了 Arcalis，这是一种近缓存 RPC 加速器，它将轻量级硬件引擎放置在末级缓存 (LLC) 附近。 Arcalis 将 RPC 处理卸载到专用微引擎，该微引擎在缓存行时延的情况下运行，同时保留可编程性。通过解耦 RPC 处理逻辑、启用特定于微服务的执行并将自身定位在 LLC 附近，与 CPU 基准相比，Arcalis 实现了 1.72-4.91 倍的端到端加速，显着降低了高达 88% 的微架构开销，并实现了比先前解决方案高出 1.62 倍的吞吐量。这些结果凸显了近缓存 RPC 加速作为高性能微服务部署的实用解决方案的潜力。

## 中文关键词

数据中心；硬件加速器；软硬件协同设计；微服务；近缓存处理；远程过程调用

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
