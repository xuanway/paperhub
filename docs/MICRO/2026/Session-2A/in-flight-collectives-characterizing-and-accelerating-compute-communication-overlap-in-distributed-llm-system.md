---
title: "In-Flight Collectives: Characterizing and Accelerating Compute-Communication Overlap in Distributed LLM System"
description: "MICRO 2026 · Session 2A · In-Flight Collectives：刻画并加速分布式 LLM 系统中的计算通信重叠"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# In-Flight Collectives: Characterizing and Accelerating Compute-Communication Overlap in Distributed LLM System

**中文标题：** In-Flight Collectives：刻画并加速分布式 LLM 系统中的计算通信重叠

**所属 Session：** [Session 2A](index.md) · [MICRO 2026](../index.md)

**作者：** Jonghoon Kang, Zhixian Jin, John Kim

**来源：** MICRO 2026，pp. 539–552；[DOI](https://doi.org/10.1109/MICRO67795.2026.00051)

## 英文摘要

Driven by Scaling Laws, large-scale, distributed model training and inference utilize hundreds to thousands of accelerators and the inter-accelerator communication can become the bottleneck for overall performance. To accelerate overall performance, compute-communication overlap has been commonly utilized but the impact of such overlap has not been well analyzed. In this work, we provide a detailed analysis on the impact of compute-communication overlap on not only communication and compute performance but end-to-end performance. In particular, the resource contention for on-chip compute and memory, as well as off-chip memory bandwidth for LLM workloads, is analyzed through micro-kernel benchmark. Our analysis show that contention during compute-communication can lead to overall performance degradation when aggressive compute-communication overlap occurs by utilizing high bandwidth for communication. To enable efficient communication-computation overlap, we propose to minimize the interference between compute and communication during overlap through a hardware-software co-design architecture that we refer to as In-Flight Collective (IFC) communication architecture. IFC enables reductions to be done "in-flight" or on-the-fly manner while streaming compute data output to communication through kernel fusion while a dedicated on-chip memory resource is provided to further minimize on-chip resource contention. We evaluate IFC across mesh and switch topologies using GPT-3 175B and 1T models and achieve up to 26.6% training speedup and 38.5% inference throughput improvement, while resulting in 8.9x lower area overhead compared to prior work. We also observed decoding speedup, on Llama3.1-405B up to 10.3% in 128K context window, and 10.8% improvement on Mixtral-8x22B with IFC.

## 中文摘要

在缩放定律的驱动下，大规模分布式模型训练和推理需要使用数百到数千个加速器，加速器间的通信可能成为整体性能的瓶颈。为了加速整体性能，计算通信重叠已被普遍利用，但这种重叠的影响尚未得到很好的分析。在这项工作中，我们详细分析了计算通信重叠不仅对通信和计算性能而且对端到端性能的影响。特别是，通过微内核基准测试分析片上计算和内存的资源争用，以及 LLM 工作负载的片外内存带宽。我们的分析表明，当利用高带宽进行通信时发生严重的计算通信重叠时，计算通信期间的争用可能会导致整体性能下降。为了实现高效的通信-计算重叠，我们建议通过硬件-软件协同设计架构（我们称之为飞行集体（IFC）通信架构）最大限度地减少重叠期间计算和通信之间的干扰。 IFC 能够以“动态”或即时方式完成缩减，同时通过内核融合将计算数据输出流式传输到通信，同时提供专用片上存储器资源以进一步最小化片上资源争用。我们使用 GPT-3 175B 和 1T 模型跨网状和交换机拓扑评估 IFC，实现了高达 26.6% 的训练加速和 38.5% 的推理吞吐量改进，同时与之前的工作相比，面积开销降低了 8.9 倍。我们还观察到解码速度在 Llama3.1-405B 上在 128K 上下文窗口中提高了 10.3%，在使用 IFC 的 Mixtral-8x22B 上提高了 10.8%。

## 中文关键词

集合通信；资源干扰；计算与通信重叠；分布式系统；在线归约

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2A](index.md) · [MICRO 2026 主页](../index.md)
