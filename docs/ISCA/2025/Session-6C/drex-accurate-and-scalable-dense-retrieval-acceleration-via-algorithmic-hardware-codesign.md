---
title: "DReX: Accurate and Scalable Dense Retrieval Acceleration via Algorithmic-Hardware Codesign"
description: "ISCA 2025 · Session 6C · DReX: 算法-硬件协同的高精度可扩展稠密检索加速"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# DReX: Accurate and Scalable Dense Retrieval Acceleration via Algorithmic-Hardware Codesign

**中文标题：** DReX: 算法-硬件协同的高精度可扩展稠密检索加速

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Derrick Quinn, E. Ezgi Y?cel, Martin Prammer, Zhenxing Fan, Kevin Skadron, Jignesh Patel, Jos? F. Mart?nez, Mohammad Alian

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731079) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Retrieval-augmented generation (RAG) supplements large language models (LLM) with information retrieval to ensure up-to-date, ac- curate, factually grounded, and contextually relevant outputs. RAG implementations often employ dense retrieval methods and approx- imate k-nearest neighbor search (ANNS). Unfortunately, ANNS is inherently dataset-specific and prone to low recall, potentially lead- ing to inaccuracies when irrelevant or incomplete context is passed to the LLM. Furthermore, sending numerous imprecise documents to the LLM for generation can significantly degrade performance compared to processing a smaller set of accurate documents. We propose DReX, a dataset-agnostic, accurate, and scalable Dense Retrieval Acceleration scheme enabled through a novel algorithmic-hardware co-design. We leverage in-DRAM logic to enable early filtering of embedding vectors far from the query vec- tor. An outside-DRAM near-memory accelerator then performs exact nearest neighbor searches on the remaining filtered embed- dings. This resulting design minimizes off-chip data movement and ensures precise and efficient retrieval, laying the foundation for robust and performant RAG systems that are broadly applica- ble. Our evaluation shows that DReX delivers a 6.2-7×reduction in time-to-first-token for a representative RAG application over a state-of-the-art mechanism while incurring reasonable area and power overheads in the memory subsystem.

## 中文摘要

检索增强生成（RAG）借助信息检索为大语言模型（LLM）补充知识，保障输出内容时效性、准确性、事实可靠性与上下文相关性。RAG通常采用稠密检索与近似k近邻搜索（ANNS）。但近似k近邻搜索本身和数据集强绑定，召回率容易偏低；如果送入大模型的上下文无关、信息残缺，就会造成回答错误。此外，向大模型送入大量低质量文档用于生成，相比送入少量精准文档，会显著拖慢性能。

本文提出DReX，一种不依赖数据集、高精度、可扩展的稠密检索加速方案，基于全新算法-硬件协同设计实现。该方案利用DRAM内部逻辑，提前过滤和查询向量距离较远的嵌入向量；再由DRAM外部的近内存加速器，对过滤后剩下的嵌入向量执行精确最近邻搜索。该架构最大限度减少片外数据搬运，实现精准高效检索，为通用性强、性能稳健的RAG系统打下基础。
评测结果表明：在一款代表性RAG应用上，对比前沿方案，DReX的首token延迟降低6.2–7倍，同时内存子系统仅带来合理的面积与功耗开销。

## 英文关键词

Dense retrieval, algorithm-hardware co-design, acceleration, scalability

## 中文关键词

稠密检索, 检索增强生成, 近存加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731079)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
