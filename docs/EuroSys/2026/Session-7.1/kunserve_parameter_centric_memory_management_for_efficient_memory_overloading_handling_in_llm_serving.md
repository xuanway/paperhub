---
title: "KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving"
description: "EuroSys 2026 · LLM Inference · Rongxin Cheng (Shanghai Jiao Tong University), Yuxin Lai (Shanghai Jiao Tong Uni"
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving

**中文标题：** KUNSERVE：以参数为中心的内存管理，用于 LLM 服务中高效处理内存过载

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Rongxin Cheng (Shanghai Jiao Tong University), Yuxin Lai (Shanghai Jiao Tong University), Xingda Wei (Shanghai Jiao Tong University), Rong Chen (Shanghai Jiao Tong University), Haibo Chen (Shanghai JiaoTong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769348)

## 英文摘要

Serving LLMs with a cluster of GPUs is common nowadays, where the serving system must meet strict latency SLOs required by applications. However, the stateful nature of LLM serving requires maintaining huge states (i.e., KVCache) in limited GPU memory. Under spikes in real-world workloads, GPU memory can be easily overloaded, leading to orders of magnitude higher response latency due to queuing introduced by waiting for KVCache to be reclaimed. Prior KVCache-centric approaches handle overloading by dropping, migrating, or swapping KVCache. These methods fail to release sufficient memory quickly with requests still queued.

This paper proposes the first parameter-centric approach to handling overloading by selectively dropping replicated parameters to instantly free memory for requests, based on an unnoticed observation that model parameters are commonly replicated across GPUs for serving LLMs. With additional memory, all requests can be served with a larger batch without queuing. To make the parameter-centric approach correct and efficient, we cooperatively execute requests on GPUs with a complete copy of parameters using pipeline parallelism, and derive an appropriate drop plan without unnecessary cooperation. We also design techniques to minimize the performance overhead due to pipeline parallelism with the execution patterns of requests under drop. Evaluations show that KUNSERVE reduces the tail TTFT of requests under overloading by up to 72.2 × compared to the state-of-the-art systems including Llumnix, vLLM and InferCept.

## 中文摘要

如今使用 GPU 集群服务 LLM 已是常态，服务系统必须满足应用所要求的严格延迟 SLO。然而，LLM 服务的有状态特性要求在有限的 GPU 内存中维持巨大的状态（即 KVCache）。在真实工作负载的尖峰下，GPU 内存很容易过载，由于等待 KVCache 被回收而引入排队，导致响应延迟高出数个数量级。先前以 KVCache 为中心的方法通过丢弃、迁移或换出 KVCache 来处理过载。这些方法无法在请求仍在排队时快速释放足够的内存。

本文提出首个以参数为中心的方法来处理过载：基于一个此前未被注意的观察——为服务 LLM，模型参数通常在多个 GPU 间被复制——有选择地丢弃副本参数，从而立即为请求释放内存。有了额外内存，所有请求都可以用更大的批处理被服务而无需排队。为使以参数为中心的方法既正确又高效，我们使用流水线并行在拥有完整参数副本的 GPU 上协同执行请求，并在无需不必要协作的情况下推导出合适的丢弃方案。我们还设计技术，以尽量减少在丢弃状态下请求执行模式因流水线并行而产生的性能开销。评估表明，与包括 Llumnix、vLLM 和 InferCept 在内的最先进系统相比，KUNSERVE 将过载下请求的尾 TTFT 最多降低 72.2 倍。

**英文关键词：** LLM Serving; Cloud computing; Parameter-centric memory management

**中文关键词：** LLM 服务、云计算、以参数为中心的内存管理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
