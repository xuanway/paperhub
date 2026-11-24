---
title: "DIP: Efficient Large Multimodal Model Training with Dynamic Interleaved Pipeline"
description: "ASPLOS 2026 · Session 2A · DIP：基于动态交错流水线的高效大型多模态模型训练"
tags:
  - "ASPLOS2026"
  - "Session 2A"
  - "LLM Training Systems"
---

# DIP: Efficient Large Multimodal Model Training with Dynamic Interleaved Pipeline

**中文标题：** DIP：基于动态交错流水线的高效大型多模态模型训练

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhenliang Xue (Shanghai Jiao Tong University), Hanpeng Hu (StepFun), Xing Chen (StepFun), Yimin Jiang (StepFun), Yixin Song (Shanghai Jiao Tong University, Zenergize AI), Zeyu Mi (Shanghai Jiao Tong University, Zenergize AI), Yibo Zhu (StepFun), Daxin Jiang (StepFun), Yubin Xia (Shanghai Jiao Tong University), Haibo Chen (Shanghai JiaoTong University)

**单位：** Shanghai Jiao Tong University；StepFun；Shanghai Jiao Tong University, Zenergize AI；Shanghai JiaoTong University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790154) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large multimodal models (LMMs) have demonstrated excellent capabilities in both understanding and generation tasks with various modalities. While these models can accept flexible combinations of input data, their training efficiency suffers from two major issues: pipeline stage imbalance caused by heterogeneous model architectures, and training data dynamicity stemming from the diversity of multimodal data. In this paper, we present DIP, a dynamic and modality-aware pipeline scheduling framework designed for LMM training. DIP tackles the challenge of dynamic imbalance via two key techniques: (1) separating computations of different modalities into dedicated pipeline segments to balance workloads within a continuous set of stages; (2) dynamically splitting input data into finer-grained, modality-specific submicrobatches to balance workloads across these segments. By asynchronously generating pipeline schedules on idle CPU resources during training, DIP dynamically tailors stage executions to each input batch without stalling the training process. We validate DIP on a diverse set of five LMMs, ranging from 12B to 94B parameters and including vision-language and diffusion models. Experimental results show that our system achieves up to 97.3% higher throughput compared to state-of-the-art systems, demonstrating strong adaptability to fluctuating multimodal training workloads.

## 中文摘要

大型多模态模型（LMM）在多种模态的理解与生成任务中均展现出卓越能力。尽管这些模型能够接受灵活的输入数据组合，但其训练效率受到两大问题的困扰：异构模型架构导致的流水线阶段不均衡，以及多模态数据多样性带来的训练数据动态性。本文提出 DIP，一个面向 LMM 训练的动态、模态感知流水线调度框架。DIP 通过两项关键技术应对动态不均衡的挑战：(1) 将不同模态的计算分离到专用的流水线段中，以在一组连续的阶段内平衡负载；(2) 将输入数据动态切分为更细粒度、模态特定的子微批，以在这些段之间平衡负载。通过在训练期间利用空闲的 CPU 资源异步生成流水线调度，DIP 能够为每个输入批次动态定制阶段执行，而不会阻塞训练过程。我们在五个 LMM 上验证了 DIP，这些模型参数量从 12B 到 94B，涵盖视觉-语言模型和扩散模型。实验结果表明，与最先进的系统相比，我们的系统实现了最高 97.3% 的吞吐量提升，展现出对波动的多模态训练负载的强适应性。

## 英文关键词

Large-Scale Training; Large Multimodal Models; Distributed Systems; Simulation

## 中文关键词

大规模训练；大型多模态模型；分布式系统；仿真

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790154)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2026](../index.md)
