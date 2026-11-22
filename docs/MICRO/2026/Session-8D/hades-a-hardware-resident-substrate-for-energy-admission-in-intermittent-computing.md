---
title: "Hades: A Hardware-Resident Substrate for Energy Admission in Intermittent Computing"
description: "MICRO 2026 · Session 8D · Hades：间歇式计算中驻留硬件的能量准入基础结构"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# Hades: A Hardware-Resident Substrate for Energy Admission in Intermittent Computing

**中文标题：** Hades：间歇式计算中驻留硬件的能量准入基础结构

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Han Wang, Chong Zhang, Qianhe Meng, Yizhe Zhao, Ruizhe Zhang, Li Lu

**来源：** MICRO 2026，pp. 3132–3146；[DOI](https://doi.org/10.1109/MICRO67795.2026.00211)

## 英文摘要

Batteryless devices operate from ambient energy and avoid the maintenance burden of replaceable batteries. Their power supply is usually intermittent, so a bounded task should begin only after local storage can support its execution. Existing systems usually make this decision in software. The microcontroller unit (MCU) wakes, senses the storage state, and runs admission code before useful work starts. Under weak input, this path can consume up to 70% of the incoming power budget. This paper presents Hades, an always-on mixed-signal substrate that performs energy admission while the MCU remains off. Its Energy Intake Front-End selects source–bank paths from characterized loaded-voltage windows. An in situ Energy Aggregator produces a calibrated analog proxy for deliverable energy across distributed capacitor banks. A Dispatch Controller applies the selected task threshold, releases the MCU, and holds the execution grant through the task window. Using a 180 nm process design kit (PDK), we calibrate a co-simulation that integrates analog mixed-signal (AMS) models with register-transfer-level (RTL) control. In this flow, Hades reduces modeled runtime admission energy by more than 98% relative to the software-mediated baseline. The reported admission-control core occupies 0.29% of the evaluated system-on-chip (SoC) area. Across 12 workloads, Hades completes 2.4× more tasks per joule and achieves up to 2.5× higher throughput than the baseline.

## 中文摘要

无电池设备利用环境能量运行，避免了可更换电池的维护负担。它们的电源通常是间歇性的，因此有界任务只能在本地存储可以支持其执行后才开始。现有系统通常在软件中做出此决定。微控制器单元 (MCU) 唤醒、感测存储状态，并在有用的工作开始之前运行准入代码。在弱输入情况下，该路径可能消耗高达 70% 的输入功率预算。本文介绍了 Hades，一种始终开启的混合信号基板，可在 MCU 保持关闭状态时执行能量接纳。其能量摄入前端从特征负载电压窗口中选择源-组路径。现场能量聚合器生成校准模拟代理，用于跨分布式电容器组输送能量。调度控制器应用选定的任务阈值，释放 MCU，并通过任务窗口保留执行授权。使用 180 nm 工艺设计套件 (PDK)，我们校准了将模拟混合信号 (AMS) 模型与寄存器传输级 (RTL) 控制集成在一起的联合仿真。在此流程中，相对于软件介导的基线，Hades 将建模的运行时准入能量减少了 98% 以上。所报告的准入控制核心占据了评估的片上系统 (SoC) 面积的 0.29%。在 12 个工作负载中，Hades 每焦耳完成的任务增加了 2.4 倍，吞吐量比基准高出 2.5 倍。

## 中文关键词

间歇计算；能量准入；能量采集系统；混合信号架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
