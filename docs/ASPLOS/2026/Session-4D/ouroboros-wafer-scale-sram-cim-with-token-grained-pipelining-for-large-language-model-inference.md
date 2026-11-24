---
title: "Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference"
description: "ASPLOS 2026 · Session 4D · Ouroboros：用于大语言模型推理的晶圆级 SRAM CIM 与令牌粒度流水线"
tags:
  - "ASPLOS2026"
  - "Session 4D"
  - "Processing-in-Memory"
---

# Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference

**中文标题：** Ouroboros：用于大语言模型推理的晶圆级 SRAM CIM 与令牌粒度流水线

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yiqi Liu (University of Chinese Academy of Sciences), Yudong Pan (University of Chinese Academy of Sciences), Mengdi Wang (Institute of Computing Technology, Chinese Academy of Sciences), Shixin Zhao (University of Chinese Academy of Sciences), Haonan Zhu (University of Chinese Academy of Sciences), Yinhe Han (Institute of Computing Technology, Chinese Academy of Sciences), Lei Zhang (Institute of Computing Technology, Chinese Academy of Sciences), Ying Wang (Institute of Computing Technology, Chinese Academy of Sciences)

**单位：** University of Chinese Academy of Sciences；Institute of Computing Technology, Chinese Academy of Sciences

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790197) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large language model (LLM) inference demands vast memory capacity and hierarchical memory structures, but conventional architectures suffer from excessive energy and latency costs due to frequent data movement across deep memory tiers. To address this, we propose a wafer-scale SRAM-based Computing-in-Memory (CIM) architecture that performs all LLM operations in situ within the first-level SRAM, eliminating off-chip data migration and achieving unprecedented energy efficiency. However, wafer-scale SRAM CIM presents multiple challenges due to the limited first-level memory capacity, which requires efficient compute-memory resource allocation. To enable efficient LLM execution on this architecture, we propose three key innovations: Token-Grained Pipelining – Conventional sequence-level pipelining suffers from underutilization due to varying input sequence lengths and batching policies. We introduce a fine-grained token-level pipeline that mitigates sequence length variations, enhancing the utilization of CIM cores while minimizing the storage capacity required for activation. Distributed Dynamic KV Cache Management – KV cache storage occupies significant memory in LLM inference. We optimize on-chip KV caching by decoupling CIM memory from compute assignment, leveraging fragmented SRAM CIM memory within already-allocated cores for efficient KV storage, and reducing dedicated memory overhead. Communication-Aware and Fault-Tolerant Core Mapping – Efficient execution on wafer-scale CIM requires optimal mapping from transformer blocks to CIM cores to minimize inter-(pipeline) stage communication while ensuring intra-stage compute locality. We design a network-on-wafer-aware mapping strategy that places pipeline stages in close proximity while also distributing large layers efficiently across multiple cores. This mapping accounts for core-level defects, improving fault tolerance in wafer-scale deployment. Experimental results demonstrate that Ouroboros achieves 4.1× average throughput improvement and 4.2× average energy efficiency gain over state-of-the-art systems, peaking at 9.1× throughput and 17× energy efficiency for the 13B model.

## 中文摘要

大语言模型（LLM）推理需要巨大的存储容量与层次化存储结构，但传统架构由于在深层存储层级之间频繁移动数据，导致过高的能耗与延迟开销。为此，我们提出一种晶圆级、基于 SRAM 的存内计算（CIM）架构，在一级 SRAM 内原位执行全部 LLM 操作，消除片外数据迁移并获得前所未有的能效。然而，受限于一级存储容量，晶圆级 SRAM CIM 面临多重挑战，需要高效的计算—存储资源分配。为使 LLM 在该架构上高效执行，我们提出三项关键创新：令牌粒度流水线（Token-Grained Pipelining）——传统的序列级流水线因输入序列长度和批处理策略的变化而存在利用率不足的问题。我们引入细粒度的令牌级流水线，缓解序列长度变化的影响，在提升 CIM 核心利用率的同时最小化激活值所需的存储容量。分布式动态 KV cache 管理（Distributed Dynamic KV Cache Management）——KV cache 存储在 LLM 推理中占用大量存储。我们通过将 CIM 存储与计算分配解耦来优化片上 KV 缓存，利用已分配核心内部碎片化的 SRAM CIM 存储实现高效的 KV 存储，并降低专用存储开销。通信感知且容错的核映射（Communication-Aware and Fault-Tolerant Core Mapping）——在晶圆级 CIM 上高效执行，需要将 Transformer 块到 CIM 核心的映射做到最优，以最小化（流水）级间通信，同时保证级内计算局部性。我们设计了一种感知片上网络（network-on-wafer）的映射策略，使流水级彼此邻近，同时将大层高效地分布到多个核心上。该映射考虑了核心级缺陷，提升了晶圆级部署的容错能力。实验结果表明，与最先进的系统相比，Ouroboros 平均吞吐量提升 4.1×，平均能效提升 4.2×，对于 13B 模型，吞吐量峰值提升 9.1×，能效峰值提升 17×。

## 英文关键词

Wafer-Scale Chips; Computing-in-Memory; Large Language Model; Scheduling

## 中文关键词

晶圆级芯片；存内计算；大语言模型；调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790197)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2026](../index.md)
