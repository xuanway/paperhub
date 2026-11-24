---
title: "Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation–Storage Awareness"
description: "FAST 2026 · AI and LLMs I · 第 101–116 页"
tags:
  - "FAST2026"
  - "AI and LLMs I"
---

# Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation–Storage Awareness

**中文标题**：Bidaw：通过计算—存储双向感知增强交互式 LLM 服务的 KV 缓存

**Session**：AI and LLMs I · 2026-02-24 11:05–12:25 · Chair：Bingzhe Li（The University of Texas at Dallas）

**作者**：Shipeng Hu and Guangyan Zhang, Tsinghua University; Yuqi Zhou, China University of Geosciences Beijing; Yaya Wei and Ziyan Zhong, China Telecom Omni-channel Operation Center; Jike Chen, Tsinghua University

**会议**：FAST 2026 · Santa Clara, CA · 第 101–116 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/hu-shipeng](https://www.usenix.org/conference/fast26/presentation/hu-shipeng)

**论文 PDF**：[fast26-hu-shipeng.pdf](https://www.usenix.org/system/files/fast26-hu-shipeng.pdf)

---

## 英文摘要

In interactive LLM serving, historical key–value tensors (KVs) of multi-round conversations are often cached in a two-tier storage system consisting of host memory and SSDs, which provides large capacity at low cost. However, loading KVs from two-tier storage in existing approaches increases serving latency by up to 3.8× and decreases throughput by up to 2.0× compared to an ideal large-memory setting on our interactive conversation workload. This inefficiency arises from poor coordination between compute engine and two-tier storage.

This paper proposes Bidaw, an efficient KV caching approach with two-tier storage that enables *bidirectional awareness between compute and storage*. Bidaw introduces two key mechanisms. First, the compute engine schedules requests with KV-loading latency awareness by separating requests whose KVs reside in different storage layers and reordering them by KV size to reduce blocking. Second, the storage system improves host memory hit rates by leveraging LLM-generated responses to predict user access patterns during KV eviction. For further optimization, Bidaw balances storage footprint against computational savings by selectively caching storage-efficient history tensors.

Experiments on our interactive conversation workload and a public multi-round conversation workload of interactive LLM serving show that Bidaw reduces response latency by up to 3.58× and improves throughput by up to 1.83× over state-of-the-art approaches, approaching the theoretical upper bound achieved when all KVs reside entirely in host memory.

## 中文摘要

在交互式 LLM 服务中，多轮对话的历史键值张量（KV）通常被缓存在由主机内存和 SSD 组成的两级存储系统中，该系统以低成本提供大容量。然而，在我们的交互式对话负载上，现有方法从两级存储加载 KV 会使服务延迟最高增加 3.8 倍，吞吐量最多下降 2.0 倍（相比理想的大内存配置）。这种低效源于计算引擎与两级存储之间协调不佳。

本文提出 Bidaw，一种高效的两级存储 KV 缓存方法，实现了计算与存储之间的双向感知。Bidaw 引入两个关键机制。第一，计算引擎在调度请求时感知 KV 加载延迟：将 KV 位于不同存储层的请求分开，并按 KV 大小重排序，以减少阻塞。第二，存储系统利用 LLM 生成的回复来预测 KV 逐出期间的用户访问模式，从而提高主机内存命中率。为进一步优化，Bidaw 通过选择性缓存存储效率高的历史张量，在存储占用与计算节省之间取得平衡。

在我们的交互式对话负载和交互式 LLM 服务的公开多轮对话负载上的实验表明，与最先进方法相比，Bidaw 将响应延迟最多降低 3.58 倍，吞吐量最多提升 1.83 倍，接近所有 KV 完全驻留主机内存时所达到的理论上限。
