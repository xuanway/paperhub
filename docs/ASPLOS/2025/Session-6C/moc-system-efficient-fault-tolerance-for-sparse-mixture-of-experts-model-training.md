---
title: "MoC-System: Efficient Fault Tolerance for Sparse Mixture-of-Experts Model Training"
description: "ASPLOS 2025 · Session 6C · MoC-System：面向稀疏混合专家模型训练的高效容错"
tags:
  - "ASPLOS2025"
  - "Session 6C"
  - "Mixture of Experts"
---

# MoC-System: Efficient Fault Tolerance for Sparse Mixture-of-Experts Model Training

**中文标题：** MoC-System：面向稀疏混合专家模型训练的高效容错

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Weilin Cai (The Hong Kong University of Science and Technology (Guangzhou)), Le Qin (The Hong Kong University of Science and Technology (Guangzhou)), Jiayi Huang (The Hong Kong University of Science and Technology (Guangzhou))

**单位：** Guangzhou

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716006) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

As large language models continue to scale up, distributed training systems have expanded beyond 10k nodes, intensifying the importance of fault tolerance. Checkpoint has emerged as the predominant fault tolerance strategy, with extensive studies dedicated to optimizing its efficiency. However, the advent of the sparse Mixture-of-Experts (MoE) model presents new challenges due to the substantial increase in model size, despite comparable computational demands to dense models. In this work, we propose the Mixture-of-Checkpoint System (MoC-System) to orchestrate the vast array of checkpoint shards produced in distributed training systems. MoCSystem features a novel Partial Experts Checkpointing (PEC) mechanism, an algorithm-system co-design that strategically saves a selected subset of experts, effectively reducing the MoE checkpoint size to levels comparable with dense models. Incorporating hybrid parallel strategies, MoC-System involves fully sharded checkpointing strategies to evenly distribute the workload across distributed ranks. Furthermore, MoC-System introduces a two-level checkpointing management method that asynchronously handles in-memory snapshots and persistence processes. We build MoC-System upon the Megatron-DeepSpeed framework, achieving up to a 98.9% reduction in overhead for each checkpointing process compared to the original method, during MoE model training with ZeRO-2 data parallelism and expert parallelism. Additionally, extensive empirical analyses substantiate that our methods enhance efficiency while maintaining comparable model accuracy, even achieving an average accuracy increase of 1.08% on downstream tasks.

## 中文摘要

随着大语言模型规模不断扩大，分布式训练系统的规模已扩展到超过一万个节点，容错的重要性日益凸显。检查点（checkpoint）已成为主流的容错策略，大量研究致力于优化其效率。然而，稀疏混合专家（MoE）模型的出现带来了新的挑战：尽管其计算需求与稠密模型相当，但模型规模却大幅增加。在本工作中，我们提出混合检查点系统（Mixture-of-Checkpoint System，MoC-System），用于编排分布式训练系统中产生的大量检查点分片。MoC-System 具有一种新的部分专家检查点（Partial Experts Checkpointing，PEC）机制，这是一种算法-系统协同设计，策略性地只保存选定的部分专家，从而有效地将 MoE 检查点规模降低到与稠密模型相当的水平。结合混合并行策略，MoC-System 采用完全分片检查点策略，将工作负载均匀分配到各个分布式 rank 上。此外，MoC-System 引入了一种两级检查点管理方法，异步处理内存快照与持久化过程。我们在 Megatron-DeepSpeed 框架之上构建了 MoC-System，在采用 ZeRO-2 数据并行与专家并行的 MoE 模型训练中，相比原始方法，每次检查点过程的额外开销最多降低 98.9%。此外，大量实证分析证实，我们的方法在提升效率的同时保持了相当的模型精度，甚至在下游任务上平均精度提升了 1.08%。

## 英文关键词

Fault Tolerance, Checkpoint, Mixture of Experts, Large Language Models, Training

## 中文关键词

容错；检查点；混合专家；大语言模型；训练

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716006)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2025](../index.md)
