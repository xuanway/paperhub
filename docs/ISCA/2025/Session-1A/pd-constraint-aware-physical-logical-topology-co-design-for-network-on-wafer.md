---
title: "PD Constraint-aware Physical/Logical Topology Co-Design for Network on Wafer"
description: "ISCA 2025 · Session 1A · 面向晶圆网络的物理/逻辑拓扑感知协同设计"
tags:
  - "ISCA2025"
  - "Session 1A"
  - "ML Accelerators I"
---

# PD Constraint-aware Physical/Logical Topology Co-Design for Network on Wafer

**中文标题：** 面向晶圆网络的物理/逻辑拓扑感知协同设计

**所属 Session：** [Session 1A](index.md) · [ISCA 2025](../index.md)

**作者：** Qize Yang, Taiquan Wei, Sihan Guan, Chengran Li, Haoran Shang, Jinyi Deng, Huizheng Wang, Chao Li, Lei Wang, Yan Zhang, Shouyi Yin, Yang Hu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731045) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

As cluster scales for LLM training expand, waferscale chips, characterized by the high integration density and bandwidth, emerge as a promising approach to enhancing training performance. The role of Network on Wafer (NoW) is becoming increasingly significant, which puts an emphasis on two facts: physical and logical topology. However, existing networks fail to co-design both aspects. Additionally, physical topology typically focuses on optimizing communication or computation separately, neglecting opportunities to improve overall training performance.

In this paper, we propose a physical design (PD) constraint-aware joint optimization strategy, developing mesh-switch physical topology and a dual-granularity logical topology. Mesh-switch leverages the high integration density of mesh and the efficient communication performance of fat tree, optimizing the allocation of on-chip communication and computation resources thoroughly considering the physical constraints of waferscale chips. Furthermore, we conduct a DSE algorithm to search for the optimal mesh-switch configuration. Based on the proposed physical topology, we design the most appropriate logical topology, and further enhance bandwidth utilization through a fine-grained overlap strategy. Evaluation results demonstrate that our NoW design achieves nearly a 2.39× performance improvement in LLM training compared to existing networks. Our comprehensive design approach, which integrates physical and logical topologies with constraint considerations, can also be applied to network designs in other contexts.

## 中文摘要

随着大语言模型（LLM）训练集群规模不断扩大，具备高集成密度与高带宽特性的晶圆级芯片，成为提升训练性能的一条极具潜力的技术路线。晶圆级片上网络（NoW）的重要性日益凸显，而该网络设计需要同时兼顾物理拓扑与逻辑拓扑两大要素。但现有网络方案无法对二者进行协同设计；并且物理拓扑的优化通常仅单独针对通信或计算进行调优，忽略了提升整体训练性能的优化空间。

本文提出一种感知物理设计（PD）约束的联合优化方案，构建了Mesh-Switch物理拓扑与双粒度逻辑拓扑。Mesh-Switch同时发挥Mesh结构高集成密度与胖树（Fat Tree）通信高效的优势，在充分考虑晶圆级芯片物理约束的前提下，对片上通信与计算资源分配进行全局优化。此外，我们采用设计空间探索（DSE）算法搜索最优的Mesh-Switch配置。在该物理拓扑基础上，我们匹配设计最优的逻辑拓扑，并借助细粒度的计算通信重叠策略进一步提升带宽利用率。实验结果表明：相较于现有网络，本文提出的NoW设计在大语言模型训练任务上实现了约2.39倍的性能提升。这套融合物理拓扑、逻辑拓扑并纳入约束感知的一体化设计思路，同样可迁移至其他场景的网络架构设计中。

## 英文关键词

Network on Wafer, Physical Topology, Logical Topology, Wafer-Scale Chips, LLM Training

## 中文关键词

晶圆级网络, 物理拓扑, 逻辑拓扑, 晶圆级芯片, 大语言模型训练

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731045)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2025](../index.md)
