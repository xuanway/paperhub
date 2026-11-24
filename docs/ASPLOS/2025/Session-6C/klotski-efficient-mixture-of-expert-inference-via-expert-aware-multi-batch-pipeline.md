---
title: "Klotski: Efficient Mixture-of-Expert Inference via Expert-Aware Multi-Batch Pipeline"
description: "ASPLOS 2025 · Session 6C · Klotski：基于专家感知多批次流水线的高效混合专家推理"
tags:
  - "ASPLOS2025"
  - "Session 6C"
  - "Mixture of Experts"
---

# Klotski: Efficient Mixture-of-Expert Inference via Expert-Aware Multi-Batch Pipeline

**中文标题：** Klotski：基于专家感知多批次流水线的高效混合专家推理

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhiyuan Fang (Sun Yat-sen University), Yuegui Huang (Sun Yat-sen University), Zicong Hong (Hong Kong University of Science and Technology), Yufeng Lyu (Huawei Technologies Co. Ltd), Wuhui Chen (Sun Yat-sen University,Peng Cheng Laboratory), Yue Yu (Peng Cheng Laboratory), Fan Yu (Huawei Technologies Co. Ltd), Zibin Zheng (Sun Yat-sen University)

**单位：** Sun Yat-sen University；Hong Kong University of Science and Technology；Huawei Technologies Co. Ltd；Sun Yat-sen University,Peng Cheng Laboratory；Peng Cheng Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716261) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Mixture of Experts (MoE), with its distinctive sparse structure, enables the scaling of language models up to trillions of parameters without significantly increasing computational costs. However, the substantial parameter size presents a challenge for inference, as the expansion in GPU memory cannot keep pace with the growth in parameters. Although offloading techniques utilise memory from the CPU and disk and parallelise the I/O and computation for efficiency, the computation for each expert in MoE models is often less than the I/O, resulting in numerous bubbles in the pipeline. Therefore, we propose Klotski, an efficient MoE inference engine that significantly reduces pipeline bubbles through a novel expert-aware multi-batch pipeline paradigm. The proposed paradigm uses batch processing to extend the computation time of the current layer to overlap with the loading time of the next layer. Although this idea has been effectively applied to dense models, more batches may activate more experts in the MoE, leading to longer loading times and more bubbles. Thus, unlike traditional approaches, we balance computation and I/O time and minimise bubbles by orchestrating their inference orders based on their heterogeneous computation and I/O requirements and activation patterns under different batch numbers. Moreover, to adapt to different hardware environments and models, we design a constraint-sensitive I/O-compute planner and a correlation-aware expert prefetcher for a schedule that minimises pipeline bubbles. Experimental results demonstrate that Klotski achieves a superior throughput-latency tradeoff compared to state-of-the-art techniques, with throughput improvements of up to 85.12×.

## 中文摘要

混合专家（MoE）以其独特的稀疏结构，使语言模型能够扩展到数万亿参数而不会显著增加计算成本。然而，庞大的参数量给推理带来了挑战，因为 GPU 内存的增长无法跟上参数的增长。尽管卸载技术利用 CPU 和磁盘的内存，并将 I/O 与计算并行化以提升效率，但 MoE 模型中每个专家的计算量往往小于 I/O 量，导致流水线中出现大量气泡。因此，我们提出 Klotski，一个高效的 MoE 推理引擎，它通过一种新的专家感知多批次流水线范式显著减少流水线气泡。该范式利用批处理延长当前层的计算时间，使其与下一层的加载时间重叠。尽管这一思路已被有效应用于稠密模型，但在 MoE 中更多批次可能激活更多专家，从而导致更长的加载时间和更多气泡。因此，与传统方法不同，我们根据专家在不同批次数量下异构的计算与 I/O 需求以及激活模式来编排其推理顺序，从而平衡计算与 I/O 时间并最小化气泡。此外，为适应不同的硬件环境和模型，我们设计了一个约束敏感的 I/O-计算规划器和一个相关性感知的专家预取器，以得到使流水线气泡最少的调度方案。实验结果表明，与最先进的技术相比，Klotski 取得了更优的吞吐-延迟折中，吞吐提升最高达 85.12 倍。

## 英文关键词

Mixture-of-Experts, Offloading, LLM Inference

## 中文关键词

混合专家；卸载；大语言模型推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716261)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2025](../index.md)
