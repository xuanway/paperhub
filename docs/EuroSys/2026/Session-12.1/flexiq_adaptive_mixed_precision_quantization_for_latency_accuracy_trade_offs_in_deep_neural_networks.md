---
title: "FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Jaemin Kim (Seoul National University), Hongjun Um (Hanyang University), Sungkyu"
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks

**中文标题：** FlexiQ：面向深度神经网络延迟/精度权衡的自适应混合精度量化

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Jaemin Kim (Seoul National University), Hongjun Um (Hanyang University), Sungkyun Kim (Hanyang University), Yongjun Park (Yonsei University), Jiwon Seo (Seoul National University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769351)

## 英文摘要

Neural networks commonly execute on hardware accelerators such as NPUs and GPUs for their size and computation overhead. These accelerators are costly and it is hard to scale their resources to handle real-time workload fluctuations.

We present FlexiQ, an adaptive mixed-precision quantization scheme for computer vision models. FlexiQ selectively applies low-bitwidth computation to feature channels with small value ranges and employs an efficient bit-lowering method to minimize quantization errors while maintaining inference accuracy. Furthermore, FlexiQ adjusts its low-bitwidth channel ratio in real time, enabling quantized models to effectively manage fluctuating inference workload.

We implemented FlexiQ prototype, including the mixed-precision inference runtime on our custom NPU and GPUs. Evaluated on eleven convolution- and transformer-based vision models, FlexiQ achieves on average 6.6% higher accuracy for 4-bit models with finetuning and outperforms four state-of-the-art quantization techniques. Moreover, our mixed-precision models achieved an efficient accuracy-latency tradeoff, with the 50% 4-bit model incurring only 0.6% accuracy loss while achieving 40% of the speedup of the 100% 4-bit model over 8-bit model. Latency evaluations on our NPU and GPUs confirmed that FlexiQ introduces minimal runtime overhead, demonstrating its hardware efficiency and overall performance benefits.

## 中文摘要

神经网络通常因其规模与计算开销而运行在 NPU、GPU 等硬件加速器上。这些加速器成本高昂，且难以通过扩展资源来应对实时负载波动。

我们提出 FlexiQ，一种面向计算机视觉模型的自适应混合精度量化方案。FlexiQ 对取值范围较小的特征通道选择性地应用低位宽计算，并采用高效的降位方法在保持推理精度的同时最小化量化误差。此外，FlexiQ 实时调整其低位宽通道比例，使量化模型能够有效应对波动的推理负载。

我们实现了 FlexiQ 原型，包括在自研 NPU 与 GPU 上的混合精度推理运行时。在 11 个基于卷积与 Transformer 的视觉模型上评估，经微调的 4-bit 模型上 FlexiQ 平均准确率高 6.6%，并优于四种最先进的量化技术。此外，我们的混合精度模型实现了高效的精度-延迟权衡：50% 4-bit 模型仅带来 0.6% 的精度损失，却获得 100% 4-bit 模型相对 8-bit 模型加速的 40%。在自研 NPU 与 GPU 上的延迟评估证实，FlexiQ 引入的运行时开销极小，体现了其硬件效率与整体性能优势。

**英文关键词：** Deep learning systems, Quantization

**中文关键词：** 深度学习系统、量化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
