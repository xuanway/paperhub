---
title: "RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving"
description: "ISCA 2025 · Session 6A · RAGO：面向检索增强生成服务的系统化性能优化"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# RAGO: Systematic Performance Optimization for Retrieval-Augmented Generation Serving

**中文标题：** RAGO：面向检索增强生成服务的系统化性能优化

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Wenqi Jiang, Suvinay Subramanian, Cat Graves, Gustavo Alonso, Amir Yazdanbakhsh, Vidushi Dadu, Suvinay Subramanian

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731093) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Retrieval-augmented generation (RAG) is emerging as a popular approach for reliable LLM serving. However, efficient RAG serving remains an open challenge due to the rapid emergence of many RAG variants and the substantial differences in workload characteristics across them. This paper makes three fundamental contributions to advancing RAG serving. First, we introduce RAGSchema, a structured abstraction that captures the wide range of RAG algorithms, serving as a foundation for performance optimization. Second, we analyze several representative RAG workloads with distinct RAGSchema, revealing significant performance variability across these workloads. Third, to address this variability and meet diverse performance requirements, we propose RAGO (Retrieval-Augmented Generation Optimizer), a system optimization framework for efficient RAG serving. RAGO achieves up to a 2ˆincrease in QPS per chip and a 55% reduction in time-to-first-token latency compared to RAG systems built on LLM-system extensions.

## 中文摘要

检索增强生成（RAG）正在成为可靠部署大语言模型服务的主流方案。但RAG变体繁多、不同变体的负载特征差异巨大，高效的RAG服务部署仍是一个难题。本文围绕RAG服务优化做出三项核心贡献：第一，提出RAGSchema，一种结构化抽象，能够刻画各类RAG算法，作为性能优化的基础；第二，基于RAGSchema对多个代表性RAG负载开展分析，发现不同负载之间性能差异显著；第三，为应对这种性能波动、满足多样化性能需求，提出RAGO（Retrieval-Augmented Generation Optimizer），面向高效RAG服务的系统优化框架。对比基于大模型系统扩展搭建的RAG系统，RAGO单芯片每秒查询数（QPS）最高提升2倍，首token延迟降低55%。

## 英文关键词

Retrieval-Augmented Generation, Computer System, Computer Architecture, Large Language Model, Performance Optimization

## 中文关键词

检索增强生成, 计算机系统, 计算机体系结构, 大语言模型, 性能优化

## 代码与研究制品

- [代码仓库](https://github.com/google/rago)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731093)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
