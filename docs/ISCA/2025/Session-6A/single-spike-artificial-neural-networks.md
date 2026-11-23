---
title: "Single Spike Artificial Neural Networks"
description: "ISCA 2025 · Session 6A · 单脉冲人工神经网络"
tags:
  - "ISCA2025"
  - "Session 6A"
  - "ML Accelerators II"
---

# Single Spike Artificial Neural Networks

**中文标题：** 单脉冲人工神经网络

**所属 Session：** [Session 6A](index.md) · [ISCA 2025](../index.md)

**作者：** Rhys Gretsch, Michael Beyeler, Jeremy Lau, Timothy Sherwood

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731027) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Spiking neural networks (SNNs) circumvent the need for large scale arithmetic using techniques inspired by biology. However, SNNs are designed with fundamentally different algorithms from ANNs, which have benefited from a rich history of theoretical advances and an increasingly mature software stack. In this paper we ex- plore the potential of a new technique that lies between these two approaches, one that can leverage the software and system level optimizations of ANNs while utilizing biologically inspired circuits for energy efficient computation. The resulting hardware represents the traditional weight of an ANN as nothing more than a delay element and the degree of activation as nothing more than arrival time of a digital signal. Building on these fundamental operations, we can implement complete ANNs through several innovations: spatial and temporal reuse that facilitates classical dataflows, reduc- ing memory system demands for ANN temporal operations; a new noise-tolerant temporal summation operation; novel hybrid digi- tal/temporal memories; and the integration of temporal memory circuits for shepherding inter-layer activations. Using the MLPerf Tiny benchmark suite, we demonstrate how several architectural parameters can impact inference accuracy, that our proposed sys- tolic array can provide 11×better energy consumption with a 4× improvement in latency compared to SNNs, and when equipped with temporal memories provides 3.5×improvements in energy compared to the most aggressive 8-bit digital systolic arrays.

## 中文摘要

脉冲神经网络（SNN）借鉴生物机制，无需大规模算术运算。但SNN的算法范式和人工神经网络（ANN）存在本质区别；ANN已有深厚理论积累，配套软件栈也日趋成熟。本文探索一种介于二者之间的新技术：既能复用ANN已有的软件与系统优化，又借助类生物电路实现高能效计算。该硬件将ANN的权重抽象为延时单元，激活值大小由数字信号的到达时刻表征。基于这些基础操作，本文通过多项创新完整实现ANN：空间与时间复用，支持经典数据流，降低ANN时序运算对存储系统的压力；一种新的抗噪时序求和机制；新型数字/时序混合存储器；以及时序存储电路，用于传递层间激活。基于MLPerf Tiny基准测试集，本文分析了多个架构参数对推理精度的影响。实验结果表明：相比SNN，本文提出的脉动阵列能效提升11倍、延迟缩短至原来的1/4；搭配时序存储器后，相比最优8比特数字脉动阵列，能效提升3.5倍。

## 英文关键词

Spiking neural networks, single spike, neuromorphic computing, accelerator

## 中文关键词

人工神经网络, 时间编码, 单脉冲计算, 时域存储器

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731027)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2025](../index.md)
