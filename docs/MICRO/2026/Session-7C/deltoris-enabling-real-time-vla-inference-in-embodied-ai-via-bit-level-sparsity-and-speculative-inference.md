---
title: "Deltoris: Enabling Real-Time VLA Inference in Embodied AI via Bit-Level Sparsity and Speculative Inference"
description: "MICRO 2026 · Session 7C · Deltoris：通过比特级稀疏性与推测推理实现具身 AI 的实时 VLA 推理"
tags:
  - "MICRO2026"
---

# Deltoris: Enabling Real-Time VLA Inference in Embodied AI via Bit-Level Sparsity and Speculative Inference

**中文标题：** Deltoris：通过比特级稀疏性与推测推理实现具身 AI 的实时 VLA 推理

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Zheng Liu, Zeyu Guo, Zihan Liu, Anbang Wu, Han Zhao, Fangxin Liu, Zhezhi He, Yinhe Han, Jingwen Leng, Minyi Guo, Yiming Gan, Yu Feng

**来源：** MICRO 2026，pp. 2559–2576；[DOI](https://doi.org/10.1109/MICRO67795.2026.00175)

## 英文摘要

Vision-language-action (VLA) models have emerged as a key component in embodied AI. Among existing approaches, diffusion-based VLA models achieve superior motion quality and generalization. However, diffusion-based VLA models are compute-intensive and must run at high control frequency, e.g., 50-200 Hz. Thus, this imposes strict latency and energy constraints on edge devices. In this work, we present Deltoris, an algorithm-hardware co-design framework for efficient diffusion-based VLA inference. First, we exploit the temporal similarity of consecutive inputs and propose a temporal-aware bit-sparsity algorithm that computes only the differences between consecutive inputs, eliminating redundant bit-level operations. To further address the extra off-chip traffic introduced by our algorithm, we propose a speculative inference technique, which amortizes data loading across multiple control steps. Lastly, to support these techniques, we co-design a dedicated accelerator with customized 1D systolic bit-serial PE arrays that eliminate PE workload imbalance. Our evaluation shows that Deltoris achieves up to 34.2x speedup over mobile GPUs and 6.1x over prior accelerators, while maintaining comparable accuracy.

## 中文摘要

视觉-语言-动作（VLA）模型已成为具身人工智能的关键组成部分。在现有方法中，基于扩散的 VLA 模型实现了卓越的运动质量和泛化。然而，基于扩散的 VLA 模型是计算密集型的，并且必须以高控制频率运行，例如 50-200 Hz。因此，这对边缘设备施加了严格的时延和能量限制。在这项工作中，我们提出了 Deltoris，一种算法-硬件协同设计框架，用于高效的基于扩散的 VLA 推理。首先，我们利用连续输入的时间相似性，并提出一种时间感知的位稀疏算法，该算法仅计算连续输入之间的差异，从而消除冗余的位级操作。为了进一步解决我们的算法引入的额外片外流量，我们提出了一种推测推理技术，该技术可以跨多个控制步骤分摊数据加载。最后，为了支持这些技术，我们与定制的一维脉动位串行 PE 阵列共同设计了专用加速器，以消除 PE 工作负载不平衡。我们的评估表明，Deltoris 的速度比移动 GPU 提高了 34.2 倍，比之前的加速器提高了 6.1 倍，同时保持了相当的精度。

## 中文关键词

视觉语言动作模型；世界动作模型；算法与硬件协同设计；比特级稀疏性；推测推理

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
