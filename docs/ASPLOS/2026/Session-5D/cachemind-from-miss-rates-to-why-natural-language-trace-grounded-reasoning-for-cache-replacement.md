---
title: "CacheMind: From Miss Rates to Why – Natural-Language, Trace-Grounded Reasoning for Cache Replacement"
description: "ASPLOS 2026 · Session 5D · CacheMind：从缺失率到原因——面向缓存替换的自然语言、基于轨迹的推理"
tags:
  - "ASPLOS2026"
  - "Session 5D"
  - "Storage & Caching"
---

# CacheMind: From Miss Rates to Why – Natural-Language, Trace-Grounded Reasoning for Cache Replacement

**中文标题：** CacheMind：从缺失率到原因——面向缓存替换的自然语言、基于轨迹的推理

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Kaushal Mhapsekar (NC State University), Azam Ghanbari (Department of ECE, NC State University), Bita Aslrousta (North Carolina State University), Samira Mirbagher (NC State University)

**单位：** NC State University；Department of ECE, NC State University；North Carolina State University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790136) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Cache replacement remains a challenging problem in CPU microarchitecture, often addressed using hand-crafted heuristics that limit cache performance. Cache data analysis requires parsing millions of trace entries with manual filtering, making the process slow and non-interactive. To address this, we introduce CacheMind, a conversational tool that uses Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to enable semantic reasoning over cache traces. Architects can now ask natural language questions like, "Why is the memory access associated with PC X causing more evictions?", and receive trace-grounded, human-readable answers linked to program semantics for the first time. To evaluate CacheMind, we present CacheMindBench, the first verified benchmark suite for LLM-based reasoning for the cache replacement problem. Using the Sieve retriever, CacheMind achieves 66.67% on 75 unseen trace-grounded questions and 84.80% on 25 unseen policy-specific reasoning tasks; with Ranger, it achieves 89.33% and 64.80% on the same evaluations. Additionally, with Ranger, CacheMind achieves 100% accuracy on 4 out of 6 categories in the trace-grounded tier of CacheMindBench. Compared to LlamaIndex (10% retrieval success), Sieve achieves 60% and Ranger achieves 90%, demonstrating that existing retrieval-augmented Generation (RAGs) are insufficient for precise, trace-grounded microarchitectural reasoning. We provided four concrete actionable insights derived using CacheMind, wherein bypassing use case improved cache hit rate by 7.66% and speedup by 2.04%, software fix use case gives speedup of 76%, and Mockingjay replacement policy use case gives speedup of 0.7%; showing the utility of CacheMind on non-trivial queries that require a natural-language interface.

## 中文摘要

缓存替换在 CPU 微架构中仍然是一个具有挑战性的问题，通常使用限制缓存性能的手工启发式方法来解决。缓存数据分析需要解析数百万条轨迹条目并进行人工过滤，这使得该过程缓慢且非交互。为解决这一问题，我们推出 CacheMind，一种对话式工具，它使用检索增强生成（RAG）和大语言模型（LLM）来对缓存轨迹进行语义推理。架构师现在可以提出自然语言问题，例如“与 PC X 相关的内存访问为何导致更多驱逐？”，并首次获得与程序语义相关联、基于轨迹且人类可读的答案。为评估 CacheMind，我们提出 CacheMindBench，这是首个针对缓存替换问题的、经过验证的基于 LLM 推理的基准测试套件。使用 Sieve 检索器，CacheMind 在 75 个未见过的基于轨迹的问题上达到 66.67%，在 25 个未见过的策略特定推理任务上达到 84.80%；使用 Ranger，它在相同评估上分别达到 89.33% 和 64.80%。此外，使用 Ranger，CacheMind 在 CacheMindBench 基于轨迹层级的 6 个类别中有 4 个达到 100% 准确率。与 LlamaIndex（10% 检索成功率）相比，Sieve 达到 60%，Ranger 达到 90%，这表明现有的检索增强生成（RAG）不足以进行精确的、基于轨迹的微架构推理。我们提供了使用 CacheMind 得出的四项具体可行的洞见，其中绕过用例将缓存命中率提高了 7.66%、加速比提高了 2.04%，软件修复用例带来 76% 的加速，Mockingjay 替换策略用例带来 0.7% 的加速；这展示了 CacheMind 在需要自然语言接口的非平凡查询上的实用性。

## 英文关键词

Cache replacement policy, natural-language-guided ChampSim, gem5, large language models, retrieval-augmented generation, microarchitecture-directed prefetching, compiler optimization, hardware-software co-design, machine learning for systems, LLM reasoning benchmark

## 中文关键词

缓存替换策略；自然语言引导的 ChampSim；gem5；大语言模型；检索增强生成；微架构导向的预取；编译器优化；软硬件协同设计；面向系统的机器学习；LLM 推理基准

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790136)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2026](../index.md)
