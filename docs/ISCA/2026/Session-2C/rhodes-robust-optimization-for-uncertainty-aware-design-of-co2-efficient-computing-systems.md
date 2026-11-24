---
title: "RHODES: Robust Optimization for Uncertainty-Aware Design of CO2-Efficient Computing Systems"
description: "ISCA 2026 · Session 2C · RHODES: Robust Optimization for Uncertainty-Aware Design of CO2-Efficient Computing Systems"
tags:
  - "ISCA2026"
  - "Session 2C"
  - "Sustainability"
---

# RHODES: Robust Optimization for Uncertainty-Aware Design of CO2-Efficient Computing Systems

**中文标题：** RHODES: 面向 CO2 高效计算系统不确定性感知设计的鲁棒优化

**所属 Session：** [Session 2C](index.md) · [ISCA 2026](../index.md)

**作者：** Mariam Elgamal, Abdulrahman Mahmoud, Gu-Yeon Wei, David Brooks, Gage Hills

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The inherent uncertainty in quantifying carbon footprint is a major challenge for designing environmentally sustainable computing systems. While existing efforts propose a variety of approaches to address this uncertainty, optimizing carbon footprint and energy efficiency together, while also accounting for uncertainty in carbon footprint, remains challenging. We identify two types of uncertainty in CO2-aware hardware design: data value (DV) uncertainty, where probability distributions of CO2-related parameters exhibit high standard deviation (e.g., fluctuations in CO2 emissions of the power grid), and data availability (DA) uncertainty, in which probability distributions of CO2-related parameters cannot even be reliably estimated due to a lack of data (e.g., carbon emissions during integrated circuit fabrication, with very few data points available). DA uncertainty is especially challenging. To address this challenge, we leverage mathematical Robust Optimization (RO) techniques that enable uncertainty-aware decision-making without requiring explicit probability distributions. We present RHODES, a robust optimization framework for designing CO2-efficient computing systems under carbon footprint data uncertainty. RHODES jointly models DV and DA uncertainties at multiple layers of the computing stack to optimize total carbon (tC) under uncertainty, and can target 3 different primary objectives (we include example results for specific systems, details in the full paper): (1) minimizing execution time given a performance constraint: designs that do not account for uncertainty incur 1.7× worse tC for the same performance constraint; (2) minimizing execution time given a tC constraint: RHODES produces robust designs with 1.36× lower tC and only 0.2% execution time degradation, for complex heterogeneous system-on-chip (SoC), considering domain specific accelerators and workload level parallelism; and (3) minimizing total carbon delay product (tCDP, a metric of CO2 efficiency): improves tCDP by 1.3–3.17× vs. state-of-the-art CO2-aware optimization frameworks.

## 中文摘要

碳足迹量化中的固有不确定性是设计环境可持续计算系统的主要挑战。尽管已有工作提出了多种应对不确定性的方法，但同时优化碳足迹和能效并考虑碳足迹的不确定性仍然困难。我们在CO2感知硬件设计中发现两类不确定性：数据值（DV）不确定性，即CO2相关参数的概率分布表现出高标准差（如电网碳排放的波动）；数据可用性（DA）不确定性，即由于缺乏数据，CO2相关参数的概率分布甚至无法可靠估计（如IC制造过程中的碳排放，仅有极少数数据点）。DA不确定性尤其具有挑战性。为应对这一挑战，我们利用数学鲁棒优化（RO）技术，在不需显式概率分布的情况下实现不确定性感知决策。我们提出RHODES，一个用于碳足迹数据不确定性下设计CO2高效计算系统的鲁棒优化框架。RHODES联合建模计算栈多个层级的DV和DA不确定性，以在不确定性下优化总碳（tC），并可针对三个不同主要目标：（1）给定性能约束下最小化执行时间：不考虑不确定性的设计在相同性能约束下tC恶化1.7×；（2）给定tC约束下最小化执行时间：对于复杂的异构片上系统（SoC），考虑领域特定加速器和工作负载级并行，RHODES生成的鲁棒设计tC降低1.36×，执行时间仅退化0.2%；（3）最小化总碳延迟乘积（tCDP，一种CO2效率指标）：相比最先进的CO2感知优化框架，tCDP提升1.3–3.17×。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：mariamelgamal/RHODES](https://github.com/mariamelgamal/RHODES)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2C](index.md) · [返回 ISCA 2026](../index.md)
