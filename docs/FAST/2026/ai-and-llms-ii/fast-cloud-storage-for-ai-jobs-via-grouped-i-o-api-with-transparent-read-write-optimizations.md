---
title: "Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations"
description: "FAST 2026 · AI and LLMs II · 第 255–270 页"
tags:
  - "FAST2026"
  - "AI and LLMs II"
---

# Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations

**中文标题**：通过分组 I/O API 与透明读写优化为 AI 作业提供快速云存储

**Session**：AI and LLMs II · 2026-02-25 10:50–12:30 · Chair：Jian Zhang（The Hong Kong University of Science and Technology）

**作者**：Yingyi Hao, Shanghai Jiao Tong University; Ting Yao, Huawei Cloud; Xingda Wei, Dingyan Zhang, and Tianle Sun, Shanghai Jiao Tong University; Yiwen Zhang, Zhiyong Fu, and Huatao Wu, Huawei Cloud; Rong Chen, Shanghai Jiao Tong University

**会议**：FAST 2026 · Santa Clara, CA · 第 255–270 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/hao](https://www.usenix.org/conference/fast26/presentation/hao)

**论文 PDF**：[fast26-hao.pdf](https://www.usenix.org/system/files/fast26-hao.pdf)

---

## 英文摘要

The emergence of AI workloads has placed rigorous bandwidth requirements on cloud storage, which are challenging to meet due to inherent hardware restrictions in cost-efficient disaggregated storage architectures, as well as the non-triviality of implementing application-tailored optimizations.

This paper presents AITURBO, a cloud storage system for AI jobs with high bandwidth demands. AITURBO first utilizes the high-bandwidth compute fabric between accelerators to meet AI applications’ bandwidth demands without incurring additional storage cost. AITURBO further introduces a simple yet powerful grouped I/O API that allows AITURBO to automatically derive optimized read and write plans at the storage layer. These plans enable optimizations that are comparable or better than application-level ones, because they capture common I/O patterns in AI workloads and have a holistic view from the storage layer’s perspective. Under common AI workloads such as checkpoint reads and writes and KV-cache reads, AITURBO achieves comparable or better performance than state-of-the-art systems, with and without application-level optimizations, including systems such as Megatron, Gemini, and Mooncake, typically with minimal application-level code changes. AITURBO has been deployed in training jobs in HUAWEI’s production cloud to support efficient training workloads.

## 中文摘要

AI 负载的出现对云存储提出了严格的带宽要求；由于高性价比的分离式存储架构存在固有硬件限制，以及实现面向应用的定制优化并非易事，这些要求难以满足。

本文提出 AITURBO，一种面向高带宽需求 AI 作业的云存储系统。AITURBO 首先利用加速器之间的高带宽计算互联来满足 AI 应用的带宽需求，而不会带来额外的存储成本。AITURBO 进一步引入一种简单而强大的分组 I/O API，使 AITURBO 能够在存储层自动推导出优化的读计划和写计划。这些计划能够实现与应用程序级优化相当或更优的效果，因为它们捕捉了 AI 负载中的常见 I/O 模式，并从存储层的视角提供了全局视图。在检查点读写和 KV 缓存读取等常见 AI 负载下，无论是否采用应用级优化，AITURBO 都能达到与最先进系统相当或更优的性能，这些系统包括 Megatron、Gemini 和 Mooncake 等，且通常只需对应用级代码做最小改动。AITURBO 已部署在华为生产云的训练作业中，以支持高效的训练负载。
