---
title: "Omnia: Efficient RAG Serving through Speculative Scheduling"
description: "HPDC 2026 · Session 1 — LLM Inference: Scheduling & Serving"
tags:
  - "HPDC2026"
  - "Session 1"
  - "LLM Inference: Scheduling & Serving"
---

# Omnia: Efficient RAG Serving through Speculative Scheduling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 1</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807814)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#FuLXWMS26](https://dblp.org/db/conf/hpdc/hpdc2026.html#FuLXWMS26)

**作者**：Rongtian Fu, Shigang Li, Youxuan Xu, Tong Wu, Zhi Ma, Jinliang Shi

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）

---

## 英文摘要

Retrieval-Augmented Generation (RAG) has emerged for enhancing Large Language Models (LLMs) by improving factual accuracy and mitigating hallucinations. A typical RAG pipeline executes in three cascaded stages: retrieval, reranking, and generation. The existing serving systems suffer from two critical system-level bottlenecks when applying to RAG serving: the first is the cumulative latency caused by rigid sequential dependencies between reranking and generation, and the second is the system saturation triggered by bursty, high fan-in reranking workloads. In this paper, we propose Omnia, an efficient distributed system designed to push the throughput-latency frontier of RAG serving. Omnia introduces chunk speculation, a two-level (coarse-to-fine) reranking architecture that enables early-termination through chunk pruning and masks reranking latency via progressive prefilling. To further improve the execution efficiency of chunk speculation, we develop backpressure-aware reranker scheduling (BARS). By monitoring concurrent client counts and real-time KV cache occupancy, BARS dynamically modulates the speculation interval to batch compute-bound prefilling with memory-bound decoding. We implement Omnia as a backend-agnostic framework, supporting vLLM, SGLang, and TensorRT-LLM. Evaluation demonstrates that Omnia maintains near-lossless accuracy while optimizing both the system-level throughput and client-level latency. Compared to existing systems, Omnia increases the maximum request rate the system can handle by 57%. The end-to-end response latency for a client is reduced by averagely 2.99× (up to 9.84×). We foresee Omnia will form a new paradigm for efficient RAG serving.

## 中文摘要

检索增强生成（RAG）通过提升事实准确性、缓解幻觉来增强大语言模型（LLM）。典型的 RAG 流水线按三个级联阶段执行：检索、重排序与生成。现有服务系统在应用于 RAG 服务时存在两个关键的系统级瓶颈：其一是重排序与生成之间刚性串行依赖造成的累积延迟；其二是突发、高扇入的重排序负载引发的系统饱和。本文提出 Omnia，一个高效的分布式系统，旨在推进 RAG 服务的吞吐-延迟前沿。Omnia 引入块推测（chunk speculation）——一种两级（由粗到细）重排序架构，通过块剪枝实现提前终止，并以渐进式预填充掩盖重排序延迟。为进一步提升块推测的执行效率，我们提出背压感知的重排序器调度（BARS）。通过监测并发客户端数量与实时 KV cache 占用，BARS 动态调节推测间隔，将计算密集的预填充与内存密集的解码批量执行。我们将 Omnia 实现为后端无关的框架，支持 vLLM、SGLang 和 TensorRT-LLM。评估表明，Omnia 在保持近乎无损精度的同时，优化了系统级吞吐与客户端级延迟。与现有系统相比，Omnia 将系统可处理的最大请求速率提升 57%，客户端端到端响应延迟平均降低 2.99 倍（最高 9.84 倍）。我们预计 Omnia 将形成高效 RAG 服务的新范式。

## 英文关键词

RAG, LLM Inference, Distributed AI Infrastructure, Chunk Speculation, Chunk Pruning, Progressive Prefilling, Backpressure-Aware Reranker Scheduling

## 中文关键词

RAG，LLM 推理，分布式 AI 基础设施，块推测，块剪枝，渐进式预填充，背压感知重排序调度

---

[← 返回 Session 1 — LLM Inference: Scheduling & Serving](index.md)
