---
title: "Heterogeneity-Aware Cross-Layer Mapping Optimization for Sparse LLMs on Layered Supernodes"
description: "MICRO 2026 · Session 9C · 面向分层超级节点上稀疏 LLM 的异构感知跨层映射优化"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# Heterogeneity-Aware Cross-Layer Mapping Optimization for Sparse LLMs on Layered Supernodes

**中文标题：** 面向分层超级节点上稀疏 LLM 的异构感知跨层映射优化

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Hanbin Zhang, Jun Liu, Rongquan Ni, Yuxuan Zhang, Guohao Dai

**来源：** MICRO 2026，pp. 3361–3377；[DOI](https://doi.org/10.1109/MICRO67795.2026.00225)

## 英文摘要

While sparse Large Language Models (LLMs) reduce compute and storage footprint, they also introduce memory access inefficiencies and communication bottlenecks. Layered supernodes offer the potential to address these limits by integrating high-bandwidth switch networks and wafer-scale chips. However, existing LLM mapping frameworks overlook cross-layer architectural heterogeneity, including the spatial memory-access disparity across nested dual-tier on-wafer meshes, and the communication traffic asymmetry between external switch networks and internal meshes. This results in three challenges. (1) Memory misplacement and pipeline stalls under single-tier mesh abstraction. Flattening the distributed HBM-SRAM hierarchy misplaces data reuse across memory levels, while inner cores stall on multi-hop accesses. Fragmented sparse-attention KV cache accesses amplify both inefficiencies, incurring over 5.02× latency overhead. (2) Multi-hop latency and inter-wafer bottlenecks due to symmetric-to-asymmetric topology mismatches. Existing mapping strategies neglect non-uniform intra-wafer connectivity and intrainter-wafer bandwidth disparity, increasing routing hops and congesting inter-wafer links. (3) Imbalanced bandwidth utilization due to traffic-oblivious bandwidth provisioning. Uniform wafer-edge bandwidth allocation ignores the mesh's spatial asymmetry, congesting center-edge ports while idling corner ports, inflating MoE all-to-all latency by 1.47×. In this paper, we propose HACMO, a holistic analysis and mapping framework that models inference behavior on the three-layer supernode abstraction (rack, wafer, and core). Based on this framework, we propose three cross-layer techniques for sparse LLM inference to address the aforementioned challenges respectively. (1) For the sparse attention module, we propose spatially-aware dual-tier mapping and scheduling, which non-uniformly maps workloads based on spatial access costs, while enabling inter-layer pipelining to hide remote access latencies. (2) For the MoE module, we propose global cost-aware expert mapping that jointly models inter-NPU communication, link congestion, and load imbalance, deriving optimal expert placements while leveraging cold links for dynamic rebalancing. (3) For network architecture design, we propose a traffic-aware decoupled edge interconnect that dynamically matches external bandwidth with the heterogeneous routing demands of the internal mesh using lightweight crossbars at the wafer boundaries. Evaluations demonstrate that HACMO reduces sparse attention and MoE latencies by up to 63.5% and 49.3%, respectively, delivering up to an 8.90× throughput improvement over SOTA baselines on GPUs and 2.03x over their direct deployments on layered supernodes.

## 中文摘要

虽然稀疏大语言模型 (LLM) 减少了计算和存储占用空间，但它们也带来了内存访问效率低下和通信瓶颈。分层超级节点通过集成高带宽交换网络和晶圆级芯片提供了解决这些限制的潜力。然而，现有的 LLM 映射框架忽视了跨层架构异构性，包括嵌套双层晶圆上网格之间的空间内存访问差异，以及外部交换机网络和内部网格之间的通信流量不对称。这导致了三个挑战。 (1) 单层网格抽象下的内存错位和管道停顿。扁平化分布式 HBM-SRAM 层次结构会导致跨内存级别的数据重用错位，同时内核会在多跳访问上停滞。碎片化的稀疏注意力 KV 缓存访问放大了这两种低效率，导致超过 5.02 倍的时延开销。 (2) 由于对称与非对称拓扑不匹配导致的多跳时延和晶圆间瓶颈。现有的映射策略忽略了不均匀的晶圆内连接和晶圆内带宽差异，从而增加了路由跳数并导致晶圆间链路拥塞。 (3) 由于流量无关的带宽配置导致带宽利用率不平衡。统一的晶圆边缘带宽分配忽略了网格的空间不对称性，导致中心边缘端口拥塞，而角落端口闲置，从而使 MoE 的所有时延增加了 1.47 倍。在本文中，我们提出了 HACMO，一种整体分析和映射框架，用于对三层超级节点抽象（机架、晶圆和核心）上的推理行为进行建模。基于这个框架，我们提出了三种稀疏LLM推理的跨层技术来分别解决上述挑战。 （1）对于稀疏注意力模块，我们提出了空间感知的双层映射和调度，它根据空间访问成本非均匀地映射工作负载，同时启用层间管道来隐藏远程访问时延。 (2) 对于 MoE 模块，我们提出了全局成本感知专家映射，对 NPU 间通信、链路拥塞和负载不平衡进行联合建模，导出最佳专家放置，同时利用冷链接进行动态重新平衡。 (3) 对于网络架构设计，我们提出了一种流量感知的解耦边缘互连，该互连在晶圆边界使用轻量级交叉开关动态地将外部带宽与内部网格的异构路由需求相匹配。评估表明，HACMO 将稀疏注意力和 MoE 时延分别降低了 63.5% 和 49.3%，与 GPU 上的 SOTA 基线相比，吞吐量提高了 8.90 倍，与直接部署在分层超级节点上相比，吞吐量提高了 2.03 倍。

## 中文关键词

超级节点；稀疏大语言模型；拓扑感知映射；异构计算；跨层优化

## 代码与研究制品

- 代码仓库：[https://github.com/hz0124/HACMO](https://github.com/hz0124/HACMO)
- 研究制品归档：[https://doi.org/10.5281/zenodo.22658850](https://doi.org/10.5281/zenodo.22658850)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
