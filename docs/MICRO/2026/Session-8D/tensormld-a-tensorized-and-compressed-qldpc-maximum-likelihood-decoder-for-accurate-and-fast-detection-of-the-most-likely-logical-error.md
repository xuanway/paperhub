---
title: "TensorMLD: A Tensorized and Compressed qLDPC Maximum-Likelihood Decoder for Accurate and Fast Detection of the Most Likely Logical Error"
description: "MICRO 2026 · Session 8D · TensorMLD：通过张量化与压缩 qLDPC 最大似然解码器，准确快速地检测最可能的逻辑错误"
tags:
  - "MICRO2026"
  - "Quantum Computing"
---

# TensorMLD: A Tensorized and Compressed qLDPC Maximum-Likelihood Decoder for Accurate and Fast Detection of the Most Likely Logical Error

**中文标题：** TensorMLD：通过张量化与压缩 qLDPC 最大似然解码器，准确快速地检测最可能的逻辑错误

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Liqiang Lu, Debin Xiang, Kaiwen Zhou, Boyu Jin, Chenning Tao, Wuwei Tian, Anbang Wu, Fangxin Liu, Jingwen Leng, Minyi Guo, Jianwei Yin

**来源：** MICRO 2026，pp. 3102–3116；[DOI](https://doi.org/10.1109/MICRO67795.2026.00209)

## 英文摘要

Quantum error correction is vital for building reliable quantum computers, and quantum Low Density Parity Check (qLDPC) codes are highly promising due to their efficient encoding. However, current decoders often struggle with low decoding accuracy. This is because they focus on identifying physical errors, which cannot always correct the underlying logical fault. While maximum likelihood decoding offers optimal performance by identifying the most likely logical error, its application to qLDPC codes is computationally prohibitive, largely due to the high-dimensional encoding between the logical and physical error spaces. We introduce TensorMLD, an efficient MLD decoder that overcomes this barrier. Our key innovation maps decoding into a spin glass model computable via tensor networks. We then compress this representation through tensor decomposition and offline compression, reducing peak memory requirements by up to 16 orders of magnitude and computational workload by up to 17 orders of magnitude. For practical decoding, we develop a parallel marginal probability strategy equipped with GPU and FPGA accelerators that enables efficient decoding with the compressed tensors. Experiments demonstrate that TensorMLD achieves an average 9.07 times lower logical error rate than the state-of-the-art RelayBP decoder while maintaining comparable latency.

## 中文摘要

量子纠错对于构建可靠的量子计算机至关重要，而量子低密度奇偶校验（qLDPC）码由于其高效的编码而非常有前途。然而，当前的解码器常常面临解码精度低的问题。这是因为他们专注于识别物理错误，而无法始终纠正潜在的逻辑错误。虽然最大似然解码通过识别最可能的逻辑错误来提供最佳性能，但其在 qLDPC 码中的应用在计算上是令人望而却步的，这主要是由于逻辑和物理错误空间之间的高维编码。我们推出 TensorMLD，这是一种克服这一障碍的高效 MLD 解码器。我们的关键创新将解码映射到可通过张量网络计算的自旋玻璃模型。然后，我们通过张量分解和离线压缩来压缩这种表示，将峰值内存需求减少多达 16 个数量级，并将计算工作量减少多达 17 个数量级。对于实际解码，我们开发了一种配备 GPU 和 FPGA 加速器的并行边际概率策略，可以使用压缩张量进行高效解码。实验表明，TensorMLD 的逻辑错误率比最先进的 RelayBP 解码器平均低 9.07 倍，同时保持相当的时延。

## 中文关键词

量子纠错；量子低密度奇偶校验码；最大似然译码；张量网络；张量压缩

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
