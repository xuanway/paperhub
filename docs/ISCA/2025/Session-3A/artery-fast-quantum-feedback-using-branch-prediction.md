---
title: "ARTERY: Fast Quantum Feedback using Branch Prediction"
description: "ISCA 2025 · Session 3A · ARTERY: 利用分支预测实现快速量子反馈"
tags:
  - "ISCA2025"
  - "Session 3A"
  - "Quantum I"
---

# ARTERY: Fast Quantum Feedback using Branch Prediction

**中文标题：** ARTERY: 利用分支预测实现快速量子反馈

**所属 Session：** [Session 3A](index.md) · [ISCA 2025](../index.md)

**作者：** Wuwei Tian, Liqiang Lu, Siwei Tan, Yun Liang, Tingting Li, Kaiwen Zhou, Xinghui Jia, Jianwei Yin

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731086) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Quantum feedback makes the execution of dynamic quantum circuits possible and is widely used in quantum algorithms. However, due to the inherent computation and transmission cost, the latency of the quantum feedback becomes a considerable burden on the current quantum algorithm. The dynamic property of the feedback also makes the gates blocked until the feedback is finished. In this paper, we propose ARTERY, which uses branch prediction to support instruction pre-execution and speed up the feedback. ARTERY integrates historical statistics of branches and a real-time readout pulse analysis to predict the branch. With this idea, we build up a reconciled branch predictor that concatenates the historical statistics of branches and a real-time branch circuit speculation obtained from the readout-pulse trajectory predictor. We further explore the implementation of peripheral hardware for feedback, including a scalable inter-FPGA connection via the backplane, a feedback trigger mechanism for dynamic instruction timing, and an adaptive pulse sampling technique to maximize the hardware bandwidth. ARTERY accelerates quantum feedback process by 2.07×compared to the state-of-the-art method, with over 90% prediction accuracy, achieving 1.24×fidelity improvement.

## 中文摘要

量子反馈使动态量子电路的执行成为可能，在量子算法中应用广泛。但由于固有的计算与传输开销，量子反馈的延迟成为当前量子算法运行中不可忽视的负担。反馈所具备的动态特性还会导致后续量子门被阻塞，必须等待反馈流程完成才能执行。本文提出ARTERY，利用分支预测实现指令预执行，以此加速量子反馈。ARTERY结合分支历史统计信息与实时读出脉冲分析完成分支预测。基于该思路，我们构建融合型分支预测器，它整合分支历史统计，以及由读出脉冲轨迹预测器得到的实时分支电路推测结果。我们进一步研究反馈配套外设硬件的实现方案，包括基于背板的可扩展FPGA间互联、适配动态指令时序的反馈触发机制，以及最大化硬件带宽的自适应脉冲采样技术。对比现有最优方案，ARTERY将量子反馈流程加速2.07倍，预测准确率高于90%，保真度提升1.24倍。

## 英文关键词

Quantum Feedback, Branch Prediction

## 中文关键词

量子反馈, 分支预测

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731086)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2025](../index.md)
