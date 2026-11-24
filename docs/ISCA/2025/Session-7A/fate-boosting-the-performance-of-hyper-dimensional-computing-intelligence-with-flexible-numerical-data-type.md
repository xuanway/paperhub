---
title: "FATE: Boosting the Performance of Hyper-Dimensional Computing Intelligence with Flexible Numerical DAta TypE"
description: "ISCA 2025 · Session 7A · FATE：利用灵活数值数据类型提升超维计算智能性能"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# FATE: Boosting the Performance of Hyper-Dimensional Computing Intelligence with Flexible Numerical DAta TypE

**中文标题：** FATE：利用灵活数值数据类型提升超维计算智能性能

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** Haomin Li, Fangxin Liu, Yichi Chen, Zongwu Wang, Shiyuan Huang, Ning Yang, Dongxu Lyu, Li Jiang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731031) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Hyper-Dimensional Computing (HDC) is a promising brain- inspired learning framework designed for efficient, hardware- friendly computation. By utilizing highly parallel operations, HDC encodes raw data into a hyper-dimensional space, facilitating ef- ficient training and inference processes. However, the high preci- sion required for representing high-dimensional vectors presents challenges for implementing HDC on resource-constrained edge devices, mainly due to the significant computational cost of per- forming multiplication for cosine similarity calculations. On the other hand, binary HDC offers lower costs but sacrifices accuracy. 

This paper addresses these challenges by focusing on data quan- tization, a hardware-efficient compression technique that incorpo- rates sparsity to effectively balance cost and accuracy on embedded FPGA. Unlike existing methods that employ the same quantiza- tion scheme for all dimensions, we propose a novel solution that applies different numerical data types to different dimensions of data representations. This approach is motivated by two factors: (1) the varying importance among dimensions and (2) the potential for better utilization of heterogeneous FPGA hardware resources. To achieve this, we propose FATE, an algorithm/architecture co- designed solution that utilizes low-precision data types for less important dimensions, enabling the replacement of multiplication operations with logic calculations. This approach leverages FPGA Look-Up Table (LUT) resources for efficient implementation. The key insight of FATE is that dimensions with high importance re- quire high-precision data types, while the low-importance dimen- sions do not, allowing them to be sacrificed for low hardware over- heads. Furthermore, to maximize resource utilization, we design a workload-aware mixed quantization scheme that offers flexible compression based on these differences in dimensional importance. The proposed quantization framework is seamlessly integrated into the existing FPGA implementations, leveraging the heteroge- neous resources available (LUTs and DSPs) for low-precision and high-precision dimensions, respectively. We evaluate FATE across multiple application domains. With optimized data type ratios on the Kintex-7 FPGA device, our design results in up to 50% speedup and 53.79% energy saving, while maintaining accuracy compared to solely exploiting DSPs for all dimension computations.

## 中文摘要

超维计算（HDC）是一种启发于大脑的学习框架，适合硬件友好、高效的计算。它依靠高度并行运算，把原始数据编码到超维空间，实现高效训练与推理。但高维向量表征所需的高精度，给资源受限的边缘设备带来实现难题，主要原因是余弦相似度计算的乘法运算开销巨大。二进制HDC虽然计算开销更低，但会损失精度。

本文针对该问题，研究数据量化这一硬件高效的压缩手段，引入稀疏性，在嵌入式FPGA上权衡计算开销与精度。以往方案对所有维度统一使用同一套量化策略；本文提出新思路：对数据表征的不同维度分配不同数据类型。该设计基于两点依据：（1）各维度的重要程度不同；（2）可以更好地利用FPGA异构硬件资源。

为此本文提出FATE，一套算法-架构协同方案：不重要维度采用低精度数据类型，把乘法运算替换为逻辑运算，依托FPGA查找表（LUT）高效实现。FATE的核心思路：高重要度维度需要高精度，低重要度维度可以降低精度，换取低硬件开销。此外，为最大化资源利用率，本文设计感知负载的混合量化方案，依据维度重要性差异实现灵活压缩。

这套量化框架可以无缝集成到现有FPGA实现中：低精度维度使用LUT、高精度维度使用DSP。本文在多个应用场景开展评测。在Kintex-7 FPGA上配置最优数据类型占比后，对比全部维度都使用DSP的方案，该设计最高提速50%，功耗节省53.79%，同时精度保持不变。

## 英文关键词

Hyper-Dimensional Computing, Bio-Inspired Computing, Neuromorphic Computing, Compression, FPGA-based Acceleration

## 中文关键词

超维计算, 仿生计算, 神经形态计算, 压缩, 基于FPGA的加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731031)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
