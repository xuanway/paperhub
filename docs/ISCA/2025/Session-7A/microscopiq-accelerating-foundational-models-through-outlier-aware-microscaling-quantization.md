---
title: "MicroScopiQ: Accelerating Foundational Models through Outlier-Aware Microscaling Quantization"
description: "ISCA 2025 · Session 7A · MicroScopiQ：通过离群值感知微缩放量化加速基础模型"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# MicroScopiQ: Accelerating Foundational Models through Outlier-Aware Microscaling Quantization

**中文标题：** MicroScopiQ：通过离群值感知微缩放量化加速基础模型

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** Akshat Ramachandran, Souvik Kundu, Tushar Krishna

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730989) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Quantization of foundational models (FMs) is significantly more challenging than traditional DNNs due to the emergence of large magnitude values called outliers. Existing outlier-aware algorithm- architecture co-design techniques either use mixed-precision, re- taining outliers at high precision but compromise hardware effi- ciency, or quantize inliers and outliers at the same precision, im- proving hardware efficiency at the cost of accuracy. To address this mutual exclusivity, we propose MicroScopiQ, a novel co-design tech- nique that leverages pruning to complement outlier-aware quantiza- tion. MicroScopiQ retains outliers at higher precision while pruning a certain fraction of least important weights to distribute the ad- ditional outlier bits; ensuring high accuracy, aligned memory and hardware efficiency. We design a high-throughput, low overhead accelerator architecture composed of multi-precision INT process- ing elements and a network-on-chip called ReCoN that efficiently abstracts the complexity of supporting high-precision outliers. Ad- ditionally, unlike prior techniques, MicroScopiQ does not assume any locality of outlier weights, enabling applicability to a broad range of FMs. Extensive experiments across diverse quantization settings demonstrate that MicroScopiQ achieves state-of-the-art quantization accuracy, while delivering up to 3×faster inference and 2×lower energy consumption compared to existing alterna- tives. Code is available at: MicroScopiQ-LLM-Quantization.git

## 中文摘要

基础模型（FM）的量化比传统深度神经网络困难得多，原因在于模型中存在幅值极大的异常值（outlier）。现有的面向异常值的算法-架构协同方案分为两类：一类采用混合精度，对异常值保留高位宽，但会损害硬件效率；另一类将正常值和异常值统一使用相同位宽量化，提升硬件效率却牺牲精度。
为解决这种精度与硬件效率不可兼得的矛盾，本文提出MicroScopiQ，一种全新协同优化方案，利用剪枝来辅助面向异常值的量化。MicroScopiQ对异常值保留更高精度，同时剪去一部分重要性最低的权重，把节省出来的位宽资源分配给异常值，兼顾高精度、规整的内存访问与硬件效率。
本文设计一款高吞吐、低开销加速器，由多精度整数运算单元与名为ReCoN的片上网络组成，屏蔽支持高精度异常值带来的复杂逻辑。此外，和以往方案不同，MicroScopiQ不假设异常权重具备局部性，因此可以广泛适配各类基础模型。
在多种量化配置下的大量实验表明：MicroScopiQ达到当前最优量化精度，对比已有方案，推理速度最高提升3倍，功耗降低2倍。代码仓库：MicroScopiQ-LLM-Quantization.git

## 英文关键词

Foundational Models, Quantization, Pruning, Hardware Accelerator

## 中文关键词

基础模型, 量化, 剪枝, 硬件加速器

## 代码与研究制品

- [代码仓库](https://github.com/georgia-tech-synergy-lab/MicroScopiQ-LLM-Quantization)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730989)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
