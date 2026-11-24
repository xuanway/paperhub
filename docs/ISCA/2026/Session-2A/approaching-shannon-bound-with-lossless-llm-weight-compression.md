---
title: "Approaching Shannon Bound with Lossless LLM Weight Compression"
description: "ISCA 2026 · Session 2A · Approaching Shannon Bound with Lossless LLM Weight Compression"
tags:
  - "ISCA2026"
  - "Session 2A"
  - "LLM 1"
---

# Approaching Shannon Bound with Lossless LLM Weight Compression

**中文标题：** 逼近香农极限的无损 LLM 权重压缩

**所属 Session：** [Session 2A](index.md) · [ISCA 2026](../index.md)

**作者：** Hongshi Tan, Yao Chen, Gustavo Alonso, Weng-Fai Wong, Bingsheng He

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large language models (LLMs) now scale to trillions of parameters, driving weight storage into the terabyte regime and creating an acute mismatch with GPU memory capacity. Although lossless compression is widely effective in other domains, it remains underutilized in LLM systems. Through a comprehensive entropy study across models from 1.5B to 405B parameters and numeric formats ranging from bf16 to int4 and AWQ/SQ8, we find that LLM weights contain far less intrinsic randomness than their stored bitwidth implies, their effective entropy is 2–10× lower, indicating that up to a 10× footprint reduction is theoretically achievable without altering any weight values. Leveraging this insight, we introduce a tile-level, on-the-fly lossless decompression framework based on Asymmetric Numeral Systems that aligns decoding with the GEMM tiling pattern of GPU inference. Our design achieves bit-rates within 0.01–0.1 bits of the Shannon limit across a wide range of LLM numerical formats, demonstrating that nearly all statistical redundancy is eliminated. Integrated into the SGLang serving framework with multi-GPU support, our approach increases the maximum batch size of Qwen-14B from 47 to 75, improving throughput by up to 1.2×. On Mixtral-176B, the feasible batch size increases from 20 to 95 (4.8×), yielding up to 1.6× throughput improvement. Compared to state-of-the-art lossless compression approaches NeuZip and DFloat11, our design further improves throughput by up to 11×.

## 中文摘要

大语言模型（LLM）现已扩展至万亿参数规模，导致权重存储进入太字节级别，与 GPU 内存容量形成严重不匹配。尽管无损压缩在其他领域广泛有效，但在 LLM 系统中仍未得到充分利用。通过对从 1.5B 到 405B 参数模型以及从 bf16 到 int4 及 AWQ/SQ8 等多种数值格式的全面熵研究，我们发现 LLM 权重的固有随机性远低于其存储位宽所暗示的水平，有效熵低 2–10 倍，这意味着在不改变任何权重值的情况下，理论上可实现高达 10 倍的存储压缩。基于这一发现，我们提出了一种基于非对称数系（ANS）的瓦片级即时无损解压框架，将解码过程与 GPU 推理的 GEMM 分块模式对齐。我们的设计在多种 LLM 数值格式下实现了距离香农极限仅 0.01–0.1 比特的码率，表明几乎消除了所有统计冗余。集成到支持多 GPU 的 SGLang 推理框架后，我们的方法将 Qwen-14B 的最大批量大小从 47 提升至 75，吞吐量提升高达 1.2×。在 Mixtral-176B 上，可行批量大小从 20 提升至 95（提升 4.8×），吞吐量提升高达 1.6×。与最先进的无损压缩方法 NeuZip 和 DFloat11 相比，我们的设计吞吐量提升高达 11×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2026](../index.md)
