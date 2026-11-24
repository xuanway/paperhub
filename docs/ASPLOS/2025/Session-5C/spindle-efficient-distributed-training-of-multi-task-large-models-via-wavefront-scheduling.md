---
title: "Spindle: Efficient Distributed Training of Multi-Task Large Models via Wavefront Scheduling"
description: "ASPLOS 2025 · Session 5C · Spindle：通过波前调度高效分布式训练多任务大模型"
tags:
  - "ASPLOS2025"
  - "Session 5C"
  - "Large Language Models"
---

# Spindle: Efficient Distributed Training of Multi-Task Large Models via Wavefront Scheduling

**中文标题：** Spindle：通过波前调度高效分布式训练多任务大模型

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yujie Wang (Peking University), Shenhan Zhu (Peking University), Fangcheng Fu (Peking University), Xupeng Miao (Purdue University), Jie Zhang (Alibaba Group), Juan Zhu (Alibaba Group), Fan Hong (Alibaba Group), Yong Li (Alibaba Group), Bin Cui (Peking University)

**单位：** Peking University；Purdue University；Alibaba Group

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715992) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recent foundation models are capable of handling multiple tasks and multiple data modalities with the unified base model structure and several specialized model components. However, efficient training of such multi-task (MT) multimodal (MM) models poses significant system challenges due to the sophisticated model architecture and the heterogeneous workloads of different tasks and modalities. In this paper, we propose Spindle, a brand new training system tailored for resource-efficient and high-performance training of MT MM models via wavefront scheduling. The key idea of Spindle is to decompose the model execution into waves and address the joint optimization problem sequentially, including both heterogeneity-aware workload parallelization and dependency-driven execution scheduling. We build our system and evaluate it on various MT MM models. Experiments demonstrate the superior performance and efficiency of Spindle, with speedup ratio up to 71% compared to state-of-the-art training systems. ∗School of Computer Science & Key Lab of High Confidence Software Technologies (MOE), Peking University †Institute of Computational Social Science, Peking University (Qingdao)

## 中文摘要

近期的基础模型凭借统一的基础模型结构与若干专用模型组件，能够处理多种任务与多种数据模态。然而，由于模型架构复杂以及不同任务与模态的工作负载异构，这类多任务（MT）多模态（MM）模型的高效训练带来了显著的系统挑战。在本文中，我们提出 Spindle，一个全新的训练系统，通过波前调度为 MT MM 模型提供资源高效且高性能的训练。Spindle 的核心思想是将模型执行分解为若干个波，并顺序地求解联合优化问题，其中既包括异构感知的工作负载并行化，也包括依赖驱动的执行调度。我们构建了该系统并在多种 MT MM 模型上进行评估。实验表明 Spindle 具有优越的性能与效率，相比最先进的训练系统加速比最高达 71%。∗School of Computer Science & Key Lab of High Confidence Software Technologies (MOE), Peking University †Institute of Computational Social Science, Peking University (Qingdao)

## 英文关键词

Multi-Task Large Models; Distributed Training; Workload Heterogeneity

## 中文关键词

多任务大模型；分布式训练；工作负载异构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715992)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2025](../index.md)
