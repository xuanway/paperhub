---
title: "SwitchQNet: Optimizing Distributed Quantum Computing for Quantum Data Centers with Switch Networks"
description: "ISCA 2025 · Session 7C · SwitchQNet: 面向量子数据中心的交换网络分布式量子计算优化"
tags:
  - "ISCA2025"
  - "Session 7C"
  - "Quantum II"
---

# SwitchQNet: Optimizing Distributed Quantum Computing for Quantum Data Centers with Switch Networks

**中文标题：** SwitchQNet: 面向量子数据中心的交换网络分布式量子计算优化

**所属 Session：** [Session 7C](index.md) · [ISCA 2025](../index.md)

**作者：** Hezi Zhang, Yiran Xu, Haotian Hu, Keyi Yin, Hassan Shapourian, Jiapeng Zhao, Ramana Rao Kompella, Reza Nejabati, Yufei Ding

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731046) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Distributed Quantum Computing (DQC) provides a scalable ar- chitecture by interconnecting multiple quantum processor units (QPUs). Among various DQC implementations, quantum data cen- ters (QDCs) — where QPUs in different racks are connected through reconfigurable optical switch networks — are becoming feasible in the near term. However, the latency of cross-rack communica- tions and dynamic switch reconfigurations poses unique challenges to communications in QDCs, significantly increasing the overall latency, thereby also reducing the overall fidelity. In this paper, we address these challenges by introducing a novel compiler that optimizes scheduling of communications across the program and network layers. Our evaluation shows that it reduces the overall latency by 8.02×over prior approaches with a small overhead and can be integrated with quantum error correction (QEC) to facilitate fault-tolerant quantum computing (FTQC). We have open-sourced our codes at [https://zenodo.org/records/15377656](https://zenodo.org/records/15377656).

## 中文摘要

分布式量子计算（DQC）将多个量子处理单元（QPU）相互连接，以此提供一种可扩展架构。在各类分布式量子计算实现方案中，量子数据中心（QDC）——不同机柜内的QPU经由可重构光交换网络互连——在近期就具备落地可行性。但是，跨机柜通信以及交换机动态重配置会带来独特挑战，大幅增加量子数据中心的通信总延迟，进而降低整体保真度。针对上述问题，本文提出一款全新编译器，在程序层与网络层对通信调度进行联合优化。 评测结果表明：相比现有方案，该编译器在少量开销的前提下，将整体延迟降低8.02倍；并且可以和量子纠错（QEC）结合，支撑容错量子计算（FTQC）。 项目已开源，代码仓库地址：https://zenodo.org/records/15377656。

## 英文关键词

Distributed Quantum Computing (DQC), Quantum Data Center (QDC), Compilation

## 中文关键词

分布式量子计算, 量子数据中心, 编译

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15377656)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731046)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2025](../index.md)
