---
title: "GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design"
description: "MICRO 2026 · Session 3B · GPU-Tile-Sim：面向 LLM 软硬件协同设计的分块 GPU 仿真框架"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
  - "Simulation"
  - "HW-SW Co-design"
---

# GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design

**中文标题：** GPU-Tile-Sim：面向 LLM 软硬件协同设计的分块 GPU 仿真框架

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Yitong Ding, Jiawei Huang, Renyang Guan, Yangjie Zhou, Zihan Liu, Yu Feng, Shixuan Sun, Minyi Guo, Jingwen Leng, Jian Weng

**来源：** MICRO 2026，pp. 1069–1083；[DOI](https://doi.org/10.1109/MICRO67795.2026.00084)

## 英文摘要

Modern LLM (large language model) workloads increasingly rely on optimized GPU kernels through hardware-software co-design. These kernels achieve high-performance through fine-grained dependency scheduling and computation-memory overlap. As such, they incur new challenges on existing GPU performance models. Instruction-driven simulators are costly to adapt to evolving architectures, while analytical models are too coarse to capture kernels' characteristics. We propose GTSim, a tile-centric GPU simulation framework for LLM hardware-software co-design. The key insight is that modern LLM kernel performance is governed less by individual instruction latency than by the dependency structure that controls execution order and overlap. Accordingly, GTSim represents kernel execution as a warp-level tile graph whose nodes capture tile-level operations and whose edges encode data and ordering constraints. Using this representation, we design an automatic tile-graph frontend and a graph-driven simulation backend. We evaluate GTSim on representative GEMM, attention, and end-to-end LLM inference workloads. On A100 and H100 across both conventional and highly optimized kernels, GTSim achieves high performance-modeling accuracy (MAPE, Mean Absolute Percentage Error, 1.22%–8.71%). We further extend GTSim to Blackwell with preliminary validation and demonstrate its utility for software and hardware co-design.

## 中文摘要

现代 LLM（大语言模型）工作负载越来越依赖于通过软硬件协同设计优化的 GPU 内核。这些内核通过细粒度的依赖调度和计算内存重叠来实现高性能。因此，它们对现有 GPU 性能模型提出了新的挑战。指令驱动的模拟器适应不断发展的架构的成本很高，而分析模型又过于粗糙，无法捕捉内核的特征。我们提出了 GTSim，一个以分块为中心的 GPU 模拟框架，用于 LLM 硬件-软件协同设计。关键的见解是，现代 LLM 内核性能较少受单个指令时延的影响，而是受控制执行顺序和重叠的依赖结构的影响。因此，GTSim 将内核执行表示为线程束级分块图，其节点捕获分块级操作，其边对数据和排序约束进行编码。使用这种表示，我们设计了一个自动平铺图前端和一个图驱动的模拟后端。我们在代表性 GEMM、注意力和端到端 LLM 推理工作负载上评估 GTSim。在传统内核和高度优化内核的 A100 和 H100 上，GTSim 实现了高性能建模精度（MAPE，平均绝对百分比误差，1.22%–8.71%）。我们通过初步验证将 GTSim 进一步扩展到 Blackwell，并展示了其软件和硬件协同设计的实用性。

## 中文关键词

GPU 仿真；大语言模型工作负载；分块图；软硬件协同设计；性能建模

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
