---
title: "sCROOGe: Circuit-level Design and Optimization Framework for RISC-V Out-of-Order GPUs"
description: "ISCA 2026 · Session 6C · sCROOGe: Circuit-level Design and Optimization Framework for RISC-V Out-of-Order GPUs"
tags:
  - "ISCA2026"
  - "Session 6C"
  - "GPUs and Compilation"
---

# sCROOGe: Circuit-level Design and Optimization Framework for RISC-V Out-of-Order GPUs

**中文标题：** sCROOGe: 面向 RISC-V 乱序 GPU 的电路级设计与优化框架

**所属 Session：** [Session 6C](index.md) · [ISCA 2026](../index.md)

**作者：** Maria Zerva, Panagiotis-Eleftherios Eleftherakis, Alexis Maras, Konstantinos Iliakis, Alexandros Moiras, Sotirios Xydis

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Graphics Processing Units (GPUs) have evolved into the dominant hardware accelerators for general-purpose computing, yet many workloads underutilize the available resources due to inadequate Thread-Level Parallelism (TLP). To address this, techniques leveraging Instruction-Level Parallelism (ILP), such as dynamic instruction reordering, have been proposed. However, existing solutions rely on software simulators lacking RTL validation and abstracting away critical micro-architectural details, limiting accuracy in performance, power, and area modeling. In this work, we present the first synthesizable RTL assessment and optimization framework of both frontend- and backend-based Out-of-Order (OoO) execution schemes within the open-source RISC-V Vortex GPGPU framework. Both schemes are directly implemented in RTL by extending the pipeline with light-weight scheduling logic and register renaming. Our approach manages to capture critical micro-architectural details absent from prior simulation-only studies and reveals key insights into the performance scalability and implementation cost of OoO execution paths in GPUs. We leverage this flexibility to explore different reordering configurations, isolate the impact of key components, and optimize hardware structures for balanced performance, power, area and timing. We evaluate their performance across diverse workloads, and perform design space exploration by tuning parameters such as warp and thread counts. Furthermore, we quantify the power and area trade-offs via ASIC synthesis flow, demonstrating a 14.4% performance gain compared to iso-area in-order GPU cores and 27.9% improved Energy-Delay Product (EDP). This work demonstrates the practical applicability of light-weight OoO schemes for enhanced GPU throughput and energy efficiency, establishing a foundation for future ILP-aware designs validated through real hardware modeling.

## 中文摘要

图形处理器（GPU）已发展为通用计算的主导硬件加速器，然而许多工作负载由于线程级并行（TLP）不足而未能充分利用可用资源。为此，人们提出了利用指令级并行（ILP）的技术，例如动态指令重排。然而，现有解决方案依赖缺乏 RTL 验证的软件模拟器，并抽象掉了关键的微架构细节，限制了性能、功耗和面积建模的准确性。在本工作中，我们提出了首个在开源 RISC-V Vortex GPGPU 框架内对基于前端和后端的乱序（OoO）执行方案进行可综合 RTL 评估与优化的框架。两种方案均通过为流水线扩展轻量级调度逻辑和寄存器重命名而直接在 RTL 中实现。我们的方法能够捕捉以往仅仿真研究缺失的关键微架构细节，并揭示了关于 GPU 中 OoO 执行路径性能可扩展性与实现成本的重要洞见。我们利用这一灵活性探索不同的重排配置，隔离关键组件的影响，并优化硬件结构以在性能、功耗、面积和时序之间取得平衡。我们在多样化的负载上评估其性能，并通过调整 warp 和线程数等参数进行设计空间探索。此外，我们通过 ASIC 综合流程量化了功耗与面积权衡，证明相比等面积的顺序 GPU 核心实现 14.4% 的性能提升和 27.9% 的能效延迟积（EDP）改善。本工作展示了轻量级 OoO 方案在提升 GPU 吞吐与能效方面的实际适用性，为未来通过真实硬件建模验证的 ILP 感知设计奠定了基础。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19453033）](https://zenodo.org/records/19453033)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2026](../index.md)
