---
title: "Clapton: Clifford Assisted Problem Transformation for Error Mitigation in Variational Quantum Algorithms"
description: "ASPLOS 2025 · Session 7B · Clapton：面向变分量子算法误差缓解的 Clifford 辅助问题变换"
tags:
  - "ASPLOS2025"
  - "Session 7B"
  - "Quantum Error Correction"
---

# Clapton: Clifford Assisted Problem Transformation for Error Mitigation in Variational Quantum Algorithms

**中文标题：** Clapton：面向变分量子算法误差缓解的 Clifford 辅助问题变换

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Lennart Maximilian Seifert (Department of Computer Science, University of Chicago), Siddharth Dangwal (Department of Computer Science, University of Chicago), Frederic T. Chong (Department of Computer Science, University of Chicago), Gokul Subramanian Ravi (Electrical Engineering and Computer Science Department, University of Michigan)

**单位：** Department of Computer Science, University of Chicago；Electrical Engineering and Computer Science Department, University of Michigan

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674178) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Variational quantum algorithms (VQAs) show potential for quantum advantage in the near term of quantum computing, but demand a level of accuracy that surpasses the current capabilities of NISQ devices. To systematically mitigate the impact of quantum device error on VQAs, we propose Clapton: Clifford-Assisted Problem Transformation for Error Mitigation in Variational Quantum Algorithms. Clapton leverages classically estimated good quantum states for a given VQA problem, classical simulable models of device noise, and the variational principle for VQAs. It applies transformations on the VQA problem's Hamiltonian to lower the energy estimates of known good VQA states in the presence of the modeled device noise. The Clapton hypothesis is that as long as the known good states of the VQA problem are close to the problem's ideal ground state and the device noise modeling is reasonably accurate (both of which are generally true), then the Clapton transformation substantially decreases the impact of device noise on the ground state of the VQA problem, thereby increasing the accuracy of the VQA solution. Clapton is built as an end-to-end application-to-device framework and achieves mean VQA initialization improvements of 1.7x to 3.7x, and up to a maximum of 13.3x, over the state-of-the-art baseline when evaluated for a variety of scientific applications from physics and chemistry on noise models and real quantum devices.

## 中文摘要

变分量子算法（VQA）在量子计算的近期阶段展现出实现量子优势的潜力，但其所需精度超出了当前 NISQ 设备的能力。为系统性地缓解量子设备错误对 VQA 的影响，我们提出 Clapton：一种用于变分量子算法误差缓解的 Clifford 辅助问题变换。Clapton 利用针对给定 VQA 问题经经典方式估计得到的良好量子态、设备噪声的经典可模拟模型，以及 VQA 的变分原理。在存在所建模的设备噪声的情况下，它对 VQA 问题的哈密顿量施加变换，以降低已知良好 VQA 态的能量估计。Clapton 的假设是：只要 VQA 问题的已知良好态接近该问题的理想基态，且设备噪声建模足够准确（两者通常都成立），那么 Clapton 变换就能显著降低设备噪声对 VQA 问题基态的影响，从而提高 VQA 解的精度。Clapton 被构建为端到端的应用—设备框架，在针对来自物理与化学领域的多种科学应用、在噪声模型与真实量子设备上评估时，相比最先进的基线，其 VQA 初始化精度平均提升 1.7 倍到 3.7 倍，最高达 13.3 倍。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674178)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2025](../index.md)
