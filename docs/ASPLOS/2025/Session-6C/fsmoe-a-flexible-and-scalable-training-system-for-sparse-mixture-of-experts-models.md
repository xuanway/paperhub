---
title: "FSMoE: A Flexible and Scalable Training System for Sparse Mixture-of-Experts Models"
description: "ASPLOS 2025 · Session 6C · FSMoE：面向稀疏混合专家模型的灵活可扩展训练系统"
tags:
  - "ASPLOS2025"
  - "Session 6C"
  - "Mixture of Experts"
---

# FSMoE: A Flexible and Scalable Training System for Sparse Mixture-of-Experts Models

**中文标题：** FSMoE：面向稀疏混合专家模型的灵活可扩展训练系统

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xinglin Pan (The Hong Kong University of Science and Technology (Guangzhou)), Wenxiang Lin (Harbin Institute of Technology, Shenzhen), Lin Zhang (Hong Kong University of Science and Technology), Shaohuai Shi (Harbin Institute of Technology, Shenzhen), Zhenheng Tang (The Hong Kong University of Science and Technology), Rui Wang (The Hong Kong University of Science and Technology (Guangzhou)), Bo Li (Hong Kong University of Science and Technology), Xiaowen Chu (The Hong Kong University of Science and Technology (Guangzhou),Hong Kong University of Science and Technology)

**单位：** Guangzhou；Harbin Institute of Technology, Shenzhen；Hong Kong University of Science and Technology；The Hong Kong University of Science and Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707272) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recent large language models (LLMs) have tended to leverage sparsity to reduce computations, employing the sparsely activated mixture-of-experts (MoE) technique. MoE introduces four modules, including token routing, token communication, expert computation, and expert parallelism, that impact model quality and training efficiency. To enable versatile usage of MoE models, we introduce FSMoE, a flexible training system optimizing task scheduling with three novel techniques: 1) Unified abstraction and online profiling of MoE modules for task scheduling across various MoE implementations. 2) Co-scheduling intra-node and inter-node communications with computations to minimize communication overheads. 3) To support near-optimal task scheduling, we design an adaptive gradient partitioning method for gradient aggregation and a schedule to adaptively pipeline communications and computations. We conduct extensive experiments with configured MoE layers and real-world MoE models on two GPU clusters. Experimental results show that 1) our FSMoE supports four popular types of MoE routing functions and is more efficient than existing implementations (with up to a 1.42× speedup), and 2) FSMoE outperforms the state-of-the-art MoE training systems (DeepSpeed-MoE and Tutel) by 1.18×-1.22× on 1458 MoE layers and 1.19×-3.01× on real-world MoE models based on GPT-2 and Mixtral using a popular routing function.

## 中文摘要

近期的大语言模型（LLM）倾向于利用稀疏性来减少计算量，采用稀疏激活的混合专家（MoE）技术。MoE 引入了四个模块，包括 token 路由、token 通信、专家计算和专家并行，它们会影响模型质量与训练效率。为使 MoE 模型能够被灵活使用，我们提出 FSMoE，一个借助三项新技术优化任务调度的灵活训练系统：1）对 MoE 模块进行统一抽象与在线性能画像，以支持跨多种 MoE 实现的任务调度。2）将节点内与节点间通信同计算协同调度，以最小化通信开销。3）为支持近乎最优的任务调度，我们设计了一种用于梯度聚合的自适应梯度划分方法，以及一个能够自适应地对通信与计算进行流水化的调度方案。我们在两个 GPU 集群上使用配置的 MoE 层和真实 MoE 模型进行了大量实验。实验结果表明：1）我们的 FSMoE 支持四种流行的 MoE 路由函数，并且比现有实现更高效（最高 1.42 倍加速）；2）在使用一种流行路由函数时，FSMoE 在 1458 个 MoE 层上比最先进的 MoE 训练系统（DeepSpeed-MoE 和 Tutel）快 1.18×-1.22×，在基于 GPT-2 和 Mixtral 的真实 MoE 模型上快 1.19×-3.01×。

## 英文关键词

Distributed Deep Learning; Large Language Model; Mixture-of-Experts; Training System; Scheduling

## 中文关键词

分布式深度学习；大语言模型；混合专家；训练系统；调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707272)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2025](../index.md)
