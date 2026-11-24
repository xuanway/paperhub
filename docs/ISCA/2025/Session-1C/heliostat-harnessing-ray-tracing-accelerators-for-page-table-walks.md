---
title: "Heliostat: Harnessing Ray Tracing Accelerators for Page Table Walks"
description: "ISCA 2025 · Session 1C · Heliostat: 利用光线追踪加速器优化页表遍历"
tags:
  - "ISCA2025"
  - "Session 1C"
  - "GPUs & Ray Tracing"
---

# Heliostat: Harnessing Ray Tracing Accelerators for Page Table Walks

**中文标题：** Heliostat: 利用光线追踪加速器优化页表遍历

**所属 Session：** [Session 1C](index.md) · [ISCA 2025](../index.md)

**作者：** Yuan Feng, Yuke Li, Jiwon Lee, Won Woo Ro, Hyeran Jeon

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731011) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

This paper introduces Heliostat, which enhances page translation bandwidth on GPUs by harnessing underutilized ray tracing accelerators (RTAs). While most existing studies focused on better utilizing the provided translation bandwidth, this paper introduces a new opportunity to fundamentally increase the translation bandwidth. Instead of overprovisioning the GPU memory management unit (GMMU), Heliostat repurposes the existing RTAs by leveraging the operational similarities between ray tracing and page table walks. Unlike earlier studies that utilized RTAs for certain workloads, Heliostat democratizes RTA for supporting any workloads by improving virtual memory performance. Heliostat+ optimizes Heliostat by handling predicted future address translations proactively. Heliostat outperforms baseline and two state-of-the-arts by 1.93×, 1.92×, and 1.66×. Heliostat+ further speeds up Heliostat by 1.23×. Compared to an overprovisioned comparable solution, Heliostat occupies only 1.53% of the area and consumes 5.8% of the power.

## 中文摘要

本文提出Heliostat架构，利用GPU中利用率不足的光线追踪加速器（RTA）提升页地址转换带宽。现有相关工作大多着眼于更高效地利用已有的转换带宽，而本文开辟了一条从根本上提升转换带宽的新思路。Heliostat并未对GPU内存管理单元（GMMU）进行过量配置，而是借助光线追踪与页表遍历在操作上的相似性，复用现有的RTA资源。不同于以往仅在特定负载下使用RTA的研究，Heliostat让RTA能够普惠支撑各类负载，提升虚拟内存性能。Heliostat+是Heliostat的优化版本，可以对未来预判的地址转换请求进行预处理。评测结果显示，Heliostat相比基线方案以及另外两项前沿工作分别取得1.93倍、1.92倍和1.66倍的性能提升；Heliostat+在Heliostat基础上进一步提速1.23倍。和同等能力的过量配置方案相比，Heliostat仅占用1.53%的芯片面积，功耗仅为后者的5.8%。

## 英文关键词

GPU, Virtual Memory, Address Translation

## 中文关键词

图形处理器, 虚拟内存, 地址转换

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731011)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1C](index.md) · [返回 ISCA 2025](../index.md)
