---
title: "ASM-SpMM: Unleashing the Potential of Arm SME for Sparse Matrix Multiplication Acceleration"
description: "PPoPP 2026 Session 5（Stencil and Sparse Matrix Computation）：SME 感知 SpMM 库，异构核工作窃取，最高 7.9× 加速"
tags:
  - "PPoPP2026"
  - "Session-5"
  - "Stencil and Sparse Matrix Computation"
  - "SpMM"
  - "Arm SME"
  - "Load Balancing"
authors:
  - "Jiazhi Jiang"
  - "Xijia Yao"
  - "Jiayu Chen"
  - "Jinhui Wei"
  - "Dan Huang"
  - "Yutong Lu"
session: "Session 5: Stencil and Sparse Matrix Computation"
session_number: 5
session_chair: "Shoaib Kamil"
date: "2026-02-03"
time: "10:10–10:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786422"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# ASM-SpMM: Unleashing the Potential of Arm SME for Sparse Matrix Multiplication Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出与 Arm SME 协同设计的高性能 SpMM 库 ASM-SpMM，结合内存高效压缩格式、外积式 SME 核、混合矩阵-向量执行与工作窃取负载均衡，最高加速 7.9×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 5: Stencil and Sparse Matrix Computation</p>
</div>

**作者**：Jiazhi Jiang, Xijia Yao, Jiayu Chen, Jinhui Wei, Dan Huang, and Yutong Lu — Sun Yat-sen University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 10:10–10:30 · Session 5: Stencil and Sparse Matrix Computation（主席：Shoaib Kamil）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786422) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Sparse Matrix–Matrix Multiplication (SpMM) is a core kernel in scientific computing, data analytics, and artificial intelligence, supporting applications such as linear solvers and Graph Neural Networks (GNNs). The Scalable Matrix Extension (SME) in Armv9 introduces dedicated matrix acceleration for ARM CPUs, but exploiting its full potential for SpMM requires architecture-aware optimizations to address irregular sparsity and hardware constraints. We present ASM-SpMM, a high-performance SpMM library co-designed with ARM SME. ASM-SpMM combines a memory-efficient compression format, an SME-aware kernel optimized for outer-product execution, a hybrid matrix–vector execution strategy, and work-stealing-based dynamic load balancing across heterogeneous cores. Experiments on emerging Armv9 platforms demonstrate up to 7.9× speedup over state-of-the-art SpMM libraries across diverse matrices. A GNN inference case study further shows that ASM-SpMM significantly improves end-to-end performance, highlighting the effectiveness of SME-aware SpMM optimization on ARM CPUs.

## 中文摘要

稀疏矩阵–矩阵乘法（SpMM）是科学计算、数据分析与人工智能中的核心内核，支撑线性求解器与图神经网络（GNN）等应用。Armv9 的可伸缩矩阵扩展（SME）为 ARM CPU 引入了专用的矩阵加速能力，但要充分挖掘其在 SpMM 上的潜力，仍需针对不规则稀疏性与硬件约束进行架构感知的优化。我们提出 ASM-SpMM，一个与 ARM SME 协同设计的高性能 SpMM 库。ASM-SpMM 结合了内存高效的压缩格式、面向外积执行优化的 SME 感知内核、矩阵–向量混合执行策略，以及跨异构核的基于工作窃取的动态负载均衡。在新兴 Armv9 平台上的实验表明，针对多样化的矩阵，ASM-SpMM 相较最先进的 SpMM 库最高取得 7.9 倍加速。一项 GNN 推理案例研究进一步表明，ASM-SpMM 显著提升了端到端性能，凸显了 ARM CPU 上 SME 感知 SpMM 优化的有效性。

## 英文关键词

SpMM, ARM SME, SVE, Outer Product

## 中文关键词

SpMM；ARM SME；SVE；外积

---

## 一句话总结

> 提出与 Arm SME 协同设计的高性能 SpMM 库 ASM-SpMM，结合内存高效压缩格式、外积式 SME 核、混合矩阵-向量执行与工作窃取负载均衡，最高加速 7.9×。

## 研究问题

Armv9 的 SME 虽提供专用矩阵加速，但要充分释放其在 SpMM 上的潜力，仍需面向不规则稀疏性与硬件约束的架构感知优化。

## 方法简述

- 采用内存高效的稀疏矩阵压缩格式。
- 设计面向外积执行方式的 SME 感知核函数。
- 提出混合的矩阵-向量执行策略，以适配不同稀疏形态。
- 基于工作窃取实现跨异构核心的动态负载均衡。

## 主要结果

- 在新型 Armv9 平台上跨多种矩阵最高取得相对 SOTA SpMM 库 7.9× 的加速。
- GNN 推理案例显示端到端性能显著提升。

---

> 所属 Session：[Session 5: Stencil and Sparse Matrix Computation](index.md) · 返回 [PPoPP 2026 总览](../index.md)
