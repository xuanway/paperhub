---
title: "TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications"
description: "ISCA 2026 · Session 5D · TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications"
tags:
  - "ISCA2026"
  - "Session 5D"
  - "Potpourri"
---

# TDMSim: Enabling High-Density and Energy-Efficient GPU DRAM Caches with 2D-Materials for Data-Intensive Applications

**中文标题：** TDMSim: 借助 2D 材料为数据密集型应用实现高密度高能效 GPU DRAM 缓存

**所属 Session：** [Session 5D](index.md) · [ISCA 2026](../index.md)

**作者：** Chao Fu, Jingyang Zheng, Xinliu He, Xiangqi Dong, Zheng Cao, Yuning Zhan, WenZhong Bao, Peng Zhou, Jun Han

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern GPUs provision increasingly large last-level caches (LLCs) to sustain the high data-reuse demands of artificial intelligence and high-performance computing workloads. As capacity scales, conventional cache designs are fundamentally constrained by a tightly coupled trade-off among density, access latency, and energy. Two-dimensional (2D) materials, with intrinsically low leakage current and atomic-scale thickness, offer a promising approach for building high-density, energy-efficient cache arrays. However, architects lack a cross-level design methodology that can propagate device-level characteristics of 2D materials into quantitative architectural guidance, leaving the system-level potential of 2D-material caches unexplored. To this end, we present TDMSim, a validated cross-level simulation toolkit that bridges transistor-level, circuit-level, and system-level modeling for 2D-material-based architectures. Based on this toolkit, we integrate 2D-material DRAM cache designs into a CPU-GPU system, and propagate the intrinsic retention-time variability of 2D-material arrays to system-level metrics. To mitigate the impact of this variability, we design a retention-aware policy that steers 2D-material DRAM caches toward their ideal performance limit, achieving a 75.6% reduction in access interference rate and a 65.4% reduction in refresh energy. We evaluate the above proposed 2D-material DRAM caches under realistic GPU workloads, observing a 79.4% reduction in energy consumption alongside a 42.1% improvement in system performance under the same area budget as an SRAM cache. Moreover, 2D-material DRAM caches deliver 25.4% higher performance and 42.7% lower energy consumption than conventional DRAM caches with state-of-the-art optimizations. TDMSim will be released as open source to foster cross-level research on emerging 2D materials and to establish device-aware modeling as a general methodology for future 2D-material-based architectures.

## 中文摘要

现代 GPU 配置了越来越大的末级缓存（LLC），以支撑人工智能与高性能计算负载对数据复用的高要求。随着容量扩展，传统缓存设计从根本上受制于密度、访问时延与能耗之间紧密耦合的权衡。二维（2D）材料具有本征的低漏电流与原子级厚度，为构建高密度、高能效的缓存阵列提供了有前景的途径。然而，架构设计者缺乏一套跨层次设计方法，能够将 2D 材料的器件级特性转化为定量的架构指导，致使 2D 材料缓存的系统级潜力尚未被探索。为此，我们提出 TDMSim，一套经过验证的跨层次仿真工具链，为基于 2D 材料的架构打通晶体管级、电路级与系统级建模。基于该工具链，我们将 2D 材料 DRAM 缓存设计集成到 CPU-GPU 系统中，并将 2D 材料阵列固有的保持时间变异性传导至系统级指标。为缓解这种变异性的影响，我们设计了一种保持时间感知策略，引导 2D 材料 DRAM 缓存逼近其理想性能极限，实现访问干扰率降低 75.6%、刷新能耗降低 65.4%。我们在真实 GPU 负载下评估上述 2D 材料 DRAM 缓存，观察到在与 SRAM 缓存相同的面积预算下，能耗降低 79.4%、系统性能提升 42.1%。此外，相比采用最先进优化的传统 DRAM 缓存，2D 材料 DRAM 缓存的性能高出 25.4%、能耗低 42.7%。TDMSim 将开源发布，以促进面向新兴 2D 材料的跨层次研究，并确立器件感知建模作为未来基于 2D 材料架构的通用方法论。

## 代码与研究制品

论文表示计划将 TDMSim 开源。截至 2026-11-23，未找到可确认属于该论文的公开代码链接。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5D](index.md) · [返回 ISCA 2026](../index.md)
