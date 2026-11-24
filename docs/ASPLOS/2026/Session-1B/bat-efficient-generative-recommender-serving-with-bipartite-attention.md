---
title: "BAT: Efficient Generative Recommender Serving with Bipartite Attention"
description: "ASPLOS 2026 · Session 1B · BAT：基于二分注意力的高效生成式推荐服务"
tags:
  - "ASPLOS2026"
  - "Session 1B"
  - "LLM Serving: Latency & Scheduling"
---

# BAT: Efficient Generative Recommender Serving with Bipartite Attention

**中文标题：** BAT：基于二分注意力的高效生成式推荐服务

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jie Sun (Zhejiang University), Shaohang Wang (The University of Hong Kong), Zimo Zhang (Zhejiang University), Zhengyu Liu (Alibaba Group), Yunlong Xu (Alibaba Group), Peng Sun (Alibaba Group), Bingsheng He (National University of Singapore), Fei Wu (Zhejiang University), Zeke Wang (Zhejiang University), Bo Zhao (Aalto University)

**单位：** Zhejiang University；The University of Hong Kong；Alibaba Group；National University of Singapore；Aalto University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790131) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Generative Recommenders (GRs) have recently emerged as promising alternatives to traditional Deep Learning Recommendation Models (DLRMs). Despite their potential, GRs remain computationally expensive in inference, exhibiting compute-bound characteristics similar to the prefill stage of Large Language Model (LLM) inference. Prefix caching can reduce redundant computation by reusing previously constructed KV caches. However, the unique properties of GRs, i.e., highly personalized user profiles and real-time item retrieval, make cache reuse across queries challenging, resulting in limited computational savings. To address these challenges, we present Bat, an efficient serving system for GRs. The key observation is that the semantics between user and item tokens are permutation-invariant. Building on this, we propose Bipartite Attention, a novel attention mechanism that enables adaptive selection of either the user or the item as the prompt prefix without compromising accuracy, thereby unlocking new opportunities for KV cache reuse. We further co-design a disaggregated KV cache pool to proactively manage user-prefix and itemprefix caches as separate components. Since introducing item caches incurs additional memory overhead, we develop a hot-replicated cold-sharded item cache placement strategy that minimizes memory usage and maintains low communication overheads. Finally, we introduce a hotness-aware prompt scheduling strategy to optimize prefix selection under memory constraints. Extensive experiments on multiple recommendation datasets demonstrate that Bat improves serving throughput by up to 1.6× over the conventional useras-prefix approach, while reducing total computation by up to 58%.

## 中文摘要

生成式推荐模型（Generative Recommenders, GRs）近来已成为传统深度学习推荐模型（DLRMs）的有前景的替代方案。尽管具有潜力，GRs 在推理时仍然计算开销高昂，表现出与大型语言模型（LLM）推理的预填充阶段类似的计算受限特征。前缀缓存可以通过复用此前构建的 KV 缓存来减少冗余计算。然而，GRs 的独特性质，即高度个性化的用户画像与实时物品检索，使得跨查询的缓存复用颇具挑战，导致计算节省有限。为应对这些挑战，我们提出 Bat，一个面向 GRs 的高效服务系统。关键观察是，用户 token 与物品 token 之间的语义具有置换不变性。基于此，我们提出二分注意力（Bipartite Attention），一种新颖的注意力机制，能够在不损失精度的前提下自适应地选择用户或物品作为提示前缀，从而为 KV 缓存复用开辟新的机会。我们进一步协同设计了一个解耦的 KV 缓存池，将用户前缀缓存与物品前缀缓存作为独立组件主动管理。由于引入物品缓存会带来额外内存开销，我们提出一种热复制、冷分片的物品缓存放置策略，以最小化内存占用并保持较低的通信开销。最后，我们引入一种热度感知的提示调度策略，以在内存约束下优化前缀选择。在多个推荐数据集上的大量实验表明，Bat 相比传统的以用户为前缀的方法将服务吞吐量提升最高 1.6 倍，同时将总计算量降低最高 58%。

## 英文关键词

Generative Recommendation; Large Language Models; AI Infrastructure

## 中文关键词

生成式推荐；大语言模型；AI 基础设施

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790131)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2026](../index.md)
