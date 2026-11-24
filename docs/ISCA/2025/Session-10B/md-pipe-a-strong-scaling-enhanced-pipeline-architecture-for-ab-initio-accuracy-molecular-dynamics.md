---
title: "MD-pipe: A Strong Scaling Enhanced Pipeline Architecture for Ab Initio Accuracy Molecular Dynamics"
description: "ISCA 2025 · Session 10B · MD-pipe：面向从头算精度分子动力学的强扩展增强流水线架构"
tags:
  - "ISCA2025"
  - "Session 10B"
  - "Domain Specific Accelerators III"
---

# MD-pipe: A Strong Scaling Enhanced Pipeline Architecture for Ab Initio Accuracy Molecular Dynamics

**中文标题：** MD-pipe：面向从头算精度分子动力学的强扩展增强流水线架构

**所属 Session：** [Session 10B](index.md) · [ISCA 2025](../index.md)

**作者：** Ning Kang, Guojun Yuan, Zihan Yan, Beining Zhang, Boyang Li, Zeyu Li, Shuo Wang, Guanglei Chen, Jiayi Rao, Zhan Wang, Weile Jia, Ninghui Sun, Guangming Tan

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731052) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Molecular Dynamics (MD) simulations with first-principles accu- racy are widely applied in various fields, including materials science and molecular pharmacology. Current research focus on reducing the solution time of ab initio molecular dynamics (AIMD) from both algorithmic and software perspectives. However, these optimiza- tions are still far from meeting the ever-increasing performance demands for AIMD. In this paper, a fine-grained pipeline archi- tecture is proposed to further optimize the solution time of MD. We design a high-utilization systolic line that eliminates the injec- tion and evacuation time during each matrix operation. Besides, in conjunction with the MD dataflow, a computation migration strategy is introduced to reduce the storage overhead. Furthermore, we leverage dataflow rearrangement and preloading to eliminate the matrix transpose costs. The MD-pipe architecture has been implemented and verified using AMD VPK180 FPGA and ASIC synthesis tools. Evaluation results show that our work on FPGA and ASIC outperforms the NVIDIA A100 GPU by 2.97×and 23.77× respectively. Moreover, the ASIC implementation achieves a sim- ulation speed of 67.6𝜇𝑠/𝑑𝑎𝑦, outperforming state-of-the-art work on Fugaku supercomputer by 454 times under extremely strong scaling deployment (one-atom-per-core).

## 中文摘要

具备第一性原理精度的分子动力学（MD）模拟广泛应用于材料科学、分子药理学等诸多领域。现有研究大多从算法与软件层面缩短从头算分子动力学（AIMD）的求解时间，但这些优化仍难以满足AIMD持续增长的性能需求。本文提出一种细粒度流水线架构，进一步降低分子动力学模拟耗时。

我们设计了高利用率脉动线性阵列，消除每次矩阵运算的数据灌入与排空开销；同时结合分子动力学数据流，提出计算迁移策略以削减存储开销；此外，通过数据流重排与预加载，省去矩阵转置带来的代价。MD-pipe架构基于AMD VPK180 FPGA与ASIC综合工具完成实现与验证。评测结果表明：FPGA版本与ASIC版本分别相比NVIDIA A100 GPU提速2.97倍、23.77倍。其中ASIC实现的模拟速度可达67.6 μs/步；在极强扩展部署（单核只负责一个原子）的条件下，对比Fugaku超算上的前沿工作，性能提升454倍。

## 英文关键词

Molecular Dynamics, DeePMD, Computational Science, Accelerator, Domain Specific Architecture

## 中文关键词

分子动力学, DeePMD, 计算科学, 加速器, 领域专用架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731052)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2025](../index.md)
