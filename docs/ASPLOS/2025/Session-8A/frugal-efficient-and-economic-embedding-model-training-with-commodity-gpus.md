---
title: "Frugal: Efficient and Economic Embedding Model Training with Commodity GPUs"
description: "ASPLOS 2025 · Session 8A · Frugal：在通用 GPU 上高效且经济地训练嵌入模型"
tags:
  - "ASPLOS2025"
  - "Session 8A"
  - "ML Training"
---

# Frugal: Efficient and Economic Embedding Model Training with Commodity GPUs

**中文标题：** Frugal：在通用 GPU 上高效且经济地训练嵌入模型

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Minhui Xie (Tsinghua University,Renmin University of China), Shaoxun Zeng (Tsinghua University), Hao Guo (Tsinghua University), Shiwei Gao (Tsinghua University), Youyou Lu (Tsinghua University)

**单位：** Tsinghua University,Renmin University of China；Tsinghua University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707245) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Embedding models show superiority in learning representations of massive ID-type features in sparse learning scenarios such as recommendation systems (e.g., user/item IDs) and graph learning (e.g., node/edge IDs). Commodity GPUs are highly favored for their cost-efficient computing power, which is ideally suited for the low computing demand of memory-intensive embedding models. However, directly running embedding model training on commodity GPUs yields poor performance because of their deficient communication resources (including low communication bandwidth and no PCIe P2P support). This paper presents Frugal, an embedding model training system tailored for commodity GPUs. Based on the observation that the communication between commodity GPUs must be bounced on host memory (due to no PCIe P2P support), the key idea of Frugal is proactively flushing, where each GPU proactively flushes its own parameters that other GPUs will access into host memory, thereby decoupling half of the communication overhead to non-critical paths. To alleviate the communication contention of proactively flushing on foreground training processes, Frugal assigns priorities to each flush operation, and prioritizes flushing parameters that GPUs will access while deferring others. Further, Frugal tailors a two-level priority queue to ensure high scalability for operations involving priorities. Frugal has been applied to train embedding models including recommendation models and graph embedding. on commodity GPUs, and achieve similar throughput compared to existing systems on datacenter GPUs with 4.0-4.3× improvement in cost-effectiveness.

## 中文摘要

嵌入模型在学习稀疏学习场景中大量 ID 类型特征的表示方面展现出优越性，例如推荐系统（如用户/物品 ID）与图学习（如节点/边 ID）。通用（commodity）GPU 因其高性价比的算力而备受青睐，这种算力恰好适合内存密集型嵌入模型较低的计算需求。然而，由于通用 GPU 的通信资源不足（包括通信带宽低以及不支持 PCIe P2P），直接在其上运行嵌入模型训练会性能不佳。本文提出 Frugal，一个为通用 GPU 量身定制的嵌入模型训练系统。基于通用 GPU 之间的通信必须经由主机内存中转（因为不支持 PCIe P2P）这一观察，Frugal 的核心思想是主动冲刷（proactively flushing）：每个 GPU 主动将自己拥有的、其他 GPU 将要访问的参数冲刷到主机内存中，从而把一半的通信开销解耦到非关键路径上。为缓解主动冲刷在前台训练进程上造成的通信争用，Frugal 为每个冲刷操作分配优先级，优先冲刷 GPU 将要访问的参数，而推迟其他参数。此外，Frugal 定制了两级优先队列，以保证涉及优先级的操作具有高可扩展性。Frugal 已被用于在通用 GPU 上训练包括推荐模型与图嵌入在内的嵌入模型，与数据中心 GPU 上的现有系统相比可达到相近的吞吐，同时在成本效益上提升 4.0-4.3×。

## 英文关键词

Deep Learning Model Training; Machine Learning System; Embedding Models; Heterogeneous Computing

## 中文关键词

深度学习模型训练；机器学习系统；嵌入模型；异构计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707245)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2025](../index.md)
