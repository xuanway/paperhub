---
title: "REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing"
description: "ISCA 2025 · Session 6C · REIS: 高性能高能效存储内检索系统"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing

**中文标题：** REIS: 高性能高能效存储内检索系统

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Kangqi Chen, Rakesh Nadig, Nika Mansouri Ghiasi, Yu Liang, Haiyu Mao, Jisung Park, Manos Frouzakis, Mohammad Sadrosadati, Onur Mutlu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731116) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large Language Models (LLMs) face an inherent challenge: their knowledge is confined to the data that they have been trained on. This limitation, combined with the significant cost of retraining ren- ders them incapable of providing up-to-date responses. To overcome these issues, Retrieval-Augmented Generation (RAG) complements the static training-derived knowledge of LLMs with an external knowledge repository. RAG consists of three stages: (i) indexing, which creates a database that facilitates similarity search on text embeddings, (ii) retrieval, which, given a user query, searches and retrieves relevant data from the database and (iii) generation, which uses the user query and the retrieved data to generate a response. 

The retrieval stage of RAG in particular becomes a significant performance bottleneck in inference pipelines. In this stage, (i) a given user query is mapped to an embedding vector and (ii) an Approximate Nearest Neighbor Search (ANNS) algorithm searches for the most semantically similar embedding vectors in the database to identify relevant items. Due to the large database sizes, ANNS incurs significant data movement overheads between the host and the storage system. To alleviate these overheads, prior works pro- pose In-Storage Processing (ISP) techniques that accelerate ANNS workloads by performing computations inside the storage system. However, existing works that leverage ISP for ANNS (i) employ algorithms that are not tailored to ISP systems, (ii) do not acceler- ate data retrieval operations for data selected by ANNS, and (iii) introduce significant hardware modifications to the storage system, limiting performance and hindering their adoption.

We propose REIS, the first Retrieval system tailored for RAG with In-Storage processing that addresses the limitations of existing im- plementations with three key mechanisms. First, REIS employs a database layout that links database embedding vectors to their associated documents, enabling efficient retrieval. Second, it en- ables efficient ANNS by introducing an ISP-tailored algorithm and data placement technique that: (i) distributes embeddings across all planes of the storage system to exploit parallelism, and (ii) employs a lightweight Flash Translation Layer (FTL) to improve performance. Third, REIS leverages an ANNS engine that uses the existing com- putational resources inside the storage system, without requiring hardware modifications. The three key mechanisms form a cohesive framework that largely enhances both the performance and energy efficiency of RAG pipelines. Compared to a high-end server-grade system, REIS improves the performance (energy efficiency) of the retrieval stage by an average of 13×(55×). REIS offers improved performance against existing ISP-based ANNS accelerators, without introducing any hardware modifications, enabling easier adoption for RAG pipelines.

## 中文摘要

大语言模型（LLM）存在一个固有难题：模型知识仅限于训练数据。受该局限，再加上重训成本高昂，大模型很难给出实时更新的回答。检索增强生成（RAG）由此应运而生，它借助外部知识库补充大模型静态的训练知识。RAG分为三个阶段：（1）索引阶段，构建支持文本嵌入向量相似度检索的数据库；（2）检索阶段，根据用户查询，从库中查找并取出相关数据；（3）生成阶段，结合用户查询与检索到的内容生成回复。

其中检索阶段成为推理链路里显著的性能瓶颈。该阶段分为两步：先将用户查询映射为嵌入向量，再通过近似最近邻搜索（ANNS）在库中寻找语义最相近的嵌入向量，筛选相关条目。当数据库规模巨大时，ANNS会带来繁重的主机与存储之间的数据搬运开销。为缓解该问题，已有研究提出存储内处理（ISP）方案，在存储设备内部完成计算以加速ANNS负载。但现有面向ANNS的ISP方案存在三点不足：（1）算法没有针对ISP系统做适配；（2）不对ANNS筛选命中后的文档读取做加速；（3）对存储硬件改动大，制约性能，也难以落地部署。

本文提出REIS，首个面向RAG的存储内处理检索系统，通过三项核心机制解决现有方案的缺陷。第一，REIS采用将嵌入向量和对应文档绑定的数据库布局，实现高效读取；第二，提出适配ISP的算法与数据放置策略：把嵌入向量分散到存储所有平面以挖掘并行度，并使用轻量闪存转换层（FTL）提升性能；第三，REIS复用存储内部原有计算资源搭建ANNS引擎，不需要修改硬件。
这三项机制构成完整框架，大幅提升RAG链路的性能与能效。对比高端服务器系统，REIS检索阶段平均性能提升13倍，能效提升55倍。对比已有基于ISP的ANNS加速器，REIS性能更优，且无需硬件改动，更容易集成到RAG流水线中。

## 英文关键词

Retrieval-Augmented Generation, In-Storage Processing, SSD, LLM

## 中文关键词

检索增强生成, 存储内处理, SSD, LLM

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731116)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
