---
title: "PECO: Prediction-Execution Co-Optimized Constant-Memory Sparse Attention Accelerator for Foundational Diffusion Model"
description: "MICRO 2026 · Session 7C · PECO：面向基础扩散模型、协同优化预测与执行的恒定内存稀疏注意力加速器"
tags:
  - "MICRO2026"
---

# PECO: Prediction-Execution Co-Optimized Constant-Memory Sparse Attention Accelerator for Foundational Diffusion Model

**中文标题：** PECO：面向基础扩散模型、协同优化预测与执行的恒定内存稀疏注意力加速器

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Xujiang Xiang, Longke Yan, Fengbin Tu

**来源：** MICRO 2026，pp. 2544–2558；[DOI](https://doi.org/10.1109/MICRO67795.2026.00174)

## 英文摘要

Sparse attention, which operates as a tightly coupled prediction-then-execution pipeline, is a promising way to accelerate long-context Foundational Diffusion Models (FDMs). However, existing accelerators are inherently myopic and locally optimized, primarily due to the absence of an analytical bottleneck model characterizing the bottlenecks throughout the whole sparse attention pipeline. To address this gap, we propose the first full-stack Analytical Bottleneck Model that jointly captures prediction, execution, and system pipeline behavior. The model reveals three fundamental bottlenecks in existing designs: memory traffic, prediction scalability, and execution efficiency. Guided by these insights, we present PECO, a prediction-execution co-optimized sparse attention accelerator for FDMs. PECO is built through modeling-guided algorithm-hardware co-design: Token Clustering removes the prediction bottleneck, its synergy with Multi-stage Fusion Dataflow enables full-pipeline O(1) constant on-chip memory requirement, and its synergy with Base-Offset PE improves execution efficiency via 4-bit quantization. As a result, PECO is the first training-free sparse attention accelerator for FDMs that achieves full-pipeline O(1) constant memory and is analytically guaranteed to remain in the scalable Execution-Bound state. PECO delivers up to 5.54x-7.93x, 4.13x-56.6x, and 4.10x-8.26x speedups over an NVIDIA H100 GPU, FACT, and EXION, respectively.

## 中文摘要

稀疏注意力作为紧密耦合的预测然后执行管道运行，是加速长上下文基础扩散模型（FDM）的一种有前途的方法。然而，现有的加速器本质上是短视和局部优化的，这主要是由于缺乏分析瓶颈模型来表征整个稀疏注意力管道的瓶颈。为了解决这一差距，我们提出了第一个全栈分析瓶颈模型，该模型联合捕获预测、执行和系统管道行为。该模型揭示了现有设计中的三个基本瓶颈：内存流量、预测可扩展性和执行效率。在这些见解的指导下，我们提出了 PECO，一种用于 FDM 的预测执行协同优化稀疏注意力加速器。 PECO 是通过建模引导的算法-硬件协同设计构建的：词元聚类消除了预测瓶颈，其与多级融合数据流的协同作用实现了全管道 O(1) 恒定片上内存需求，其与 Base-Offset PE 的协同作用通过 4 位量化提高了执行效率。因此，PECO 是第一个用于 FDM 的免训练稀疏注意力加速器，它实现了全管道 O(1) 常量内存，并在分析上保证保持在可扩展的执行绑定状态。与 NVIDIA H100 GPU、FACT 和 EXION 相比，PECO 分别可提供高达 5.54x-7.93x、4.13x-56.6x 和 4.10x-8.26x 的加速。

## 中文关键词

稀疏注意力；基础扩散模型；加速器；解析模型；常量内存

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
