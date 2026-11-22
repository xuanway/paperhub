---
title: "Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM"
description: "MICRO 2026 · Session 8A · 重新思考 NPU-PIM 系统的统一内存：面向 LLM 动态推理的双视图内存"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Processing-in-Memory"
---

# Rethinking Unified Memory for NPU-PIM Systems: Dual-View Memory for Dynamic Inference of LLM

**中文标题：** 重新思考 NPU-PIM 系统的统一内存：面向 LLM 动态推理的双视图内存

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Shixin Zhao, Lian Liu, Tianhua Han, Mengdi Wang, Yinhe Han, Ying Wang

**来源：** MICRO 2026，pp. 2800–2814；[DOI](https://doi.org/10.1109/MICRO67795.2026.00190)

## 英文摘要

Heterogeneous architectures that combine neural processing units (NPUs) and processing-in-memory (PIM) are increasingly adopted to accelerate LLM inference. Prior work focuses on building a unified memory that allows NPUs and PIM to share data without duplication. However, these designs implicitly assume that each tensor is bound to a fixed execution device, and therefore rely on static, device-biased data mappings. We observe that this assumption does not hold in modern LLM workloads. Due to phase changes (e.g., prefill vs. decode) and dynamic behaviors such as MoE routing, the optimal execution device for the same tensor can change at runtime. Under such dynamic execution, device-biased mappings become mismatched to access patterns, leading to substantial bandwidth underutilization and performance loss. This paper presents PFM (PIM-as-Flexible-Memory), a dual-view memory system that decouples physical data layout from accessor-visible logical views. PFM stores data in a jointly optimized physical layout and exposes different logical interpretations to NPUs and PIM, enabling efficient access across devices without data duplication or relayout. We further design accessor-aware address translation and runtime scheduling mechanisms to support dynamic execution when LLM workloads fluctuate and the optimal execution device dynamically changes. Our evaluation across LLMs shows that PFM improves end-to-end throughput by up to 2.32, demonstrating its effectiveness and broad applicability as a unified memory management solution for NPU-PIM systems.

## 中文摘要

越来越多地采用结合神经处理单元 (NPU) 和存内处理 (PIM) 的异构架构来加速 LLM 推理。之前的工作重点是构建统一内存，允许 NPU 和 PIM 共享数据而无需重复。然而，这些设计隐含地假设每个张量都绑定到固定的执行设备，因此依赖于静态的、设备偏向的数据映射。我们观察到，这种假设在现代大语言模型工作负载中并不成立。由于阶段变化（例如预填充与解码）和 MoE 路由等动态行为，同一张量的最佳执行设备可能会在运行时发生变化。在这种动态执行下，偏向设备的映射与访问模式不匹配，导致大量带宽未充分利用和性能损失。本文提出了 PFM（PIM 作为灵活内存），这是一种双视图内存系统，它将物理数据布局与访问者可见的逻辑视图解耦。 PFM 将数据存储在联合优化的物理布局中，并向 NPU 和 PIM 公开不同的逻辑解释，从而实现跨设备的高效访问，而无需数据重复或重新布局。我们进一步设计了访问器感知的地址转换和运行时调度机制，以支持当LLM工作负载波动和最佳执行设备动态变化时的动态执行。我们对大语言模型的评估表明，PFM 的端到端吞吐量最高达到基线的 2.32 倍，证明了其作为 NPU-PIM 系统统一内存管理解决方案的有效性和广泛适用性。

## 中文关键词

存内处理；NPU-PIM 系统；大语言模型推理；统一内存；双视图内存

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
