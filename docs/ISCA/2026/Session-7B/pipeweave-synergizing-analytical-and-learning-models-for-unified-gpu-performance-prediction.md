---
title: "PIPEWEAVE: Synergizing Analytical and Learning Models for Unified GPU Performance Prediction"
description: "ISCA 2026 · Session 7B · PIPEWEAVE: Synergizing Analytical and Learning Models for Unified GPU Performance Prediction"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# PIPEWEAVE: Synergizing Analytical and Learning Models for Unified GPU Performance Prediction

**中文标题：** PIPEWEAVE: 协同解析模型与学习模型的统一 GPU 性能预测

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Kaixuan Zhang, Yunfan Cui, Shuhao Zhang, Chutong Ding, Shiyou Qian, Luping Wang, Jian Cao, Guangtao Xue, Cheng Huang, Guodong Yang, Liping Zhang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The rapid expansion of Transformer-based large language models has dramatically increased the need for high-performance GPUs. As a result, there is growing demand for fast, accurate, and widely generalizable GPU performance models to support next-generation hardware selection and system-level exploration. However, current data-driven methods are limited, exhibiting poor generalization across hardware and inadequate modeling of complex production-level kernels common in modern inference stacks. To address these issues, we present PIPEWEAVE, a unified GPU modeling framework. This approach first employs an analytical model to quantify a given kernel’s demands on the GPU’s heterogeneous instruction pipelines. These analytical features are then fed into a machine learning (ML) model to capture complex cross-pipeline interactions and resource dependencies, enabling high-fidelity performance prediction. Our evaluation across 11 GPU types from four generations of major architectures on two widely-used serving systems demonstrates that PIPEWEAVE delivers high fidelity and strong generalizability. It achieves accurate predictions, with only 6.1% average error at the kernel level and 8.5% for end-to-end inference—reducing the error of state-of-the-art methods by 6.7× and 4.4×, respectively. We also demonstrate PIPEWEAVE’s value “beyond simulation” by utilizing its performance ceiling to diagnose implementation shortcomings and guide the optimization of a production fused MoE Triton kernel, achieving up to 1.7× speedup. Code is available online.

## 中文摘要

基于 Transformer 的大语言模型的快速扩张，极大提升了对高性能 GPU 的需求。因此，人们越来越需要快速、准确且具有广泛泛化能力的 GPU 性能模型，以支撑下一代硬件选型和系统级探索。然而，当前的数据驱动方法存在局限：跨硬件的泛化能力差，且对现代推理栈中常见的复杂生产级内核建模不足。为解决这些问题，我们提出 PIPEWEAVE，一个统一的 GPU 建模框架。该方法首先采用解析模型来量化给定内核对 GPU 异构指令流水线的需求，然后将这些解析特征输入机器学习（ML）模型，以捕捉复杂的跨流水线交互和资源依赖关系，从而实现高保真性能预测。我们在两个广泛使用的服务系统上，针对来自四代主流架构的 11 种 GPU 类型进行评估，结果表明 PIPEWEAVE 具有高保真度与强泛化能力。它实现了准确的预测：内核级平均误差仅 6.1%，端到端推理误差 8.5%，分别将最先进方法的误差降低了 6.7× 和 4.4×。我们还通过利用其性能上限来诊断实现缺陷并指导优化一个生产级融合 MoE Triton 内核，展示了 PIPEWEAVE“超越仿真”的价值，实现了最高 1.7× 的加速。代码已在线提供。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：zksainx/pipeweave](https://github.com/zksainx/pipeweave)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
