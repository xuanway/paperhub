---
title: "SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs"
description: "FAST 2026 · AI and LLMs I · 第 67–82 页"
tags:
  - "FAST2026"
  - "AI and LLMs I"
---

# SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs

**中文标题**：SolidAttention：内存受限 PC 上的低延迟 SSD 服务

**Session**：AI and LLMs I · 2026-02-24 11:05–12:25 · Chair：Bingzhe Li（The University of Texas at Dallas）

**作者**：Xinrui Zheng, Dongliang Wei, Jianxiang Gao, Yixin Song, Zeyu Mi, and Haibo Chen, Shanghai Jiao Tong University

**会议**：FAST 2026 · Santa Clara, CA · 第 67–82 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zheng](https://www.usenix.org/conference/fast26/presentation/zheng)

**论文 PDF**：[fast26-zheng.pdf](https://www.usenix.org/system/files/fast26-zheng.pdf)

---

## 英文摘要

AI personal computers (AIPCs) enable the local deployment of large language model (LLM) inference, offering enhanced privacy guarantees and customizable serving. However, such deployments are constrained by limited memory capacity, primarily due to the substantial key-value (KV) cache overhead. This paper introduces SolidAttention, an LLM inference engine which addresses these limitations through a tight co-design of dynamic attention sparsity algorithms and SSD-based storage management. Specifically, to maximize SSD bandwidth utilization, SolidAttention consolidates multiple KV pairs into coarse-grained blocks and implements speculative prefetching mechanisms that exploit temporal locality in sparse attention. By fine-grained orchestration of computation and I/O operations while reusing synchronization points, SolidAttention further minimizes SSD-induced blocking latency. With a 128k-token context, SolidAttention improves the inference speed by up to 3.1× and reduces the KV cache memory footprint by up to 98% without compromising inference accuracy.

## 中文摘要

AI 个人电脑（AIPC）使大语言模型（LLM）推理能够在本地部署，从而提供更强的隐私保障和可定制的服务。然而，此类部署受限于有限的内存容量，主要原因是键值（KV）缓存开销巨大。本文提出 SolidAttention，一种 LLM 推理引擎，它通过动态注意力稀疏算法与基于 SSD 的存储管理的紧密协同设计来解决这些限制。具体而言，为最大化 SSD 带宽利用率，SolidAttention 将多个 KV 对整合为粗粒度块，并实现可利用稀疏注意力时间局部性的推测性预取机制。通过细粒度地编排计算与 I/O 操作并复用同步点，SolidAttention 进一步将 SSD 引起的阻塞延迟降至最低。在 128k token 上下文下，SolidAttention 将推理速度最高提升 3.1 倍，并将 KV 缓存内存占用最多减少 98%，同时不损害推理精度。
