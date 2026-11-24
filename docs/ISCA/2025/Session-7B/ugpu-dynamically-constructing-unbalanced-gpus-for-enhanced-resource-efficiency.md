---
title: "UGPU: Dynamically Constructing Unbalanced GPUs for Enhanced Resource Efficiency"
description: "ISCA 2025 · Session 7B · UGPU：动态构建非均衡 GPU 以提升资源效率"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# UGPU: Dynamically Constructing Unbalanced GPUs for Enhanced Resource Efficiency

**中文标题：** UGPU：动态构建非均衡 GPU 以提升资源效率

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Xia Zhao, GUANGDA ZHANG, LU Wang, HUADONG DAI

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731103) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Different GPU generations have various numbers of SMs but still keep the balanced idea during the manufacture, i.e., the propor- tion of compute and memory resources within a single physical GPU is similar. Although GPU applications have different charac- teristics, it is still uncommon and uneconomic to build unbalanced physical GPUs for customers. With their powerful computational capabilities, GPUs are widely used in the cloud to accelerate diverse workloads from multiple users, creating opportunities to explore the unbalanced GPU concept in multitasking environments. In this paper, we take the first step in exploring the feasibility and performance benefits of building unbalanced GPUs. Specifically, these unbalanced GPUs, referred to as GPU slices, are dynamically constructed with dedicated compute and memory resources from a single physical GPU to effectively address the diverse demands of co-executing applications, achieving high performance during the execution. However, there are two challenges that must to be solved. First, determining the size of unbalanced GPU slices during execution is challenging, as predicting GPU performance under varying resource allocations is inherently difficult. Second, reallo- cating memory resources after partitioning requires extensive data migration, with traditional methods leading to unacceptable perfor- mance degradation. To address the first challenge, UGPU employs a demand-aware resource partitioning algorithm that partitions resources dynamically without relying on a complex or inaccurate performance model. For the second challenge, UGPU introduces PageMove, a novel mechanism for efficient page migration between different memory dies within an HBM stack. Our key insight is that all memory channels already have physical connections to all through-silicon via (TSV) within a DRAM stack, while different bank groups can transfer data at the same time. PageMove slightly modifies DRAM architecture, uses a customized memory address mapping, designs a new parallel page migration mode (PPMM) and updates the virtual memory management scheme. By doing this, PageMove supports fast entire page migration from one memory die to another memory die which significantly reduces the data mi- gration overhead during the memory resource reallocation. For the heterogeneous workloads with different characteristics, compared to the traditional balanced GPU design, UGPU increases the system performance by 34.3% on average while providing QoS support.

## 中文摘要

不同代际GPU的流多处理器（SM）数量各不相同，但在芯片制造时都遵循均衡设计思路：单块物理GPU内部算力资源与内存资源占比保持相近。虽然GPU应用的特征各不相同，但为用户定制非均衡物理GPU并不常见，成本也很高。GPU算力强大，在云端广泛用于加速多用户的多样化负载，这给我们在多任务场景下探索非均衡GPU架构带来机会。

本文首次探索非均衡GPU的可行性与性能收益。这类非均衡GPU称为GPU切片（GPU slice）：从一块物理GPU中动态划分专属算力与内存资源，适配并发运行应用的差异化需求，实现高性能执行。但该方案存在两个核心难点：第一，运行时确定非均衡GPU切片的规模很困难，因为很难预测不同资源分配下GPU的性能；第二，资源划分后重新分配内存会带来大量数据迁移，传统方案会造成严重性能衰减。

针对第一个问题，UGPU采用需求感知型资源划分算法，无需复杂、误差大的性能模型，动态完成资源划分；针对第二个问题，UGPU提出PageMove，一种在HBM堆叠内部不同存储裸片之间高效迁移内存页的机制。核心思路：所有内存通道与DRAM堆叠内所有硅通孔（TSV）都存在物理连接，并且不同存储组可以并行传输数据。PageMove对DRAM架构做少量改动，配合定制内存地址映射、全新并行页迁移模式（PPMM）以及更新后的虚存管理方案。基于该机制，PageMove支持整页在不同存储裸片之间快速迁移，大幅降低内存重分配时的数据搬运开销。在特征各异的异构负载上，对比传统均衡GPU，支持QoS的UGPU平均提升系统性能34.3%。

## 英文关键词

GPUs, HBM, Multitasking, Unbalanced, PageMove

## 中文关键词

GPU, 高带宽内存, 多任务, 负载不均衡, 页面迁移

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731103)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
