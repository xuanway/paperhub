---
title: "Ecco: Improving Memory Bandwidth and Capacity for LLMs via Entropy-Aware Cache Compression"
description: "ISCA 2025 · Session 5B · Ecco：通过熵感知缓存压缩提升 LLM 的内存带宽与容量"
tags:
  - "ISCA2025"
  - "Session 5B"
  - "HPC for ML/AI"
---

# Ecco: Improving Memory Bandwidth and Capacity for LLMs via Entropy-Aware Cache Compression

**中文标题：** Ecco：通过熵感知缓存压缩提升 LLM 的内存带宽与容量

**所属 Session：** [Session 5B](index.md) · [ISCA 2025](../index.md)

**作者：** Feng Cheng, Cong Guo, Chiyue Wei, Junyao Zhang, Changchun Zhou, Edward Hanson, Jiaqi Zhang, Xiaoxiao Liu, Hai "Helen" Li, Yiran Chen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731024) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large language models (LLMs) have demonstrated transformative capabilities across diverse artificial intelligence applications, yet their deployment is hindered by substantial memory and computa- tional demands, especially in resource-constrained environments. Quantization techniques have emerged as a critical solution, re- ducing data precision to enhance memory and computational effi- ciency. However, existing methods often suffer from high runtime overheads and potential accuracy degradation. To address these challenges, we propose Ecco, an entropy-based cache compression technique tailored for LLMs. Ecco combines group-wise and non- uniform quantization with pre-defined shared k-means patterns and Huffman coding to exploit the inherent entropy characteristics of LLM cache data. Recognizing the inefficiencies of traditional Huffman coding in terms of parallelism and latency, we introduce a novel parallel Huffman-based decoding process with a multi-stage pipeline design, reducing latency by two orders of magnitude and achieving throughput comparable to GPU L2 caches. Comprehen- sive evaluations demonstrate that Ecco achieves an up to 2.9×and 1.9×speedup over the state-of-the-art AWQ and SmoothQuant framework, 2.4×over the Olive accelerator, all while increasing memory capacity by nearly 4×and maintaining state-of-the-art LLM accuracy. These results underscore the effectiveness of our entropy-based cache compression in enhancing LLM performance and efficiency, paving the way for more deployable large-scale AI models.

## 中文摘要

大语言模型（LLM）在各类人工智能应用中展现出变革性能力，但其部署受巨大内存与计算开销制约，在资源受限环境下尤为突出。量化技术是关键解决方案，通过降低数据精度提升内存与计算能效。但现有量化方案通常运行时开销高，还可能带来精度损失。针对这些问题，本文提出Ecco，一种面向LLM、基于熵的缓存压缩技术。Ecco结合分组非均匀量化、预定义共享k-means模式与哈夫曼编码，挖掘LLM缓存数据本身的熵特征。
传统哈夫曼编码并行度差、延迟高，为此本文设计一种新型并行哈夫曼解码流水线，采用多级流水结构，将延迟降低两个数量级，吞吐可以媲美GPU L2缓存。大量评测表明：对比前沿AWQ、SmoothQuant框架，Ecco最高提速2.9倍、1.9倍；对比Olive加速器提速2.4倍；同时内存容量提升近4倍，并且保持大模型的高精度。该结果证明这种基于熵的缓存压缩方案可以有效提升LLM性能与能效，为大规模AI模型落地提供支撑。

## 英文关键词

Cache Compression, Entropy Coding, GPUs, Information Entropy, Large Language Models, Memory Systems

## 中文关键词

缓存压缩, 熵编码, GPU, 信息熵, 大语言模型, 内存系统

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731024)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2025](../index.md)
