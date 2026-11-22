---
title: "SERenaDE: Hardware Acceleration of Serialization Frameworks"
description: "MICRO 2026 · Session 9C · SERenaDE：序列化框架的硬件加速"
tags:
  - "MICRO2026"
---

# SERenaDE: Hardware Acceleration of Serialization Frameworks

**中文标题：** SERenaDE：序列化框架的硬件加速

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Christos Zarkos, Qihang Chen, Nikita Lazarev, Shabnam Sheikhha, James Tsai, Andy Anderson, Bhushan Chitlur, Christina Delimitrou

**来源：** MICRO 2026，pp. 3412–3428；[DOI](https://doi.org/10.1109/MICRO67795.2026.00228)

## 英文摘要

Serialization frameworks are a fundamental part of datacenters, as they enable language- and platform-neutral communication and storage. However, software serialization faces major performance bottlenecks, accounting for a significant fraction of cloud cycles. Prior work has proposed specialized hardware accelerators to address serialization overheads. While they achieve considerable speedups, they are expensive in terms of verification, fabrication, and deployment, and often hardcode too many details about the (de) serialization framework in hardware. We propose SERenaDE, a serialization framework designed to integrate commodity and readily-available accelerators currently deployed in datacenters in order to accelerate and offload serialization to hardware. Specifically, we utilize the Intel In-Memory Analytics Accelerator (IAA), an accelerator engine offering fast compression, to enable fast and transparent serialization and deserialization to the user, significantly simplifying the software encoding step. We evaluate our system on production-class server machines, both with synthetic microbenchmarks, open-source representative fleet-wide benchmarks, and a representative microservice application. Our results show higher end-to-end performance across a broad range of evaluated messages, while significantly improving throughput and achieving high compression ratios alongside substantial speedups for larger messages. Under both 50th and 95th latency percentile latency constraints, SERenaDE improves serialization and deserialization throughput, by up to 24% and 260% respectively, while reducing serialized message size by up to 8.4x.

## 中文摘要

序列化框架是数据中心的基本组成部分，因为它们支持语言和平台中立的通信和存储。然而，软件序列化面临着主要的性能瓶颈，占云周期的很大一部分。先前的工作提出了专门的硬件加速器来解决序列化开销。虽然它们实现了相当大的加速，但在验证、制造和部署方面成本高昂，并且通常在硬件中硬编码了有关（反）序列化框架的太多细节。我们提出了 SERenaDE，这是一种序列化框架，旨在集成当前部署在数据中心中的商品和现成的加速器，以加速序列化并将其卸载到硬件。具体来说，我们利用英特尔内存分析加速器 (IAA)（一种提供快速压缩的加速器引擎）为用户提供快速、透明的序列化和反序列化，从而显着简化软件编码步骤。我们在生产级服务器机器上评估我们的系统，包括综合微基准、开源代表性的车队范围基准和代表性的微服务应用程序。我们的结果显示，在广泛的评估消息中具有更高的端到端性能，同时显着提高了吞吐量并实现了高压缩比，同时大幅提高了较大消息的速度。在第 50 个和第 95 个时延百分位数时延限制下，SERenaDE 将序列化和反序列化吞吐量分别提高了 24% 和 260%，同时将序列化消息大小减少了 8.4 倍。

## 中文关键词

序列化；硬件加速；硬件卸载；压缩；数据中心系统

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/czarkos/serenade_artifact_evaluation](https://github.com/czarkos/serenade_artifact_evaluation)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21551554](https://doi.org/10.5281/zenodo.21551554)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
