---
title: "Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign"
description: "MICRO 2026 · Session 5B · Fengshui：揭示芯粒生态与定制神经网络加速器协同设计"
tags:
  - "MICRO2026"
  - "Neural Networks"
---

# Fengshui: Demystifying Chiplet Ecosystem and Bespoke Neural Network Accelerator Codesign

**中文标题：** Fengshui：揭示芯粒生态与定制神经网络加速器协同设计

**所属 Session：** [Session 5B](index.md) · [MICRO 2026](../index.md)

**作者：** Haoran Jin, Jirong Yang, Zhiheng Zhang, Justin Shin, Barry Lyu, Kangqi Zhang, Yunpeng Liu, Nathan Bleier

**来源：** MICRO 2026，pp. 1645–1661；[DOI](https://doi.org/10.1109/MICRO67795.2026.00119)

## 英文摘要

Modern ML workloads, with stringent latency and energy constraints, are increasingly hard to run efficiently on homogeneous commodity hardware. We argue that operator-level disaggregation–tailoring microarchitecture, batching, and memory hierarchy to each operator–is essential to overcome these limitations, though the resulting highly bespoke accelerators incur prohibitive Non-Recurring Engineering (NRE) costs. Chiplet-based integration amortizes NRE across applications, but choosing which chiplets to build and how to compose them into accelerators is circularly dependent–a chiplet pool's value depends on the constructed accelerators, while accelerator quality is constrained by available chiplets. This paper introduces Fengshui, a chiplet ecosystem and accelerator co-design framework that jointly optimizes chiplet pool composition and bespoke application-specific integrated circuit (BASIC) design. Fengshui constructs BASICs through operator-level disaggregation, co-exploring chiplet and memory heterogeneity, tensor fusion, and pipeline/tensor/expert parallelism with place-and-route validation for physical implementability. With just 8 strategically selected chiplets, encompassing network switches, processing-in-memory units, and accelerators with diverse microarchitectures, Fengshui-generated BASICs achieve 48.5%, 88.1%, 93.0%, and 97.8% reductions in energy, energy-cost product (energy×$), energy-delay product (EDP), and energy-delay-cost product (EDP×$) over homogeneous accelerators, while scoring within 4.1% of unconstrained heterogeneous designs across diverse neural networks. For datacenter MoE and dense LLM serving, Fengshui reduces prefill energy and energy×$ by up to 16.8% and 28.7%, respectively; for edge autonomous vehicle perception, it achieves 12.0% energy and 23.6% energy×$ reductions under real-time latency constraints.

## 中文摘要

现代机器学习工作负载具有严格的时延和能源限制，越来越难以在同构商用硬件上高效运行。我们认为，算子级别的分解（为每个算子定制微架构、批处理和内存层次结构）对于克服这些限制至关重要，尽管由此产生的高度定制的加速器会产生高昂的非重复性工程（NRE）成本。基于 Chiplet 的集成可以跨应用分摊 NRE，但选择构建哪些 Chiplet 以及如何将它们组合成加速器是循环依赖的 - Chiplet 池的价值取决于构建的加速器，而加速器质量则受到可用 Chiplet 的限制。本文介绍了 Fengshui，这是一种小芯片生态系统和加速器协同设计框架，可联合优化小芯片池组成和定制专用集成电路 (BASIC) 设计。 Fengshui 通过算子级分解、共同探索小芯片和内存异构性、张量融合、管道/张量/专家并行性以及物理可实现性的布局布线验证来构建 BASIC。仅通过 8 个战略性选择的小芯片（包括网络交换机、存内处理单元和具有不同微架构的加速器），Fengshui 生成的 BASIC 就比同类加速器实现了 48.5%、88.1%、93.0% 和 97.8% 的能耗、能源成本乘积 (energy×$)、能量时延乘积 (EDP) 和能量时延成本乘积 (EDP×$) 降低，同时得分在4.1% 的跨不同神经网络的无约束异构设计。对于数据中心 MoE 和密集 LLM 服务，风水分别减少预填充能量和能量×$ 高达 16.8% 和 28.7%；对于边缘自动驾驶车辆感知，它在实时时延限制下实现了 12.0% 的能耗和 23.6% 的能耗×$ 降低。

## 中文关键词

芯粒；芯片设计；机器学习；算子级解耦；存内处理

## 代码与研究制品

- 代码仓库：[https://github.com/CrucibleComputingGroup/fengshui](https://github.com/CrucibleComputingGroup/fengshui)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5B](index.md) · [MICRO 2026 主页](../index.md)
