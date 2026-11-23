---
title: "InfiniMind: A Learning-Optimized Large-Scale Brain-Computer Interface"
description: "ISCA 2025 · Session 10B · InfiniMind：面向学习优化的大规模脑机接口"
tags:
  - "ISCA2025"
  - "Session 10B"
  - "Domain Specific Accelerators III"
---

# InfiniMind: A Learning-Optimized Large-Scale Brain-Computer Interface

**中文标题：** InfiniMind：面向学习优化的大规模脑机接口

**所属 Session：** [Session 10B](index.md) · [ISCA 2025](../index.md)

**作者：** Yeongwoo Jang, Daye Jung, Seunghyun Song, Hunjun Lee, Jangwoo Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731067) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Brain-computer interfaces (BCIs) provide an interactive closed-loop connection between the brain and a computer. By employing signal processors implanted within the brain, BCIs are driving innovations across various fields in neuroscience and medicine. Recent studies highlight the need to integrate non-volatile memories (NVMs) into the implanted system for large-scale applications. At the same time, they emphasize the importance of continual learning within the system to address non-stationarities in the recorded signals. This work is the first to address the performance and lifetime is- sues of deploying learning on NVM-assisted BCI systems. To reduce excessive write overhead associated with learning support, we pro- pose four optimization schemes tailored for BCI workloads. First, update filtering minimizes unnecessary writes by leveraging the sparse and recurring nature of BCI signals. Second, delta buffering exploits temporal locality inherent in BCI signals to minimize NVM writes. Third, out-of-place flushing reduces write amplification by packing multiple sub-page updates into a single page write. Fourth, waveform compression decreases the volume of written data by exploiting the structural characteristics of neural signals. We imple- ment these optimizations in a memory controller and integrate it into the state-of-the-art NVM-assisted BCI system, realizing an end- to-end learning-optimized system. Evaluation results show that our system improves performance and lifetime by 5.39×and 23.52×, respectively, on representative continual learning algorithms.

## 中文摘要

脑机接口（BCI）在大脑与计算机之间构建闭环交互通路。借助植入脑内的信号处理单元，BCI正推动神经科学与医学多个领域的创新。近期研究指出，面向规模化应用，植入式系统需要集成非易失性存储器（NVM）；同时，系统内部必须支持持续学习，以应对采集信号的非平稳特性。

本文首次研究在基于NVM的脑机接口系统上部署学习算法时面临的性能与存储寿命问题。为降低学习带来的高额写开销，我们针对BCI负载设计四项优化方案：
1）更新过滤：利用BCI信号稀疏、重复出现的特点，减少无效写操作；
2）增量缓冲（delta buffering）：挖掘脑电信号的时间局部性，削减NVM写入次数；
3）异地刷写（out-of-place flushing）：将多个子页更新合并为一次页写入，缓解写放大；
4）波形压缩：利用神经信号自身结构特征，减少待写入数据总量。

我们将上述优化实现在存储控制器中，并集成到现有先进的NVM型BCI系统，形成一套端到端面向持续学习优化的系统。评测结果表明：在代表性持续学习算法上，该系统性能提升5.39倍，存储寿命提升23.52倍。

## 英文关键词

Brain-Computer Interface, Continual Learning, Non-Volatile Mem- ory, Low-Power System, Hardware Accelerator

## 中文关键词

脑机接口, 持续学习, 非易失性存储器, 低功耗系统, 硬件加速器

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731067)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2025](../index.md)
