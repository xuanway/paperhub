---
title: "Stateful Large Language Model Serving with Pensieve"
description: "EuroSys 2025 · LLM Serving · Lingfan Yu (New York University), Jinkun Lin (New York University), Jinyang Li ("
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# Stateful Large Language Model Serving with Pensieve

**中文标题：** 利用 Pensieve 提供有状态大语言模型服务

**所属 Session：** [Session 1.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Lingfan Yu (New York University), Jinkun Lin (New York University), Jinyang Li (New York University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696086)

## 英文摘要

Large Language Models (LLMs) are wildly popular today and it is important to serve them efficiently. Existing LLM serving systems are stateless across requests. Consequently, when LLMs are used in the common setting of multi-turn conversations, a growing log of the conversation history must be processed alongside any request by the serving system at each turn, resulting in repeated processing.

In this paper, we design 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒, a system optimized for multi-turn conversation LLM serving. 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒maintains the conversation state across requests by caching previously processed history to avoid duplicate processing. 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒’s multi-tier caching strategy can utilize both GPU and CPU memory to efficiently store and retrieve cached data. 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒 also generalizes the recent PagedAttention kernel to support attention between multiple input tokens with a GPU cache spread over non-contiguous memory. Our evaluation shows that 𝑃𝑒𝑛𝑠𝑖𝑒𝑣𝑒can achieve 1.14-3.0× the throughput of vLLM and TensorRT-LLM and significantly reduce latency.

## 中文摘要

大语言模型（LLM）如今极为流行，因此高效地为其提供服务十分重要。现有的 LLM 服务系统在请求之间是无状态的。因此，当 LLM 用于多轮对话这一常见场景时，服务系统在每一轮都必须在处理请求的同时处理不断增长的对话历史日志，导致重复处理。

本文设计了 Pensieve，一个针对多轮对话 LLM 服务进行优化的系统。Pensieve 通过缓存已处理的历史在请求之间维护对话状态，从而避免重复处理。Pensieve 的多级缓存策略能够同时利用 GPU 和 CPU 内存来高效地存储和检索缓存数据。Pensieve 还将近期的 PagedAttention 内核推广到支持多个输入 token 之间的注意力计算，且 GPU 缓存分散在非连续内存上。我们的评估显示，Pensieve 可达到 vLLM 和 TensorRT-LLM 的 1.14–3.0 倍吞吐量，并显著降低延迟。

**英文关键词：** LLM Serving, Multi-turn Conversations, Cache

**中文关键词：** LLM 服务、多轮对话、缓存

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
