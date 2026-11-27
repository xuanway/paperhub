---
title: "ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving"
description: "HPCA 2026 · LLM Inference Serving Systems"
tags:
  - "HPCA2026"
  - "LLM Inference Serving Systems"
---

# ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Inference Serving Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Inference Serving Systems</p>
</div>

**论文链接**：
**作者**：Jiuchen Shi Shanghai Jiao Tong University & The Hong Kong Polytechnic University , Hang Zhang Shanghai Jiao Tong University , Yixiao Wang Shanghai Jiao Tong University , Quan Chen Shanghai Jiao Tong University, China , Yizhou Shan Huawei Cloud , Kaihua Fu Hong Kong University of Science and Technology , Wei Wang Hong Kong University of Science and Technology , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

ELORA：面向 Multi-LoRA LLM 服务的高效 LoRA 与 KV 缓存管理

## 英文摘要

Multiple Low-Rank Adapters (Multi-LoRA) are gaining popularity for task-specific Large Language Model (LLM) applications. For Multi-LoRA serving, caching hot LoRAs and KV caches in the GPU memory can improve inference performance. However, existing Multi-LoRA inference systems fail to optimize serving performance like Time-To-First-Token (TTFT), neglecting usage dependencies when caching LoRAs and KV caches. We therefore propose ELORA, a Multi-LoRA caching system to optimize the serving performance. ELORA comprises a dependency-aware cache manager and a performance-driven cache swapper. The cache manager maintains the usage dependencies between LoRAs and KV caches during inference with a unified caching pool. The cache swapper determines the swap-in or swap-out of LoRAs and KV caches based on a unified cost model, when the GPU memory is idle or busy, respectively. Experimental results show that ELORA reduces the TTFT by 45.7% on average, compared to state-of-the-art works.

## 中文摘要

多种低秩适配器（Multi-LoRA）在面向特定任务的大语言模型（LLM）应用中日益流行。在 Multi-LoRA 服务中，将热点 LoRA 与 KV 缓存驻留在 GPU 内存可提升推理性能。然而，现有 Multi-LoRA 推理系统未能优化诸如首个 Token 时延（TTFT）之类的服务性能，在缓存 LoRA 与 KV 缓存时忽略了使用依赖关系。为此我们提出 ELORA，一个用于优化服务性能的 Multi-LoRA 缓存系统。ELORA 由依赖感知的缓存管理器与性能驱动的缓存换入换出器组成。缓存管理器通过统一的缓存池维护推理过程中 LoRA 与 KV 缓存之间的使用依赖关系。缓存换出器则依据统一代价模型，在 GPU 内存空闲或繁忙时分别决定 LoRA 与 KV 缓存的换入或换出。实验结果表明，与最先进的工作相比，ELORA 平均将 TTFT 降低 45.7%。
