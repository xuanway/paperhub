---
title: "DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training"
description: "ISCA 2026 · Session 10A · DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training"
tags:
  - "ISCA2026"
  - "Session 10A"
  - "LLM 5"
---

# DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training

**中文标题：** DisDP: 面向模型分片数据并行训练的计算、网络与存储解耦

**所属 Session：** [Session 10A](index.md) · [ISCA 2026](../index.md)

**作者：** Mo Sun, Zihan Yang, Changyue Liao, Yingtao Li, Jie Zhang, Kaiqi Chen, Fei Wu, Zeke Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Model-sharded data parallelism (MSDP), e.g., ZeRO, evenly shards the model states across all GPUs, and thus has been widely adopted by LLM pre-training, such as Llama and DeepSeek, due to its low GPU memory capacity requirement. However, MSDP introduces severe overhead from additional network communication collectives (i.e., AllGather and ReduceScatter). Although the collectives themselves only occupy fewer than 10% of GPU SMs, their execution time increases by 41% due to the serial execution of aggregated CPU/GPU-managed compute (i.e., GEMM), network (i.e., NCCL), and storage (i.e., optimizer states). To this end, we present DisDP, a fully disaggregated distributed data-parallel architecture that first fully disaggregates compute, network, and storage for MSDP, such that GPUs only focus on the computing part, and thus the GPU utilization is maximized. The key idea is 1) fully offloading collectives to SmartNICs and SmartSwitch to avoid interference between GEMM kernels and collective kernels, and 2) fully offloading storage to a SmartSwitch-enhanced parameter server that allows a single PS to serve massive workers with linear scalability. DisDP on 8 distributed GPUs outperforms the state-of-the-art training systems by 3.98× when training on a 175B model, validating the efficiency of disaggregation.

## 中文摘要

模型分片数据并行（MSDP，如ZeRO）将模型状态均匀分片到所有GPU上，因其低GPU内存容量需求而被广泛用于Llama和DeepSeek等大语言模型的预训练。然而，MSDP引入了额外的网络通信集合（即AllGather和ReduceScatter）带来的严重开销。尽管这些集合操作本身仅占用不到10%的GPU SM，但由于CPU/GPU管理的计算（GEMM）、网络（NCCL）和存储（优化器状态）的串行执行，其执行时间增加了41%。为此，我们提出了DisDP，一种完全解耦的分布式数据并行架构，首次针对MSDP实现了计算、网络和存储的完全解耦，使得GPU仅专注于计算部分，从而最大化GPU利用率。其关键思想是：1）将集合操作完全卸载到SmartNIC和SmartSwitch上，以避免GEMM内核与集合内核之间的干扰；2）将存储完全卸载到SmartSwitch增强的参数服务器上，使得单个参数服务器能够以线性可扩展性服务大量工作节点。在8个分布式GPU上，DisDP在训练175B模型时的性能比最先进的训练系统提升了3.98倍，验证了解耦的高效性。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2026](../index.md)
