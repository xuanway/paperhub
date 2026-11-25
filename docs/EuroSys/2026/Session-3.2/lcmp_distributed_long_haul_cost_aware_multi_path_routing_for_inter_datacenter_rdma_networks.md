---
title: "LCMP: Distributed Long-Haul Cost-Aware Multi-Path Routing for Inter-Datacenter RDMA Networks"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Dong-Yang Yu (Beijing University of Posts and Telecommunications), Yuchao Zhang "
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# LCMP: Distributed Long-Haul Cost-Aware Multi-Path Routing for Inter-Datacenter RDMA Networks

**中文标题：** LCMP：面向跨数据中心 RDMA 网络的分布式长距离代价感知多路径路由

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Dong-Yang Yu (Beijing University of Posts and Telecommunications), Yuchao Zhang (Beijing University of Posts and Telecommunications), Xiaodi Wang (Beijing University of Posts and Telecommunications), Jun Wang (Beijing University of Posts and Telecommunications), Wenfei Wu (Peking University), Haipeng Yao (Beijing University of Posts and Telecommunications), Wendong Wang (Beijing University of Posts and Telecommunications), Ke Xu (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803593)

## 英文摘要

RDMA-empowered cloud services are gradually deployed across datacenters (DCs) with multiple paths, which exhibit new properties of path asymmetry, delayed congestion signals, and simultaneous flow routing collisions, and further fail existing routing methods.

We present LCMP, a distributed long-haul cost-aware multi-path routing framework that aims to place RDMA flows on multiple inter-DC paths, achieving low-cost, low-latency, and congestion-responsive transmission. LCMP combines a control-plane path-quality score with compact on-switch congestion signals, where the former unifies quality assessment for asymmetric paths and the latter enables responsive reaction to path congestion. LCMP further resolves the simultaneous flow decision collision problem by filtering high-cost candidates, and performing a diversity-preserving hash inside the reduced set. On an 8-DC testbed, LCMP reduces median and tail FCT slowdown by up to 76% and 64%, respectively compared to state-of-the-art (SOTA) baselines. And large-scale NS-3 simulations under the 2000 km inter-DC scenario confirm similar improvements.

## 中文摘要

基于 RDMA 的云服务正逐步以多路径方式跨数据中心（DC）部署，由此呈现出路径不对称、拥塞信号延迟以及并发流路由冲突等新特性，使得现有路由方法失效。

我们提出 LCMP，一个分布式长距离代价感知多路径路由框架，旨在将 RDMA 流放置到多条跨 DC 路径上，实现低成本、低延迟且能响应拥塞的传输。LCMP 将控制平面的路径质量评分与交换机上紧凑的拥塞信号相结合：前者统一了非对称路径的质量评估，后者使系统能够对路径拥塞做出及时响应。LCMP 进一步通过过滤高代价候选路径，并在缩减后的集合中执行保持多样性的哈希，解决了并发流决策冲突问题。在 8 个 DC 的测试床上，与最先进（SOTA）基线相比，LCMP 将流完成时间（FCT）中位数和尾部的劣化分别降低最多 76% 和 64%。在 2000 公里跨 DC 场景下的大规模 NS-3 仿真也印证了类似的改进。

**英文关键词：** Data center networks, RDMA, Routing, Long haul, Multi-path routing

**中文关键词：** 数据中心网络、RDMA、路由、长距离传输、多路径路由

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
