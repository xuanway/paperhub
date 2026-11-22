---
title: "Beyond Linear Scaling for LLM Training on Wafer-Scale GPUs"
description: "MICRO 2026 · Session 4C · 突破晶圆级 GPU 上 LLM 训练的线性扩展限制"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
  - "LLM Training"
---

# Beyond Linear Scaling for LLM Training on Wafer-Scale GPUs

**中文标题：** 突破晶圆级 GPU 上 LLM 训练的线性扩展限制

**所属 Session：** [Session 4C](index.md) · [MICRO 2026](../index.md)

**作者：** Qijun Zhang, Jingchen Zhu, Chen Zhang, Zixiao Chen, Yiqi Chen, Mengming Li, Guangyu Sun, Cheng Zhang, Zhe Zhou, Zhiyao Xie

**来源：** MICRO 2026，pp. 1492–1506；[DOI](https://doi.org/10.1109/MICRO67795.2026.00110)

## 英文摘要

Wafer-scale GPUs integrate many dies on a single substrate to break the reticle limit for LLM training. Current systems adopt distributed execution that achieves at best linear scaling, but linear scaling is suboptimal: ideal single-GPU performance scaling, e.g., attainable FLOP per second relative to the hardware resources, is beyond linear, as proportional resource scaling creates memory-system redundancy. The root cause preventing this is L2 isolation, where distributed execution confines each die to its local L2. We propose Halo, a hardware-software co-design framework that breaks L2 isolation through architecturally managed SM-direct remote loads, enabling practical cross-die L2 sharing at wafer scale. Remote-access scheduling reduces communication overhead by confining traffic within topology-aligned regions and partitioning wafer into L2-sharing domains. Speculative pipelining hides the elevated remote-access latency by deferring shared-memory allocation until data arrives, allowing deep software pipelining beyond physical shared-memory capacity. Evaluated on a cycle-accurate simulator with diverse LLM workloads, Halo achieves 1.24x average speedup over state-of-the-art distributed execution, reaching 98% of the theoretical beyond-linear bound, at <0.02% die-area overhead.

## 中文摘要

晶圆级 GPU 在单个基板上集成了许多芯片，打破了 LLM 训练的标线限制。当前系统采用分布式执行，最多可实现线性扩展，但线性扩展并不是最理想的：理想的单 GPU 性能扩展（例如，相对于硬件资源每秒可实现的 FLOP）超出了线性，因为按比例的资源扩展会产生内存系统冗余。阻止这种情况的根本原因是 L2 隔离，其中分布式执行将每个芯片限制在其本地 L2 中。我们提出 Halo，一种硬件-软件协同设计框架，通过架构管理的 SM 直接远程加载打破 L2 隔离，从而实现晶圆级的实际跨芯片 L2 共享。远程访问调度通过将流量限制在拓扑对齐区域内并将晶圆划分为 L2 共享域来减少通信开销。推测性流水线通过推迟共享内存分配直到数据到达来隐藏增加的远程访问时延，从而允许超出物理共享内存容量的深度软件流水线。在具有不同 LLM 工作负载的周期精确模拟器上进行评估，Halo 的平均加速比最先进的分布式执行提高了 1.24 倍，达到理论超线性界限的 98%，芯片面积开销<0.02%。

## 中文关键词

图形处理器；晶圆级芯片；大语言模型训练加速；扩展性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4C](index.md) · [MICRO 2026 主页](../index.md)
