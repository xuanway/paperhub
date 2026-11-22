---
title: "UDYR: An Adaptive Accelerator for Optimization-Based Humanoid Robot Control"
description: "MICRO 2026 · Session 5A · UDYR：面向基于优化的人形机器人控制的自适应加速器"
tags:
  - "MICRO2026"
---

# UDYR: An Adaptive Accelerator for Optimization-Based Humanoid Robot Control

**中文标题：** UDYR：面向基于优化的人形机器人控制的自适应加速器

**所属 Session：** [Session 5A](index.md) · [MICRO 2026](../index.md)

**作者：** Yuhui Hao, Bo Yu, Shaoshan Liu, Yinhe Han, Yu Feng, Yiming Gan

**来源：** MICRO 2026，pp. 1629–1644；[DOI](https://doi.org/10.1109/MICRO67795.2026.00118)

## 英文摘要

Smoothly controlling a humanoid robot is critical to the success of embodied artificial intelligence (EAI), yet it remains an open challenge. Researchers lack clear guidance on which physical models—simple or complex—best capture humanoid dynamics, or how fast control algorithms must run under each model to enable high-dynamic movements. Not to mention how to design efficient hardware to support these algorithms. In this work, we take the first step of translating the physical need of a robot into the computational need of the chip. We propose UDYR, a unified control framework and hardware accelerator for high-performance humanoid robot control. UDYR framework encompasses a full control stack, including high-level model predictive control (MPC), mid-level whole-body control (WBC), and low-level proportional-derivative (PD) control. It adaptively selects the appropriate physical model and control frequency. We unify all different control optimizations into a single-format quadratic programming problem and design the UDYR accelerator to support all configurations efficiently. Evaluation results show that UDYR achieves up to 5.9x speedup over a high-performance CPU and successfully completes a wide range of dynamic tasks where baselines fail.

## 中文摘要

顺利控制人形机器人对于嵌入式人工智能（EAI）的成功至关重要，但这仍然是一个开放的挑战。研究人员缺乏明确的指导，无法确定哪种物理模型（简单或复杂）最能捕捉人形动力学，或者控制算法在每个模型下必须运行多快才能实现高动态运动。更不用说如何设计高效的硬件来支持这些算法了。在这项工作中，我们迈出了将机器人的物理需求转化为芯片的计算需求的第一步。我们提出了UDYR，一种用于高性能人形机器人控制的统一控制框架和硬件加速器。 UDYR框架包含完整的控制堆栈，包括高级模型预测控制（MPC）、中级全身控制（WBC）和低级比例微分（PD）控制。它自适应地选择适当的物理模型和控制频率。我们将所有不同的控制优化统一为单一格式的二次规划问题，并设计 UDYR 加速器以有效支持所有配置。评估结果表明，UDYR 比高性能 CPU 实现了高达 5.9 倍的加速，并成功完成了基线失败的各种动态任务。

## 中文关键词

人形机器人控制；机器人加速器；优化求解；自适应架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5A](index.md) · [MICRO 2026 主页](../index.md)
