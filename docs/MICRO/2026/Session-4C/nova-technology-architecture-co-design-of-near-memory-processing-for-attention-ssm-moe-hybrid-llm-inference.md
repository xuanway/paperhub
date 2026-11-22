---
title: "NOVA: Technology-Architecture Co-Design of Near-Memory Processing for Attention-SSM-MoE Hybrid LLM Inference"
description: "MICRO 2026 · Session 4C · NOVA：面向注意力、SSM 与 MoE 混合 LLM 推理的近存处理技术与架构协同设计"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Near-Memory Computing"
  - "HW-SW Co-design"
---

# NOVA: Technology-Architecture Co-Design of Near-Memory Processing for Attention-SSM-MoE Hybrid LLM Inference

**中文标题：** NOVA：面向注意力、SSM 与 MoE 混合 LLM 推理的近存处理技术与架构协同设计

**所属 Session：** [Session 4C](index.md) · [MICRO 2026](../index.md)

**作者：** In-Jun Jung, Jaeha Min, Joo-Young Kim

**来源：** MICRO 2026，pp. 1507–1528；[DOI](https://doi.org/10.1109/MICRO67795.2026.00111)

## 英文摘要

The rapid evolution of hybrid large language models (LLMs), which interleave grouped-query-attention (GQA), state-space model (SSM), and Mixture-of-Experts (MoE) layers, introduces two fundamental challenges for near-memory processing (NMP) architectures. First, the Technology Wall: the conventional 6F^2 DRAM cell is approaching its physical scaling limits at current 10nm-class nodes, making it difficult to meet the rapidly increasing memory capacity demands driven by MoE models with hundreds of experts. Second, the Architecture Wall: existing NMP designs are optimized for narrow arithmetic intensity (Op/B) ranges and cannot efficiently support the highly heterogeneous compute characteristics of hybrid LLMs, spanning memory-bound SSM layers, compute-intensive GQA layers, and large Op/B variations across experts. In this paper, we propose NOVA, a technology-architecture co-designed NMP system that simultaneously overcomes both walls. On the technology side, NOVA combines a 4F^2 vertical channel transistor (VCT) DRAM cell with a peri-over-cell (POC) structure to achieve approximately 2× memory density at iso-area compared to conventional 6F^2-based DRAM, enabling continued scaling into sub-10nm nodes. On the architecture side, NOVA repurposes the POC peripheral-die (peri-die) to host processing units, forming a 2-tier NMP architecture: Tier-1 (peri-die NMP), optimized for low-to-mid Op/B operations, and Tier-2 (base-die NMP), optimized for mid-to-high Op/B operations. By enabling parallel execution across tiers, NOVA effectively supports diverse compute patterns for hybrid LLMs, maximizing inference performance. Evaluated on state-of-the-art hybrid and MoE LLMs, including Nemotron3-Nano, Nemotron3-Super, Falcon-H1R, and Qwen3, NOVA achieves an average of 4.5× higher throughput, 69.8% lower end-to-end latency, and 5× better energy efficiency compared to a GPU baseline, with only 3.9% area overhead and no loss in memory capacity.

## 中文摘要

混合大语言模型 (LLM) 的快速发展，交织了分组查询注意 (GQA)、状态空间模型 (SSM) 和专家混合 (MoE) 层，为近存处理 (NMP) 架构带来了两个基本挑战。首先是技术墙：传统的6F^2 DRAM单元在当前10nm级节点上已接近其物理缩放极限，难以满足由数百名专家组成的MoE模型驱动的快速增长的内存容量需求。其次，架构墙：现有的 NMP 设计针对狭窄的算术强度 (Op/B) 范围进行了优化，无法有效支持混合 LLM 的高度异构计算特性、跨越内存限制的 SSM 层、计算密集型 GQA 层以及专家之间的大 Op/B 变化。在本文中，我们提出了 NOVA，一种技术架构共同设计的 NMP 系统，可以同时克服两面墙。在技​​术方面，NOVA 将 4F^2 垂直沟道晶体管 (VCT) DRAM 单元与单元重叠 (POC) 结构相结合，与传统基于 6F^2 的 DRAM 相比，在等面积上实现约 2 倍的存储密度，从而能够继续扩展到 10nm 以下节点。在架构方面，NOVA 将 POC 外设芯片（peri-die）重新调整为主机处理单元，形成 2 层 NMP 架构：针对中低 Op/B 操作进行优化的 Tier-1（peri-die NMP），以及针对中高级 Op/B 操作进行优化的 Tier-2（基础芯片 NMP）。通过启用跨层并行执行，NOVA 有效支持混合 LLM 的多种计算模式，从而最大限度地提高推理性能。在最先进的混合和 MoE LLM（包括 Nemotron3-Nano、Nemotron3-Super、Falcon-H1R 和 Qwen3）上进行评估后，与 GPU 基准相比，NOVA 的吞吐量平均提高了 4.5 倍，端到端时延降低了 69.8%，能效提高了 5 倍，面积开销仅为 3.9%，并且内存容量没有损失。

## 中文关键词

混合大语言模型；分组查询注意力；状态空间模型；混合专家模型；近存处理；工艺与架构协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4C](index.md) · [MICRO 2026 主页](../index.md)
