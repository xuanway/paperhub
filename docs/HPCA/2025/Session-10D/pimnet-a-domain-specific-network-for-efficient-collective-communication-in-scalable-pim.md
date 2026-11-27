---
title: "PIMnet: A Domain-Specific Network for Efficient Collective Communication in Scalable PIM"
description: "HPCA 2025 · Colluding to Even the Odds"
tags:
  - "HPCA2025"
  - "Colluding to Even the Odds"
---

# PIMnet: A Domain-Specific Network for Efficient Collective Communication in Scalable PIM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Colluding to Even the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Colluding to Even the Odds</p>
</div>

**论文链接**：
**作者**：Hyojun Son (KAIST), Gilbert Jonatan (KAIST), Wu Xiangyu (KAIST), Haeyoon Cho (KAIST), Kaustubh Shivdikar (Northeastern University), José L. Abellán (Universidad de Murcia), Ajay Joshi (Boston University), David Kaeli (Northeastern University), John Kim (KAIST)
**会议**：HPCA 2025

---

## 中文标题

PIMnet：面向可扩展 PIM 中高效集合通信的领域专用网络

## 英文摘要

Processing-in-memory (PIM), where compute is moved closer to memory or data, has been explored to accelerate emerging workloads. Different PIM-based systems have been announced, each offering a unique microarchitectural organization of their compute units, ranging from fixed functional units to programmable general-purpose compute cores near memory. However, one fundamental limitation of PIM is that each compute unit can only access its local memory; access to “remote” memory must occur through the host CPU – potentially limiting application performance scalability. In this work, we first characterize the scalability of real PIM architectures using the UPMEM PIM system. We analyze how the overhead of communicating through the host (instead of providing direct communication between the PIM compute units) can become a bottleneck for collective communications that are commonly used in many workloads. To overcome this inter-PIM bank communication, we propose PIMnet – a PIM interconnection network for PIM banks that provides direct connectivity between compute units and removes the overhead of communicating through the host. PIMnet exploits bandwidth parallelism where communication across the different PIM bank/chips can occur in parallel to maximize communication performance. PIMnet also matches the DRAM packaging hierarchy with a multi-tier network architecture. Unlike traditional interconnection networks, PIMnet is a PIMcontrolled network where communication is managed by the PIM logic, optimizing collective communications and minimizing the hardware overhead of PIMnet. Our evaluation of PIMnet shows that it provides up to 85× speedup on collective communications and achieves a 11.8× improvement on real applications compared to the baseline PIM.

## 中文摘要

存内处理（PIM）把计算移近内存或数据，已被探索用于加速新兴负载。已有多种基于 PIM 的系统被发布，它们的计算单元在微架构组织上各不相同，从固定功能单元到近内存的可编程通用计算核心。然而，PIM 的一项根本限制是每个计算单元只能访问其本地内存；对“远程”内存的访问必须经由主机 CPU 进行——这可能限制应用性能的可扩展性。在本工作中，我们首先使用 UPMEM PIM 系统刻画真实 PIM 架构的可扩展性。我们分析了经由主机通信（而非在 PIM 计算单元之间提供直接通信）的开销如何成为许多负载中常用集合通信的瓶颈。为克服这种 PIM bank 间通信问题，我们提出 PIMnet——一种面向 PIM bank 的 PIM 互连网络，它在计算单元之间提供直接连接并消除经由主机通信的开销。PIMnet 利用带宽并行性，使跨不同 PIM bank/芯片的通信可以并行进行以最大化通信性能。PIMnet 还以多级网络架构匹配 DRAM 封装层次。与传统互连网络不同，PIMnet 是一种 PIM 控制的网络，通信由 PIM 逻辑管理，从而优化集合通信并最小化 PIMnet 的硬件开销。我们对 PIMnet 的评估表明，与基线 PIM 相比，它在集合通信上提供最高 85 倍的加速比，并在真实应用上取得 11.8 倍的改进。
