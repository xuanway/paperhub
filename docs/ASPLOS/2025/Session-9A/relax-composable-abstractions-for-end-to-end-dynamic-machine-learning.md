---
title: "Relax: Composable Abstractions for End-to-End Dynamic Machine Learning"
description: "ASPLOS 2025 · Session 9A · Relax：面向端到端动态机器学习的一组可组合抽象"
tags:
  - "ASPLOS2025"
  - "Session 9A"
  - "ML Compilers"
---

# Relax: Composable Abstractions for End-to-End Dynamic Machine Learning

**中文标题：** Relax：面向端到端动态机器学习的一组可组合抽象

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ruihang Lai (Carnegie Mellon University), Junru Shao (OpenAI), Siyuan Feng (Shanghai Jiao Tong University), Steven Lyubomirsky (NVIDIA), Bohan Hou (Carnegie Mellon University), Wuwei Lin (OpenAI), Zihao Ye (University of Washington), Hongyi Jin (Carnegie Mellon University), Yuchen Jin (Hyperbolic), Jiawei Liu (University of Illinois Urbana-Champaign), Lesheng Jin (Hyperbolic), Yaxing Cai (NVIDIA), Ziheng Jiang (ByteDance), Yong Wu (NVIDIA), Sunghyun Park (NVIDIA), Prakalp Srivastava (Netflix), Jared Roesch (NVIDIA), Todd C. Mowry (Carnegie Mellon University), Tianqi Chen (Carnegie Mellon University,NVIDIA)

**单位：** Carnegie Mellon University；OpenAI；Shanghai Jiao Tong University；NVIDIA；University of Washington；Hyperbolic；University of Illinois Urbana-Champaign；ByteDance；Netflix；Carnegie Mellon University,NVIDIA

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716249) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Dynamic shape computations have become critical in modern machine learning workloads, especially in emerging large language models. The success of these models has driven the demand for their universal deployment across a diverse set of backend environments. In this paper, we present Relax, a compiler abstraction for optimizing end-toend dynamic machine learning workloads. Relax introduces a cross-level abstraction that encapsulates computational graphs, loop-level tensor programs and external libraries calls in a single representation. Relax also introduces firstclass symbolic shape annotations to track dynamic shape computations globally across the program, enabling dynamic shape–aware cross-level optimizations. We build an end-toend compilation framework using the proposed approach. to optimize dynamic shape models. Experimental results on LLMs show that Relax delivers performance competitive with state-of-the-art systems across various GPUs and enables deployment of emerging models to a broader set of emerging environments, including mobile phones, embedded devices, and web browsers.

## 中文摘要

动态形状计算在现代机器学习工作负载中已变得至关重要，尤其是在新兴的大语言模型中。这些模型的成功推动了将其通用部署到多样化后端环境的需求。在本文中，我们提出 Relax，一种用于优化端到端动态机器学习工作负载的编译器抽象。Relax 引入跨层抽象，将计算图、循环级张量程序以及对外部库的调用封装在单一表示之中。Relax 还引入一等公民式的符号形状标注，以在整个程序中全局跟踪动态形状计算，从而使动态形状感知的跨层优化成为可能。我们使用所提出的方法构建了一个端到端编译框架，用于优化动态形状模型。在 LLM 上的实验结果表明，Relax 在各种 GPU 上都提供了与最先进系统相竞争的性能，并使新兴模型能够部署到更广泛的新兴环境中，包括移动电话、嵌入式设备和网页浏览器。

## 英文关键词

Machine Learning Compiler; Dynamic-Shape Machine Learning

## 中文关键词

机器学习编译器；动态形状机器学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716249)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2025](../index.md)
