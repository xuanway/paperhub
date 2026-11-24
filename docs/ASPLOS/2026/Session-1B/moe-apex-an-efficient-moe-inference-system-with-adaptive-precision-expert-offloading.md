---
title: "MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading"
description: "ASPLOS 2026 · Session 1B · MoE-APEX：一种采用自适应精度专家卸载的高效 MoE 推理系统"
tags:
  - "ASPLOS2026"
  - "Session 1B"
  - "LLM Serving: Latency & Scheduling"
---

# MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading

**中文标题：** MoE-APEX：一种采用自适应精度专家卸载的高效 MoE 推理系统

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Peng Tang (Shanghai Jiaotong University), Jiacheng Liu (CUHK), Xiaofeng Hou (Shanghai Jiao Tong University), Yifei Pu (Shanghai Jiao Tong University), Jing Wang (Shanghai Jiao Tong University), Pheng-Ann Heng (CUHK), Chao Li (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

**单位：** Shanghai Jiaotong University；CUHK；Shanghai Jiao Tong University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790187) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Mixture-of-experts (MoE) architectures enable scalable Large Language Models (LLMs) with reduced computational overhead, yet their deployment on memory-constrained edge devices is hindered by substantial memory demands. Traditional expert-offloading techniques mitigate memory constraints but often significantly increase inference latency. We introduce MoE-APEX, an Adaptive Precision EXpert offloading system that optimizes MoE inference for edge architectures by dynamically managing expert precision. Our core innovation is to replace less critical cache-miss experts with low-precision variants, reducing loading latency while maintaining accuracy. MoE-APEX introduces three innovative techniques that map the natural hierarchy of MoE computation: (1) a token-level dynamic expert loading mechanism, (2) a layer-level adaptive expert prefetching technique, and (3) a sequence-level cost-aware expert caching policy. These innovations enable MoE-APEX to leverage the benefits of mixed-precision expert inference fully. Implemented atop Llama.cpp, MoE-APEX achieves decoding speedups ranging from 1.34× to 9.75× compared to state-of-the-art MoE offloading systems across diverse edge devices, offering a robust solution for efficient MoE deployment in resource-constrained environments.

## 中文摘要

专家混合（MoE）架构使大型语言模型（LLM）能够以更低的计算开销实现可扩展性，但它们在内存受限的边缘设备上的部署受到巨大内存需求的阻碍。传统的专家卸载技术缓解了内存约束，却往往显著增加推理延迟。我们提出 MoE-APEX，一种自适应精度专家卸载系统，通过动态管理专家精度来优化面向边缘架构的 MoE 推理。我们的核心创新是用低精度变体替换较不关键的缓存未命中专家，在保持精度的同时降低加载延迟。MoE-APEX 引入三项与 MoE 计算的自然层级相对应的创新技术：(1) token 级动态专家加载机制，(2) 层级自适应专家预取技术，以及 (3) 序列级代价感知专家缓存策略。这些创新使 MoE-APEX 能够充分获得混合精度专家推理的收益。MoE-APEX 在 Llama.cpp 之上实现，在多种边缘设备上相比最先进的 MoE 卸载系统取得 1.34× 至 9.75× 的解码加速，为资源受限环境中的高效 MoE 部署提供了稳健的解决方案。

## 英文关键词

Edge Computing; Inference Acceleration; Parameter Offloading

## 中文关键词

边缘计算；推理加速；参数卸载

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790187)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2026](../index.md)
