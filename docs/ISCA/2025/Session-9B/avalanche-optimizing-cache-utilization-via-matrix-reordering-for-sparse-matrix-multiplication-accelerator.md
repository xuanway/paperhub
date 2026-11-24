---
title: "Avalanche: Optimizing Cache Utilization via Matrix Reordering for Sparse Matrix Multiplication Accelerator"
description: "ISCA 2025 · Session 9B · Avalanche：通过矩阵重排优化稀疏矩阵乘法加速器的缓存利用率"
tags:
  - "ISCA2025"
  - "Session 9B"
  - "HPC"
---

# Avalanche: Optimizing Cache Utilization via Matrix Reordering for Sparse Matrix Multiplication Accelerator

**中文标题：** Avalanche：通过矩阵重排优化稀疏矩阵乘法加速器的缓存利用率

**所属 Session：** [Session 9B](index.md) · [ISCA 2025](../index.md)

**作者：** Gwangeun Byeon, Seongwook Kim, Hyungjin Kim, Sukhyun Han, Jinkwon Kim, Prashant Nair, Taewook Kang, Seokin Hong

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730990) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Sparse Matrix Multiplication (SpMM) is essential in various scien- tific and engineering applications but poses significant challenges due to irregular memory access patterns. Many hardware accel- erators have been proposed to accelerate SpMM. However, they have yet to focus on on-chip memory utilization. In this paper, we highlight the underutilization of the on-chip memory in the SpMM accelerators. Then we propose Avalanche, a novel hardware ac- celerator that optimally utilizes the on-chip memory to efficiently cache both matrices 𝐵 and 𝐶. Avalanche incorporates three key techniques: Matrix Reordering (Mat-Reorder), Dead-Product Early Eviction (DP-Evict), and Reuse Distance-Aware Matrix Caching (RM-Caching). Mat-Reorder enhances data locality by reordering the columns of matrix 𝐴, ensuring early completion of computa- tions for matrix 𝐶. DP-Evict optimizes on-chip memory usage by promptly evicting fully computed (dead) products from on-chip memory. RM-Caching maximizes data reuse by caching frequently accessed elements of matrix 𝐵 based on their reuse distance. Ex- perimental results demonstrate that Avalanche achieves an average performance improvement of 1.97×compared to the state-of-the- art SpMM accelerator, with a chip area of 6.15 mm2

## 中文摘要

稀疏矩阵乘法（SpMM）是各类科学与工程应用中的核心算子，但不规则的访存模式给加速带来巨大挑战。目前已有大量面向SpMM的硬件加速器，但很少关注片上存储利用率。本文首先指出现有SpMM加速器普遍存在片上存储利用率不足的问题，继而提出Avalanche这款新型硬件加速器，它充分利用片上存储，同时缓存矩阵B与矩阵C。

Avalanche包含三项核心技术：矩阵重排（Mat-Reorder）、无效乘积提前驱逐（DP-Evict）、感知复用距离的矩阵缓存（RM-Caching）。Mat-Reorder通过重排矩阵A的列提升数据局部性，让矩阵C的计算可以更早完成；DP-Evict将已经计算完成、不再需要的乘积项及时从片上存储中清出，优化片上空间；RM-Caching依据复用距离，对矩阵B中高频访问元素做缓存，最大化数据复用。实验结果表明：Avalanche相比前沿SpMM加速器平均性能提升1.97倍，芯片面积为6.15 mm²。

## 英文关键词

sparse matrix, sparse matrix multiplication, accelerator, matrix reordering, tiling, application-specific accelerator

## 中文关键词

稀疏矩阵, 稀疏矩阵乘法, 加速器, 矩阵重排, 分块, 专用加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730990)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2025](../index.md)
