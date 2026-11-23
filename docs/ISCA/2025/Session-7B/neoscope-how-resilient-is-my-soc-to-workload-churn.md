---
title: "Neoscope: How Resilient Is My SoC to Workload Churn?"
description: "ISCA 2025 · Session 7B · Neoscope：我的 SoC 对负载变动有多强的韧性？"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# Neoscope: How Resilient Is My SoC to Workload Churn?

**中文标题：** Neoscope：我的 SoC 对负载变动有多强的韧性？

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Joseph Rogers, Lieven Eeckhout, Taha Soliman, Magnus Jahre

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731014) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The lifetime of hardware is increasing, but the lifetime of software is not. This leads to devices that, while performant when released, have fall-off due to changing workload suitability. To ensure that performance is maintained, computer architects must begin consid- ering the effects of evolving workloads early in the design process. The ways that workloads can change, i.e., churn, over time pro- foundly affect hardware’s ability to maintain performance. 

To better understand churn, we introduce the concepts Magni- tude and Disruption, which enable how workloads change to be quantitatively described. By leveraging these terms, we present churn as a span, where the churn of a given workload can be cat- egorized as either Minimal, Perturbing, Escalating, or Volatile. To account for how churn affects performance, we propose Neoscope, the first multi-objective pre-silicon design space exploration tool for investigating System-on-Chip (SoC) architectures that are resilient to workload churn. Neoscope uses integer linear programming and concepts from job-shop scheduling to construct near-optimal SoCs for a given workload. Unlike previous methods, Neoscope approaches (and often finds) the globally optimal SoC with a single invocation, instead of needing to parameter sweep. Neoscope is also multi-objective, i.e., it can optimize for many kinds of met- rics other than absolute performance, including area, energy, cost, and carbon efficiencies. Using Neoscope, we explore near-optimal SoCs for many workload-churn configurations, and investigate how changing the objective function changes the ideal SoC. Neoscope shows that small SoCs need high levels of specialization, but that this is risky, as it increases susceptibility to churn.

## 中文摘要

硬件使用寿命越来越长，但软件和负载的生命周期却很短。这就造成一种现象：设备刚发布时性能很好，但随着负载变化，硬件适配性下降，性能逐步衰减。想要持续保障性能，体系结构研究者需要在硬件设计早期就考虑负载演化带来的影响。负载随时间发生变化（也就是负载波动 churn），会深刻影响硬件维持性能的能力。

为更好刻画负载波动，本文提出两个指标：变化幅度（Magnitude）与扰动度（Disruption），用于定量描述负载的变化方式。基于这两个指标，本文把负载波动划分为一个区间：最小波动（Minimal）、扰动型（Perturbing）、递增型（Escalating）和剧烈波动（Volatile）。

为评估负载波动对性能的影响，本文提出Neoscope，首款面向片上系统（SoC）、支持多目标的流片前设计空间探索工具，用于寻找对负载波动鲁棒的SoC架构。Neoscope结合整数线性规划与作业车间调度思想，为给定负载生成近似最优的SoC方案。和以往方法不同，Neoscope单次运行就可以逼近全局最优架构，不需要遍历参数网格。Neoscope支持多目标优化：除原始性能外，还可以同时优化面积、功耗、成本以及碳排放效率。我们使用Neoscope，在多种负载波动场景下搜索近似最优SoC，并研究优化目标变化如何改变最优架构。实验表明：小规模SoC需要高度专用化，但这种方案风险很高，更容易受负载波动冲击。

## 英文关键词

computer architecture, system-on-chip design, design space exploration, workload churn, performance, workload, carbon modeling

## 中文关键词

计算机体系结构, 片上系统设计, 设计空间探索, 负载波动, 性能, 工作负载, 碳排放建模

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15101433)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731014)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
