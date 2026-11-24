---
title: "Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference"
description: "ISCA 2026 · Session 2A · Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference"
tags:
  - "ISCA2026"
  - "Session 2A"
  - "LLM 1"
---

# Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference

**中文标题：** 应对内存墙：长上下文智能体 LLM 推理的优化路径

**所属 Session：** [Session 2A](index.md) · [ISCA 2026](../index.md)

**作者：** Haoran Wu, Can Xiao, Jiayi Nie, Xuan Guo, Binglei Lou, Jeffrey T.H. Wong, Zhiwen Mo, Cheng Zhang, Przemyslaw Forys, Chengyang Ai, Timi Adeniran, Wayne Luk, Hongxiang Fan, Jianyi Cheng, Timothy M. Jones, Rika Antonova, Robert Mullins, Aaron Zhao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large Language Models (LLMs) serve as the core components of AI agents used across a wide range of applications, including enterprise workflow automation, software engineering, web automation, computer use, and research. These agentic LLM inference tasks are fundamentally different from traditional chatbot-focused inference — they often have much larger context lengths to capture complex, prolonged inputs, such as an entire webpage DOM or complicated tool call trajectories. This, in turn, generates significant off-chip memory traffic for hardware at the inference stage and causes the workload to be constrained by the two memory walls, namely the bandwidth and capacity walls, preventing the compute units from achieving high utilization. In this paper, we introduce PLENA, a hardware–software co-designed system that applies three core optimization pathways. PLENA features a novel flattened systolic-array architecture (Pathway 1) and efficient compute and memory units that support an asymmetric quantization scheme (Pathway 2). It also provides native support for FlashAttention (Pathway 3). In addition, PLENA is developed with a complete software–hardware stack, including a custom ISA, a compiler, a transaction-level simulator, and an automated design-space exploration flow. Experimental results show that PLENA delivers up to 2.23× and 4.70× higher throughput than the A100 GPU and TPU v6e, respectively, under identical multiplier counts and memory configurations during LLaMA agentic inference. PLENA also achieves up to 4.04× higher energy efficiency than the A100 GPU.

## 中文摘要

大语言模型（LLM）是 AI 智能体在企业工作流自动化、软件工程、网页自动化、计算机使用和研究等广泛应用中的核心组件。这类智能体 LLM 推理任务与传统面向聊天机器人的推理有根本不同——它们通常需要更长的上下文长度来容纳复杂且持续时间较长的输入，例如完整网页 DOM 或复杂的工具调用轨迹。这反过来会在推理阶段为硬件带来大量片外内存流量，并使工作负载受两类内存墙约束，即带宽墙和容量墙，从而妨碍计算单元达到高利用率。本文提出 PLENA，这是一种采用三条核心优化路径的软硬件协同设计系统。PLENA 具有新颖的扁平化脉动阵列架构（路径 1），以及支持非对称量化方案的高效计算和存储单元（路径 2）。它还原生支持 FlashAttention（路径 3）。此外，PLENA 配备了完整的软硬件技术栈，包括自定义 ISA、编译器、事务级模拟器和自动化设计空间探索流程。实验结果表明，在 LLaMA 智能体推理期间、乘法器数量和内存配置相同的条件下，PLENA 相比 A100 GPU 和 TPU v6e 的吞吐量最高分别达到 2.23× 和 4.70×。PLENA 相比 A100 GPU 的能效最高提升 4.04×。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：AICrossSim/PLENA](https://github.com/AICrossSim/PLENA)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2026](../index.md)
