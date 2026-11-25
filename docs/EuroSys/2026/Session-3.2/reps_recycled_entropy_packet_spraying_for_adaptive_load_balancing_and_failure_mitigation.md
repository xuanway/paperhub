---
title: "REPS: Recycled Entropy Packet Spraying for Adaptive Load Balancing and Failure Mitigation"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Tommaso Bonato (ETH Zürich / Microsoft), Abdul Kabbani (Microsoft), Ahmad Ghalay"
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# REPS: Recycled Entropy Packet Spraying for Adaptive Load Balancing and Failure Mitigation

**中文标题：** REPS：面向自适应负载均衡与故障缓解的回收熵数据包喷洒

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Tommaso Bonato (ETH Zürich / Microsoft), Abdul Kabbani (Microsoft), Ahmad Ghalayini (Microsoft), Michael Papamichael (Microsoft), Mohammad Dohadwala (Microsoft), Lukas Gianinazzi (ETH Zürich), Mikhail Khalilov (ETH Zürich), Elias Achermann (ETH Zürich), Daniele De Sensi (Sapienza University of Rome), Torsten Hoefler (ETH Zürich / Microsoft)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769320)

## 英文摘要

Next-generation datacenters require highly efficient network load balancing to manage the growing scale of artificial intelligence (AI) training and general datacenter traffic. However, existing Ethernet-based solutions, such as Equal Cost MultiPath (ECMP) and oblivious packet spraying (OPS), struggle to maintain high network utilization due to both increasing traffic demands and the expanding scale of datacenter topologies, which also exacerbate network failures. To address these limitations, we propose REPS, a lightweight decentralized per-packet adaptive load balancing algorithm designed to optimize network utilization while ensuring rapid recovery from link failures. REPS adapts to network conditions by caching good-performing paths. In case of a network failure, REPS re-routes traffic away from it in less than 100 microseconds. REPS is designed to be deployed with next-generation out-of-order transports, such as Ultra Ethernet, and uses less than 25 bytes of per-connection state regardless of the topology size. We extensively evaluate REPS in large-scale simulations and FPGA-based NICs.

## 中文摘要

下一代数据中心需要高效的网络负载均衡，以应对不断增长的人工智能（AI）训练流量和通用数据中心流量规模。然而，现有基于以太网的方案，如等价多路径（ECMP）和不感知状态的包喷洒（OPS），由于流量需求增长和数据中心拓扑规模扩大而难以维持高网络利用率，而这种规模扩张还加剧了网络故障。为解决这些局限，我们提出REPS，一种轻量级去中心化的逐包自适应负载均衡算法，旨在优化网络利用率，同时确保从链路故障中快速恢复。REPS通过缓存性能良好的路径来适应网络状况。在网络发生故障时，REPS可在不到100微秒内将流量重新路由离开该故障。REPS被设计为与Ultra Ethernet等下一代乱序传输配合部署，且无论拓扑规模如何，每条连接的状态均少于25字节。我们在大规模仿真和基于FPGA的网卡上对REPS进行了广泛评估。

**英文关键词：** load balancing; packet spraying; out-of-order transport; RDMA; Ultra Ethernet

**中文关键词：** 负载均衡、包喷洒、乱序传输、RDMA、Ultra Ethernet

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
