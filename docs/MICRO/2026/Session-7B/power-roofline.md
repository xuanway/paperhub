---
title: "Power Roofline"
description: "MICRO 2026 · Session 7B · 功率屋顶线模型"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# Power Roofline

**中文标题：** 功率屋顶线模型

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Michael Jaemin Kim, Doe Hyun Yoon, Jovan Stojkovic, Gefei Zuo, Jong Bin Lim, Harsha Jagannati, Zhan Shu, Shobhit Kanaujia

**来源：** MICRO 2026，pp. 2438–2451；[DOI](https://doi.org/10.1109/MICRO67795.2026.00167)

## 英文摘要

Modern AI accelerators increasingly operate at their power limits, creating a widening gap between peak and attainable performance. On the other hand, the Roofline model, while widely adopted for reasoning about compute and memory bottlenecks, provides little insight when power is the binding constraint. To address this challenge, we propose Power Roofline, an extension that replaces operational intensity (ops/byte) with energy efficiency (ops/Joule), directly capturing how power budgets limit attainable performance. The model naturally generalizes to a 3D formulation that unifies compute, memory, and power bounds. We apply Power Roofline to GEMM and attention kernels across multiple generations of GPUs and uncover several insights that the conventional Roofline cannot express. First, we show that input data values affect energy efficiency and, consequently, throughput under power caps. Second, we identify an energy-efficiency optimal operating point, below the maximum TDP, due to the interplay between static power and voltage scaling. Third, we demonstrate that power excursion during short profiling runs can mislead kernel auto-tuning, causing it to select configurations that underperform under sustained operation. Finally, guided by Power Roofline, we optimize a decode attention kernel by eliminating wasted computation, improving performance under power-constrained settings by up to 19.2%. Together, these results show that energy efficiency is becoming a first-order performance metric for power-limited accelerators, and Power Roofline offers a practical lens to reason about it.

## 中文摘要

现代人工智能加速器越来越多地在功率极限下运行，导致峰值性能与可达到的性能之间的差距越来越大。另一方面，Roofline 模型虽然广泛用于计算和内存瓶颈的推理，但当功率是约束条件时，它提供的洞察力很少。为了应对这一挑战，我们提出了 Power Roofline，这是一种用能效（操作/焦耳）代替操作强度（操作/字节）的扩展，直接捕获功率预算如何限制可达到的性能。该模型自然地推广为统一计算、内存和功率范围的 3D 公式。我们将 Power Roofline 应用于多代 GPU 上的 GEMM 和注意力内核，并揭示了传统 Roofline 无法表达的一些见解。首先，我们表明输入数据值会影响能效，从而影响功率上限下的吞吐量。其次，由于静态功耗和电压缩放之间的相互作用，我们确定了低于最大 TDP 的能效最佳工作点。第三，我们证明短时间分析运行期间的功率偏移可能会误导内核自动调整，导致其选择在持续运行下表现不佳的配置。最后，在 Power Roofline 的指导下，我们通过消除浪费的计算来优化解码注意力内核，将功耗受限设置下的性能提高高达 19.2%。总之，这些结果表明，能效正在成为功率有限的加速器的首要性能指标，而 Power Roofline 提供了一个实用的镜头来解释它。

## 中文关键词

功耗 Roofline 模型；图形处理器；能效；动态电压频率调节

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
