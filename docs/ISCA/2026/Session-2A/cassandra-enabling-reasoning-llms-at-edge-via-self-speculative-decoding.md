---
title: "Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding"
description: "ISCA 2026 · Session 2A · Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding"
tags:
  - "ISCA2026"
  - "Session 2A"
  - "LLM 1"
---

# Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding

**中文标题：** Cassandra: 通过自推测解码在边缘端实现推理 LLM

**所属 Session：** [Session 2A](index.md) · [ISCA 2026](../index.md)

**作者：** Soongyu Choi, Yuntae Kim, Muyoung Son, Joo-Young Kim

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Speculative decoding has emerged as a promising lossless approach to accelerating Large Language Models (LLMs). Recently, as the overhead of the decode stage has increased in reasoning LLMs, while algorithmic approximations cause significant accuracy degradation, lossless acceleration through speculative decoding has become a key component for efficient LLM serving systems. However, despite numerous advances, a speculative decoding method that can provide sufficient performance at low batch sizes without requiring additional training remains elusive. This presents a considerable challenge for achieving lossless acceleration in low-batch LLM inference on consumer-grade devices. To address this limitation, we propose Cassandra, an algorithm–hardware co-designed self-speculative decoding framework tailored explicitly for low-batch scenarios. The core idea of Cassandra is to construct a high-performance, training-free draft model through fine-grained data selection. By leveraging optimized pruning and mantissa truncation, Cassandra identifies and isolates the most salient values within both model weights and the Key–Value (KV) cache. These selected values are first loaded to rapidly generate candidate tokens, followed by parallel verification using full-precision data. This design achieves substantial performance gains over prior self-speculative decoding methods, which primarily rely on layer skipping or structured KV cache compression. In addition, to mitigate the overhead of format conversion between the Cassandra representation and standard floating-point formats, we introduce a lightweight encoder–decoder hardware module designed for seamless integration with commercial GPUs and NPUs. Our evaluation demonstrates that Cassandra achieves a performance improvement of up to 2.41× than the BFloat16 baseline without additional training. Moreover, when running Llama3-8B on an RTX 4090, Cassandra is capable of generating 1.81× more tokens under a fixed memory budget compared to Eagle-3, a state-of-the-art speculative decoding method.

## 中文摘要

推测解码已成为加速大语言模型（LLM）的一种有前景的无损方法。随着推理LLM解码阶段开销的增加，而算法近似方法会导致显著的精度下降，通过推测解码实现无损加速已成为高效LLM服务系统的关键。然而，尽管取得了诸多进展，能够在不需额外训练的情况下在低批量场景中提供足够性能的推测解码方法仍然难以实现。为应对这一挑战，我们提出Cassandra——一种专门针对低批量场景设计的算法-硬件协同自推测解码框架。其核心思想是通过细粒度数据选择构建高性能、无需训练的草稿模型：利用优化的剪枝和尾数截断技术，识别并分离模型权重和键值缓存（KV Cache）中最显著的值，首先加载这些值以快速生成候选词元，随后使用全精度数据进行并行验证。该设计相比以往依赖跳层或结构化KV缓存压缩的方法，实现了显著性能提升。此外，为减少格式转换开销，我们引入了一个轻量级编码器-解码器硬件模块，可与商用GPU和NPU无缝集成。评估表明，Cassandra在无需额外训练的情况下比BFloat16基线提升2.41×性能；在RTX 4090上运行Llama3-8B时，在固定内存预算下比最先进的Eagle-3方法多生成1.81×词元。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2026](../index.md)
