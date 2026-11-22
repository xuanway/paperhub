---
title: "KAIROS: Fast Microarchitectural Design Space Exploration by Bridging Architectural Semantics and Logic Gates"
description: "MICRO 2026 · Session 3B · KAIROS：连接架构语义与逻辑门，实现快速微架构设计空间探索"
tags:
  - "MICRO2026"
---

# KAIROS: Fast Microarchitectural Design Space Exploration by Bridging Architectural Semantics and Logic Gates

**中文标题：** KAIROS：连接架构语义与逻辑门，实现快速微架构设计空间探索

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Shilin Tian, Sanjay Gandham, Lingxiang Yin, Mingjie Lin, Hao Zheng

**来源：** MICRO 2026，pp. 1021–1037；[DOI](https://doi.org/10.1109/MICRO67795.2026.00081)

## 英文摘要

The proliferation of generative AI and Large Language Models (LLMs), with the availability of open-source RTL libraries, has drastically shortened the time needed for RTL development. Hardware design is poised to transition from traditional manual coding to parameterized microarchitectural compilation. However, this rapid acceleration in RTL generation has inadvertently exposed a severe bottleneck in microarchitectural Design Space Exploration (DSE). Effective DSE requires evaluating candidate architectures in terms of functional performance (e.g., instructions per cycle) and physical performance (e.g., achievable clock frequency). However, while functional performance can be assessed using cycle-accurate simulation, evaluating physical performance still relies on gate-level logic synthesis, which often takes hours or even days to refine and optimize microarchitectural configurations. In this paper, we identify the primary bottleneck in current chip design workflows as the semantic gap between microarchitectural design and physical design, through which the original design intent is irreversibly lost after logic synthesis. To address this challenge, we introduce a new Circuit Intermediate Representation (CIR) that preserves microarchitectural design intent by connecting RTL functional semantics with the corresponding synthesized gate-level netlist. On top of CIR, we build KAIROS, an optimization framework for efficient microarchitectural exploration. By retaining word-level RTL operators and signal names, KAIROS supports traceable operator-level critical path analysis without suffering from the semantic loss inherent in gate-level synthesis. In addition, we construct And-Inverter Graphs (AIGs) for operator-level timing prediction and develop CIR-based fan-out optimization and retiming techniques to identify Pareto-optimal physical implementations. This framework thus enables fast microarchitectural design space exploration with RTL-level accuracy. Evaluated on 41 designs spanning datapath, control, and memory components, from embedded cores to industrial-scale designs (the NVDLA accelerator and the CVA6 application-class core), KAIROS preserves post-synthesis Fmax rankings with Spearman ρ=0.96, achieves 7.1-13.4% frequency improvement on datapath circuits with 9.4% average area overhead, and completes timing evaluation 113× faster than synthesis on average, up to 213× on industrial-scale designs.

## 中文摘要

生成式 AI 和大语言模型 (LLM) 的激增，以及开源 RTL 库的可用性，大大缩短了 RTL 开发所需的时间。硬件设计准备从传统的手动编码过渡到参数化微架构编译。然而，RTL 生成的快速加速无意中暴露了微架构设计空间探索 (DSE) 中的严重瓶颈。有效的 DSE 需要根据功能性能（例如，每个周期的指令）和物理性能（例如，可实现的时钟频率）来评估候选架构。然而，虽然可以使用周期精确的仿真来评估功能性能，但评估物理性能仍然依赖于门级逻辑综合，这通常需要数小时甚至数天的时间来细化和优化微架构配置。在本文中，我们将当前芯片设计工作流程的主要瓶颈确定为微架构设计和物理设计之间的语义差距，通过这种差距，原始设计意图在逻辑综合后不可逆转地丢失。为了应对这一挑战，我们引入了一种新的电路中间表示（CIR），它通过将 RTL 功能语义与相应的综合门级网表连接起来来保留微架构设计意图。在 CIR 之上，我们构建了 KAIROS，一个用于高效微架构探索的优化框架。通过保留字级 RTL 运算符和信号名称，KAIROS 支持可追踪的运算符级关键路径分析，而不会遭受门级综合中固有的语义损失。此外，我们还构建了用于算子级时序预测的与逆变器图 (AIG)，并开发了基于 CIR 的扇出优化和重定时技术来识别帕累托最优物理实现。因此，该框架能够实现具有 RTL 级精度的快速微架构设计空间探索。对涵盖数据路径、控制和内存组件的 41 种设计进行评估，从嵌入式内核到工业规模设计（NVDLA 加速器和 CVA6 应用级内核），KAIROS 保留了 Spearman ρ = 0.96 的综合后 Fmax 排名，在数据路径电路上实现了 7.1-13.4% 的频率改进，平均面积开销为 9.4%，完成时序评估的速度平均比综合快 113 倍，高达工业规模设计可达 213×。

## 中文关键词

集成电路；微架构；设计空间探索；逻辑综合；时序预测；RTL 优化

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
