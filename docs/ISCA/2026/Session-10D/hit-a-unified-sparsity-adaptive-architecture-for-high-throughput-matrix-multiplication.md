---
title: "HiT: A Unified Sparsity-Adaptive Architecture for High-Throughput Matrix Multiplication"
description: "ISCA 2026 · Session 10D · HiT: A Unified Sparsity-Adaptive Architecture for High-Throughput Matrix Multiplication"
tags:
  - "ISCA2026"
  - "Session 10D"
  - "Domain Specific Accelerators 3"
---

# HiT: A Unified Sparsity-Adaptive Architecture for High-Throughput Matrix Multiplication

**中文标题：** HiT: 面向高吞吐矩阵乘法的统一稀疏自适应架构

**所属 Session：** [Session 10D](index.md) · [ISCA 2026](../index.md)

**作者：** Tingting Xiang, Xiaochen Wang, Miao Yu, Trevor E. Carlson

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Accelerating matrix operations has become increasingly critical as AI models and scientific workloads continue to scale. These applications involve matrices spanning sparsity levels from <0.0001% to fully dense, demanding accelerators that maintain high performance across this full range. However, prior designs either target a narrow sparsity range, resulting in inefficiencies outside their specialization, or support broad sparsity at the cost of throughput, with the state-of-the-art accelerator achieving less than 3.125% of peak performance on highly sparse matrices. We present HiT, a unified sparsity-adaptive architecture that delivers consistently high throughput and efficiency across the entire sparsity spectrum. HiT introduces two novel outer-product-based dataflows, HSparse and MSparse, supported by a Parallel Intersection & Distribution Unit and a Dual-mode Accumulator, targeting highly and moderately sparse workloads, respectively. These dataflows enable regular memory access to sparse data and on-chip accumulation of partial sums while exploiting two levels of spatial parallelism. As a result, HiT achieves high intersection rates (more valid non-zero matches per cycle) and data reuse, leading to high throughput. For dense workloads, HiT employs an inner-product dataflow to maximize compute efficiency. We benchmark HiT against Trapezoid, a state-of-the-art accelerator for full-spectrum sparsity. Specifically, it delivers a 3.24× geomean performance/area improvement on highly sparse× highly sparse multiplications, 2.18× across all highly sparse workloads, and 1.99× on moderately sparse workloads. Across a comprehensive set of dense and sparse workloads, HiT achieves 1.93× higher geomean performance/area and reduces energy consumption by 1.64× compared to Trapezoid.

## 中文摘要

随着 AI 模型和科学工作负载持续扩展，加速矩阵运算变得日益关键。这些应用涉及的矩阵稀疏度跨度从 <0.0001% 一直到完全稠密，要求加速器在整个范围内都保持高性能。然而，先前设计要么只针对狭窄的稀疏度区间，在其专门化范围之外效率低下；要么以牺牲吞吐量为代价支持宽泛的稀疏度——最先进的加速器在高度稀疏矩阵上仅达到峰值性能的不到 3.125%。我们提出 HiT，一种统一的稀疏度自适应架构，在整个稀疏度谱上都提供稳定的高吞吐量与高效率。HiT 引入两种新颖的基于外积（outer-product）的数据流——HSparse 与 MSparse，分别由并行求交与分发单元（Parallel Intersection & Distribution Unit）和双模累加器（Dual-mode Accumulator）支撑，面向高度稀疏和中度稀疏的工作负载。这些数据流使稀疏数据能够以规则的方式访存，并支持部分和的片上累加，同时利用两个层次的空间并行性。因此，HiT 实现了高求交率（每周期更多有效的非零匹配）和数据复用，从而带来高吞吐量。对于稠密工作负载，HiT 采用内积（inner-product）数据流以最大化计算效率。我们以 Trapezoid（一款面向全谱稀疏度的最先进加速器）为基准对 HiT 进行了评测。具体而言，它在高度稀疏×高度稀疏乘法上带来 3.24× 的几何平均性能/面积提升，在所有高度稀疏工作负载上为 2.18×，在中度稀疏工作负载上为 1.99×。在涵盖稠密与稀疏的全面工作负载集上，与 Trapezoid 相比，HiT 的几何平均性能/面积高 1.93×，并将能耗降低 1.64×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10D](index.md) · [返回 ISCA 2026](../index.md)
