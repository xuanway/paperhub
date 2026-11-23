---
title: "MeshSlice: Efficient 2D Tensor Parallelism for Distributed DNN Training"
description: "ISCA 2025 · Session 5B · MeshSlice：面向分布式 DNN 训练的高效二维张量并行"
tags:
  - "ISCA2025"
  - "Session 5B"
  - "HPC for ML/AI"
---

# MeshSlice: Efficient 2D Tensor Parallelism for Distributed DNN Training

**中文标题：** MeshSlice：面向分布式 DNN 训练的高效二维张量并行

**所属 Session：** [Session 5B](index.md) · [ISCA 2025](../index.md)

**作者：** Hyoungwook Nam, Gerasimos Gerogiannis, Josep Torrellas

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731077) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

In distributed training of large DNN models, the scalability of one- dimensional (1D) tensor parallelism (TP) is limited because of its high communication cost. 2D TP attains extra scalability and ef- ficiency because it reduces communication relative to 1D TP. Un- fortunately, existing algorithms for general matrix multiplication (GeMM) in 2D TP suffer from inefficiencies. Indeed, Cannon’s al- gorithm incurs high traffic, SUMMA suffers from high synchro- nization overhead, and a 2D GeMM with collective communication operations does not overlap communication with computation. In addition, it is difficult to optimize the numerous parameters of 2D TP, including the dataflow, mesh shape, and sharding. As a result, human experts are needed to find efficient configurations of 2D TP. To address these problems, this paper proposes MeshSlice, a novel 2D GeMM algorithm for efficient 2D TP in distributed DNN training. The MeshSlice algorithm slices the collective communications into multiple partial collectives that allow overlapping communication with computation. As a result, MeshSlice hides most of the com- munication latency. We also present the MeshSlice LLM autotuner, which automates finding an efficient 2D GeMM dataflow config- uration, mesh shape, and communication granularity for Large Language Model (LLM) training using analytical cost models. To evaluate MeshSlice, we simulate TPUv4 clusters training LLM mod- els. We show that MeshSlice maintains good efficiency up to at least 256-way 2D TP. In a cluster of 256 TPUs, MeshSlice trains the GPT- 3 and Megatron-NLG models 12.0% and 23.4% faster, respectively, than the state-of-the-art algorithm.

## 中文摘要

在大规模深度神经网络分布式训练中，一维张量并行（1D TP）受高昂通信开销制约，可扩展性有限。二维张量并行（2D TP）相比一维张量并行降低通信量，获得更好的可扩展性与效率。但现有二维张量并行下的通用矩阵乘法（GeMM）算法存在低效问题：Cannon算法流量大，SUMMA同步开销高，基于集合通信的二维矩阵乘法无法做到通信与计算重叠。此外，二维张量并行的参数空间庞大，数据流、网格形状、分片策略等难以调优，需要人工专家寻找高效配置。

针对上述问题，本文提出MeshSlice，一种面向分布式DNN训练、支持高效二维张量并行的新型二维矩阵乘法算法。MeshSlice将集合通信拆分为多段部分集合通信，实现通信与计算重叠，掩盖大部分通信延迟。本文还配套MeshSlice LLM自动调优器：基于解析代价模型，自动搜索适合大语言模型训练的高效二维矩阵乘法数据流、网格拓扑与通信粒度。
我们在TPUv4集群上仿真LLM训练，实验表明MeshSlice在至少256路二维张量并行下仍保持较高效率。在256颗TPU集群上，对比前沿算法，MeshSlice训练GPT-3提速12.0%，训练Megatron-NLG提速23.4%。

## 英文关键词

Large-scale Machine Learning, Large Language Model, Distributed Training, Collective Communication

## 中文关键词

大规模机器学习, 大语言模型, 分布式训练, 集合通信

## 代码与研究制品

- [代码仓库](https://github.com/hwnam831/meshslice)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731077)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2025](../index.md)
