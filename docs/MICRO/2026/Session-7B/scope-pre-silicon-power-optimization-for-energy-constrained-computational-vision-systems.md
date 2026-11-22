---
title: "SCOPE: Pre-Silicon Power Optimization for Energy-Constrained Computational Vision Systems"
description: "MICRO 2026 · Session 7B · SCOPE：面向能量受限计算视觉系统的流片前功耗优化"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# SCOPE: Pre-Silicon Power Optimization for Energy-Constrained Computational Vision Systems

**中文标题：** SCOPE：面向能量受限计算视觉系统的流片前功耗优化

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Qing Yu, Yiexian Tay, Qidan Cai, Erxiang Ren, Haijin Su, Tianrui Ma, An Zou, Li Luo, Yan Liang, Qi Wei, Zidong Du, Qi Guo, Fei Qiao

**来源：** MICRO 2026，pp. 2479–2494；[DOI](https://doi.org/10.1109/MICRO67795.2026.00170)

## 英文摘要

As computational vision workloads migrate from the cloud to energy-constrained edge devices, the mismatch between computational demand and limited, intermittent power supply becomes a first-order bottleneck. Prior efforts predominantly optimize compute and dataflow, while power management and energy scheduling, which co-determine energy, latency, and task accuracy, remain insufficiently integrated into pre-silicon evaluation. Conventional Power Management Units (PMUs) are unaware of workload dynamics, and existing energy schedulers are typically ad hoc. Therefore, the community lacks a PMU-aware, system-level tool for pre-silicon early design. We introduce SCOPE, a modular framework that closes this gap by (i) jointly modeling sensing, compute, storage, and PMU behavior; (ii) coupling a cycle-accurate execution engine with a power-flow model to co-simulate timing and energy delivery; and (iii) enabling system-level pre-silicon design space exploration. Validated against published and in-house chip data, SCOPE models PMU output voltage with 95.64% average accuracy and PMU power consumption with 87.06% average accuracy. Using SCOPE, we evaluate different compute strategies under various power management profiles, and show actionable design choices for selecting operating points, storage sizing, and scheduling strategies. These results provide a PMU-aware, cross-stack path for optimizing energy-constrained computational vision systems.

## 中文摘要

随着计算视觉工作负载从云端迁移到能源受限的边缘设备，计算需求与有限的间歇性电源之间的不匹配成为首要瓶颈。先前的努力主要是优化计算和数据流，而共同决定能源、时延和任务准确性的电源管理和能源调度仍然没有充分集成到投片前评估中。传统的电源管理单元 (PMU) 不了解工作负载动态，并且现有的能源调度程序通常是时间的。因此，社区缺乏用于硅前早期设计的 PMU 感知系统级工具。我们引入了 SCOPE，这是一个模块化框架，它通过以下方式缩小了这一差距：(i) 联合建模传感、计算、存储和 PMU 行为； (ii) 将周期精确的执行引擎与功率流模型耦合以共同模拟时序和能量传输； (iii) 实现系统级硅前设计空间探索。根据已发布和内部芯片数据进行验证，SCOPE 对 PMU 输出电压进行建模，平均精度为 95.64%，对 PMU 功耗建模，平均精度为 87.06%。使用 SCOPE，我们评估各种电源管理配置文件下的不同计算策略，并展示用于选择操作点、存储大小和调度策略的可行设计选择。这些结果为优化能量受限的计算视觉系统提供了 PMU 感知的跨堆栈路径。

## 中文关键词

建模工具；功耗管理；优化；硅前设计；计算视觉系统

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
