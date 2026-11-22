---
title: "Helios: Enabling Dynamic KV Cache Management for Near-Memory Processing via Hybrid-Bonding-Based 3D-DRAM"
description: "MICRO 2026 · Session 5B · Helios：利用混合键合三维 DRAM 实现近存处理中的动态 KV 缓存管理"
tags:
  - "MICRO2026"
  - "Near-Memory Computing"
  - "DRAM"
  - "Cache"
---

# Helios: Enabling Dynamic KV Cache Management for Near-Memory Processing via Hybrid-Bonding-Based 3D-DRAM

**中文标题：** Helios：利用混合键合三维 DRAM 实现近存处理中的动态 KV 缓存管理

**所属 Session：** [Session 5B](index.md) · [MICRO 2026](../index.md)

**作者：** Cong Li, Yihan Yin, Chenhao Xue, Zhao Wang, Fujun Bai, Yixin Guo, Xiping Jiang, Qiang Wu, Yuan Xie, Guangyu Sun

**来源：** MICRO 2026，pp. 1714–1730；[DOI](https://doi.org/10.1109/MICRO67795.2026.00123)

## 英文摘要

Large language models (LLMs) have been widely deployed for online generative services, where numerous LLM instances jointly handle requests with fluctuating arrival rates and variable request lengths. To efficiently execute coexisting compute-intensive and memory-intensive operators, near-memory processing (NMP) based computing paradigm has been extensively proposed. However, existing NMP designs adopt coarse-grained KV cache management and inflexible attention execution flow. Such limitations hinder these proposals from efficiently handling highly dynamic LLM serving workloads, limiting their ability to accelerate LLM serving. To tackle these problems, we propose HeLios, a Hybrid-bonding-based LLM Serving accelerator. Helios aims to bridge the fundamental gap between dynamic KV cache management in LLM serving and the distributed, non-uniform memory abstraction among NMP processing engines (PEs). To this end, we design both the hardware architecture and operator execution for distributed tiled attention execution. We further propose spatially-aware KV cache allocation mechanism to balance the attention workload distribution while minimizing the inter-PE data transfer overhead. Compared with existing GPU/NMP designs, Helios achieves 3.25× (geomean) speedup and 3.36× (geomean) better energy efficiency, along with ≥72%/76% P50/P99 time-between-tokens reduction.

## 中文摘要

大语言模型 (LLM) 已广泛部署用于在线生成服务，其中大量 LLM 实例共同处理到达率波动和请求长度可变的请求。为了有效地执行共存的计算密集型和内存密集型运算符，人们广泛提出了基于近存处理（NMP）的计算范例。然而，现有的NMP设计采用粗粒度的KV缓存管理和不灵活的注意力执行流程。这些限制阻碍了这些提案有效处理高度动态的 LLM 服务工作负载，从而限制了它们加速 LLM 服务的能力。为了解决这些问题，我们提出了 HeLios，一种基于混合结合的 LLM 服务加速器。 Helios 旨在弥合 LLM 服务中的动态 KV 缓存管理与 NMP 处理引擎 (PE) 之间的分布式非统一内存抽象之间的根本差距。为此，我们设计了分布式平铺注意力执行的硬件架构和算子执行。我们进一步提出了空间感知的 KV 缓存分配机制，以平衡注意力工作负载分配，同时最小化 PE 间数据传输开销。与现有的 GPU/NMP 设计相比，Helios 实现了 3.25 倍（几何平均值）的加速和 3.36 倍（几何平均值）的能效，以及 ≥72%/76% 的 P50/P99 词元间隔时间缩短。

## 中文关键词

大语言模型；三维 DRAM 加速器；动态键值缓存管理；混合键合；近存处理

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5B](index.md) · [MICRO 2026 主页](../index.md)
