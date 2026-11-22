---
title: "Better Call SoL: Enhancing GPUs with a Sea of LUTs Core"
description: "MICRO 2026 · Session 1A · Better Call SoL：通过查找表海洋核心增强 GPU"
tags:
  - "MICRO2026"
  - "GPU"
  - "FPGA"
  - "Reconfigurable Computing"
---

# Better Call SoL: Enhancing GPUs with a Sea of LUTs Core

**中文标题：** Better Call SoL：通过查找表海洋核心增强 GPU

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Shashank Nag, Justin Garrigus, Yuting Chen, Lizy K. John

**来源：** MICRO 2026，pp. 48–63；[DOI](https://doi.org/10.1109/MICRO67795.2026.00020)

## 英文摘要

GPUs have emerged as a pervasive compute acceleration platform for a wide range of workloads. Their highly data-parallel architecture enables high-throughput applications, including machine learning, scientific computing, and graphics rendering. In recent years, the prevalence of GEMM-based applications led to the introduction of dedicated Tensor Cores in the GPU architecture, which were optimized for such workloads. However, current GPUs lack support for custom dataflow architectures and operations, and often perform sub-optimally for workloads with primitives not supported on GPU hardware. In this work, we propose introducing a Sea-of-LUTs (SoL) core to the GPU alongside typical functional units, providing a programmable logic area that can be dynamically reconfigured from within the GPU to implement custom operators or dataflow architectures. By tightly integrating this core on the same GPU die, we offer a fast, reconfigurable architecture while avoiding the external pin and I/O bottlenecks observed in heterogeneous platforms involving FPGAs. We evaluate the SoL core using a combination of GPU performance evaluation tools (Accel-Sim & AccelWattch) and FPGA architecture modeling tools (COFFE & VTR). We assess a diverse set of workloads on the GPU-SoL architecture, offloading custom functions such as Softmax to the SoL core. With only 6% area overhead, the proposed SoL core enables over 1.34× performance improvement and 1.22× energy reduction across the evaluated workloads.

## 中文摘要

GPU 已成为广泛应用于各类工作负载的计算加速平台。其高度数据并行的架构支持机器学习、科学计算和图形渲染等高吞吐量应用。近年来，基于通用矩阵乘法（GEMM）的应用日益普及，推动 GPU 引入针对这类工作负载优化的专用张量核。然而，现有 GPU 缺少对自定义数据流架构和运算的支持；当工作负载依赖 GPU 硬件未支持的原语时，其性能通常不够理想。本文提出在常规功能单元之外，为 GPU 增加查找表海洋（Sea-of-LUTs，SoL）核，提供可由 GPU 内部动态重配置的可编程逻辑区域，用于实现自定义算子或数据流架构。通过将 SoL 核紧密集成在同一 GPU 裸片上，我们获得了快速、可重配置的架构，同时避免了 FPGA 异构平台中常见的外部引脚与输入输出瓶颈。我们结合 GPU 性能评估工具 Accel-Sim、AccelWattch 与 FPGA 架构建模工具 COFFE、VTR 评估 SoL 核，并在 GPU-SoL 架构上运行多种工作负载，将 Softmax 等自定义函数卸载到 SoL 核。评估表明，所提设计仅增加 6% 面积，即可使性能超过基线的 1.34 倍，能耗降至基线的约 1/1.22。

## 中文关键词

图形处理器；现场可编程门阵列；细粒度可编程逻辑；自定义运算；数据流架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
