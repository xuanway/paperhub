---
title: "Adyna: Accelerating Dynamic Neural Networks with Adaptive Scheduling"
description: "HPCA 2025 · Stacking the Layers"
tags:
  - "HPCA2025"
  - "Stacking the Layers"
---

# Adyna: Accelerating Dynamic Neural Networks with Adaptive Scheduling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers</p>
</div>

**论文链接**：
**作者**：Zhiyao Li (Tsinghua University), Bohan Yang (University of Science and Technology of China), Jiaxiang Li (University of Toronto), Taijie Chen (Tsinghua University), Xintong Li (Tsinghua University), Mingyu Gao (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

Adyna：以自适应调度加速动态神经网络

## 英文摘要

Dynamic architecture neural networks (DynNNs) are an emerging type of deep learning models that can leverage different processing difficulties of data samples to dynamically reduce computation demands at runtime. However, current GPUs and specialized accelerators lack the necessary architecture and dataflow support to achieve the promised theoretical efficiency improvements due to the high dynamism in DynNN execution. We propose Adyna, a novel hardware-software co-design solution to efficiently support DynNN inference. Adyna uses a unified representation to capture most existing DynNNs to enable a general design. It features a dynamism-aware, multi-kernel selection paradigm, in which the dataflow scheduler makes resource allocation decisions according to the distribution of dynamic size values, and the hardware architecture keeps multiple precompiled kernels and selects the best matching one to process each specific data sample according to its dynamic size. Adyna further uses an effective kernel sampling algorithm to carefully choose the set of kernels to load onto the hardware. Evaluated on various DynNN models, Adyna can outperform state-of-the-art multi-tile and multi-tenant accelerators by 1.70× and 1.57× on average, and up to 2.32× and 2.01×.

## 中文摘要

动态架构神经网络（DynNN）是一类新兴的深度学习模型，可利用不同数据样本的处理难度差异在运行时动态降低计算需求。然而由于 DynNN 执行的高度动态性，现有 GPU 与专用加速器缺乏必要的架构与数据流支持，无法实现其所承诺的理论效率提升。我们提出 Adyna，一种新颖的软硬件协同设计解决方案，用于高效支持 DynNN 推理。Adyna 用统一表示刻画大多数现有 DynNN，以实现通用设计。它采用动态性感知的多核选择范式：数据流调度器依据动态尺寸值的分布做出资源分配决策，硬件架构则保留多个预编译内核，并根据每个数据样本的动态尺寸选择最匹配者进行处理。Adyna 还使用有效的内核采样算法来谨慎选择加载到硬件上的内核集合。在多种 DynNN 模型上评估，Adyna 平均分别比最先进的多 tile 与多租户加速器快 1.70× 和 1.57×，最高达 2.32× 和 2.01×。
