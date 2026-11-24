---
title: "S-SYNC: Shuttle and Swap Co-Optimization in Quantum Charge-Coupled Devices"
description: "ISCA 2025 · Session 3A · S-SYNC: 量子电荷耦合器件中的Shuttle与Swap协同优化"
tags:
  - "ISCA2025"
  - "Session 3A"
  - "Quantum I"
---

# S-SYNC: Shuttle and Swap Co-Optimization in Quantum Charge-Coupled Devices

**中文标题：** S-SYNC: 量子电荷耦合器件中的Shuttle与Swap协同优化

**所属 Session：** [Session 3A](index.md) · [ISCA 2025](../index.md)

**作者：** Chenghong Zhu, Xian Wu, Jingbo Wang, Xin Wang, Chenghong Zhu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731084) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The Quantum Charge-Coupled Device (QCCD) architecture is a modular design to expand trapped-ion quantum computer that relies on the coherent shuttling of qubits across an array of segmented electrodes. Leveraging trapped ions for their long coherence times and high-fidelity quantum operations, QCCD technology represents a significant advancement toward practical, large-scale quantum processors. However, shuttling increases thermal motion and consistently necessitates qubit swaps, significantly extend execution time and negatively affect application success rates. In this paper, we introduce S-SYNC – a compiler designed to co-optimize the number of shuttling and swapping operations. S-SYNC exploits the unique properties of QCCD and incorporates generic SWAP operations to efficiently manage shuttle and SWAP counts simultaneously. Building on the static topology formulation of QCCD, we develop scheduling heuristics to enhance overall performance. Our evaluations demonstrate that our approach reduces the shuttling number by 3.69x on average and improves the success rate of quantum applications by 1.73x on average. Moreover, we apply S-SYNC to gain insights into executing applications across various QCCD topologies and to compare the trade-offs between different initial mapping methods.

## 中文摘要

量子电荷耦合器件（QCCD）架构是一种用于扩展离子阱量子计算机的模块化方案，它依靠量子比特在分段电极阵列上的相干迁移实现功能。离子阱具备长相干时间与高保真量子操作的优势，依托离子阱的QCCD技术是迈向实用化大规模量子处理器的重要进展。但离子迁移会加剧热运动，并且往往需要执行量子比特交换操作，大幅拉长执行时长，降低应用的成功率。本文提出S-SYNC，一款协同优化迁移次数与交换操作次数的编译器。S-SYNC充分利用QCCD的独有特性，引入通用SWAP操作，同时高效管控迁移与SWAP的数量。基于QCCD的静态拓扑建模，我们设计调度启发式算法来提升整体性能。评测结果表明，该方案平均将迁移次数降低至原来的1/3.69，量子应用的成功率平均提升1.73倍。此外，我们借助S-SYNC分析不同QCCD拓扑下应用的运行特征，并对比不同初始映射策略之间的权衡关系。

## 英文关键词

Ion Trap, Quantum Charge-Coupled Devices, Shuttle Scheduling.

## 中文关键词

离子阱, 量子电荷耦合器件, 搬运调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731084)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2025](../index.md)
