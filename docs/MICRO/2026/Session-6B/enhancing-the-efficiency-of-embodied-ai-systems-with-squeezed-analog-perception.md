---
title: "Enhancing the Efficiency of Embodied AI Systems with Squeezed Analog Perception"
description: "MICRO 2026 · Session 6B · 通过压缩式模拟感知提高具身 AI 系统效率"
tags:
  - "MICRO2026"
---

# Enhancing the Efficiency of Embodied AI Systems with Squeezed Analog Perception

**中文标题：** 通过压缩式模拟感知提高具身 AI 系统效率

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Cheng Xu, Xiaofeng Hou, Chao Li, Chenhe Yuan, Jinyang Guo, Xinkai Wang, Yang Hu, Yu Feng, Dimitris Gizopoulos, Minyi Guo

**来源：** MICRO 2026，pp. 1967–1982；[DOI](https://doi.org/10.1109/MICRO67795.2026.00138)

## 英文摘要

Embodied AI systems increasingly rely on computational sensors to execute multimodal perception close to the data source. While this organization improves locality and responsiveness, the sensing frontend itself can become a major energy and latency bottleneck. Existing efforts primarily optimize downstream computation, while leaving two frontend inefficiencies under-addressed: excessive mandatory sensor operations, such as repeated data conversion and internal data movement, and redundant sensor activation, where sensing and preprocessing proceed even when the corresponding data contribute little to the final decision. To address these challenges, we propose SAP, a Squeezed Analog Perception framework for embodied AI systems. SAP is an architecture–system co-design that makes adaptive control effective before full digitization, jointly reducing mandatory frontend processing and enabling recoverable perception. At the architecture layer, the Memristor-based Reduced Sensor Architecture (MRSA) reorganizes the sensing frontend around a unified memristive processing bank, enabling in-situ buffering and staged analog processing of raw signals before digitization. At the system layer, the Adaptive Analog Perception Driver (AAPD) orchestrates buffering, promotion of deferred data, and early termination under input difficulty and analog non-idealities. We implement SAP through hardware prototyping and detailed simulation, and evaluate it across representative embodied perception workloads. The results show that SAP reduces energy consumption by up to 17.47× and latency by up to 2.88× compared with the conventional edge-centric NPU full-execution baseline, while exposing a configurable accuracy–efficiency tradeoff for deployment-sensitive workloads.

## 中文摘要

具身人工智能系统越来越依赖计算传感器来执行靠近数据源的多模态感知。虽然该组织提高了局部性和响应能力，但传感前端本身可能成为主要的能源和时延瓶颈。现有的工作主要优化下游计算，同时留下两个前端效率低下的问题：过多的强制传感器操作，例如重复的数据转换和内部数据移动，以及冗余的传感器激活，即使相应的数据对最终决策贡献很小，传感和预处理也会继续进行。为了应对这些挑战，我们提出了 SAP，这是一种用于具体人工智能系统的压缩模拟感知框架。 SAP 是一种架构-系统协同设计，使自适应控制在完全数字化之前有效，共同减少强制性前端处理并实现可恢复的感知。在架构层，基于忆阻器的简化传感器架构 (MRSA) 围绕统一的忆阻器处理组重新组织了传感前端，从而在数字化之前实现原始信号的原位缓冲和分阶段模拟处理。在系统层，自适应模拟感知驱动程序 (AAPD) 协调缓冲、时延数据的提升以及输入困难和模拟非理想情况下的提前终止。我们通过硬件原型设计和详细模拟来实现模型名称，并跨代表性的具身感知工作负载对其进行评估。结果表明，与传统的以边缘为中心的 NPU 完全执行基准相比，SAP 可将能耗降低高达 17.47 倍，将时延降低高达 2.88 倍，同时为部署敏感的工作负载提供可配置的精度与效率权衡。

## 中文关键词

具身人工智能；计算传感器；自适应感知；架构与系统协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

## 来源核对说明

元数据中的 modelname/modelnamenospace 已根据论文 PDF 摘要恢复为 SAP。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
