---
title: "BoostX™-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration"
description: "ISCA 2026 · Session 5B · BoostX™-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration"
tags:
  - "ISCA2026"
  - "Session 5B"
  - "Industry Track 2"
---

# BoostX™-NTI: Fast, Scalable and Flexible Storage Architecture with NVMe/TCP Initiator Acceleration

**中文标题：** BoostX™-NTI: 面向 NVMe/TCP 发起端加速的快速、可扩展且灵活的存储架构

**所属 Session：** [Session 5B](index.md) · [ISCA 2026](../index.md)

**作者：** Hamin Jang, Jinha Jeong, Wonseok Lee, Jun Heo, Jongcheon Lee, Hyunjae Chu, Taehyun Kim, Youngwoo Jeong, Dongu Kim, Heetaek Jeong, Changsu Kim, Dongup Kwon, Jangwoo Kim

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Storage disaggregation has become a key architectural trend in modern datacenters, improving utilization and flexibility by decoupling compute and storage. Among transport options, NVMe/TCP has gained significant traction for its compatibility with commodity Ethernet infrastructure. However, as performance demands rise, sustaining line-rate throughput places excessive overhead on host CPUs. On-device sidecore-based approaches have been proposed to mitigate this burden, but their limited compute capability and memory bandwidth severely restrict scalability, resulting in constrained performance. In this paper, we present MangoBoost BoostX-NTI (NTI), a fast and scalable NVMe/TCP DPU solution with FPGA-based hardware acceleration that satisfies three design goals: host CPU efficiency, line-rate performance, and practical deployability. First, NTI eliminates host CPU overhead by offloading the entire storage disaggregation stack onto a DPU card. Second, it achieves line-rate performance by executing the full I/O path directly in hardware, removing sidecore involvement and avoiding off-chip memory traversal. Finally, NTI ensures practical deployability in real-world datacenters by meeting tight form-factor and power constraints, adhering to protocol standards for interoperability, and enabling dynamic fallback and recovery between hardware and software for operational resilience. Our evaluation shows that NTI achieves up to 9.17× higher throughput than sidecore-based baselines and 16.7× higher core efficiency than software baselines, while consistently outperforming them across AI, cloud, and database workloads.

## 中文摘要

存储解耦（storage disaggregation）已成为现代数据中心的关键架构趋势，它通过将计算与存储分离来提升利用率与灵活性。在各类传输方案中，NVMe/TCP 因其与通用以太网基础设施的兼容性而受到广泛关注。然而，随着性能需求上升，维持线速吞吐会给主机 CPU 带来过高开销。已有研究提出基于设备侧 sidecore 的方案来缓解这一负担，但其有限的计算能力和内存带宽严重限制了可扩展性，导致性能受限。本文提出 MangoBoost BoostX-NTI（NTI），一种基于 FPGA 硬件加速的快速、可扩展 NVMe/TCP DPU 方案，满足三项设计目标：主机 CPU 效率、线速性能以及实际可部署性。首先，NTI 将整个存储解耦软件栈卸载到 DPU 卡上，从而消除主机 CPU 开销。其次，它通过直接在硬件中执行完整的 I/O 路径，消除 sidecore 参与并避免片外内存访问，从而实现线速性能。最后，NTI 通过满足严苛的板型与功耗约束、遵循协议标准以保证互操作性，并支持硬件与软件之间的动态回退与恢复以保障运行韧性，从而确保在真实数据中心中的实际可部署性。我们的评估显示，NTI 相比基于 sidecore 的基线吞吐最高提升 9.17×，相比软件基线核效率提升 16.7×，并在 AI、云和数据库负载上始终优于这些基线。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2026](../index.md)
