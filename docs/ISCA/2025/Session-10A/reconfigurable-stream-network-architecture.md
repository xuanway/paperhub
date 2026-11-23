---
title: "Reconfigurable Stream Network Architecture"
description: "ISCA 2025 · Session 10A · 可重构流网络架构"
tags:
  - "ISCA2025"
  - "Session 10A"
  - "ML Accelerators IV"
---

# Reconfigurable Stream Network Architecture

**中文标题：** 可重构流网络架构

**所属 Session：** [Session 10A](index.md) · [ISCA 2025](../index.md)

**作者：** Chengyue Wang, Xiaofan Zhang, Jason Cong, James C. Hoe

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731088) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

As AI systems grow increasingly specialized and complex, manag- ing hardware heterogeneity becomes a pressing challenge. How can we efficiently coordinate and synchronize heterogeneous hard- ware resources to achieve high utilization? How can we minimize the friction of transitioning between diverse computation phases, reducing costly stalls from initialization, pipeline setup, or drain? Our insight is that a network abstraction at the ISA level naturally unifies heterogeneous resource orchestration and phase transitions. This paper presents a Reconfigurable Stream Network Architec- ture (RSN), a novel ISA abstraction designed for the DNN domain. RSN models the datapath as a circuit-switched network with stateful functional units as nodes and data streaming on the edges. Pro- gramming a computation corresponds to triggering a path. Software is explicitly exposed to the compute and communication latency of each functional unit, enabling precise control over data move- ment for optimizations such as compute-communication overlap and layer fusion. As nodes in a network naturally differ, the RSN abstraction can efficiently virtualize heterogeneous hardware re- sources by separating control from the data plane, enabling low instruction-level intervention. We build a proof-of-concept design RSN-XNN on VCK190, a het- erogeneous platform with FPGA fabric and AI engines. Compared to the SOTA solution on this platform, it reduces latency by 6.1x and improves throughput by 2.4x–3.2x. Compared to the T4 GPU with the same FP32 performance, it matches latency with only 18% of the memory bandwidth. Compared to the A100 GPU at the same 7nm process node, it achieves 2.1x higher energy efficiency in FP32.

## 中文摘要

随着AI系统日趋专用化与复杂化，硬件异构资源的管理成为一项紧迫难题。我们如何高效调度、同步异构硬件资源，实现高利用率？如何降低不同计算阶段切换带来的开销，减少因初始化、流水线配置、排空流水而产生的昂贵停顿？

本文核心思路：在指令集架构（ISA）层面引入网络抽象，统一异构资源编排与阶段切换。本文提出**可重构流网络架构（RSN, Reconfigurable Stream Network Architecture）**，一种面向深度神经网络领域的全新ISA抽象。RSN将数据通路建模为电路交换网络：节点是带状态的功能单元，边承载流式数据。编程执行计算等价于激活一条通路。软件可以显式感知每个功能单元的计算与通信延迟，从而精细管控数据搬运，支持计算通信重叠、层融合等优化。
由于网络中的节点天然具备差异性，RSN抽象通过分离控制面与数据面，能够对异构硬件资源做高效虚拟化，指令侧干预开销很低。

我们在VCK190（一款包含FPGA逻辑阵列与AI引擎的异构平台）上搭建验证原型RSN-XNN。对比该平台上的前沿方案，延迟降低6.1倍，吞吐提升2.4–3.2倍；和同等FP32算力的T4 GPU相比，在延迟相当的前提下，仅需18%的内存带宽；与同为7nm工艺的A100 GPU相比，FP32下能效提升2.1倍。

## 英文关键词

Architecture, FPGA, AI Engines, Versal, Overlay, Streaming, Dataflow, Heterogeneous Systems, Transformer

## 中文关键词

架构, 现场可编程门阵列, AI引擎, Versal, Overlay, 流处理, 数据流, 异构系统, Transformer

## 代码与研究制品

- [代码仓库](https://github.com/ChengyueWang/ISCA25-Stream-Network-Arch)
- [研究制品](https://doi.org/10.5281/zenodo.15103085)
- [研究制品](https://doi.org/10.5281/zenodo.15102698)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731088)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2025](../index.md)
