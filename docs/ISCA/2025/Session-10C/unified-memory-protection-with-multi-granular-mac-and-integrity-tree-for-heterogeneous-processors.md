---
title: "Unified Memory Protection with Multi-granular MAC and Integrity Tree for Heterogeneous Processors"
description: "ISCA 2025 · Session 10C · 面向异构处理器的多粒度 MAC 与完整性树统一内存保护"
tags:
  - "ISCA2025"
  - "Session 10C"
  - "Security"
---

# Unified Memory Protection with Multi-granular MAC and Integrity Tree for Heterogeneous Processors

**中文标题：** 面向异构处理器的多粒度 MAC 与完整性树统一内存保护

**所属 Session：** [Session 10C](index.md) · [ISCA 2025](../index.md)

**作者：** Sunho Lee, Seonjin Na, Jeongwon Choi, Jinwon Pyo, Jaehyuk Huh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731066) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Recent system-on-a-chip (SoC) architectures for edge systems incor- porate a variety of processing units, such as CPUs, GPUs, and NPUs. Although hardware-based memory protection is crucial for the se- curity of edge systems, conventional mechanisms experience a sig- nificant performance degradation in such heterogeneous SoCs due to the increased memory traffic with diverse access patterns from different processing units. To mitigate the overheads, recent studies, targeting a specific domain such as machine learning software or accelerator, proposed techniques based on custom granularities applicable either to counters or MACs, but not both. In response to this challenge, we propose a unified mechanism to support both multi-granular MACs and counters in a device-independent way. It supports a granularity-aware integrity tree to make it adaptable to various access patterns. The multi-granular tree architecture stores both coarse-grained and fine-grained counters at different levels in the tree. Combined with the multi-granularity technique for MACs. Our optimization technique, termed multi-granular MAC&tree, sup- ports four different levels of granularity. Its dynamic detection mechanism can select the most appropriate granularity for differ- ent memory regions accessed by heterogeneous processing units. In addition, we combine the multi-granularity support with the prior subtree approaches to further reduce the overheads. Our simulation- based evaluation results show that the multi-granular MAC and tree reduce the execution time by 14.2% from the conventional fixed-granular MAC&tree. By combining prior sub-tree techniques, the multi-granular MAC and tree finally reduce the execution time by 21.1% compared to the conventional fixed-granular MAC&tree.

## 中文摘要

面向边缘系统的新一代片上系统（SoC）集成了CPU、GPU、NPU等多种处理单元。基于硬件的内存保护对边缘系统安全至关重要，但在这类异构SoC中，来自不同计算单元的访存模式差异大、内存流量激增，传统保护机制会带来显著性能下降。为降低开销，近期面向机器学习、专用加速器等特定领域的工作，提出了定制粒度方案，但它们只能适配消息认证码（MAC）或计数器其中一种，无法同时兼顾二者。

针对该问题，本文提出一种与设备无关的统一机制，同时支持多粒度MAC与计数器。该机制采用感知粒度的完整性树，适配多样化访存模式。多粒度树架构在树的不同层级分别存放粗粒度与细粒度计数器，并搭配MAC多粒度技术。
这套优化方案命名为**多粒度MAC&树**，支持4档不同粒度；动态检测机制可以为异构单元访问的不同内存区域自动选择最合适粒度。此外，本文将多粒度能力与已有子树优化技术结合，进一步压低开销。仿真评测结果表明：相比传统固定粒度MAC&树，多粒度MAC&树可将执行时间缩短14.2%；在叠加子树优化后，最终相比传统方案缩短21.1%。

## 英文关键词

Hardware security, memory protection, heterogeneous processors

## 中文关键词

硬件安全, 内存保护, 异构处理器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731066)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2025](../index.md)
