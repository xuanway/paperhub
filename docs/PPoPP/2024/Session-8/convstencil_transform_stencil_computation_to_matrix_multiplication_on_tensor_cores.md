---
title: "ConvStencil: Transform Stencil Computation to Matrix Multiplication on Tensor Cores"
description: "PPoPP 2024 Session Optimizing for Memory：将 stencil 计算转为张量核矩阵乘，显著超越 AMOS、cuDNN 等框架"
tags:
  - "PPoPP2024"
  - "Session-8"
  - "Optimizing for Memory"
  - "Stencil Computation"
  - "Tensor Cores"
  - "Matrix Multiplication"
authors:
  - "Yuetao Chen"
  - "Kun Li"
  - "Yuhao Wang"
  - "Donglin Bai"
  - "Lei Wang"
  - "Lingxiao Ma"
  - "Liang Yuan"
  - "Yunquan Zhang"
  - "Ting Cao"
  - "Mao Yang"
session: "Session 8: Optimizing for Memory"
session_number: 8
session_chair: "Yan Gu"
date: "2024-03-05"
time: "16:10–16:30"
room: "Moorfoot"
doi: "10.1145/3627535.3638476"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
award: "Best Paper Award"
---

# ConvStencil: Transform Stencil Computation to Matrix Multiplication on Tensor Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ConvStencil 是一个将 stencil 计算转换为张量核上矩阵乘法的计算系统，先建立性能模型指导设计，再以布局变换、计算适配与冲突消除三项技术取得显著加速。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 8: Optimizing for Memory</p>
</div>

**作者**：Yuetao Chen, Kun Li, Yuhao Wang, Donglin Bai, Lei Wang, Lingxiao Ma (Microsoft Research); Liang Yuan, Yunquan Zhang (Chinese Academy of Sciences); Ting Cao, Mao Yang (Microsoft Research)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 16:10–16:30 · Session 8: Optimizing for Memory（主席：Yan Gu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638476) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

> 🏆 **Best Paper Award**

---

## 英文摘要

Tensor Core Unit (TCU) is increasingly integrated into modern high-performance processors to enhance matrix multiplication performance. However, constrained to its over-specification, its potential for improving other critical scientific operations like stencil computations remains untapped. This paper presents ConvStencil, a novel stencil computing system designed to efficiently transform stencil computation to matrix multiplication on Tensor Cores. We first develop a performance model for ConvStencil to guide algorithm design and optimization on TCUs. Based on this model, we propose three techniques: (1) Memory-efficient Layout Transformation using the stencil2row method; (2) Computation-dense Compute Adaptation with Dual Tessellation and kernel fusion; and (3) Performance-boosting Conflict Removal using a Lookup Table and Dirty Bits Padding. ConvStencil outperforms other stencil optimization frameworks, achieving significant speedups compared to solutions like AMOS, cuDNN, Brick, DRStencil, and TCStencil. By transforming stencil computation on Tensor Cores, ConvStencil promises to improve the performance of various scientific and engineering applications.

## 中文摘要

张量核单元（TCU）越来越多地被集成到现代高性能处理器中，以增强矩阵乘法性能。然而，受限于其过度特化，它在提升诸如 stencil 计算等其他关键科学运算方面的潜力仍未被发掘。本文提出 ConvStencil，一个新颖的 stencil 计算系统，旨在高效地将 stencil 计算转换为张量核上的矩阵乘法。我们首先为 ConvStencil 建立一个性能模型，以指导张量核上的算法设计与优化。基于该模型，我们提出三项技术：(1) 使用 stencil2row 方法的访存高效布局变换；(2) 采用 Dual Tessellation 与 kernel fusion 的计算密集型计算适配；(3) 使用查找表和 Dirty Bits Padding 消除冲突以提升性能。ConvStencil 优于其他 stencil 优化框架，与 AMOS、cuDNN、Brick、DRStencil 和 TCStencil 等方案相比取得了显著加速。通过在张量核上变换 stencil 计算，ConvStencil 有望提升各类科学与工程应用的性能。

## 英文关键词

Stencil Computation, Convolution, Matrix Multiplication, Tensor Cores

## 中文关键词

stencil 计算；卷积；矩阵乘法；张量核

---

## 一句话总结

> ConvStencil 是一个将 stencil 计算转换为张量核上矩阵乘法的计算系统，先建立性能模型指导设计，再以布局变换、计算适配与冲突消除三项技术取得显著加速。

## 研究问题

张量核单元（TCU）受其过度特化的限制，在提升 stencil 计算等关键科学运算性能方面的潜力仍未被发掘。

## 方法简述

- 建立 ConvStencil 的性能模型，用于指导张量核上的算法设计与优化
- 采用 stencil2row 方法实现访存高效的布局变换
- 设计 Dual Tessellation 与 kernel fusion，实现计算密集的计算适配
- 采用查找表（Lookup Table）与 Dirty Bits Padding 进行冲突消除以提升性能

## 主要结果

- 性能优于其他 stencil 优化框架，相比 AMOS、cuDNN、Brick、DRStencil 与 TCStencil 等方案取得显著加速
- 定性结论：通过在张量核上变换 stencil 计算，有望提升各类科学与工程应用的性能

---

> 所属 Session：[Session 8: Optimizing for Memory](index.md) · 返回 [PPoPP 2024 总览](../index.md)
