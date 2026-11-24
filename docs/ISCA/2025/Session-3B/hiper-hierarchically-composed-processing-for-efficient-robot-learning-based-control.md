---
title: "HiPER: Hierarchically-Composed Processing for Efficient Robot Learning-Based Control"
description: "ISCA 2025 · Session 3B · HiPER：面向高效机器人学习控制的分层组合处理"
tags:
  - "ISCA2025"
  - "Session 3B"
  - "Domain Specific Accelerators I"
---

# HiPER: Hierarchically-Composed Processing for Efficient Robot Learning-Based Control

**中文标题：** HiPER：面向高效机器人学习控制的分层组合处理

**所属 Session：** [Session 3B](index.md) · [ISCA 2025](../index.md)

**作者：** Justin Ting, Minsik Kim, Junkang Zhu, Cody Sheng, Zhengya Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731097) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Learning-Based Model Predictive Control (LMPC) is a class of algo-

rithms that enhances Model Predictive Control (MPC) by including

machine learning methods, improving robot navigation in complex

environments. However, the combination of machine learning and

MPC computation in LMPC creates a unique workload that can-

not be efficiently handled by a simple GPU and CPU integration.

We present HiPER, a hierarchically-composed processing array

that provides temporal and spatial mapping capabilities, allowing

efficient adaptation to workload changes at runtime. To simplify

control, HiPER employs a pointer queue hierarchy to compose

and orchestrate program execution. Additionally, HiPER utilizes

a fractal interconnect topology that combines local systolic inter-

connects and their hierarchical extensions to efficiently support

the workload’s traffic characteristics. To evaluate the performance

and efficiency of HiPER, we synthesized a 16.37 mm2 design in

16nm CMOS. The design consists of 6 pointer queue levels and

1024 PEs. The prototype was assessed using a representative LMPC

workload, demonstrating 10.75×improvement in performance com-

pared to a GTX 1080 GPU, 12.80×improvement in energy efficiency

compared to a Jetson Orin Nano embedded GPU, and 11.6×/22.2×

improvement in performance compared to the RoboX/Plasticine

accelerators.

## 中文摘要

基于学习的模型预测控制（LMPC）是一类算法，它在模型预测控制（MPC）中引入机器学习方法，提升机器人在复杂环境下的导航能力。但LMPC中将机器学习与MPC计算融合后形成了独特负载，简单的GPU与CPU组合方案无法对其高效处理。本文提出HiPER，一种分层组合式处理阵列，具备时间与空间映射能力，能够在运行时高效适配负载变化。为简化控制，HiPER采用指针队列分层结构，对程序执行进行组装与调度。此外，HiPER使用分形互连拓扑，融合局部脉动互连及其分层扩展结构，高效适配该负载的流量特征。为评估HiPER的性能与能效，我们基于16nm CMOS工艺综合得到面积16.37 mm²的设计。该设计包含6级指针队列与1024个处理单元（PE）。我们采用典型LMPC负载对原型进行测试：相比GTX 1080 GPU，性能提升10.75倍；相比Jetson Orin Nano嵌入式GPU，能量效率提升12.80倍；对比RoboX与Plasticine加速器，性能分别提升11.6倍、22.2倍。

## 英文关键词

Accelerators, Model Predictive Control, Robotics

## 中文关键词

加速器, 模型预测控制, 机器人技术

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731097)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2025](../index.md)
