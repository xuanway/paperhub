---
title: "AIPerf: Meta's Performance Modeling and HW/SW Co-Design Framework for Datacenter-Scale LLM Training"
description: "MICRO 2026 · Session 1C · AIPerf：Meta 面向数据中心规模大语言模型训练的性能建模与软硬件协同设计框架"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "HW-SW Co-design"
  - "LLM Training"
---

# AIPerf: Meta's Performance Modeling and HW/SW Co-Design Framework for Datacenter-Scale LLM Training

**中文标题：** AIPerf：Meta 面向数据中心规模大语言模型训练的性能建模与软硬件协同设计框架

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Pyeongsu Park, Hwijoon Lim, Seah Kim, Mustafa Ozdal, Yi-Chien Lin, Kevin Siu, Pavan Yalamanchili, Benjamin Ghaemmaghami, Yufeng Gu, Jongsoo Park, Joel Coburn, Paul Baumstarck, Shobhit Kanaujia, Chunqiang Tang

**来源：** MICRO 2026，pp. 222–236；[DOI](https://doi.org/10.1109/MICRO67795.2026.00031)

## 英文摘要

Co-designing large language models and infrastructure is a critical challenge at hyperscale. Because models evolve daily while hardware decisions require years of lead time, misalignments can cause significant inefficiencies in our AI ecosystem. This paper presents AIPerf, a performance-modeling framework designed to guide decisions throughout our six-phase model-hardware co-design lifecycle. We outline practical challenges at each phase—such as cross-platform competitive analysis, parallelism configuration, and workload-dependent rack decisions—and derive five core requirements for a production-grade modeling framework. We demonstrate how AIPerf meets these needs through five case studies, ranging from using headroom analysis to identify software optimization roadmaps to conducting what-if analysis for network topology and scale-up domain size. AIPerf has supported this lifecycle for years, directly informing our in-house AI chip design and frontier model training decisions.

## 中文摘要

共同设计大语言模型和基础设施是超大规模的一项关键挑战。由于模型每天都在发展，而硬件决策需要数年的准备时间，因此偏差可能会导致我们的人工智能生态系统效率严重低下。本文介绍了 AIPerf，这是一个性能建模框架，旨在指导整个六阶段模型-硬件​​协同设计生命周期的决策。我们概述了每个阶段的实际挑战，例如跨平台竞争分析、并行配置和依赖于工作负载的机架决策，并得出生产级建模框架的五个核心要求。我们通过五个案例研究展示了 AIPerf 如何满足这些需求，从使用余量分析来确定软件优化路线图，到对网络拓扑和扩展域大小进行假设分析。 AIPerf 多年来一直支持这个生命周期，直接为我们内部的 AI 芯片设计和前沿模型训练决策提供信息。

## 中文关键词

生成式人工智能；性能建模；并行计算；混合专家模型；软硬件协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
