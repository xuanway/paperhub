---
title: "Occamy: A Preemptive Buffer Management for On-chip Shared-memory Switches"
description: "EuroSys 2025 · Network - Van Oldebarneveldt · Danfeng Shan (Xi'an Jiaotong University), Yunguang Li (Xi'an Jiaotong University"
tags:
  - "EuroSys2025"
  - "Network - Van Oldebarneveldt"
---

# Occamy: A Preemptive Buffer Management for On-chip Shared-memory Switches

**中文标题：** 面向片上共享内存交换机的抢占式缓冲区管理

**所属 Session：** [Session 10.1: Network](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network - Van Oldebarneveldt。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network - Van Oldebarneveldt</p>
</div>

**作者**：Danfeng Shan (Xi'an Jiaotong University), Yunguang Li (Xi'an Jiaotong University), Jinchao Ma (Xi'an Jiaotong University), Zhenxing Zhang (Huawei), Zeyu Liang (Xi'an Jiaotong University), Xinyu Wen (Xi'an Jiaotong University), Hao Li (Xi'an Jiaotong University), Wanchun Jiang (Central South University), Nan Li (Huawei), Fengyuan Ren (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717495)

## 英文摘要

Today’s high-speed switches employ an on-chip shared packet buffer. The buffer is becoming increasingly insufficient as it cannot scale with the growing switching capacity. Nonetheless, the buffer needs to face highly intense bursts and meet stringent performance requirements for datacenter applications. This imposes rigorous demand on the Buffer Management (BM) scheme, which dynamically allocates the buffer across queues. However, the de facto BM scheme, designed over two decades ago, is ill-suited to meet the requirements of today’s network.

In this paper, we argue that shallow-buffer switches, intense bursts, along with dynamic traffic call for a highly agile BM that can quickly adjust the buffer allocation as traffic changes. However, the agility of the current BM is fundamentally limited by its non-preemptive nature. Nonetheless, we find that preemptive BM, considered unrealizable in history, is now feasible on modern switch chips. We propose Occamy1, a preemptive BM that can quickly adjust buffer allocation. Occamy utilizes the redundant memory bandwidth to actively reclaim and reallocate the over-allocated buffer. Testbed experiments and large-scale simulations show that Occamy can improve the end-to-end performance by up to ∼55%.

## 中文摘要

如今的高速交换机采用片上共享分组缓冲区。随着交换容量不断增长，缓冲区无法随之扩展，正变得越来越不足。尽管如此，缓冲区仍需应对高强度的突发流量，并满足数据中心应用的严苛性能要求。这对缓冲区管理（BM）方案提出了严格要求，该方案负责在各队列之间动态分配缓冲区。然而，事实上的 BM 方案设计于二十多年前，已不适应当今网络的需求。

本文认为，浅缓冲区交换机、剧烈突发以及动态流量，要求一种高度敏捷的 BM，能够随流量变化快速调整缓冲区分配。然而，现有 BM 的敏捷性从根本上受限于其非抢占特性。尽管如此，我们发现历史上被认为不可实现的抢占式 BM 在现代交换机芯片上已变得可行。我们提出 Occamy，一种可快速调整缓冲区分配的抢占式 BM。Occamy 利用冗余的内存带宽主动回收并重新分配超额分配的缓冲区。测试床实验和大规模仿真表明，Occamy 可将端到端性能提升最高约 55%。

**英文关键词：** Datacenter Networks, Buffer Management, Traffic Bursts

**中文关键词：** 数据中心网络、缓冲区管理、流量突发

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
