---
title: "SCOPE: Array-Native Nonlinear Acceleration for LLM Inference via Shape-Constrained Neural Approximation"
description: "MICRO 2026 · Session 8C · SCOPE：通过形状约束神经近似实现 LLM 推理的阵列原生非线性加速"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "LLM Training"
  - "Neural Networks"
---

# SCOPE: Array-Native Nonlinear Acceleration for LLM Inference via Shape-Constrained Neural Approximation

**中文标题：** SCOPE：通过形状约束神经近似实现 LLM 推理的阵列原生非线性加速

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Chenyu Zhang, Chenxi Xu, Jiaxiang Zou, Yonghao Chen, Xinyu Chen

**来源：** MICRO 2026，pp. 2956–2972；[DOI](https://doi.org/10.1109/MICRO67795.2026.00200)

## 英文摘要

Nonlinear operators increasingly bottleneck large language model (LLM) inference as low-precision GEMMs accelerate while nonlinear functions remain on separate scalar, vector, or special-function units. Existing solutions struggle to combine broad operator support, approximation fidelity, and scalable hardware efficiency. We present SCOPE, a software-hardware co-design for array-native nonlinear evaluation. Its shape-constrained neural approximator (SCNA) encodes structural priors in a compact one-hidden-layer ReLU network. A lightweight systolic-array extension executes SCNA directly, while a scale-fused dataflow integrates it with statically quantized GEMMs. Across 11 nonlinear functions, SCNA-16 reduces geometric-mean approximation MSE by 356 times over reported NN-LUT values on 11 functions and 14.9 times over reported T-LUT values on nine functions. Across five LLMs, SCNA-8 maintains BF16/INT8 perplexity and zero-shot accuracy with limited additional degradation. In compute-focused simulations, SCOPE achieves up to 2.81 times INT8 long-context attention speedup over FlashAttention on TPUv6e and up to 2.69 times INT8 full-prefill speedup on B200 in the 512K-context extrapolation. SCNA-8 also lowers throughput-normalized incremental area and power overhead by 12.8 times and 9.5 times, respectively, compared with prior nonlinear accelerators. The code is open-sourced on GitHub.

## 中文摘要

随着低精度 GEMM 加速，而非线性函数仍保留在单独的标量、向量或特殊函数单元上，非线性算子日益成为大语言模型 (LLM) 推理的瓶颈。现有的解决方案很难将广泛的算子支持、近似保真度和可扩展的硬件效率结合起来。我们推出了 SCOPE，一种用于阵列原生非线性评估的软硬件协同设计。其形状约束神经逼近器 (SCNA) 在紧凑的单隐藏层 ReLU 网络中编码结构先验。轻量级脉动阵列扩展直接执行 SCNA，而尺度融合数据流将其与静态量化 GEMM 集成。在 11 个非线性函数上，相比已报告的 NN-LUT 结果，SCNA-16 的近似均方误差（MSE）几何平均值降至其 1/356；在九个函数上，相比已报告的 T-LUT 结果，该值降至其 1/14.9。在五个大语言模型中，SCNA-8 保持了 BF16/INT8 困惑度和零样本精度，且额外降级有限。在以计算为中心的模拟中，SCOPE 在 TPUv6e 上实现了比 FlashAttention 高达 2.81 倍的 INT8 长上下文注意力加速，在 512K 上下文外推中在 B200 上实现了高达 2.69 倍的 INT8 全预填充加速。与之前的非线性加速器相比，SCNA-8 还将吞吐量归一化增量面积和功率开销分别降低了 12.8 倍和 9.5 倍。该代码在 GitHub 上开源。

## 中文关键词

大语言模型推理；非线性运算加速；形状约束神经近似；阵列原生计算

## 代码与研究制品

- 代码仓库：[https://github.com/CLab-HKUST-GZ/SCOPE-MICRO26-AE](https://github.com/CLab-HKUST-GZ/SCOPE-MICRO26-AE)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
