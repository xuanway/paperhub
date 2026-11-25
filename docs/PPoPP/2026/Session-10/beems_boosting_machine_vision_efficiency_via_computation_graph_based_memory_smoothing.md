---
title: "BEEMS: Boosting Machine Vision Efficiency via Computation Graph-Based Memory Smoothing"
description: "PPoPP 2026 Session 10（ML Inference）：高峰算子降内存、低谷算子提延迟，峰值内存最多降 90%"
tags:
  - "PPoPP2026"
  - "Session-10"
  - "ML Inference"
  - "Memory Optimization"
  - "Compiler"
  - "Vision Models"
authors:
  - "Hanjing Shen"
  - "Fangxin Liu"
  - "Jian Liu"
  - "Li Jiang"
  - "Haibing Guan"
session: "Session 10: ML Inference"
session_number: 10
session_chair: "Hailong Yang"
date: "2026-02-03"
time: "15:50–16:10"
room: "Balmoral"
doi: "10.1145/3774934.3786430"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# BEEMS: Boosting Machine Vision Efficiency via Computation Graph-Based Memory Smoothing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 BEEMS，一种双目标编译器，通过平滑视觉基础模型计算图的内存使用同时优化内存与延迟，六个模型上峰值内存最多降低 90%、延迟改善 10%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 10: ML Inference</p>
</div>

**作者**：Hanjing Shen, Fangxin Liu, Jian Liu, Li Jiang, and Haibing Guan — Shanghai Jiao Tong University, China; Beihang University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 15:50–16:10 · Session 10: ML Inference（主席：Hailong Yang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786430) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

With the rapid advances of deep learning-based computer vision (CV) technology, digital images are increasingly processed not by humans, but by downstream CV algorithms. In particular, the growing popularity of vision foundation models has heightened interest in deploying these models on edge devices. However, limited memory remains a key bottleneck, making memory footprint reduction essential. Mainstream model customization methods often require intensive deployment efforts and can severely degrade accuracy. Moreover, existing deep learning frameworks generally do not prioritize memory optimization. Existing memory management schemes face practical limitations, including layer-wise memory imbalance, high management overhead, and volatile memory budgets. To tackle these issues, this work focuses on compilation-level optimizations that are explicitly designed to be memory-aware. We observe that memory usage during vision foundation model inference varies significantly over time (up to a 10× difference), with extended periods of low memory demand. Based on this, we propose BEEMS, a dual-objective compiler that optimizes both memory and latency by smoothing memory usage across the computational graph. BEEMS analyzes the vision foundation model computational graph to identify peak and trough operators in terms of memory demand. It then builds an efficient optimization search space, offering a flexible interface that applies different strategies based on operator characteristics. Specifically, peak operators are optimized using techniques such as operator partitioning, kernel substitution, swapping, and rematerialization to reduce memory pressure, while trough operators apply subgraph substitutions to improve latency. Experiments on six diverse models show that BEEMS reduces peak memory by up to 90% and improves latency by 10%, demonstrating its effectiveness in jointly optimizing memory and performance.

## 中文摘要

随着基于深度学习的计算机视觉（CV）技术的快速发展，数字图像越来越多地不是由人处理，而是由下游的 CV 算法处理。特别是视觉基础模型（vision foundation model）的日益普及，进一步提升了将这些模型部署到边缘设备上的兴趣。然而，有限的内存仍是关键瓶颈，因此降低内存占用至关重要。主流的模型定制方法通常需要大量部署工作，且可能严重降低精度。此外，现有深度学习框架一般并不优先考虑内存优化。现有的内存管理方案面临实际局限，包括逐层内存不均衡、管理开销高以及内存预算波动。为解决这些问题，本文聚焦于显式为内存感知而设计的编译级优化。我们观察到，视觉基础模型推理过程中的内存使用随时间显著变化（差异最高可达 10×），并存在较长的低内存需求时段。基于此，我们提出 BEEMS，一种双目标编译器，通过平滑整个计算图上的内存使用，同时优化内存与延迟。BEEMS 分析视觉基础模型的计算图，以识别内存需求上的峰值算子与谷值算子。随后，它构建高效的优化搜索空间，提供灵活的接口，根据算子特征应用不同策略。具体而言，峰值算子通过算子划分、核函数替换、换出（swapping）与重算（rematerialization）等技术进行优化以降低内存压力，而谷值算子则应用子图替换以改善延迟。在六个不同模型上的实验表明，BEEMS 将峰值内存最多降低 90%，并将延迟改善 10%，证明了其在联合优化内存与性能方面的有效性。

## 英文关键词

AI compilation, deep learning systems, memory optimization

## 中文关键词

AI 编译；深度学习系统；内存优化

---

## 一句话总结

> 提出 BEEMS，一种双目标编译器，通过平滑视觉基础模型计算图的内存使用同时优化内存与延迟，六个模型上峰值内存最多降低 90%、延迟改善 10%。

## 研究问题

视觉基础模型部署到边缘设备受限于内存；主流模型定制方法部署成本高且可能严重损害精度，现有内存管理方案又存在层间内存不均衡、管理开销大、内存预算波动等问题。

## 方法简述

- 观察到视觉基础模型推理期内存使用随时间显著变化（差异可达 10×），并存在较长的低内存需求区间。
- 分析计算图，按内存需求识别高峰算子与低谷算子，并构建高效的优化搜索空间与灵活接口。
- 对高峰算子采用算子划分、算子替换（kernel substitution）、换出（swapping）与重算（rematerialization）等技术降低内存压力。
- 对低谷算子应用子图替换以改善延迟，实现编译级内存感知的协同优化。

## 主要结果

- 在六个多样化模型上，峰值内存最多降低 90%。
- 延迟改善 10%，验证了内存与性能联合优化的有效性。

---

> 所属 Session：[Session 10: ML Inference](index.md) · 返回 [PPoPP 2026 总览](../index.md)
