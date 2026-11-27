---
title: "VectorLiteRAG: Latency-Aware and Fine-Grained Resource Partitioning for Efficient RAG"
description: "HPCA 2026 · Graph Neural Networks and Retrieval Systems"
tags:
  - "HPCA2026"
  - "Graph Neural Networks and Retrieval Systems"
---

# VectorLiteRAG: Latency-Aware and Fine-Grained Resource Partitioning for Efficient RAG

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Graph Neural Networks and Retrieval Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Graph Neural Networks and Retrieval Systems</p>
</div>

**论文链接**：
**作者**：Junkyum Kim Georgia Institute of Technology , Divya Mahajan Georgia Institute of Technology
**会议**：HPCA 2026

---

## 中文标题

VectorLiteRAG：面向高效 RAG 的时延感知细粒度资源划分

## 英文摘要

Retrieval-Augmented Generation leverages vector similarity search to enhance large language models with up-to-date, external knowledge, enabling accurate and reliable responses. While CPU-only vector search incurs high latency on large, high-dimensional indices, co-locating the retriever and the LLM on the GPU leads to resource sharing that can create resource contention. Specifically, vector search is memory and I/O intensive, placing it in direct conflict with LLM inference, which demands memory for KV cache and compute for higher throughput. We present VECTORLITERAG, a latency-aware RAG serving system that explicitly orchestrates data placement and execution across retrieval and inference to meet strict end-to-end SLOs. VECTORLITERAG is driven by access-pattern analysis and performance estimation to regulate how retrieval variability can be mitigated and managed in the system with LLM inference, enabling SLO-compliant execution under skewed and dynamic workloads. By jointly modeling search latency and query hit-rate distributions, VECTORLITERAG identifies an optimal index partitioning point across CPU and GPU that minimizes contention and stabilizes batching behavior, thereby maximizing sustained throughput under skewed access patterns. A low-overhead online index update mechanism allows VECTORLITERAG to continuously adapt to evolving request distributions, preserving batching efficiency and throughput as access patterns evolve. Our evaluations demonstrate that VECTORLITERAG consistently expands the range of SLO-compliant request rate across all tested configurations. Without increasing the generation latency or requiring additional hardware, VECTORLITERAG outperforms both naive and existing alternative frameworks, improving attainable SLO-bound throughput by up to 1.5×.

## 中文摘要

检索增强生成利用向量相似度搜索为大语言模型补充最新的外部知识，从而给出准确可靠的回答。纯 CPU 的向量搜索在大型高维索引上时延很高，而把检索器与 LLM 共置于 GPU 又会导致资源共享与争用：向量搜索是内存与 I/O 密集型任务，与 LLM 推理直接冲突——后者需要内存容纳 KV 缓存、需要算力换取更高吞吐。我们提出 VECTORLITERAG，一个时延感知的 RAG 服务系统，显式编排检索与推理之间的数据放置与执行，以满足严格的端到端 SLO。该系统由访问模式分析与性能估计驱动，调控检索波动如何与 LLM 推理在系统中共存，从而在偏斜且动态的负载下实现符合 SLO 的执行。通过联合建模搜索时延与查询命中率分布，VECTORLITERAG 确定跨 CPU 与 GPU 的最优索引划分点，以最小化争用并稳定批处理行为，在偏斜访问模式下最大化持续吞吐。低开销的在线索引更新机制使其能持续适应变化的请求分布，在访问模式演化时保持批处理效率与吞吐。评估表明，VECTORLITERAG 在所有测试配置下都扩大了符合 SLO 的请求速率范围，且在不增加生成时延、不需额外硬件的情况下优于朴素方案与现有替代框架，将可达到的 SLO 约束吞吐最高提升 1.5 倍。
