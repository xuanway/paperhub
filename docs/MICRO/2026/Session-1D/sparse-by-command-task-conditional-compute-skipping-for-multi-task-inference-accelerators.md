---
title: "Sparse by Command: Task-Conditional Compute Skipping for Multi-Task Inference Accelerators"
description: "MICRO 2026 · Session 1D · Sparse by Command：面向多任务推理加速器的任务条件计算跳过机制"
tags:
  - "MICRO2026"
---

# Sparse by Command: Task-Conditional Compute Skipping for Multi-Task Inference Accelerators

**中文标题：** Sparse by Command：面向多任务推理加速器的任务条件计算跳过机制

**所属 Session：** [Session 1D](index.md) · [MICRO 2026](../index.md)

**作者：** Afzal Ahmad, Gaoyu Mao, Shoubo Hu, Hui-Ling Zhen, Mingxuan Yuan, Xinyu Chen, Wei Zhang

**来源：** MICRO 2026，pp. 326–341；[DOI](https://doi.org/10.1109/MICRO67795.2026.00038)

## 英文摘要

Multi-task inference models share a single backbone across diverse tasks, yet execute identical computation regardless of which task is active - wasting energy and cycles on task-irrelevant operations. We observe that the task command, typically available before inference begins, provides a free signal that can be exploited to skip unnecessary computation at the hardware level. We present a HW/SW co-designed approach in which a lightweight gating network, trained jointly with the backbone, predicts per-tile binary execution masks conditioned on the task input. Each tile corresponds to a fixed group of output channels (the native scheduling granularity of the accelerator), enabling masked tiles to be skipped with zero overhead. This yields a task-dependent reduction in compute, where each command activates only the subset of the network it requires, without changes to the model architecture or inference pipeline. We co-design the full system stack: a command-conditioned training procedure that learns hardware-aligned tile masks under a sparsity objective; an instruction set architecture whose instructions carry per-tile bitmask fields, allowing the hardware to skip masked tiles without software intervention; and a tiled inference accelerator with configurable parallelism, double-buffered memory, and INT8 datapath that natively supports sparse tile execution. We prototype on an AMD/Xilinx Alveo U50 FPGA and evaluate on a closed-loop visuomotor driving task in CARLA autonomous driving simulator. Task-conditional sparsity reduces FLOPs by 66-76% while maintaining driving quality. On-device latency decreases by 51-59%, from 9.12 ms to 3.74-4.44 ms (2.1-2.4x speedup), with energy per inference dropping from 263 to 108-128mJ.

## 中文摘要

多任务推理模型在不同的任务之间共享一个主干，但无论哪个任务处于活动状态，都执行相同的计算 - 在与任务无关的操作上浪费能量和周期。我们观察到，任务命令通常在推理开始之前可用，它提供了一个空闲信号，可用于跳过硬件级别不必要的计算。我们提出了一种硬件/软件联合设计的方法，其中与主干网络联合训练的轻量级门控网络可以根据任务输入来预测每个分块的二进制执行掩码。每个分块对应于一组固定的输出通道（加速器的本机调度粒度），从而能够以零开销跳过屏蔽的分块。这会减少与任务相关的计算量，其中每个命令仅激活所需的网络子集，而无需更改模型架构或推理管道。我们共同设计了完整的系统堆栈：一个命令条件训练程序，可以在稀疏目标下学习硬件对齐的平铺掩码；指令集架构，其指令携带每个分块位掩码字段，允许硬件在没有软件干预的情况下跳过掩码分块；以及具有可配置并行性、双缓冲内存和原生支持稀疏切片执行的 INT8 数据路径的切片推理加速器。我们在 AMD/Xilinx Alveo U50 FPGA 上进行原型设计，并在 CARLA 自动驾驶模拟器中评估闭环视觉运动驱动任务。任务条件稀疏性将 FLOP 减少 66-76%，同时保持驾驶质量。设备上时延减少了 51-59%，从 9.12 毫秒减少到 3.74-4.44 毫秒（加速 2.1-2.4 倍），每次推理的能量从 263 下降到 108-128 毫焦。

## 中文关键词

硬件加速器；多任务学习；软硬件协同设计；现场可编程门阵列；动态执行

## 代码与研究制品

- 代码仓库：[https://github.com/afzalxo/sparse-by-command](https://github.com/afzalxo/sparse-by-command)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21503283](https://doi.org/10.5281/zenodo.21503283)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1D](index.md) · [MICRO 2026 主页](../index.md)
