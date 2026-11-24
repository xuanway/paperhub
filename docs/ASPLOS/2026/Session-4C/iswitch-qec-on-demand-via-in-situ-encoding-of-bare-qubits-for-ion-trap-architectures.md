---
title: "iSwitch: QEC on Demand via In-Situ Encoding of Bare Qubits for Ion Trap Architectures"
description: "ASPLOS 2026 · Session 4C · iSwitch：面向离子阱架构、通过裸量子比特原位编码实现按需 QEC"
tags:
  - "ASPLOS2026"
  - "Session 4C"
  - "Quantum Error Correction"
---

# iSwitch: QEC on Demand via In-Situ Encoding of Bare Qubits for Ion Trap Architectures

**中文标题：** iSwitch：面向离子阱架构、通过裸量子比特原位编码实现按需 QEC

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Keyi Yin (University of California, San Diego), Xiang Fang (University of California, San Diego), Zhuo Chen (University of California, San Diego), David Hayes (Quantinuum), Eneet Kaur (Cisco Quantum Lab), Reza Nejabati (Cisco Quantum Lab), Hartmut Haeffner (University of California, Berkeley), Wes Campbell (University of California, Los Angeles), Eric Hudson (University of California, Los Angeles), Jens Palsberg (University of California, Los Angeles), Travis Humble (Oak Ridge National Laboratory), Yufei Ding (University of California, San Diego)

**单位：** University of California, San Diego；Quantinuum；Cisco Quantum Lab；University of California, Berkeley；University of California, Los Angeles；Oak Ridge National Laboratory

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790177) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Recent advances in quantum hardware and error correction have paved the way for early fault-tolerant (EFT) quantum computing. We propose iSwitch, a hybrid system architecture for trapped-ion quantum computers (TIQC) that exploits ultra-high-fidelity single-qubit gates and efficient logical CNOTs enabled by ion shuttling. iSwitch employs bare qubits for single-qubit operations and QEC-encoded logical qubits for two-qubit gates, avoiding full logical encoding, gate synthesis, and magic state distillation. To enable this selective encoding, we develop a low-noise conversion protocol between bare and logical qubits, a hybrid instruction set tailored to two-dimensional (2D) TIQC layouts, and a compiler that minimizes conversion overhead and optimizes scheduling. Evaluations on variational quantum algorithm benchmarks show that iSwitch achieves comparable fidelity to conventional QEC methods, while reducing qubit and operation counts by roughly 33–50%, offering a practical, resource-efficient path toward EFT quantum computing.

## 中文摘要

量子硬件与纠错方面的近期进展为早期容错（EFT）量子计算铺平了道路。我们提出 iSwitch，一种面向囚禁离子量子计算机（TIQC）的混合系统架构，它利用了超高保真度的单量子比特门以及由离子移动（shuttling）所实现的高效逻辑 CNOT 门。iSwitch 在单量子比特操作中使用裸量子比特，在双量子比特门中使用经 QEC 编码的逻辑量子比特，从而避免了完整的逻辑编码、门合成以及魔态蒸馏。为实现这种选择性编码，我们开发了一种裸量子比特与逻辑量子比特之间的低噪声转换协议、一套针对二维（2D）TIQC 布局定制的混合指令集，以及一个可最小化转换开销并优化调度的编译器。在变分量子算法基准上的评估表明，iSwitch 达到与常规 QEC 方法相当的保真度，同时将量子比特数和操作数降低约 33–50%，为通向 EFT 量子计算提供了一条实用且资源高效的路径。

## 英文关键词

Quantum computing, Quantum error correction, Ion Trap

## 中文关键词

量子计算；量子纠错；离子阱

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790177)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2026](../index.md)
