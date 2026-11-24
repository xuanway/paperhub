---
title: "WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips"
description: "ISCA 2025 · Session 1A · WSC-LLM: 面向Wafer-scale芯片的高效LLM服务与体系结构协同探索"
tags:
  - "ISCA2025"
  - "Session 1A"
  - "ML Accelerators I"
---

# WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips

**中文标题：** WSC-LLM: 面向Wafer-scale芯片的高效LLM服务与体系结构协同探索

**所属 Session：** [Session 1A](index.md) · [ISCA 2025](../index.md)

**作者：** Zheng Xu, Dehao Kong, Jinxi Li, Jiaxin Liu, Jingxiang Hou, Xu Dai, Chao Li, Shaojun Wei, Yang Hu, Shouyi Yin

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731101) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The deployment of large language models (LLMs) imposes significant demands on computing, memory, and communication resources. Wafer-scale technology enables the high-density integration of multiple single-die chips with high-speed Die-to-Die (D2D) interconnections, presenting a promising solution to meet these demands arising from LLMs. However, given the limited wafer area, a trade-off needs to be made among computing, storage, and communication resources. Maximizing the benefits and minimizing the drawbacks of wafer-scale technology is crucial for enhancing the performance of LLM service systems, which poses challenges to both architecture and scheduling. Unfortunately, existing methods cannot effectively address these challenges.

To bridge the gap, we propose WSC-LLM, an architecture and scheduling co-exploration framework. We first define a highly configurable general hardware template designed to explore optimal architectural parameters for wafer-scale chips. Based on it, we capitalize on the high D2D bandwidth and fine-grained operation advantages inherent to wafer-scale chips to investigate optimal disaggregated scheduling strategies, effectively addressing the highly dynamic demands of LLM workloads. Compared to the state-of-the-art (SOTA) LLM service systems, WSC-LLM can achieve an average overall performance improvement of 3.12×across various LLM models and datasets. Moreover, we leverage WSC-LLM to reveal intriguing insights about wafer-scale architecture design and the execution of LLM workloads.

## 中文摘要

大语言模型 (LLM) 的部署对计算、内存和通信资源提出了很高的要求。晶圆级技术实现了多个单裸片芯片与高速芯片间 (D2D) 互连的高密度集成，为满足大语言模型提出的这些需求提供了一种有前景的解决方案。然而，考虑到晶圆面积有限，需要在计算、存储和通信资源之间进行权衡。最大化晶圆级技术的优势并降低其局限带来的影响对于提高LLM服务系统的性能至关重要，这对架构和调度都提出了挑战。不幸的是，现有方法无法有效应对这些挑战。为了弥补这一差距，我们提出了 WSC-LLM，一种架构和调度协同探索框架。我们首先定义一个高度可配置的通用硬件模板，旨在探索晶圆级芯片的最佳架构参数。

在此基础上，我们利用晶圆级芯片固有的高D2D带宽和细粒度操作优势，研究最佳的解耦调度策略，有效解决LLM工作负载的高度动态需求。与最先进（SOTA）的LLM服务系统相比，WSC-LLM在各种LLM模型和数据集上可以实现平均3.12倍的整体性能提升。此外，我们利用 WSC-LLM 揭示有关晶圆级架构设计和 LLM 工作负载执行的有趣见解。

## 英文关键词

Large Language Models, Wafer-Scale Chips, Architecture-Scheduling Co-Exploration, Disaggregated Scheduling

## 中文关键词

大语言模型, 晶圆级芯片, 架构与调度协同探索, 解耦调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731101)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2025](../index.md)
