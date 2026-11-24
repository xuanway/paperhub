---
title: "CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory"
description: "ASPLOS 2025 · Session 6C · CoServe：面向有限内存的高效多专家协作（CoE）模型推理"
tags:
  - "ASPLOS2025"
  - "Session 6C"
  - "Mixture of Experts"
---

# CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory

**中文标题：** CoServe：面向有限内存的高效多专家协作（CoE）模型推理

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiashun Suo (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Xiaojian Liao (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Limin Xiao (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Li Ruan (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Jinquan Wang (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Xiao Su (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University), Zhisheng Huo (State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University)

**单位：** State Key Laboratory of CCSE and School of Computer Science and Engineering, Beihang University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715986) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Large language models like GPT-4 are resource-intensive, but recent advancements suggest that smaller, specialized experts can outperform the monolithic models on specific tasks. The Collaboration-of-Experts (CoE) approach integrates multiple expert models, improving the accuracy of generated results and offering great potential for precision-critical applications, such as automatic circuit board quality inspection. However, deploying CoE serving systems presents challenges to memory capacity due to the large number of experts required, which can lead to significant performance overhead from frequent expert switching across different memory and storage tiers. We propose CoServe, an efficient CoE model serving system on heterogeneous CPU and GPU with limited memory. CoServe reduces unnecessary expert switching by leveraging expert dependency, a key property of CoE inference. CoServe introduces a dependency-aware request scheduler and dependency-aware expert management for efficient inference. It also introduces an offline profiler to automatically find optimal resource allocation on various processors and devices. In real-world intelligent manufacturing workloads, CoServe achieves 4.5× to 12× higher throughput compared to state-of-the-art systems.

## 中文摘要

像 GPT-4 这样的大语言模型资源消耗巨大，但近期进展表明，更小的专用专家模型可以在特定任务上胜过单体模型。多专家协作（Collaboration-of-Experts，CoE）方法集成了多个专家模型，提升了生成结果的准确率，并为精度关键型应用（例如电路板自动质量检测）提供了巨大潜力。然而，由于所需的专家数量众多，部署 CoE 服务系统对内存容量提出了挑战，这会导致在不同内存与存储层级之间频繁切换专家，从而带来显著的性能开销。我们提出 CoServe，一个在内存有限的异构 CPU 与 GPU 上高效服务 CoE 模型的系统。CoServe 利用专家依赖（expert dependency）这一 CoE 推理的关键特性来减少不必要的专家切换。CoServe 引入了依赖感知的请求调度器与依赖感知的专家管理，以实现高效推理。它还引入了一个离线分析器（profiler），用于自动寻找各种处理器与设备上的最优资源分配。在真实智能制造工作负载中，与最先进的系统相比，CoServe 的吞吐量提高了 4.5 倍至 12 倍。

## 英文关键词

Collaboration-of-Experts (CoE); ML Inference; Edge Computing

## 中文关键词

多专家协作（CoE）；机器学习推理；边缘计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715986)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2025](../index.md)
