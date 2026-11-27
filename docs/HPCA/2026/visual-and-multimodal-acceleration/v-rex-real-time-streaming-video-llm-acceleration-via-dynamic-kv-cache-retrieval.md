---
title: "V-Rex: Real-Time Streaming Video LLM Acceleration via Dynamic KV Cache Retrieval"
description: "HPCA 2026 · Visual and Multimodal Acceleration"
tags:
  - "HPCA2026"
  - "Visual and Multimodal Acceleration"
---

# V-Rex: Real-Time Streaming Video LLM Acceleration via Dynamic KV Cache Retrieval

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Visual and Multimodal Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Visual and Multimodal Acceleration</p>
</div>

**论文链接**：
**作者**：Donghyuk Kim KAIST , Sejeong Yang KAIST , Wonjin Shin KAIST , Joo-Young Kim KAIST
**会议**：HPCA 2026

---

## 中文标题

V-Rex：通过动态 KV 缓存检索实现实时流式视频大语言模型加速

## 英文摘要

Streaming video large language models (LLMs) are increasingly used for real-time multimodal tasks such as video captioning, question answering, conversational agents, and augmented reality. However, these models face fundamental memory and computational challenges because their key-value (KV) caches grow substantially with continuous streaming video input. This process requires an iterative prefill stage, which is a unique feature of streaming video LLMs. Prior works reduce excessive cache overhead by utilizing the KV cache retrieval algorithm, which offloads the full KV cache to CPU memory or storage, then selectively fetches the most relevant entries. Nevertheless, due to its iterative prefill stage, they suffer from significant limitations, including extensive computation, substantial data transfer, and degradation in accuracy. Crucially, this issue is exacerbated for edge deployment, which is the primary target for these models. The memory footprint exceeds the memory capacity within minutes of video streams, making low-latency, energy-efficient inference infeasible. In this work, we propose V-Rex, the first software-hardware co-designed accelerator that comprehensively addresses both algorithmic and hardware bottlenecks in streaming video LLM inference. At its core, V-Rex introduces ReSV, a training-free dynamic KV cache retrieval algorithm. ReSV exploits temporal and spatial similarity-based token clustering to reduce excessive KV cache memory across video frames, and dynamically adjusts token selection per transformer layer and attention head to minimize the number of selected tokens. To fully realize these algorithmic benefits, V-Rex offers a compact, low-latency hardware accelerator with a dynamic KV cache retrieval engine (DRE), featuring bit-level and early-exit based computing units, as well as hierarchical KV cache memory management. Evaluated on COIN benchmarks, V-Rex achieves unprecedented real-time of 3.9-8.3 FPS and energy-efficient streaming video LLM inference on edge deployment with negligible accuracy loss. While DRE only accounts for 2.2% power and 2.0% area, the system delivers 1.9-19.7× speedup and 3.1-18.5× energy efficiency improvements over AGX Orin GPU. This work is the first to comprehensively tackle KV cache retrieval across algorithm and hardware, enabling real-time streaming video LLM inference on resource-constrained edge devices, with clear potential for scalable deployment in large-scale server environments.

## 中文摘要

流式视频大语言模型（LLM）正日益用于视频描述、问答、对话智能体与增强现实等实时多模态任务。然而，随着视频持续流入，键值（KV）缓存大幅增长，这类模型面临根本的内存与计算挑战：该过程需要迭代式预填充阶段，这是流式视频 LLM 的独特特征。已有工作采用 KV 缓存检索算法缓解过高的缓存开销——将完整 KV 缓存卸载到 CPU 内存或存储，再有选择地取回最相关条目；但受迭代式预填充影响，它们存在计算量大、数据传输多与精度下降等显著局限。该问题在这些模型的主要目标——边缘部署中更为严重：视频流仅持续数分钟，内存占用便超出容量，使低时延、高能效推理无法实现。本文提出 V-Rex，首个软硬件协同设计的加速器，全面应对流式视频 LLM 推理的算法与硬件瓶颈。其核心 ReSV 是一种免训练的动态 KV 缓存检索算法：以基于时空相似性的词元聚类降低跨帧 KV 缓存内存占用，并按 transformer 层与注意力头动态调整词元选择，最小化所选词元数。为充分兑现算法收益，V-Rex 提供紧凑低时延的硬件加速器，配备动态 KV 缓存检索引擎（DRE），含位级与提前退出计算单元及层次化 KV 缓存内存管理。在 COIN 基准上，V-Rex 在边缘部署实现前所未有的 3.9-8.3 FPS 实时性与高能效流式视频 LLM 推理，精度损失可忽略；DRE 仅占 2.2% 功耗与 2.0% 面积，系统相比 AGX Orin GPU 取得 1.9-19.7 倍加速比与 3.1-18.5 倍能效提升。本工作首次在算法与硬件层面全面解决 KV 缓存检索，使资源受限边缘设备可实时进行流式视频 LLM 推理，并有望扩展到大规模服务器环境。
