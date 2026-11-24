---
title: "DARTH-PUM: A Hybrid Processing-Using-Memory Architecture"
description: "ASPLOS 2026 · Session 4D · DARTH-PUM：一种混合的存内处理架构"
tags:
  - "ASPLOS2026"
  - "Session 4D"
  - "Processing-in-Memory"
---

# DARTH-PUM: A Hybrid Processing-Using-Memory Architecture

**中文标题：** DARTH-PUM：一种混合的存内处理架构

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ryan Wong (University of Illinois Urbana-Champaign), Ben Feinberg (Sandia National Laboratories), Saugata Ghose (University of Illinois Urbana-Champaign)

**单位：** University of Illinois Urbana-Champaign；Sandia National Laboratories

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790151) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Analog processing-using-memory (PUM; a.k.a. in-memory computing) makes use of electrical interactions inside memory arrays to perform bulk matrix–vector multiplication (MVM) operations. However, many popular matrix-based kernels need to execute non-MVM operations, which analog PUM cannot directly perform. To retain its energy efficiency, analog PUM architectures augment memory arrays with CMOSbased domain-specific fixed-function hardware to provide complete kernel functionality, but the difficulty of integrating such specialized CMOS logic with memory arrays has largely limited analog PUM to being an accelerator for machine learning inference, or for closely related kernels. An opportunity exists to harness analog PUM for general-purpose computation: recent works have shown that memory arrays can also perform Boolean PUM operations, albeit with very different supporting hardware and electrical signals than analog PUM. We propose DARTH-PUM, a general-purpose hybrid PUM architecture that tackles key hardware and software challenges to integrating analog PUM and digital PUM. We propose optimized peripheral circuitry, coordinating hardware to manage and interface between both types of PUM, an easy-touse programming interface, and low-cost support for flexible data widths. These design elements allow us to build a practical PUM architecture that can execute kernels fully in memory, and can scale easily to cater to domains ranging from embedded applications to large-scale data-driven computing. We show how three popular applications (AES encryption, convolutional neural networks, large-language models) can map to and benefit from DARTH-PUM, with speedups of 59.4×, 14.8×, and 40.8× over an analog+CPU baseline.

## 中文摘要

模拟存内处理（processing-using-memory, PUM；亦称 in-memory computing）利用存储阵列内部的电学相互作用来执行批量矩阵–向量乘法（MVM）操作。然而，许多流行的基于矩阵的内核需要执行非 MVM 操作，而模拟 PUM 无法直接完成这些操作。为保持能效，模拟 PUM 架构用基于 CMOS 的领域专用固定功能硬件来增强存储阵列，以提供完整的内核功能，但将此类专用 CMOS 逻辑与存储阵列集成的困难，在很大程度上使模拟 PUM 局限于作为机器学习推理或密切相关内核的加速器。将模拟 PUM 用于通用计算存在机会：近期工作表明，存储阵列也能执行布尔 PUM 操作，尽管其支撑硬件和电信号与模拟 PUM 截然不同。我们提出 DARTH-PUM，一种通用混合 PUM 架构，解决了集成模拟 PUM 与数字 PUM 的关键硬件与软件挑战。我们提出优化的外围电路、用于在两类 PUM 之间进行管理和接口的协调硬件、易用的编程接口，以及对灵活数据宽度的低成本支持。这些设计要素使我们能够构建一种实用的 PUM 架构，它可在存储中完整执行内核，并能轻松扩展以适用于从嵌入式应用到大规模数据驱动计算的各种领域。我们展示了三个流行应用（AES 加密、卷积神经网络、大语言模型）如何映射到 DARTH-PUM 并从中受益，相比模拟+CPU 基线分别获得 59.4×、14.8× 和 40.8× 的加速。

## 英文关键词

Processing-Using-Memory; In-Memory Computing; Hybrid Architecture

## 中文关键词

存内处理（PUM）；存内计算；混合架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790151)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2026](../index.md)
