---
title: "Cambricon-SR: An Accelerator for Neural Scene Representation with Sparse Encoding Table"
description: "ISCA 2025 · Session 7A · Cambricon-SR：面向稀疏编码表神经场景表示的加速器"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# Cambricon-SR: An Accelerator for Neural Scene Representation with Sparse Encoding Table

**中文标题：** Cambricon-SR：面向稀疏编码表神经场景表示的加速器

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** Tianbo Liu, Xinkai Song, Zhifei Yue, Rui Wen, Xing Hu, Zhuoran Song, Yuanbo Wen, Yifan Hao, Wei Li, Zidong Du, Rui Zhang, Jiaming Guo, Di Huang, Shaohui Peng, GuangZhong Sun, Qi Guo, Tianshi Chen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731018) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Neural Scene Representation (NSR) is a promising technique for representing real scenes. By learning from dozens of 2D photos captured from different viewpoints, NSR computes the 3D repre- sentation of real scenes. However, the performance of NSR process- ing running on GPU is insufficient for applications. Cambricon-R achieves high performance of more than 60 scenes per second, but at the cost of modeling quality. 

In this paper, we propose Cambricon-SR, an algorithm-hardware co-designed accelerator to improve NSR performance and quality. First, we propose a novel NSR algorithm with sparse encoding table, it achieves more than 80% of sparsity for the encoding table with negligible accuracy loss. Second, to efficiently eliminate the invalid memory access requests to the pruned entries, we propose the sparse index unit based on sequential SRAM access to address the challenge of irregular memory access to the sparse structure bitmap. It achieves a throughput increase of 7.54×for the encoding stage with an additional area overhead of 8.59%. Third, we propose the dynamic shared buffer for the MLP units to reduce the buffer usage by 85.3% so that we can increase the number of the MLP units. 

We conduct experimental evaluations on 8 typical scenes. The results demonstrate that, compared with A100 GPU and Cambricon- R, Cambricon-SR achieves 1259×and 4.12×speedup, and reduces the energy consumption by 1139×and 2.98×for each training iteration of NSR, respectively.

## 中文摘要

神经场景表示（NSR）是一种前景广阔的实景重建技术。它通过学习多张不同视角拍摄的二维照片，计算得到真实场景的三维表达。但在GPU上运行的NSR处理性能难以满足应用需求。寒武纪Cambricon-R虽然可以达到每秒60帧以上场景的高性能，但代价是重建质量下降。
本文提出Cambricon-SR，一款算法硬件协同设计的加速器，同时提升NSR的性能与重建质量。首先，本文提出带稀疏编码表的新型NSR算法，在精度损失极小的前提下，编码表的稀疏度可达80%以上；其次，为高效剔除被裁剪条目的无效内存请求，本文基于顺序SRAM访问设计稀疏索引单元，解决稀疏结构位图带来的不规则访存难题，使编码阶段吞吐提升7.54倍，面积开销仅增加8.59%；最后，为MLP计算单元设计动态共享缓冲区，缓冲区占用降低85.3%，从而容纳更多MLP单元。

本文在8个典型场景上开展实验。结果表明：在NSR单次训练迭代任务上，对比A100 GPU与Cambricon-R，Cambricon-SR分别实现1259倍和4.12倍提速，功耗分别降低1139倍和2.98倍。

## 英文关键词

neural scene representation, sparse encoding table, accelerator

## 中文关键词

神经场景表示, 稀疏编码表, 加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731018)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
