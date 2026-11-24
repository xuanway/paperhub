---
title: "DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures"
description: "ISCA 2026 · Session 10C · DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures"
tags:
  - "ISCA2026"
  - "Session 10C"
  - "PIM/PNM, cont."
---

# DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures

**中文标题：** DCC: 面向存内计算架构的以数据为中心的机器学习内核编译

**所属 Session：** [Session 10C](index.md) · [ISCA 2026](../index.md)

**作者：** Peiming Yang, Sankeerth Durvasula, Ivan Fernandez, Mohammad Sadrosadati, Onur Mutlu, Gennady Pekhimenko, Christina Giannoula

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

High-performance Host processors (e.g., GPUs) can integrate Processing-In-Memory (PIM) devices, which can accelerate memory-intensive kernels of Machine Learning (ML) models, including Large Language Models (LLMs), by leveraging the large memory bandwidth available at PIM cores. However, Host processor and PIM cores require different data layouts: Host processor needs consecutive elements distributed across DRAM banks, while PIM cores need consecutive elements within their local banks. This necessitates data rearrangements in ML kernel execution that pose significant performance and programmability challenges, further exacerbated by the need to support diverse PIM devices (e.g., Samsung HBM-PIM, SK Hynix GDDR6-AiM). Current compilation approaches lack systematic optimization for diverse ML kernels and multiple PIM devices, and may largely ignore data rearrangement costs during the compute code optimization step. We demonstrate that data rearrangements and compute code optimization are interdependent, and need to be jointly optimized during the tuning process. To address this, we design DCC, the first data-centric ML compiler for PIM systems that jointly co-optimizes data rearrangements and compute code in a unified tuning process to enable high performance execution. DCC integrates a multi-layer PIM abstraction that enables various data distribution strategies on different PIM backends. DCC enables effective co-optimization of data partitioning strategies with compute loop partitioning schemes. DCC applies PIM-specific code optimizations, and leverages a fast and accurate performance prediction model to select the best-performing code schedule for a given kernel on a target PIM architecture. Our evaluations in various individual ML kernels show that DCC achieves up to 7.68× speedup (2.21× average) on HBM-PIM, and up to 13.17× speedup (3.92× average) on AttAcc PIM, over GPU-only execution. In end-to-end LLM inference, DCC on AttAcc accelerates GPT-3 and LLaMA-2 by 4.52× average (up to 7.71× in LLaMA-2) over GPU. DCC is open-sourced at https://github.com/SPIN-Research-Group/DCC.

## 中文摘要

高性能主机处理器（例如 GPU）可以集成存内处理（PIM）设备，借助 PIM 核可提供的大内存带宽，加速机器学习（ML）模型（包括大语言模型，LLM）中访存密集的 kernel。然而，主机处理器与 PIM 核需要不同的数据布局：主机处理器需要跨 DRAM bank 分布的连续元素，而 PIM 核需要位于其本地 bank 内的连续元素。这使得 ML kernel 执行中必须进行数据重排，带来显著的性能与可编程性挑战，而支持多种 PIM 设备（例如 Samsung HBM-PIM、SK Hynix GDDR6-AiM）的需求进一步加剧了这些挑战。当前的编译方法缺乏针对多样化 ML kernel 与多种 PIM 设备的系统性优化，并且可能在计算代码优化步骤中很大程度上忽略数据重排的开销。我们证明数据重排与计算代码优化是相互依赖的，需要在调优过程中联合优化。为解决这一问题，我们设计了 DCC，首个面向 PIM 系统的以数据为中心的 ML 编译器，它在统一的调优过程中联合协同优化数据重排与计算代码，以实现高性能执行。DCC 集成了一个多层 PIM 抽象，使不同 PIM 后端上可以采用多种数据分布策略。DCC 能够将数据划分策略与计算循环划分方案进行有效的协同优化。DCC 应用 PIM 特有的代码优化，并利用快速而准确的性能预测模型，为给定 kernel 在目标 PIM 架构上选择性能最佳的代码调度方案。我们在多种独立 ML kernel 上的评估显示，相比仅使用 GPU 执行，DCC 在 HBM-PIM 上实现最高 7.68× 加速（平均 2.21×），在 AttAcc PIM 上实现最高 13.17× 加速（平均 3.92×）。在端到端 LLM 推理中，AttAcc 上的 DCC 相比 GPU 将 GPT-3 和 LLaMA-2 平均加速 4.52×（LLaMA-2 中最高 7.71×）。DCC 已开源于 https://github.com/SPIN-Research-Group/DCC。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：SPIN-Research-Group/DCC](https://github.com/SPIN-Research-Group/DCC)
- [实验材料归档（Zenodo 19442321）](https://zenodo.org/records/19442321)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2026](../index.md)
