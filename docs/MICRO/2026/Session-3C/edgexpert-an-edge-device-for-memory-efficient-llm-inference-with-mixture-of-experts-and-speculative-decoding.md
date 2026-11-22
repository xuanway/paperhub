---
title: "EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding"
description: "MICRO 2026 · Session 3C · EdgeXpert：融合混合专家模型与推测解码的内存高效 LLM 推理边缘设备"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding

**中文标题：** EdgeXpert：融合混合专家模型与推测解码的内存高效 LLM 推理边缘设备

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Sangwoo Ha, Hyunwoo Seo, Yurim Jo, Youngjin Moon, Hoi-Jun Yoo

**来源：** MICRO 2026，pp. 1150–1165；[DOI](https://doi.org/10.1109/MICRO67795.2026.00089)

## 英文摘要

On-device deployment of Large Language Models (LLMs) has become essential for personalized edge applications. A primary bottleneck is external memory access (EMA) in feed-forward network (FFN) layers. Speculative decoding and mixture-of-experts (MoE) are promising solutions. Speculative decoding reduces the number of decoding stages by generating multiple tokens per stage, and MoE minimizes per-stage cost through sparse expert activation. However, there is an incompatibility when combining these two techniques. We propose EdgeXpert, a software-hardware co-designed LLM accelerator that resolves this incompatibility. In the prefill stage, the prompt-wise expert reuse reformulates routing as prompt-level expert reuse rather than independent per-token expert selection. It identifies important tokens using a lightweight encoder, constructs a shared expert set from them, and routes less important tokens with a reduced expert budget to lower expert EMA. In the decode stage, depth-aware expert coalescing exploits the contextual similarity and mutual exclusivity of same-depth candidate tokens. Rather than loading the union of all required channels, EdgeXpert loads only salient channels and applies computational calibration to recover accuracy without additional memory access. Synthesized in Samsung 28nm technology at 800 MHz, EdgeXpert achieves up to 56.3% latency reduction and 44.1% energy reduction compared to prior works, while maintaining near-baseline accuracy.

## 中文摘要

大语言模型 (LLM) 的设备上部署对于个性化边缘应用程序至关重要。主要瓶颈是前馈网络（FFN）层中的外部存储器访问（EMA）。推测性解码和专家混合 (MoE) 是有前途的解决方案。推测性解码通过在每个阶段生成多个词元来减少解码阶段的数量，而 MoE 通过稀疏专家激活来最小化每个阶段的成本。然而，结合这两种技术时存在不兼容性。我们提出了 EdgeXpert，这是一种软件-硬件共同设计的 LLM 加速器，可以解决这种不兼容性。在预填充阶段，提示级专家重用将路由重新制定为提示级专家重用，而不是独立的每个词元专家选择。它使用轻量级编码器识别重要词元，从中构建共享专家集，并将专家预算减少的不太重要的词元路由到较低的专家 EMA。在解码阶段，深度感知专家合并利用相同深度候选标记的上下文相似性和互斥性。 EdgeXpert 不加载所有所需通道的并集，而是仅加载显着通道并应用计算校准来恢复精度，而无需额外的内存访问。 EdgeXpert 采用 800 MHz 频率下的三星 28 纳米技术进行合成，与之前的作品相比，时延降低高达 56.3%，能耗降低 44.1%，同时保持接近基线的精度。

## 中文关键词

边缘设备；大语言模型；混合专家模型；推测解码；内存优化

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21481269](https://doi.org/10.5281/zenodo.21481269)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
