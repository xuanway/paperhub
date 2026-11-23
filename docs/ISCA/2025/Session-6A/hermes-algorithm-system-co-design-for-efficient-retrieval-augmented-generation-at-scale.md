---
title: "Hermes: Algorithm-System Co-design for Efficient Retrieval-Augmented Generation At-Scale"
description: "ISCA 2025 · Session 6A · Hermes：面向大规模高效检索增强生成的算法—系统协同设计"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# Hermes: Algorithm-System Co-design for Efficient Retrieval-Augmented Generation At-Scale

**中文标题：** Hermes：面向大规模高效检索增强生成的算法—系统协同设计

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Michael Shen, Muhammad Umar, Kiwan Maeng, G. Edward Suh, Udit Gupta

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731076) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rapid advancement of Large Language Models (LLMs) as well as the constantly expanding amount of data make keeping the latest models constantly up-to-date a challenge. The high computational cost required to constantly retrain models to handle evolving data has led to the development of Retrieval-Augmented Generation (RAG). RAG presents a promising solution that enables LLMs to access and incorporate real-time information from external datas- tores, thus minimizing the need for retraining to update the infor- mation available to an LLM. However, as the RAG datastores used to augment information expand into the range of trillions of tokens, retrieval overheads become significant, impacting latency, through- put, and energy efficiency. To address this, we propose Hermes, an algorithm-systems co-design framework that addresses the unique bottlenecks of large-scale RAG systems. Hermes mitigates retrieval latency by partitioning and distributing datastores across multi- ple nodes, while also enhancing throughput and energy efficiency through an intelligent hierarchical search that dynamically directs queries to optimized subsets of the datastore. On open-source RAG datastores and models, we demonstrate Hermes optimizes end-to- end latency and energy by up to 9.33×and 2.10×, without sacrificing retrieval quality for at-scale trillion token retrieval datastores.

## 中文摘要

大语言模型（LLM）快速迭代、数据规模持续增长，让模型的实时更新变得十分困难。持续重训模型以适配不断变化的数据会带来高昂算力开销，检索增强生成（RAG）由此应运而生。RAG是一种很有前景的方案：它让大模型可以读取并融合外部数据存储中的实时信息，减少依靠重训来更新模型知识的需求。但当用于RAG的外部知识库规模达到万亿token级别时，检索开销会急剧增大，拖累系统延迟、吞吐与能效。针对该问题，本文提出Hermes，一套算法-系统协同设计框架，专门解决大规模RAG系统的特有瓶颈。Hermes将知识库分片并分发到多节点，以此降低检索延迟；同时采用智能分层搜索，把查询动态路由到经过优化的知识库子集，提升吞吐与能效。基于开源RAG知识库与模型的实验表明：在万亿token级检索库上，Hermes在不损失检索质量的前提下，端到端延迟最高优化9.33倍，能效最高优化2.10倍。

## 英文关键词

Retrieval-Augmented Generation, Machine Learning Systems, Vector Search, Large Language Models, Retrieval and Ranking Models, k-Nearest Neighbor (kNN) Search

## 中文关键词

检索增强生成, 机器学习系统, 向量搜索, 大语言模型, 检索和排序模型, k 最近邻 (kNN) 搜索

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15192352)
- [代码仓库](https://github.com/S4AI-CornellTech/Hermes)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731076)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
