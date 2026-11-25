---
title: "PKAS: Predictive KVCache-Aware Scheduling for Faster LLM and Transformer Inferences"
description: "HPDC 2026 · Session 1 — LLM Inference: Scheduling & Serving"
tags:
  - "HPDC2026"
  - "Session 1"
  - "LLM Inference: Scheduling & Serving"
---

# PKAS: Predictive KVCache-Aware Scheduling for Faster LLM and Transformer Inferences

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 1</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807819)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#YeMCNKS26](https://dblp.org/db/conf/hpdc/hpdc2026.html#YeMCNKS26)

**作者**：Jie Ye, Avinash Maurya, Krishna Teja Chitty-Venkata, Bogdan Nicolae, Anthony Kougkas, Xian-He Sun

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）

---

## 英文摘要

With rising popularity of LLMs, the performance, scalability, and resource-efficiency of inferences become a crucial challenge. The core part of the inference process is the KV cache, which avoids recomputing intermediate attention states, and the batching strategy that batches multiple requests per forward pass to leverage GPU parallelism. KV cache memory grows linearly with sequence length and batch sizes, easily exceeding the limited GPU memory capacity. State-of-the-art inference runtimes use continuous batching to maximize GPU utilization by interleaving the processing of new requests (i.e., prefill requests) with ongoing generation requests (i.e., decode requests). However, existing schedulers greedily admit prefill requests without considering the future KV cache memory required to successfully run the decode phases. This shortsighted approach causes frequent KV cache overflows, which in turn trigger preemption and recomputation of requests, severely degrading both throughput and latency. We propose PKAS, a Predictive KV Cache-Aware Scheduling algorithm to mitigate this inefficiency by reducing preemptions. PKAS uses a low-overhead technique to simulate future KV cache utilization and guide the admissibility for new request candidates. Combined with lightweight output-length predictions, PKAS can make better batching decisions, preventing KV cache overflows and drastically reducing preemptions. Evaluations on diverse models and workloads show that PKAS achieves up to 7.34x higher throughput and 8x lower latency compared to state-of-the-art scheduling, with the largest gains on long-context workloads where KV cache pressure is high.

## 中文摘要

随着 LLM 的日益普及，推理的性能、可扩展性与资源效率成为关键挑战。推理过程的核心是 KV cache——它避免重复计算中间注意力状态，以及批处理策略——它将多个请求合并到一次前向传播中以利用 GPU 并行性。KV cache 内存随序列长度和批大小线性增长，很容易超出有限的 GPU 显存容量。最先进的推理运行时使用连续批处理，通过将新请求（即预填充请求）的处理与正在进行的生成请求（即解码请求）交错执行，以最大化 GPU 利用率。然而，现有调度器在接纳预填充请求时过于贪婪，未考虑成功运行解码阶段所需的未来 KV cache 内存。这种短视做法导致 KV cache 频繁溢出，进而触发请求抢占与重计算，严重降低吞吐和延迟。我们提出 PKAS，一种预测式 KV 缓存感知调度算法，通过减少抢占来缓解这一低效问题。PKAS 使用低开销技术模拟未来 KV cache 使用率，并指导新候选请求的可接纳性。结合轻量级输出长度预测，PKAS 能够做出更好的批处理决策，防止 KV cache 溢出并大幅减少抢占。在多种模型与负载上的评估表明，与最先进调度相比，PKAS 实现最高 7.34 倍吞吐和 8 倍延迟降低，在 KV cache 压力较大的长上下文负载上收益最大。

## 英文关键词

KV Cache Management, LLM Inference Serving, Scheduling

## 中文关键词

KV 缓存管理，LLM 推理服务，调度

---

[← 返回 Session 1 — LLM Inference: Scheduling & Serving](index.md)
