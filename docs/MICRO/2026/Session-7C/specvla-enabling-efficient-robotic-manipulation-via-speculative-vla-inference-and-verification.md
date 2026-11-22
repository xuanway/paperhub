---
title: "SpecVLA: Enabling Efficient Robotic Manipulation via Speculative VLA Inference and Verification"
description: "MICRO 2026 · Session 7C · SpecVLA：通过推测式 VLA 推理与验证实现高效机器人操作"
tags:
  - "MICRO2026"
---

# SpecVLA: Enabling Efficient Robotic Manipulation via Speculative VLA Inference and Verification

**中文标题：** SpecVLA：通过推测式 VLA 推理与验证实现高效机器人操作

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Chunyu Qi, Zhuoran Song, Jian Weng, Haozhe Jiang, Xueyuan Liu, Naifeng Jing, Guanghui He, Xiaoyao Liang, Haibing Guan

**来源：** MICRO 2026，pp. 2593–2607；[DOI](https://doi.org/10.1109/MICRO67795.2026.00177)

## 英文摘要

Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in the field of embodied AI, but their high computational cost and limited predicted action length hinder real-time deployment. Although Dadu-Corki, a dedicated accelerator for efficient embodied AI, has been introduced, it does not exploit the inherent interaction patterns between the robot and its environment, which results in a relatively short predicted action length. We observe that robotic environments naturally alternate between active states—where precise actions are crucial—and inactive states—where actions have limited impact on task success. This insight enables a new scheduling opportunity: long-action-length speculative prediction in inactive states, paired with selective verification in active states. We propose SpecVLA, an algorithm–system co-design framework that adaptively balances action length, inference latency, and task reliability. On the algorithm side, SpecVLA introduces a state-aware VLA inference execution paradigm and a hardware-friendly construction of a smaller verification model (sVLA) using differential residuals and block-wise mixed-precision quantization. On the system side, we develop a heterogeneous architecture consisting of a GPU and a robotic-specific hardware module, along with a speculative dataflow that decouples VLA and sVLA through parallel execution. The hardware module integrates preprocessing, state prediction, and low-precision compute units into a single tightly coupled pipeline, eliminating redundant data movement and enabling low-latency verification. Comprehensive evaluations on OpenVLA and RDT across LIBERO and ManiSkill benchmarks show that SpecVLA achieves a 2.9x reduction in end-to-end latency while preserving task success rate. By enabling long-action-length speculative prediction with timely verification, SpecVLA achieves real-time robotic manipulation with both high efficiency and reliability.

## 中文摘要

视觉-语言-动作（VLA）模型在具身人工智能领域展现了卓越的能力，但其高计算成本和有限的预测动作长度阻碍了实时部署。尽管已经推出了高效具身人工智能的专用加速器Dadu-Corki，但它没有利用机器人与其环境之间的固有交互模式，这导致预测动作长度相对较短。我们观察到，机器人环境自然地在活动状态（精确的行动至关重要）和非活动状态（行动对任务成功的影响有限）之间交替。这种洞察力带来了新的调度机会：非活动状态下的长动作长度推测预测，与活动状态下的选择性验证相结合。我们提出了 SpecVLA，一种算法系统协同设计框架，可以自适应地平衡动作长度、推理时延和任务可靠性。在算法方面，SpecVLA 引入了状态感知 VLA 推理执行范例，以及使用差分残差和块级混合精度量化的硬件友好型较小验证模型 (sVLA) 构造。在系统方面，我们开发了一个由 GPU 和机器人专用硬件模块组成的异构架构，以及通过并行执行解耦 VLA 和 sVLA 的推测数据流。该硬件模块将预处理、状态预测和低精度计算单元集成到单个紧密耦合的管道中，消除了冗余数据移动并实现低时延验证。通过 LIBERO 和 ManiSkill 基准对 OpenVLA 和 RDT 进行的综合评估表明，SpecVLA 在保持任务成功率的同时，将端到端时延降低了 2.9 倍。通过实现长动作长度推测预测并及时验证，SpecVLA 实现了高效可靠的实时机器人操作。

## 中文关键词

视觉语言动作模型；机器人操作；异构系统；推测推理；验证

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
