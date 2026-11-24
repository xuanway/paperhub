# TwinCache: A Retrieval- and Reranking-Aware Caching System for Efficient RAG Serving

**中文标题**：TwinCache：面向高效 RAG 服务的检索与重排感知缓存系统

**所属 Session**：[Session 28: LLM Inference IV](index.md) · [ATC 2026](../index.md)

**作者**：Youxuan Xu (Beijing University of Posts and Telecommunications), Rongtian Fu (Beijing University of Posts and Telecommunications), Jinliang Shi (Beijing University of Posts and Telecommunications), Tong Wu (Beijing University of Posts and Telecommunications), Zhi Ma (Beijing University of Posts and Telecommunications), Shigang Li (Beijing University of Posts and Telecommunications)

## 英文摘要
Retrieval-augmented generation (RAG) improves the factuality of large language models (LLMs) by grounding responses in external knowledge, but introduces substantial pre-generation latency. We observe that both database retrieval and neural reranking can dominate time-to-first-token (TTFT) under different serving configurations, while related queries exhibit cross-query locality in retrieved chunks and high-ranked evidence after reranking. However, existing optimizations typically target retrieval or reranking in isolation, leaving this locality underexploited across the two stages. To this end, we present TwinCache, a retrieval- and reranking-aware caching system that exploits cross-query locality to jointly accelerate both stages of RAG serving. TwinCache organizes historical queries and retrieved chunks into locality-aware cache regions and constructs a compact, high-utility candidate set for each incoming query using nearest-query evidence, historical reranking feedback, and current-query similarity. This avoids expensive database retrieval on validated cache hits while reducing the number of chunks submitted to the reranker. To further reduce pre-generation latency, TwinCache introduces priority-guided reranking, which processes high-priority chunks first, overlaps subsequent reranking with LLM chunked prefill, and stops once the leading evidence chunks stabilize. TwinCache also mitigates potential false cache hits through online validation and refreshes cache regions during low-load periods using online feedback. Across diverse serving loads, TwinCache achieves up to 2.44× the serving throughput of a vLLM-based RAG system while maintaining response quality comparable to standard RAG.

## 中文摘要
检索增强生成（RAG）通过将回答建立在外部知识之上提升了大型语言模型（LLM）的事实性，但引入了可观的生成前延迟。我们观察到，在不同的服务配置下，数据库检索与神经重排都可能主导首 token 时延（TTFT），而相关查询在检索到的分块以及重排后的高排名证据上表现出跨查询局部性。然而，现有优化通常孤立地针对检索或重排，使这种局部性未能在这两个阶段之间得到充分利用。为此，我们提出 TwinCache，一个检索与重排感知的缓存系统，它利用跨查询局部性联合加速 RAG 服务的两个阶段。TwinCache 将历史查询与检索到的分块组织为局部性感知的缓存区域，并利用最近查询证据、历史重排反馈与当前查询相似性，为每个到来的查询构建一个紧凑、高价值的候选集。这在对已验证的缓存命中避免昂贵的数据库检索的同时，减少了提交给重排器的分块数量。为进一步降低生成前延迟，TwinCache 引入优先级引导的重排，优先处理高优先级分块，将后续重排与 LLM 分块预填充重叠，并在领先的证据分块稳定后即停止。TwinCache 还通过在线验证缓解潜在的假缓存命中，并利用在线反馈在低负载时段刷新缓存区域。在多样的服务负载下，TwinCache 的服务吞吐最高达到基于 vLLM 的 RAG 系统的 2.44×，同时保持与标准 RAG 相当的响应质量。

## 英文关键词
AI Infrastructure, LLM Inference, RAG Serving, Caching System, Cross-query Locality, Cache-based Retrieval, Priority-guided Reranking

## 中文关键词
AI 基础设施，LLM 推理，RAG 服务，缓存系统，跨查询局部性，基于缓存的检索，优先级引导的重排

[返回 Session 28](index.md) · [返回 ATC 2026](../index.md)
