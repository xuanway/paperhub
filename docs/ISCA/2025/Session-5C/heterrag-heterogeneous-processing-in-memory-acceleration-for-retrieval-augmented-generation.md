---
title: "HeterRAG: Heterogeneous Processing-in-Memory Acceleration for Retrieval-augmented Generation"
description: "ISCA 2025 · Session 5C · HeterRAG: 异构存内计算加速检索增强生成"
tags:
  - "ISCA2025"
  - "Session 5C"
  - "Processing-in-Memory"
---

# HeterRAG: Heterogeneous Processing-in-Memory Acceleration for Retrieval-augmented Generation

**中文标题：** HeterRAG: 异构存内计算加速检索增强生成

**所属 Session：** [Session 5C](index.md) · [ISCA 2025](../index.md)

**作者：** Chaoqiang Liu, Haifeng Liu, Dan Chen, Yu Huang, Yi Zhang, Wenjing Xiao, XIAOFEI LIAO, Hai Jin

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731089) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

By integrating external knowledge bases, Retrieval-augmented Gen- eration (RAG) enhances natural language generation for knowledge- intensive scenarios and specialized domains, producing content that is both more informative and personalized. RAG systems typically consist of two fundamental stages: retrieval and generation. The retrieval stage experiences low bandwidth utilization due to its random and irregular memory access patterns. Meanwhile, the generation stage is also constrained by memory bandwidth limita- tions, which arise from involving a significant number of General Matrix-Vector Multiplications (GEMV) operations. These two stages collectively lead to memory bottlenecks within RAG systems. Re- cent efforts leverage HBM-based Processing-in-Memory (PIM) to accelerate conventional Large Language Models (LLMs). However, the retrieval stage incurs substantial storage overhead due to the need to maintain large-scale knowledge bases, resulting in a capac- ity bottleneck. Solely relying on HBM-based PIM in RAG is both costly and insufficient to meet the capacity demands. Fortunately, DIMM-based PIM provides a low-cost, high-capacity alternative that complements HBM. In this work, we propose HeterRAG, a novel heterogeneous PIM acceleration system for RAG. It combines HBM-based PIM and DIMM-based PIM to achieve high perfor- mance, energy efficiency, and low hardware cost. HeterRAG uses HBM-based PIM for the generation stage to meet bandwidth needs and DIMM-based PIM for the retrieval stage to satisfy memory capacity requirements. To further improve performance, HeterRAG incorporates three software–hardware co-optimization techniques: locality-aware retrieval, locality-aware generation, and fine-grained parallel pipelining. Experimental results demonstrate that, com- pared to RAG systems deployed on Intel Xeon CPUs and NVIDIA GPUs, HeterRAG achieves up to 26.5×higher throughput, up to 27.6×lower latency, and up to 2.8×greater energy efficiency.

## 中文摘要

检索增强生成（RAG）通过接入外部知识库，提升知识密集型场景与专业领域下的文本生成能力，输出内容信息量更足、更贴合个性化需求。RAG系统主要包含两个阶段：检索阶段与生成阶段。检索阶段的访存随机、不规则，带宽利用率低；生成阶段包含大量通用矩阵向量乘法（GEMV），同样受内存带宽约束。两个阶段共同造成RAG系统的内存瓶颈。
已有研究利用基于HBM的存内计算（PIM）加速传统大语言模型。但检索阶段需要维护大规模知识库，存储开销巨大，带来容量瓶颈。仅依靠HBM-PIM成本高昂，也无法满足容量需求。而基于DIMM的PIM成本低、容量大，可以作为HBM的补充。
本文提出HeterRAG，面向RAG的异构PIM加速系统，融合HBM-PIM与DIMM-PIM，同时兼顾高性能、高能效与低成本。HeterRAG使用HBM-PIM承载生成阶段，满足高带宽需求；使用DIMM-PIM承载检索阶段，满足大容量需求。为进一步提升性能，HeterRAG配套三项软硬件协同优化：感知局部性的检索、感知局部性的生成、细粒度并行流水线。
实验结果表明，对比部署在Intel至强CPU与NVIDIA GPU上的RAG系统，HeterRAG最高可将吞吐提升26.5倍、延迟降低至原来的1/27.6、能效提升2.8倍。

## 英文关键词

Retrieval-augmented generation, Large language models, Approximate nearest neighbor search, Processing-in-memory, DIMM, HBM

## 中文关键词

检索增强生成, 大语言模型, 近似最近邻搜索, 存内计算, 双列直插内存模块, 高带宽内存

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731089)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2025](../index.md)
