---
title: "VQVLA: Motion-Aware Vector Quantization with Computation Fusion for VLA Acceleration"
description: "MICRO 2026 · Session 8C · VQVLA：通过运动感知向量量化与计算融合加速 VLA"
tags:
  - "MICRO2026"
  - "Quantization"
---

# VQVLA: Motion-Aware Vector Quantization with Computation Fusion for VLA Acceleration

**中文标题：** VQVLA：通过运动感知向量量化与计算融合加速 VLA

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan

**来源：** MICRO 2026，pp. 3005–3019；[DOI](https://doi.org/10.1109/MICRO67795.2026.00203)

## 英文摘要

Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited. In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution dynamics. We first introduce MotionVQ, a motion-aware vector quantization scheme that dynamically adjusts quantization precision based on the robot execution state, reducing memory access while preserving task success rate. We then propose a merged-centroid vectorized GEMM paradigm that operates on the codebook-index representation, eliminating redundant multiplications through spatial aggregation and temporal reuse of centroids. To realize these optimizations, we design an accelerator that efficiently supports dynamic precision selection and centroid-reuse computation. Experimental results show that VQVLA achieves 6.5x, 2.8x, 1.9x, 3.3x, and 4.3x speedup over the A100 GPU, Dadu-Corki, LUT-DLA, CodeGEMM, and ShiftAddLLM, respectively, with negligible accuracy degradation.

## 中文摘要

视觉-语言-动作 (VLA) 模型已经展示了嵌入式 AI 的强大潜力，但它们在 GPU 上的高推理时延限制了实时部署。现有的加速器（例如 Dadu-Corki）提高了效率，但将 VLA 模型视为全精度工作负载，从而导致内存和计算中的大量冗余未得到充分利用。在本文中，我们提出了 VQVLA，这是一种算法-硬件协同设计框架，可通过利用权重相似性和执行动态来加速 VLA 推理。我们首先介绍 MotionVQ，这是一种运动感知矢量量化方案，可根据机器人执行状态动态调整量化精度，减少内存访问，同时保持任务成功率。然后，我们提出了一种合并质心矢量化 GEMM 范例，该范例在码本索引表示上运行，通过质心的空间聚合和时间重用消除冗余乘法。为了实现这些优化，我们设计了一个加速器，可以有效支持动态精度选择和质心重用计算。实验结果表明，与 A100 GPU、Dadu-Corki、LUT-DLA、CodeGEMM 和 ShiftAddLLM 相比，VQVLA 分别实现了 6.5 倍、2.8 倍、1.9 倍、3.3 倍和 4.3 倍的加速，且精度下降可以忽略不计。

## 中文关键词

视觉语言动作模型；向量量化；加速器；运动感知；计算融合

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
