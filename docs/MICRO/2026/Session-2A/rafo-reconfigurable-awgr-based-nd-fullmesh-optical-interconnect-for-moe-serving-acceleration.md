---
title: "RAFO: Reconfigurable AWGR-Based nD-Fullmesh Optical Interconnect for MoE Serving Acceleration"
description: "MICRO 2026 · Session 2A · RAFO：面向 MoE 服务加速的可重构 AWGR 多维全互连光互连"
tags:
  - "MICRO2026"
  - "Interconnect"
  - "Reconfigurable Computing"
---

# RAFO: Reconfigurable AWGR-Based nD-Fullmesh Optical Interconnect for MoE Serving Acceleration

**中文标题：** RAFO：面向 MoE 服务加速的可重构 AWGR 多维全互连光互连

**所属 Session：** [Session 2A](index.md) · [MICRO 2026](../index.md)

**作者：** Yuxuan Zhang, Rongquan Ni, Jun Liu, Hanbin Zhang, Guohao Dai

**来源：** MICRO 2026，pp. 449–465；[DOI](https://doi.org/10.1109/MICRO67795.2026.00046)

## 英文摘要

To overcome the expensive All-to-All communication introduced by Mixture of Experts (MoE) on traditional clusters (e.g., DGX), all-optical nD-Fullmesh Supernodes have emerged as a promising direction with the maturation of Co-packaged Optics (CPO), offering both scalability and high bandwidth. However, they still face several pressing challenges: (1) Inflexible bandwidth configuration fails to meet the diverse communication patterns introduced by MoE (e.g., All-Reduce and All-to-All) at once, as well as emerging models, leading to inevitable bandwidth underutilization. (2) Stage-limited All-to-All communication incurs heavy traffic and is confined to the Expert Parallelism (EP) stage while overlooking the Tensor Parallelism (TP) stage, accounting for a large portion of the total communication time, which leads to high latency. (3) Uneven communication across experts leads to hot link pressure, while existing load balancing strategies fail because of the lack of support for redundant expert placement in nD-Fullmesh. In this paper, we propose a Reconfigurable AWGR-Based nD-Fullmesh Optical Interconnect architecture (RAFO), which includes three technologies: (1) We design a novel all-optical bandwidth-reconfigurable network based on dOCS bandwidth reconfiguration components and AWGR redundant networks, achieving a speedup up to 1.52x. (2) Beyond hardware design, we propose SCCL, a Stage-cross Collective Communication Library that moves part of the All-to-All traffic from the EP-stage to the TP-stage, achieving a speedup up to 10.09x. (3) Furthermore, we develop R2-Mapping, an MoE expert mapping strategy for Redundant experts in a Reconfigurable architecture, which supports expert balancing strategies, achieving a speedup up to 1.93x. Finally, we evaluate our design under a practically realizable 3D-Fullmesh configuration — a configuration highly compatible with current optical manufacturing constraints. The results demonstrate that our design achieves: (1) a high-bandwidth scale-up domain encompassing 4,096 nodes; (2) a speedup up to 3.70x in communication latency compared with NVL72; (3) a 2.44x improvement per GBps in cost and 3.38x improvement per GBps power efficiency compared with NVL72.

## 中文摘要

为了克服专家混合 (MoE) 在传统集群（例如 DGX）上引入的昂贵的全对全通信，随着共封装光学 (CPO) 的成熟，全光 nD-Fullmesh 超级节点已成为一个有前途的方向，提供可扩展性和高带宽。然而，他们仍然面临几个紧迫的挑战：（1）不灵活的带宽配置无法同时满足MoE引入的多样化通信模式（例如All-Reduce和All-to-All）以及新兴模型，导致不可避免的带宽利用率不足。 (2)阶段限制的All-to-All通信流量大，且仅限于专家并行(EP)阶段，而忽略张量并行(TP)阶段，占总通信时间的很大一部分，导致高时延。 (3)专家之间的通信不均匀导致热链路压力，而现有的负载均衡策略由于nD-Fullmesh中缺乏对冗余专家放置的支持而失败。在本文中，我们提出了一种基于可重构AWGR的nD-Fullmesh光互连架构（RAFO），其中包括三种技术：（1）我们设计了一种基于dOCS带宽重构组件和AWGR冗余网络的新型全光带宽可重构网络，实现了高达1.52倍的加速。 (2) 除了硬件设计之外，我们提出了 SCCL，一种跨阶段集体通信库，它将部分 All-to-All 流量从 EP 阶段移动到 TP 阶段，实现了高达 10.09 倍的加速。 (3) 此外，我们开发了 R2-Mapping，这是一种针对可重构架构中的冗余专家的 MoE 专家映射策略，它支持专家平衡策略，实现了高达 1.93 倍的加速。最后，我们在实际可实现的 3D 全网格配置下评估我们的设计，该配置与当前光学制造限制高度兼容。结果表明，我们的设计实现了：（1）包含 4,096 个节点的高带宽扩展域； (2) 与NVL72相比，通信时延加速高达3.70倍； (3) 与 NVL72 相比，每 GBps 对应的成本降至原来的 1/2.44，每 GBps 的功率效率提高了 3.38 倍。

## 中文关键词

光互连；阵列波导光栅路由器；可重构网络；混合专家模型服务

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22351147](https://doi.org/10.5281/zenodo.22351147)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2A](index.md) · [MICRO 2026 主页](../index.md)
