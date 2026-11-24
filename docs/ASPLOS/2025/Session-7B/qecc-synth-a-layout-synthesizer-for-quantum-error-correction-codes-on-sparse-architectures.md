---
title: "QECC-Synth: A Layout Synthesizer for Quantum Error Correction Codes on Sparse Architectures"
description: "ASPLOS 2025 · Session 7B · QECC-Synth：面向稀疏体系结构的量子纠错码布局综合器"
tags:
  - "ASPLOS2025"
  - "Session 7B"
  - "Quantum Error Correction"
---

# QECC-Synth: A Layout Synthesizer for Quantum Error Correction Codes on Sparse Architectures

**中文标题：** QECC-Synth：面向稀疏体系结构的量子纠错码布局综合器

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Keyi Yin (University of California, San Diego), Hezi Zhang (University of California, San Diego), Xiang Fang (University of California, San Diego), Yunong Shi (AWS Quantum Technologies), Travis S. Humble (Oak Ridge National Laboratory), Ang Li (Pacific Northwest National Laboratory), Yufei Ding (University of California, San Diego)

**单位：** University of California, San Diego；AWS Quantum Technologies；Oak Ridge National Laboratory；Pacific Northwest National Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707236) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Quantum Error Correction (QEC) codes are essential for achieving fault-tolerant quantum computing (FTQC). However, their implementation faces significant challenges due to disparity between required dense qubit connectivity and sparse hardware architectures. Current approaches often either underutilize QEC circuit features or focus on manual designs tailored to specific codes and architectures, limiting their capability and generality. In response, we introduce QECC-Synth, an automated compiler for QEC code implementation that addresses these challenges. We leverage the ancilla bridge technique tailored to the requirements of QEC circuits and introduces a systematic classification of its design space flexibilities. We then formalize this problem using the MaxSAT framework to optimize these flexibilities. Evaluation shows that our method significantly outperforms existing methods while demonstrating broader applicability across diverse QEC codes and hardware architectures.

## 中文摘要

量子纠错（QEC）码对于实现容错量子计算（FTQC）至关重要。然而，由于所需的密集量子比特连通性与稀疏硬件架构之间存在差距，其实现面临重大挑战。现有方法往往要么未能充分利用 QEC 电路特性，要么专注于针对特定码和架构的手工设计，从而限制了其能力与通用性。为此，我们提出 QECC-Synth，一个用于 QEC 码实现的自动化编译器，以应对这些挑战。我们采用面向 QEC 电路需求定制的 ancilla bridge 技术，并对其设计空间中的灵活性提出系统化分类。随后，我们使用 MaxSAT 框架对该问题进行形式化，以优化这些灵活性。评估表明，我们的方法显著优于现有方法，同时在多种 QEC 码和硬件架构上展现出更广泛的适用性。

## 英文关键词

Quantum computing, Quantum error correction, QEC circuit synthesis

## 中文关键词

量子计算；量子纠错；QEC 电路综合

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707236)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2025](../index.md)
