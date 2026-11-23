---
title: "In-Storage Acceleration of Retrieval Augmented Generation as a Service"
description: "ISCA 2025 · Session 3C · 面向检索增强生成即服务的存内加速"
tags:
  - "ISCA2025"
  - "Session 3C"
  - "Storage"
---

# In-Storage Acceleration of Retrieval Augmented Generation as a Service

**中文标题：** 面向检索增强生成即服务的存内加速

**所属 Session：** [Session 3C](index.md) · [ISCA 2025](../index.md)

**作者：** Rohan Mahapatra, Harsha Santhanam, Christopher Priebe, Hanyang Xu, Hadi S. Esmaeilzadeh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731032) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Retrieval-augmented generation (RAG) services are rapidly gaining adoption in enterprise settings as they combine information retrieval systems (e.g., databases) with large language models (LLMs) to en- hance response generation and reduce hallucinations. By augment- inganLLM’sfixedpre-trainedknowledgewithreal-timeinformation retrieval, RAG enables models to effectively extend their context to large knowledge bases by selectively retrieving only the most rel- evant information. As a result, RAG provides the effect of dynamic updates to the LLM’s knowledge without requiring expensive and time-consuming retraining. While some deployments keep the entire database in memory, RAG services are increasingly shifting toward persistent storage to accommodate ever-growing knowledge bases, enhance utility, and improve cost-efficiency. However, this transition fundamentally reshapes the system’s performance profile: empirical analysis reveals that the Search & Retrieval phase emerges as the dominant contributor to end-to-end latency. This phase typically involves (1) running a smaller language model to generate query em- beddings, (2) executing similarity and relevance checks over varying data structures, and (3) performing frequent, long-latency accesses to persistent storage. To address this triad of challenges, we propose a metamorphic in-storage accelerator architecture that provides the necessary programmability to support diverse RAG algorithms, dynamic data structures, and varying computational patterns. The architecture also supports in-storage execution of smaller language models for query embedding generation while final LLM generation is executed on DGX A100 systems. Experimental results show up to 4.3×and 1.5×improvement in end-to-end throughput compared to conventional retrieval pipelines using Xeon CPUs with NVMe storage and A100 GPUs with DRAM, respectively.

## 中文摘要

检索增强生成（RAG）服务在企业场景中得到快速普及，它将信息检索系统（例如数据库）与大语言模型（LLM）结合，优化生成效果并降低幻觉问题。RAG借助实时检索到的信息来补充LLM固有的预训练知识，通过选择性提取相关性最高的信息，让模型能够把上下文有效扩展到大规模知识库。因此RAG可以实现模型知识的动态更新，无需开销巨大、耗时漫长的重新训练。部分部署方案会把整个数据库放在内存中，但随着知识库持续膨胀，RAG服务越来越多地转向持久化存储，以此提升容量、控制成本。然而该转变彻底改变了系统性能特征：实测分析表明，检索阶段成为端到端延迟的主要来源。该阶段一般包含三步：（1）运行轻量语言模型生成查询嵌入向量；（2）在不同数据结构上执行相似度与相关性校验；（3）频繁访问持久化存储，带来高延迟。针对这三重难题，本文提出一种可变形存储内加速器架构。该架构具备可编程能力，支持多样的RAG算法、动态数据结构以及不同的计算模式。该架构还支持在存储内部运行轻量语言模型，生成查询嵌入，而最终的LLM生成任务仍在DGX A100平台上执行。实验结果表明，对比基于Xeon CPU+NVMe存储、A100 GPU+DRAM的传统检索流水线，该方案端到端吞吐量最高分别提升4.3倍、1.5倍。

## 英文关键词

Retrieval-Augmented Generation, RAG, Large Language Models, LLM, In-Storage Acceleration, Specialized Accelerators

## 中文关键词

检索增强生成, RAG, 大语言模型, LLM, 存储内加速, 专用加速器

## 代码与研究制品

- [代码仓库](https://github.com/rohanmahapatra/ragx)
- [研究制品](https://zenodo.org/records/15092497)
- [代码仓库](https://github.com/he-actlab/ragx)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731032)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2025](../index.md)
