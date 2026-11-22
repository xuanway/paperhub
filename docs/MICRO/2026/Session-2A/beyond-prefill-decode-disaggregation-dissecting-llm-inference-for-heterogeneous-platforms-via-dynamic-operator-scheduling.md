---
title: "Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling"
description: "MICRO 2026 · Session 2A · 超越预填充与解码分离：通过动态算子调度剖析异构平台上的 LLM 推理"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling

**中文标题：** 超越预填充与解码分离：通过动态算子调度剖析异构平台上的 LLM 推理

**所属 Session：** [Session 2A](index.md) · [MICRO 2026](../index.md)

**作者：** Jiaqi Yang, Jiayi Li, Yihan Fu, Hongxiao Zhao, Zhan Chen, Qiuping Wu, Yuchao Yang, Bonan Yan

**来源：** MICRO 2026，pp. 522–538；[DOI](https://doi.org/10.1109/MICRO67795.2026.00050)

## 英文摘要

Prefill–decode disaggregation (PD) and roofline-based operator placement are common strategies for partitioning Large Language Model (LLM) inference across heterogeneous systems, but they are often insufficient in practice. End-to-end latency also depends on workload shape, runtime device contention, and persistent weight layout. We present DOPS (dynamic operator scheduling), a hardware-aware, closed-loop framework that jointly optimizes operator scheduling and blockwise weight layouts. DOPS constructs a stage-aware directed acyclic graph (DAG) and integrates two components: the Bifocal scheduler for dynamic operator-to-device placement and the Weight Layout Arbiter (WLA) for selecting hardware-efficient weight layouts under strict memory constraints. Across representative heterogeneous systems combining neural processing units (NPUs) and processing-in-memory (PIM) devices, Bifocal achieves geometric-mean speedups of 1.20× to 2.23× over the PD baseline. WLA provides an additional geometric-mean speedup of 1.28× to 1.33× over Bifocal/Linear. DOPS also supports systematic analysis of workload sensitivity and hardware scalability for LLM serving. The source code is available at https://github.com/YIAI-02/DOPS, and a demonstration of the visualization tool is available at https://youtu.be/Ya_oMCyYno0

## 中文摘要

预填充解码分解（PD）和基于屋顶线的算子放置是跨异构系统划分大语言模型（LLM）推理的常见策略，但它们在实践中通常是不够的。端到端时延还取决于工作负载形状、运行时设备争用和持久权重布局。我们提出了 DOPS（动态算子调度），这是一种硬件感知的闭环框架，可联合优化算子调度和块式权重布局。 DOPS 构建了一个阶段感知的有向无环图 (DAG)，并集成了两个组件：用于动态算子到设备放置的双焦调度器和用于在严格内存限制下选择硬件高效权重布局的权重布局仲裁器 (WLA)。在结合神经处理单元 (NPU) 和存内处理 (PIM) 设备的代表性异构系统中，Bifocal 在 PD 基线上实现了 1.20 倍至 2.23 倍的几何平均加速。与双焦/线性相比，WLA 提供额外的几何平均加速 1.28 倍至 1.33 倍。 DOPS 还支持对 LLM 服务的工作负载敏感性和硬件可扩展性进行系统分析。源代码位于 https://github.com/YIAI-02/DOPS，可视化工具的演示位于 https://youtu.be/Ya_oMCyYno0

## 中文关键词

大语言模型推理；异构系统；存内处理；算子调度；权重布局

## 代码与研究制品

- 代码仓库：[https://github.com/YIAI-02/DOPS](https://github.com/YIAI-02/DOPS)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2A](index.md) · [MICRO 2026 主页](../index.md)
