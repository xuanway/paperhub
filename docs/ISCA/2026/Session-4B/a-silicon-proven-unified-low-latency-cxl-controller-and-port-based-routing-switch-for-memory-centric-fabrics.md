---
title: "A Silicon-Proven Unified Low-Latency CXL Controller and Port-Based Routing Switch for Memory-Centric Fabrics"
description: "ISCA 2026 · Session 4B · A Silicon-Proven Unified Low-Latency CXL Controller and Port-Based Routing Switch for Memory-Centric Fabrics"
tags:
  - "ISCA2026"
  - "Session 4B"
  - "Industry Track 1"
---

# A Silicon-Proven Unified Low-Latency CXL Controller and Port-Based Routing Switch for Memory-Centric Fabrics

**中文标题：** 经硅验证的统一低延迟 CXL 控制器与面向以内存为中心互连结构的基于端口的路由交换器

**所属 Session：** [Session 4B](index.md) · [ISCA 2026](../index.md)

**作者：** Miryeong Kwon, Seungjun Lee, Donghyun Gouk, Hongjoo Jung, Eojin Ryu, Seyeong Huh, Junseok Moon, Hyein Woo, Junhee Kim, Kyungkuk Nam, Jinwoo Baek, Hyunkyu Choi, Woojin Choi, Yongjin Cho, Myoungsoo Jung

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Compute Express Link (CXL) enables composable and memory-centric fabrics, but existing controllers inherit PCIe-derived hierarchy, boundary buffering, and deep pipelines, which constrain scalability and increase latency. This work presents a unified low-latency CXL controller and a port-based routing (PBR) switch. The controller integrates the physical, link, and transaction layers into a single pipeline operating under a unified timing reference, removing high-overhead layer-level synchronization.

A hardware-driven conversion and routing path is integrated into each port of the switch. All steps, including HBR to PBR translation, header reconstruction, routing lookup, and arbitration, are issued through fixed-cycle hardware pipelines without firmware involvement. An internal non-blocking on-chip network supports parallel forwarding and maintains constant per-hop delay regardless of port count or topology depth.

A silicon prototype fabricated in a 4 nm process achieves roughly 2.1× latency reduction and preserves deterministic behavior under congestion and multi-hop operation. System-level evaluation with database and microservice workloads shows up to 2× higher throughput than HBR-based designs. These results indicate that a unified controller and hardware-automated PBR switch provide a deterministic and scalable CXL fabric for multi-host memory pooling and sharing.

## 中文摘要

Compute Express Link (CXL) 支持可组合的以内存为中心的互连结构，但现有控制器继承自 PCIe 的层次结构、边界缓冲和深层流水线限制了可扩展性并增加了延迟。本文提出统一的低延迟 CXL 控制器和基于端口的路由（PBR）交换器，将物理层、链路层和事务层集成到单一流水线中，消除了高开销的层间同步。交换器各端口集成硬件驱动的转换和路由路径，通过固定周期的硬件流水线完成全部步骤。采用 4 nm 工艺制造的硅原型实现约 2.1× 的延迟降低，在拥塞和多跳操作下保持确定性行为。系统级评估显示，相比基于 HBR 的设计，吞吐量提升最高 2×。

## 代码与研究制品

截至 2026-11-23，未在论文及公开检索中找到本论文对应的开源程序链接。已检查 [Panmnesia 官方论文介绍](https://panmnesia.com/news/en/2026-06-24-panmnesia-isca2026-eng/)。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2026](../index.md)
