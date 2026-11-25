---
title: "A Portable, Fast, DCT-based Compressor for AI Accelerators"
description: "HPDC 2024 · Session 1 — Compression and AI"
tags:
  - "HPDC2024"
  - "Session 1"
  - "Compression and AI"
---

# A Portable, Fast, DCT-based Compressor for AI Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 1</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658662)

**作者**：Milan Shah, Xiaodong Yu, Sheng Di, Michela Becchi, Franck Cappello

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）

---

## 英文摘要

Lossy compression can be an effective tool in AI training and inference to reduce memory requirements, storage footprint, and in some cases, execution time. With the rise of novel architectures designed to accelerate AI workloads, compression can continue to serve these purposes, but must be adapted to the new accelerators. Due to programmability and architectural differences, existing lossy compressors cannot be directly ported to and are not optimized for any AI accelerator, thus requiring new compression designs. In this paper, we propose a novel, portable, DCT-based lossy compressor that can be used across a variety of AI accelerators. More specifically, we make the following contributions: 1) We propose a DCT-based lossy compressor design for training data that uses operators supported across four state-of-the-art AI accelerators: Cerebras CS-2, SambaNova SN30, Groq GroqChip, and Graphcore IPU. 2) We design two optimization techniques to allow for higher resolution compressed data on certain platforms and improved compression ratio on the IPU. 3) We evaluate our compressor’s ability to preserve accuracy on four benchmarks, three of which are AI for science benchmarks going beyond image classification. Our experiments show that accuracy degradation can be limited to 3% or less, and sometimes, compression improves accuracy. 4) We study compression/decompression time as a function of resolution and batch size, finding that our compressor can achieve throughputs on the scale of tens of GB/s, depending on the platform.

## 中文摘要

有损压缩可作为 AI 训练与推理中的有效工具，用于降低内存需求、存储占用，在某些情况下还能缩短执行时间。随着专为加速 AI 负载而设计的新型架构兴起，压缩仍可发挥这些作用，但必须适配新的加速器。由于可编程性与架构差异，现有有损压缩器无法直接移植到任何 AI 加速器，也未经针对其优化，因此需要新的压缩设计。本文提出一种新颖、可移植、基于 DCT 的有损压缩器，可跨多种 AI 加速器使用。更具体地说，我们的贡献如下：1) 我们提出一种面向训练数据的基于 DCT 的有损压缩器设计，其使用的算子受四种最先进 AI 加速器支持：Cerebras CS-2、SambaNova SN30、Groq GroqChip 和 Graphcore IPU。2) 我们设计两种优化技术，以在某些平台上获得更高分辨率的压缩数据，并在 IPU 上提升压缩比。3) 我们在四个基准上评估压缩器保持精度的能力，其中三个是超越图像分类的 AI for Science 基准。实验表明，精度下降可限制在 3% 以内，有时压缩甚至能提升精度。4) 我们研究了压缩/解压时间随分辨率与批大小的变化，发现压缩器可实现数十 GB/s 量级的吞吐，具体取决于平台。

## 英文关键词

Compression, AI accelerator, ML training

## 中文关键词

压缩，AI 加速器，ML 训练

---

[← 返回 Session 1 — Compression and AI](index.md)
