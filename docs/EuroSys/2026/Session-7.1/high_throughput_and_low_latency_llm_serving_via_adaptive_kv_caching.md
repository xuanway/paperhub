---
title: "High Throughput and Low Latency LLM Serving via Adaptive KV Caching"
description: "EuroSys 2026 · LLM Inference · Wenyan Chen (University of Macau; Shenzhen Institute of Advanced Technology, CAS"
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# High Throughput and Low Latency LLM Serving via Adaptive KV Caching

**中文标题：** 通过自适应KV缓存实现高吞吐、低延迟的LLM服务

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Wenyan Chen (University of Macau; Shenzhen Institute of Advanced Technology, CAS), Chengzhi Lu (Nanyang Technological University), Huanle Xu (University of Macau), Kejiang Ye (Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences), ChengZhong Xu (University of Macau)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803570)

## 英文摘要

The substantial memory demands of model weights and key-value (KV) caches often lead to severe memory bottlenecks in LLM serving. Existing systems address this by offloading KV caches to host memory and rapidly restoring them on demand before decoding. However, these approaches are too coarse-grained and fail to fully exploit the combined computational and storage capabilities of GPUs.

In this paper, we introduce eLLM, a novel LLM serving system designed to achieve high throughput and low latency through fine-grained KV caching. The core innovation lies in adaptively storing partial tokens with KV caches while dynamically recomputing non-cached tokens in parallel with decoding, thereby balancing memory usage and computational efficiency. This new mechanism enables dual-level optimizations: At the request level, eLLM employs token-wise caching to adaptively adjust batch sizes and uncached token ratios in real time. At the layer level, eLLM leverages communication-computation overlap and kernel fusion for resource-complementary operations to further enhance throughput and reduce latency. Experiments demonstrate that eLLM achieves 3.03× higher throughput while satisfying strict per-output-token latency SLOs. It also reduces first-token latency by 2.63× compared to state-of-the-art systems.

## 中文摘要

模型权重和键值（KV）缓存的巨大内存需求往往导致LLM服务中出现严重的内存瓶颈。现有系统通过将KV缓存卸载到主机内存并在解码前按需快速恢复来解决这一问题。然而，这些方法粒度太粗，无法充分利用GPU的计算与存储能力。

本文提出eLLM，一种新颖的LLM服务系统，通过细粒度KV缓存实现高吞吐与低延迟。其核心创新在于自适应地缓存部分token的KV，同时与解码并行地动态重算未缓存的token，从而在内存使用与计算效率之间取得平衡。这一新机制实现了两级优化：在请求层面，eLLM采用逐token缓存，实时自适应调整批大小和未缓存token比例；在层层面，eLLM利用通信-计算重叠以及面向资源互补操作的核融合，进一步提升吞吐并降低延迟。实验表明，eLLM在满足严格的每输出token延迟SLO的同时实现3.03倍更高的吞吐。与最先进系统相比，它还将首token延迟降低2.63倍。

**英文关键词：** LLM Serving, Adaptive KV Caching, High throughput, Low Latency

**中文关键词：** LLM服务、自适应KV缓存、高吞吐、低延迟

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
