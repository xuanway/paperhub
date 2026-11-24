---
title: "Scalable Synthesis of distributed LLM workloads through Symbolic Tensor Graphs"
description: "ISCA 2026 · Session 10A · Scalable Synthesis of distributed LLM workloads through Symbolic Tensor Graphs"
tags:
  - "ISCA2026"
  - "Session 10A"
  - "LLM 5"
---

# Scalable Synthesis of distributed LLM workloads through Symbolic Tensor Graphs

**中文标题：** 基于符号化张量图的分布式 LLM 工作负载可扩展合成

**所属 Session：** [Session 10A](index.md) · [ISCA 2026](../index.md)

**作者：** Changhai Man, Joongun Park, Hanjiang Wu, Huan Xu, Srinivas Sridharan, Tushar Krishna

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Optimizing the performance of large language models (LLMs) on large-scale AI training and inference systems requires a scalable and expressive mechanism to model distributed workload execution. Such modeling is essential for pre-deployment system-level optimizations (e.g., parallelization strategies) and hardware design-space explorations. While recent efforts have proposed collecting execution traces from real systems, access to large-scale infrastructure remains limited to major cloud providers. Moreover, traces capturing execution on a specific platform cannot be easily adapted to study alternate software and/or hardware configurations, especially at scale. We introduce STAGE, a framework that synthesizes high-fidelity execution graphs to accurately model distributed AI workloads (including LLMs and MoEs). STAGE supports a comprehensive set of parallelization strategies, allowing users to systematically explore a wide spectrum of model architectures and system configurations. STAGE demonstrates its scalability by synthesizing high-fidelity LLM traces spanning over 128K GPUs, while preserving tensor-level accuracy in compute, memory, and communication. STAGE is publicy available at https://github.com/astra-sim/stage

## 中文摘要

在大规模AI训练和推理系统上优化大语言模型（LLM）的性能，需要一种可扩展且富有表达力的机制来建模分布式工作负载的执行。这种建模对于部署前的系统级优化（如并行化策略）和硬件设计空间探索至关重要。尽管最近的研究尝试从真实系统收集执行轨迹，但对大规模基础设施的访问仍仅限于主要云服务提供商。此外，捕获特定平台上执行情况的轨迹无法轻易适用于研究其他软件和/或硬件配置，尤其是在大规模场景下。我们提出了STAGE，一个合成高保真执行图来精确建模分布式AI工作负载（包括LLM和MoE）的框架。STAGE支持全面的并行化策略，允许用户系统地探索广泛的模型架构和系统配置。STAGE通过合成跨越128K以上GPU的高保真LLM轨迹，同时保持计算、内存和通信方面的张量级精度，展示了其可扩展性。STAGE已公开于https://github.com/astra-sim/stage。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：astra-sim/stage](https://github.com/astra-sim/stage)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2026](../index.md)
