---
title: "Variational Quantum Algorithms in the Era of Early Fault Tolerance"
description: "ISCA 2025 · Session 7C · 早期容错时代的变分量子算法"
tags:
  - "ISCA2025"
  - "Session 7C"
  - "Quantum II"
---

# Variational Quantum Algorithms in the Era of Early Fault Tolerance

**中文标题：** 早期容错时代的变分量子算法

**所属 Session：** [Session 7C](index.md) · [ISCA 2025](../index.md)

**作者：** Siddharth Dangwal, Suhas Vittal, Lennart Maximilian Seifert, Fred Chong, Gokul Ravi

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731112) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Quantum computing roadmaps predict the availability of 10,000- qubit devices within the next 3–5 years. With projected two-qubit error rates of 0.1%, these systems will enable certain operations under quantum error correction (QEC) using lightweight codes, offering significantly improved fidelities compared to the NISQ era. However, the high qubit cost of QEC codes like the surface code (especially at near-threshold physical error rates) limits the error correction capabilities of these devices. In this emerging era of Early Fault Tolerance (EFT), it will be essential to use QEC resources efficiently and focus on applications that derive the greatest benefit. In this work, we investigate the implementation of Variational Quantum Algorithms in the EFT regime (EFT-VQA). We explore the ideas of partial quantum error correction (pQEC), a strategy that error-corrects Clifford operations while performing 𝑅𝑧(𝜃)rotations via magic state injection instead of the more expensive T-state distillation, and adapt it to VQAs. Our results show that pQEC can improve VQA fidelities by 9.27x over standard approaches. Furthermore, we propose architectural optimizations that reduce circuit latency by∼2x, and achieve qubit packing efficiency of 66% in the EFT regime. The source code can be accessed here https: //github.com/siddharthdangwal/EFT-VQA.

## 中文摘要

量子计算路线图预测，未来3–5年内将问世具备一万个量子比特的设备。如果双量子门错误率达到预期的0.1%，这类设备可以借助轻量化纠错码，在量子纠错（QEC）支撑下执行部分运算，保真度相比NISQ时代会大幅提升。
但表面码这类量子纠错码的比特开销很高（尤其在物理错误率接近容错阈值时），限制了这类设备的纠错能力。在这个新兴的早期容错（EFT）阶段，高效利用量子纠错资源、优先部署收益最高的应用至关重要。

本文研究在早期容错区间运行变分量子算法（EFT-VQA）。我们探索**部分量子纠错（pQEC）**方案：仅对克利福德操作做纠错，而$R_z(\theta)$旋转门采用魔法态注入实现，替代开销更大的T态蒸馏，并将该方案适配到变分量子算法。实验结果表明：相比传统方案，pQEC可将VQA的保真度提升9.27倍。此外，本文提出架构优化手段，线路延迟降低约2倍，在早期容错场景下实现66%的量子比特打包利用率。源码地址：https://github.com/siddharthdangwal/EFT-VQA

## 英文关键词

Quantum Error Correction, Early Fault Tolerance, Variational Quantum Algorithms

## 中文关键词

量子纠错, 早期容错, 变分量子算法

## 代码与研究制品

- [代码仓库](https://github.com/siddharthdangwal/EFT-VQA)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731112)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2025](../index.md)
