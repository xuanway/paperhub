---
title: "Despoina: Depth-Amortized Incremental Inference for Deep Dynamic GNN Acceleration"
description: "MICRO 2026 · Session 8C · Despoina：面向深层动态图神经网络加速的深度摊销增量推理"
tags:
  - "MICRO2026"
  - "Graph Processing"
---

# Despoina: Depth-Amortized Incremental Inference for Deep Dynamic GNN Acceleration

**中文标题：** Despoina：面向深层动态图神经网络加速的深度摊销增量推理

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Yujin Lee, Minsu Jang, Ji-Hoon Kim, Tony Tae-Hyoung Kim

**来源：** MICRO 2026，pp. 2940–2955；[DOI](https://doi.org/10.1109/MICRO67795.2026.00199)

## 英文摘要

Dynamic graph neural networks (DGNNs) are deployed in latency-sensitive applications that require both temporal update awareness and multi-hop relational reasoning. We identify depth-scaling failure as a key systems bottleneck: prior accelerators handle incremental updates efficiently at shallow depths, but permit the affected region to grow with depth, causing end-to-end cost to scale poorly in the deep regime that real applications require but current hardware cannot sustain. This paper presents Despoina, a deep DGNN accelerator built around a simple observation that explains depth-scaling failure: as depth increases, an update can reach many rows through graph connectivity, but only a much smaller subset produces changes large enough to influence later layers. Despoina makes this surviving subset of rows, rather than all reachable rows, the unit of work. It combines exact changed-row computation, propagation scoping, and a heterogeneous sparse-to-dense datapath so that the shrinking runtime workload translates into end-to-end latency and energy savings. Together, these mechanisms make incremental execution scale nearly flat with depth. Evaluated on five benchmarks spanning 1.9K–2.3M nodes and 2–5 layers, Despoina outperforms the evaluated analytical baseline models. At 5L, its geomean latency speedup and supported-component energy-efficiency gain are 28.6×/45.1×, 35.8×45.1×, and 41.9×52.5× over I-DGNN, RACE, and Cambricon-DG (CDG), respectively. At 3L, the corresponding gains are 18.0×30.1×, 24.0×28.4×, and 25.8×30.9×. From 3L to 5L, Despoina's own cost grows by only 1.13×, while I-DGNN continues to rise from 4L onward. From L3 onward, the geomean propagating-row fraction remains below 1% under τ*. At 5L, Despoina remains near-lossless versus golden FP32, with |ΔAverage Precision (AP)| ≤ 0.03 pp, |ΔHits@20| ≤ 0.04 pp, and cosine similarity (CosSim) ≥ 0.99978.

## 中文摘要

动态图神经网络 (DGNN) 部署在需要时间更新感知和多跳关系推理的时延敏感应用中。我们认为深度扩展失败是一个关键的系统瓶颈：以前的加速器可以在浅深度有效地处理增量更新，但允许受影响的区域随着深度的增加而增长，导致端到端成本在实际应用程序需要但当前硬件无法承受的深度范围内扩展得很差。本文介绍了 Despoina，这是一个围绕简单观察构建的深度 DGNN 加速器，它解释了深度缩放失败：随着深度的增加，更新可以通过图连接到达许多行，但只有较小的子集会产生足够大的变化，足以影响后面的层。 Despoina 将这个幸存的行子集（而不是所有可到达的行）作为工作单元。它结合了精确的更改行计算、传播范围和异构稀疏到密集数据路径，以便减少运行时工作负载转化为端到端时延和节能。这些机制共同使得增量执行的规模与深度几乎持平。经过对涵盖 1.9K-2.3M 节点和 2-5 层的五个基准进行评估，Despoina 的性能优于评估的分析基线模型。在 5L 时，与 I-DGNN、RACE 和 Cambricon-DG (CDG) 相比，其几何平均时延加速和支持组件能效增益分别为 28.6×/45.1×、35.8×45.1× 和 41.9×52.5×。在3L时，相应的增益为18.0×30.1×、24.0×28.4×和25.8×30.9×。从3L到5L，Despoina自身的成本仅增长了1.13倍，而I-DGNN从4L开始持续上升。从 L3 开始，几何平均传播行分数在 τ* 下保持在 1% 以下。在 5L 时，Despoina 与黄金 FP32 相比仍然接近无损，具有 |Δ平均精度 (AP)| ≤ 0.03 pp, |ΔHits@20| ≤ 0.04 pp，余弦相似度 (CosSim) ≥ 0.99978。

## 中文关键词

动态图神经网络加速；存内计算；图神经网络；增量推理；硬件加速器

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21510101](https://doi.org/10.5281/zenodo.21510101)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
