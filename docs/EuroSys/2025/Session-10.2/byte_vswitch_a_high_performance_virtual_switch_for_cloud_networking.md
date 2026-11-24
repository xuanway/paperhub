---
title: "Byte vSwitch: A High-Performance Virtual Switch for Cloud Networking"
description: "EuroSys 2025 · Cloud and Networking - Rotterdam hall 1B · Xin Wang (ByteDance Inc.), Deguo Li (ByteDance Inc.), Zhihong Wang (ByteDance In"
tags:
  - "EuroSys2025"
  - "Cloud and Networking - Rotterdam hall 1B"
---

# Byte vSwitch: A High-Performance Virtual Switch for Cloud Networking

**中文标题：** 面向云网络的高性能虚拟交换机

**所属 Session：** [Session 10.2: Cloud and Networking](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Networking - Rotterdam hall 1B。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Networking - Rotterdam hall 1B</p>
</div>

**作者**：Xin Wang (ByteDance Inc.), Deguo Li (ByteDance Inc.), Zhihong Wang (ByteDance Inc.), Lidong Jiang (ByteDance Inc.), Shubo Wen (ByteDance Inc.), Daxiang Kang (ByteDance Inc.), Engin Arslan (ByteDance Inc.), Peng He (ByteDance Inc.), Xinyu Qian (ByteDance Inc.), Bin Niu (ByteDance Inc.), Jianwen Pi (ByteDance Inc.), Xiaoning Ding (ByteDance Inc.), Ke Lin (ByteDance Inc.), Hao Luo (ByteDance Inc.)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717479)

## 英文摘要

Virtual switch is a fundamental component of cloud computing as it provides core networking functionalities for VMs and containers. Open vSwitch (OVS) is widely adopted in cloud environments due to its open-source nature, programmability, and rich set of features. At ByteDance, we initially adopted OVS in our public cloud, but as our cloud business grew, its generic design along with its complex codebase quickly became obstacles to improvements. Hence, we developed Byte vSwitch (BVS), a high-performance virtual switch that was specifically designed to address the performance, scalability, serviceability, and operational efficiency needs of our cloud services. More specifically, BVS adopts a simple architecture with an optimized hash table to maximize forwarding performance. In addition, we introduced several optimizations to improve BVS scalability, operability, and serviceability in cloud environments. Our evaluations show that BVS achieves up to 3.3× higher PPS and 25% lower latency compared to OVS. BVS has been deployed at scale across all regions of the ByteDance public cloud for over four years, and this paper presents our experience in designing, deploying, and operating BVS in production.

## 中文摘要

虚拟交换机是云计算的基础组件，因为它为虚拟机和容器提供核心网络功能。Open vSwitch（OVS）因其开源特性、可编程性和丰富的功能集而在云环境中被广泛采用。在字节跳动，我们最初在公有云中采用 OVS，但随着云业务增长，其通用设计以及复杂的代码库很快成为改进的障碍。因此，我们开发了 Byte vSwitch（BVS），这是一个高性能虚拟交换机，专门为满足我们云服务在性能、可扩展性、可维护性和运维效率方面的需求而设计。更具体地，BVS 采用简单架构并配合优化的哈希表，以最大化转发性能。此外，我们引入了多项优化，以提升 BVS 在云环境中的可扩展性、可操作性和可维护性。我们的评估表明，与 OVS 相比，BVS 的 PPS 最高提升 3.3 倍，延迟降低 25%。BVS 已在字节跳动公有云所有区域大规模部署超过四年，本文介绍了我们在生产环境中设计、部署和运维 BVS 的经验。

**英文关键词：** Virtual Switch, Cloud Networking

**中文关键词：** 虚拟交换机、云网络

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
