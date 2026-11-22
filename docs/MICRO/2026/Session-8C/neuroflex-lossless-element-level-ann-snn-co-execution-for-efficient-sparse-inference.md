---
title: "NeuroFlex: Lossless Element-Level ANN-SNN Co-Execution for Efficient Sparse Inference"
description: "MICRO 2026 · Session 8C · NeuroFlex：通过无损元素级 ANN-SNN 协同执行实现高效稀疏推理"
tags:
  - "MICRO2026"
---

# NeuroFlex: Lossless Element-Level ANN-SNN Co-Execution for Efficient Sparse Inference

**中文标题：** NeuroFlex：通过无损元素级 ANN-SNN 协同执行实现高效稀疏推理

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Varun Manjunath, Pranav Ramesh, Gopalakrishnan Srinivasan

**来源：** MICRO 2026，pp. 2991–3004；[DOI](https://doi.org/10.1109/MICRO67795.2026.00202)

## 英文摘要

Sparse DNN accelerators specialize in ANN or SNN execution, leaving energy or latency on the table when workload characteristics vary within a layer. Hybrid accelerator designs that switch modes at layer or tile granularity suffer from low PE utilization since one core type idles whenever the other is active. NeuroFlex is the first accelerator to assign every output element independently to ANN or SNN execution mode with zero accuracy loss. We extend integer-exact ANN-SNN equivalence from layers to individual output elements, thereby enabling mode switching with no conversion error. An offline cost-guided scheduler scores each element by its marginal energy-delay trade-off and packs work across PEs, achieving 97-99% PE utilization compared to 40-45% for layer-wise hybrids. NeuroFlex reduces EDP by 57-67% over a strong ANN-only baseline and delivers up to 2.5x speedup over a dual-sparse SNN-only baseline. Our cost-guided scheduler improves throughput by 16-19% over random element assignment across vision, language, and transformer workloads.

## 中文摘要

稀疏 DNN 加速器专门用于 ANN 或 SNN 执行，当工作负载特征在层内变化时，会留下能量或时延。在层或分块粒度上切换模式的混合加速器设计会遇到 PE 利用率低的问题，因为只要一种核心类型处于活动状态，另一种核心类型就会空闲。 NeuroFlex 是第一个将每个输出元素独立分配给 ANN 或 SNN 执行模式且零精度损失的加速器。我们将整数精确的 ANN-SNN 等价性从层扩展到各个输出元素，从而实现模式切换而不会出现转换错误。离线成本引导调度程序通过其边际能量时延权衡对每个元素进行评分，并在 PE 之间打包工作，实现 97-99% 的 PE 利用率，而分层混合的利用率为 40-45%。与强大的仅 ANN 基线相比，NeuroFlex 将 EDP 降低了 57-67%，并比双稀疏仅 SNN 基线提供高达 2.5 倍的加速。与跨视觉、语言和Transformer 工作负载的随机元素分配相比，我们的成本引导调度程序将吞吐量提高了 16-19%。

## 中文关键词

深度神经网络推理；人工神经网络；脉冲神经网络；混合加速器；稀疏推理

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21546571](https://doi.org/10.5281/zenodo.21546571)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
