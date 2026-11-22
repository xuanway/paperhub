---
title: "Fidelio: Agentic AI Framework for Synthesizing Microarchitecture-Faithful Datacenter Benchmarks"
description: "MICRO 2026 · Session 3B · Fidelio：用于合成忠实反映微架构特征的数据中心基准测试的智能体 AI 框架"
tags:
  - "MICRO2026"
---

# Fidelio: Agentic AI Framework for Synthesizing Microarchitecture-Faithful Datacenter Benchmarks

**中文标题：** Fidelio：用于合成忠实反映微架构特征的数据中心基准测试的智能体 AI 框架

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Alan Andrade, Petar Acimovic, Wei Su, Suyash Mahar, Apostolos Kokolis, Abhishek Dhanotia, Jovan Stojkovic

**来源：** MICRO 2026，pp. 1038–1053；[DOI](https://doi.org/10.1109/MICRO67795.2026.00082)

## 英文摘要

Datacenter workloads drive modern processor design, yet representative benchmarks remain scarce. Production services cannot be shared due to confidentiality, and manually engineered proxies are expensive to build, difficult to maintain, and quickly drift out of date. On the other hand, prior automated approaches, e.g., statistical cloning, target a single hardware configuration, offering no guarantee that the resulting benchmark will respond to microarchitectural design changes in the same way as the original workload. We present Fidelio, an agentic AI framework that automatically synthesizes portable benchmark clones from lightweight hardware telemetry. Fidelio orchestrates a closed-loop, multi-agent workflow in two phases. First, agents iteratively generate, measure, and refine candidate programs on real hardware to match a tiered, weighted set of performance counters. Next, agents sweep key design knobs (e.g., prefetcher, branch predictor, replacement policy) through architectural simulations for these candidates and repair any divergence in performance-sensitivity trends relative to the target workload. Microarchitecture-aware diagnostic playbooks guide each transformation, ensuring that fixes for one objective do not regress another. We evaluate Fidelio on open-source datacenter benchmarks from the DCPerf suite and production workloads at a hyperscaler. Across both sets, Fidelio produces clones that faithfully reproduce hardware-counter profiles and preserve sensitivity to microarchitectural design changes. This enables credible, privacy-preserving design-space exploration for realistic datacenter workloads.

## 中文摘要

数据中心工作负载推动现代处理器设计，但具有代表性的基准测试仍然稀缺。由于保密性，生产服务无法共享，并且手动设计的代理构建成本高昂，难以维护，并且很快就会过时。另一方面，先前的自动化方法（例如统计克隆）针对单一硬件配置，无法保证生成的基准测试将以与原始工作负载相同的方式响应微架构设计更改。我们推出了 Fidelio，这是一种代理 AI 框架，可以根据轻量级硬件遥测自动合成便携式基准克隆。 Fidelio 分两个阶段编排闭环、多代理工作流程。首先，代理在真实硬件上迭代生成、测量和完善候选程序，以匹配分层、加权的性能计数器集。接下来，代理通过这些候选者的架构模拟扫描关键设计旋钮（例如预取器、分支预测器、替换策略），并修复相对于目标工作负载的性能敏感度趋势的任何差异。微架构感知诊断手册指导每一次转型，确保一个目标的修复不会使另一个目标倒退。我们根据 DCPerf 套件的开源数据中心基准和超大规模企业的生产工作负载来评估 Fidelio。在这两个集合中，Fidelio 生成的克隆可以忠实地再现硬件计数器配置文件并保留对微架构设计更改的敏感性。这使得能够针对实际数据中心工作负载进行可靠、保护隐私的设计空间探索。

## 中文关键词

数据中心服务；基准测试；智能体人工智能；微架构保真

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
