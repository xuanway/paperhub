---
title: "Hardware-aware Calibration Protocol for Quantum Computers"
description: "ISCA 2025 · Session 3A · 面向量子计算机的硬件感知校准协议"
tags:
  - "ISCA2025"
  - "Session 3A"
  - "Quantum I"
---

# Hardware-aware Calibration Protocol for Quantum Computers

**中文标题：** 面向量子计算机的硬件感知校准协议

**所属 Session：** [Session 3A](index.md) · [ISCA 2025](../index.md)

**作者：** Yuchen Zhu, Jinglei Cheng, Boxi Li, Kecheng Liu, Yidong Zhou, Hanrui Wang, Yufei Ding, Zhiding Liang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731036) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Calibration of a quantum computer is the process of optimizing its control parameters to ensure the accurate implementation of quantum gates. It remains a critical challenge in scaling quantum computers. Existing calibration methods take a generalized approach that focuses on the trade-off between calibration time and fidelity. However, these methods lack the awareness of hardware differences among physical qubits and an elaborate design of parallel calibration. In this paper, we introduce a fine-grained calibration protocol that contains three calibration policies for hardware differences and a method to enable parallel calibration. We begin by profiling qubit pairs to evaluate their responses to different waveform candidates. Based on profiling results, we determine the best calibration policy for the quantum computer, which is the first part of the calibration protocol. The second part of our protocol is to use graph traverse to enable parallel calibration by identifying compatible calibration operations. We validate our protocol through intensive experiments on real quantum machines with up to 127 qubits. Our experimental results demonstrate a 1.84×reduction in terms of the medium of the two-qubit gate error rate, 1.26×reduction in pulse duration, an 8×to 25×reduction in total calibration overhead compared with sequential calibration, an average of 2.12×further reduction in total calibration overhead owing to profiling policy, double of the quantum volume, and a 2.0×to 2.3×reduction in error per layered gate. The proposed protocol emphasizes the importance of hardware-aware and parallel calibration and advances current quantum computers towards fault-tolerant quantum computing.

## 中文摘要

量子计算机校准是优化其控制参数、保证量子门精准执行的过程，也是量子计算机规模化路上的核心难题。现有校准方案属于通用思路，主要权衡校准时间与保真度，但这类方案无法感知物理量子比特之间的硬件差异，并行校准机制也缺乏精巧设计。本文提出一种细粒度校准协议，包含三类适配硬件差异的校准策略以及一套支持并行校准的方法。我们首先对量子比特对进行特征剖析，评估它们对不同候选波形的响应；基于剖析结果，为量子计算机选定最优校准策略，这是本校准协议的第一部分。协议第二部分借助图遍历识别可兼容的校准操作，从而实现并行校准。我们在最多127比特的真实量子设备上开展大量实验验证该协议。实验结果表明：相比串行校准，双量子门错误率的中位数下降至原来的1/1.84，脉冲时长缩短至原来的1/1.26，总校准开销降低至原来的1/8~1/25；得益于特征剖析策略，总校准开销可进一步平均降低2.12倍；量子体积提升一倍，分层门错误率下降至原来的1/2.0~1/2.3。该协议凸显了硬件感知与并行校准的重要性，推动现有量子计算机向容错量子计算迈进。

## 英文关键词

Quantum Computing, Calibration, Quantum Control

## 中文关键词

量子计算, 校准, 量子控制

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15104875)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731036)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2025](../index.md)
