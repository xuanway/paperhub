---
title: "BoostX™-RNIC: Fast, Scalable and Flexible AI RNIC"
description: "MICRO 2026 · Session 1C · BoostX™-RNIC：快速、可扩展且灵活的 AI RDMA 网卡"
tags:
  - "MICRO2026"
---

# BoostX™-RNIC: Fast, Scalable and Flexible AI RNIC

**中文标题：** BoostX™-RNIC：快速、可扩展且灵活的 AI RDMA 网卡

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Kanghyun Choi, Bogyeong Park, Gihwan Lee, Hanmin Kim, Nayeon Kim, Chanmyeong Kim, Hyeonseong Choi, Dongjoo Lee, Jaehyun Lee, Eunjin Baek, Changsu Kim, Changyeon Jo, Minho Chu, Jangwoo Kim

**来源：** MICRO 2026，pp. 283–299；[DOI](https://doi.org/10.1109/MICRO67795.2026.00035)

## 英文摘要

AI workloads are growing at an unprecedented rate, making RDMA-based scale-out architectures the standard approach. They now demand more than raw network performance from an RNIC. It must sustain high performance at scale and provide flexibility to offload data-centric processing tasks at line-rate. However, no existing RNIC solution meets all of these demands simultaneously. In this paper, we present BoostX-RNIC, an industry-developed, FPGA-based AI RNIC that achieves high network scalability and flexibility to support diverse data-centric processing tasks, while maintaining line-rate performance. Based on the novel line-rate RoCEv2 engine, BoostX-RNIC designs a multi-path RDMA transport and a programmable congestion control framework to effectively resolve network congestion for network scalability. Moreover, BoostX-RNIC offers a configurable block that provides flexibility to offload diverse data-centric processing tasks without compromising performance. Crucially, BoostX-RNIC delivers all of these capabilities while ensuring system deployability: it fits a low-profile form factor, and its endpoint-oriented design provides software compatibility and interoperability. BoostX-RNIC provides up to 1.73× speedup in collective communication, up to 28.5% higher tokens-per-second, and up to 11.6% lower energy-per-token in end-to-end AI workloads on a multi-level switch network and 1.83× faster secure RDMA performance compared to existing RNIC solutions.

## 中文摘要

AI 工作负载正在以前所未有的速度增长，使得基于 RDMA 的横向扩展架构成为标准方法。他们现在对 RNIC 的要求不仅仅是原始网络性能。它必须大规模维持高性能，并提供以线速卸载以数据为中心的处理任务的灵活性。然而，现有的 RNIC 解决方案还没有同时满足所有这些需求。在本文中，我们介绍了 BoostX-RNIC，这是一种业界开发的、基于 FPGA 的 AI RNIC，它实现了高网络可扩展性和灵活性，以支持各种以数据为中心的处理任务，同时保持线速性能。基于新颖的线速RoCEv2引擎，BoostX-RNIC设计了多路径RDMA传输和可编程拥塞控制框架，以有效解决网络拥塞，实现网络可扩展性。此外，BoostX-RNIC 提供了一个可配置块，可以灵活地卸载各种以数据为中心的处理任务，而不会影响性能。至关重要的是，BoostX-RNIC 提供所有这些功能，同时确保系统可部署性：它适合低调的外形尺寸，其面向端点的设计提供软件兼容性和互操作性。与现有 RNIC 解决方案相比，BoostX-RNIC 在集体通信中提供高达 1.73 倍的加速，每秒词元数提高高达 28.5%，在多级交换网络上的端到端 AI 工作负载中每个词元的能耗​​降低高达 11.6%，并且安全 RDMA 性能比现有 RNIC 解决方案快 1.83 倍。

## 中文关键词

远程直接内存访问；RoCEv2；RDMA 网卡；现场可编程门阵列；网络可扩展性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
