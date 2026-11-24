---
title: "Mapping and Communication Optimizations with Fault Tolerance for Wafer-Scale LLM Inference"
description: "ISCA 2026 · Session 5A · Mapping and Communication Optimizations with Fault Tolerance for Wafer-Scale LLM Inference"
tags:
  - "ISCA2026"
  - "Session 5A"
  - "LLM 3"
---

# Mapping and Communication Optimizations with Fault Tolerance for Wafer-Scale LLM Inference

**中文标题：** 面向晶圆级 LLM 推理的容错映射与通信优化

**所属 Session：** [Session 5A](index.md) · [ISCA 2026](../index.md)

**作者：** Junwei Cui, Le Qin, Weilin Cai, Jiayi Huang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The accelerating scale of large language models (LLMs) has driven an unprecedented increase in computational and memory demands that outpace the capability of conventional systems. Wafer-scale integration, with its dense, low-latency mesh interconnects across tightly packed arrays of compute and memory dies, emerges as a promising paradigm for massive system scaling. However, existing LLM deployment strategies, largely optimized for switch-based distributed GPU systems, are mismatched with the asymmetric mesh topology and bandwidth heterogeneity across tiers of wafer-scale systems. The inherent complexity of wafer-scale systems also makes them highly susceptible to node and link failures arising from manufacturing defects or runtime degradation, making fault-tolerant communication essential for robust LLM inference. To address these challenges, we introduce BusyBarn, a comprehensive framework that provides mapping and communication optimizations for efficient, fault-tolerant LLM inference on wafer-scale systems. BusyBarn introduces two key techniques: a hierarchical mapping algorithm that exploits the structural symmetry between Transformer blocks and die arrays to jointly optimize inter-die and intra-die workload deployment; and the Balanced Allocation with Load and Distance awareness (BALD) communication algorithm, which manages irregular traffic and balances load via link allocation for point-to-point and multicast collective primitives. Crucially, BusyBarn seamlessly integrates fault tolerance into these optimizations. Evaluation demonstrates that BusyBarn achieves up to 2.55× speedup in typical communication patterns and 1.08–2.14× end-to-end speedup for LLM inference compared to state-of-the-art methods.

## 中文摘要

大语言模型（LLM）规模的不断扩张，推动计算与内存需求以前所未有的速度增长，已超出传统系统的能力。晶圆级集成通过在紧密排布的计算与存储裸片阵列之间提供高密度、低延迟的网格互连，成为实现大规模系统扩展的一种颇具前景的范式。然而，现有 LLM 部署策略大多针对基于交换机的分布式 GPU 系统进行优化，与晶圆级系统不对称的网格拓扑以及各层级之间的带宽异构性并不匹配。晶圆级系统固有的复杂性也使其极易受到由制造缺陷或运行时退化所引发的节点与链路故障的影响，因此容错通信对于稳健的 LLM 推理至关重要。为应对这些挑战，我们提出 BusyBarn——一个综合性框架，为晶圆级系统上高效、容错的 LLM 推理提供映射与通信优化。BusyBarn 引入两项关键技术：一是分层映射算法，利用 Transformer 块与裸片阵列之间的结构对称性，联合优化裸片间与裸片内的工作负载部署；二是负载与距离感知的均衡分配（BALD）通信算法，针对点对点与多播集合原语，通过链路分配来管理不规则流量并均衡负载。尤为关键的是，BusyBarn 将容错能力无缝集成到这些优化之中。评估表明，与最先进方法相比，BusyBarn 在典型通信模式下最高实现 2.55× 的加速，在 LLM 推理端到端上实现 1.08–2.14× 的加速。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19686855）](https://zenodo.org/records/19686855)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2026](../index.md)
