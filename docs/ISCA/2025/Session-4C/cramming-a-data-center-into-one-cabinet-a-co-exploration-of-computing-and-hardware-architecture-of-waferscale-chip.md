---
title: "Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture of Waferscale Chip"
description: "ISCA 2025 · Session 4C · 将数据中心装进一个机柜：晶圆级芯片计算与硬件架构协同探索"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture of Waferscale Chip

**中文标题：** 将数据中心装进一个机柜：晶圆级芯片计算与硬件架构协同探索

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Xingmao Yu, Dingcheng Jiang, Jinyi Deng, Jingyao Liu, Chao Li, Shouyi Yin, Yang Hu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731016) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rapid advancements in large language models (LLMs) have sig- nificantly increased hardware demands. Wafer-scale chips, which integrate numerous compute units on an entire wafer, offer a high- density computing solution for data centers and can extend Moore’s Law at system level. However, current wafer-scale data center ar- chitectures face inefficiencies, such as uncoordinated resource al- location and lack of co-optimization for system area, preventing optimal integration density and performance within given cost and physical constraints. We propose a co-exploration approach of computing and hardware architectures to bridge this gap. We first develop an optimized wafer-scale single-cabinet data center model, integrating configurable on-chip memory dies and employing a vertically stacked hardware architecture. Based on this model, we introduce Titan, an automated exploration framework for intra-chip and inter-chip architecture design and optimization. Based on the architecture features of wafer-scale systems with opti- mal integration density, Titan establishes parameter dependencies to co-design the computing and hardware architectures. To reduce the design cycle for wafer-scale systems, Titan introduces vertical area constraints and pre-checks physical limits by integrating a series of reliability prediction models. It also integrates hardware capacity and cost evaluations to enable multi-objective optimiza- tion. Under the same cost constraint, on average, Titan’s cabinet design architecture improves system computing capacity by 2.90×, communication bandwidth by 2.11×, and memory bandwidth by 11.23×compared to the state-of-the-art Dojo-like wafer-scale single tray architecture. Simulated in different scenarios, Titan’s design delivers 3.17×and 10.66×performance improvement for Llama2-7B and Llama2-72B. Moreover, we leverage Titan to uncover insights into the optimal single-chip area choice within a cabinet under different cost constraints.

## 中文摘要

大语言模型（LLM）的快速发展大幅提升了硬件需求。晶圆级芯片在整片晶圆上集成大量计算单元，为数据中心提供高密度计算方案，可以在系统层面延续摩尔定律。然而当前晶圆级数据中心架构存在诸多低效问题：资源分配缺乏协同、系统面积没有协同优化，导致在既定成本与物理约束下，集成密度和性能无法达到最优。本文提出一套计算与硬件架构协同探索方案，解决上述问题。

首先，我们搭建经过优化的晶圆级单柜数据中心模型，集成可配置片上存储裸片，并采用垂直堆叠硬件架构。基于该模型，本文提出Titan，一个用于芯片内、芯片间架构设计与优化的自动化探索框架。Titan基于具备最优集成密度的晶圆级系统特征，建立参数依赖关系，实现计算与硬件架构协同设计。为缩短晶圆级系统的设计周期，Titan引入垂直面积约束，并集成一系列可靠性预测模型，提前校验物理极限；同时纳入硬件容量与成本评估，支持多目标优化。

在相同成本约束下，Titan输出的机柜架构对比前沿、类似Dojo的晶圆级单托盘架构，平均系统计算容量提升2.90倍、通信带宽提升2.11倍、内存带宽提升11.23倍。在不同场景仿真测试中，Titan设计在Llama2-7B、Llama2-72B上分别实现3.17倍、10.66倍性能提升。此外，我们借助Titan分析了在不同成本约束下，机柜内单芯片最优面积的选择规律。

## 英文关键词

Wafer-scale integration, Computing and hardware architecture, Datacenter

## 中文关键词

晶圆级集成, 计算和硬件架构, 数据中心

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731016)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
