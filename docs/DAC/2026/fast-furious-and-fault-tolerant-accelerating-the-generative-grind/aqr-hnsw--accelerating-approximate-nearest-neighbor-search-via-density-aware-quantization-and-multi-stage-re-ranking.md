AQR-HNSW: Accelerating Approximate Nearest Neighbor Search via Density-Aware Quantization and Multi-Stage Re-Ranking
Authors：
[Ganap Tewary](https://63dac.conference-program.com/?post_type=page&p=15&uid=43831388740439093021)，[Nrusinga Charan Gantayat](https://63dac.conference-program.com/?post_type=page&p=15&uid=98716290299412265241)，[Jeff Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3292043392856372077)

## 中文标题

AQR-HNSW：通过密度感知量化与多阶段重排序加速近似最近邻搜索

## 英文摘要

Approximate Nearest Neighbor (ANN) search has become fundamental to modern AI infrastructure, powering recommendation systems, search engines, and large language models across industry leaders from Google to OpenAI. Hierarchical Navigable Small World (HNSW) graphs have emerged as the dominant ANN algorithm, widely adopted in production systems due to their superior recall vs. latency balance. However, as vector databases scale to billions of embeddings, HNSW faces critical bottlenecks: memory consumption expands, distance computation overhead dominates query latency, and it suffers suboptimal performance on heterogeneous data distributions. This paper presents Adaptive Quantization and Rerank HNSW (AQR-HNSW), a novel framework that synergistically integrates three strategies to enhance HNSW’s scalability. AQR-HNSW introduces (1) density-aware adaptive quantization, achieving 4× compression while preserving distance relationships; (2) multi-state re-ranking that reduces unnecessary computations by 35%; and (3) quantization-optimized SIMD implementations delivering 16-64 operations per cycle across architectures. Evaluation on standard benchmarks demonstrates 2.5-3.3× higher queries per second (QPS) than state-of-the-art HNSW implementations while maintaining 98%+ recall, with 75% memory reduction for the index graph and 5× faster index construction.

## 中文摘要

近似最近邻（ANN）搜索已成为现代 AI 基础设施的基础，支撑着从 Google 到 OpenAI 等业界领先者的推荐系统、搜索引擎与大语言模型。分层可导航小世界（HNSW）图已成为主流的 ANN 算法，凭借卓越的召回率与时延平衡在生产系统中被广泛采用。然而，随着向量数据库规模扩展到数十亿个嵌入向量，HNSW 面临关键瓶颈：内存占用持续膨胀、距离计算开销主导查询时延，且在处理异构数据分布时性能欠佳。本文提出自适应量化与重排序 HNSW（AQR-HNSW），这是一个协同集成三种策略以提升 HNSW 可扩展性的新框架。AQR-HNSW 引入：（1）密度感知自适应量化，在保持距离关系的同时实现 4 倍压缩；（2）多状态重排序，将不必要的计算减少 35%；（3）量化优化的 SIMD 实现，跨架构每周期可完成 16–64 次运算。在标准基准上的评测表明，与最先进的 HNSW 实现相比，其每秒查询数（QPS）提升 2.5–3.3 倍，同时保持 98% 以上的召回率，索引图内存降低 75%，索引构建速度提升 5 倍。
