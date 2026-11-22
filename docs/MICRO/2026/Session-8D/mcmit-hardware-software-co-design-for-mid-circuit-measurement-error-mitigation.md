---
title: "MCMit: Hardware-Software Co-Design for Mid-Circuit Measurement Error Mitigation"
description: "MICRO 2026 · Session 8D · MCMit：面向量子电路中途测量误差缓解的软硬件协同设计"
tags:
  - "MICRO2026"
  - "HW-SW Co-design"
---

# MCMit: Hardware-Software Co-Design for Mid-Circuit Measurement Error Mitigation

**中文标题：** MCMit：面向量子电路中途测量误差缓解的软硬件协同设计

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Emmanouil Giortamis, Felix Gust, Aleksandra Swierkowska, Sandra Stankovic, Innocenzo Fulginiti, Yanbin Chen, Xiaorang Guo, Benjamin Lienhard, Martin Schulz, Pramod Bhatotia

**来源：** MICRO 2026，pp. 3053–3071；[DOI](https://doi.org/10.1109/MICRO67795.2026.00207)

## 英文摘要

Distributed Quantum Computing (DQC) and Quantum Error Correction (QEC) rely on dynamic circuits that include Mid-Circuit Measurements (MCMs) and classical feedback. These operations present a major bottleneck: MCMs suffer from high error rates that lead to real-time branching errors, while MCM and classical feedback latencies amplify decoherence errors. Current hardware controllers, qubit-state discriminators, and software error mitigation techniques fail to address these challenges holistically. We propose MCMit, a hardware-software co-design to mitigate branching and latency-induced errors. MCMit introduces a scalable, constant-latency multi-control branch instruction for faster classical feedback and two qubit-state discriminators, a transformer, and a CNN, with high accuracy even under short measurement durations. On the software side, static MCM elimination and stochastic branching complement the hardware by mitigating residual branching errors that persist despite hardware improvements. We implement MCMit on Qubic and evaluate it using experimentally extracted QPU readout traces. Our branch instruction reduces feedback latency by up to 70%, improving circuit depths by up to 7× over Qubic. Our CNN discriminator achieves up to 62% higher accuracy for short measurement durations than the baselines, driving 1.2-9.4× lower logical error rates in QEC. Last, our software mitigation improves fidelity by 18-30% over baseline methods in DQC workloads.

## 中文摘要

分布式量子计算（DQC）和量子纠错 (QEC) 依赖于包括电路中途测量 (MCM) 和经典反馈的动态电路。这些操作存在一个主要瓶颈：MCM 的错误率很高，导致实时分支错误，而 MCM 和经典反馈时延会放大退相干错误。当前的硬件控制器、量子位状态鉴别器和软件错误缓解技术无法全面解决这些挑战。我们提出了 MCMit，这是一种硬件软件协同设计，可以减少分支和时延引起的错误。 MCMit 引入了可扩展、恒定时延的多控制分支指令，可实现更快的经典反馈和两个量子位状态鉴别器、一个Transformer和一个 CNN，即使在较短的测量持续时间下也具有高精度。在软件方面，静态 MCM 消除和随机分支通过减少尽管硬件改进但仍然存在的残余分支错误来补充硬件。我们在 Qubic 上实现 MCMit，并使用实验提取的 QPU 读出轨迹对其进行评估。我们的分支指令将反馈时延减少了 70%，与 Qubic 相比，电路深度提高了 7 倍。我们的 CNN 判别器在短测量时间内的准确度比基线高出 62%，从而使 QEC 中的逻辑错误率降低 1.2-9.4 倍。最后，我们的软件缓解措施比 DQC 工作负载中的基准方法提高了 18-30% 的保真度。

## 中文关键词

中途电路测量；量子误差缓解；软硬件协同设计；量子计算

## 代码与研究制品

- 代码仓库：[https://github.com/manosgior/MCMit](https://github.com/manosgior/MCMit)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21485912](https://doi.org/10.5281/zenodo.21485912)

以上入口来自论文正文或 Artifact 附录。

## 来源核对说明

元数据漏掉摘要开头的 Distributed Quantum Computing；中文译文按 PDF 补为“分布式量子计算”。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
