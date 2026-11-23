---
title: "Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization"
description: "ISCA 2025 · Session 4A · Oaken: 在线/离线混合KV Cache量化的高效LLM服务"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization

**中文标题：** Oaken: 在线/离线混合KV Cache量化的高效LLM服务

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Minsu Kim, Seongmin Hong, RyeoWook Ko, Soongyu Choi, Hunjong Lee, Junsoo Kim, Joo-Young Kim, Jongse Park

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731019) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Modern Large Language Model (LLM) serving system batches mul- tiple requests to achieve high throughput, while batching attention operations is challenging, rendering memory bandwidth a criti- cal bottleneck. Today, to mitigate this issue, the community relies on high-end GPUs with multiple high-bandwidth memory (HBM) channels. Unfortunately, HBM’s high bandwidth often comes at the expense of limited memory capacity, necessitating systems to scale, which reduces core utilization and increases costs. Moreover, recent advancements enabling longer contexts for LLMs have substantially increased the key-value (KV) cache size, further intensifying the pressures on memory capacity. To lower the pressure, the literature has explored KV cache quantization techniques, which commonly use low bitwidth (e.g., INT4) for most values, selectively using higher bitwidth (e.g., FP16) for outlier values. While this approach helps achieve high accuracy and low bitwidth simultaneously, it comes with the limitation that the cost for online outlier detection is excessively high, negating the advantages of quantization. Inspired by these insights, we propose Oaken, an acceleration solution that achieves high accuracy and high performance simul- taneously through co-designing algorithm and hardware. To ef- fectively find a sweet spot in the accuracy-performance trade-off space of KV cache quantization, Oaken employs an online-offline hybrid approach, setting outlier thresholds offline, which are then used to determine the quantization scale online. To translate the proposed algorithmic technique into tangible performance gains, Oaken also comes with custom quantization/dequantization en- gines and memory management units that can be integrated with any LLM accelerators. We built an Oaken accelerator on top of an LLM accelerator, LPU, and conducted a comprehensive evalu- ation. Our experiments show that for a batch size of 256, Oaken achieves up to 1.58×throughput improvement over NVIDIA A100 GPU, incurring a minimal accuracy loss of only 0.54% on average, compared to state-of-the-art KV cache quantization techniques.

## 中文摘要

现代大语言模型（LLM）服务系统对多个请求进行批处理以实现高吞吐，但注意力机制的批处理实现难度较高，使得内存带宽成为关键瓶颈。目前业界主要依靠搭载多通道高带宽内存（HBM）的高端GPU来缓解该问题。但HBM的高带宽是以容量受限为代价的，这迫使系统进行扩容，进而降低核心利用率并提升成本。此外，LLM长上下文技术的发展大幅增大了键值（KV）缓存的体积，进一步加剧内存容量压力。为缓解该压力，已有研究探索KV缓存量化技术：对大部分数值采用低位宽（如INT4），仅对异常值选择性使用高位宽（如FP16）。该方案可以同时保证较高精度与较低位宽，但在线异常检测开销过高，抵消了量化带来的收益。

基于上述问题，本文提出Oaken，一套算法与硬件协同设计的加速方案，同时兼顾高精度与高性能。为在KV缓存量化的精度-性能权衡空间中找到最优平衡点，Oaken采用在线-离线混合策略：离线确定异常阈值，再在运行时利用该阈值确定量化缩放系数。为将该算法优化转化为实际性能收益，Oaken配套专用量化/反量化引擎与内存管理单元，可集成到任意LLM加速器中。我们在LLM加速器LPU之上搭建Oaken加速器，并开展全面评测。实验表明，在批大小为256时，对比现有最优KV缓存量化方案，Oaken相比NVIDIA A100 GPU最高实现1.58倍吞吐提升，平均精度损失仅0.54%。

## 英文关键词

Accelerator, Large Language Models (LLM), Serving, Batched Inference, Quantization, Key-Value (KV) Cache

## 中文关键词

加速器, 大语言模型（LLM）, 推理服务, 批处理推理, 量化, 键值缓存（KV Cache）

## 代码与研究制品

- [代码仓库](https://github.com/casys-kaist/oaken)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731019)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
