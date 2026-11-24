---
title: "DICE: Detailed Inter-Chiplet End-to-End PHY Modeling for Accurate Chiplet Simulation"
description: "ISCA 2026 · Session 7A · DICE: Detailed Inter-Chiplet End-to-End PHY Modeling for Accurate Chiplet Simulation"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# DICE: Detailed Inter-Chiplet End-to-End PHY Modeling for Accurate Chiplet Simulation

**中文标题：** DICE: 面向精确 chiplet 仿真的细粒度 chiplet 间端到端 PHY 建模

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Rashid Aligholipour, Stefanos Kaxiras, Yuan Yao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Scaling monolithic multicores is increasingly constrained by power/thermal limits, yield, and rising manufacturing and testing costs. Chiplet designs address these challenges by partitioning large dies into smaller parts (typically multiple core-complex dies and an I/O die) linked via high-bandwidth physical fabrics (PHY). As bandwidth and wiring density scale, however, these short-reach links are pushed closer to their signal-integrity limits, increasing susceptibility to noise, crosstalk, and channel loss, motivating stronger link-level reliability mechanisms such as forward error correction (FEC). Despite this trend, state-of-the-art simulation infrastructures often approximate inter-chiplet links using oversimplified, fixed-latency models. Such abstractions overlook the inherently dynamic, runtime-dependent behavior of the PHY—including channel conditions (e.g., signal-to-noise ratio shifts, signal crosstalk, clock jitter), iterative decoder convergence and packet retransmissions, and application dynamics (e.g., LLC-misses that travel across chiplet boundaries)—all of which are hard to determine offline. We show that neglecting these effects distorts inter-chiplet packet-level timing and high-level performance metrics such as IPC, leading to off-trend simulation results. We present DICE, an in-simulation, runtime PHY modeling in gem5 that captures the end-to-end inter-chiplet datapath, including QC-LDPC encoding/decoding, PAM4 modulation, lossy-channel transmission, LLR-based demodulation, adaptive packet re-sending, and PHY-level flow control between chiplets. For fidelity, we calibrate component latencies via hardware synthesis (e.g., QC-LDPC decode paths and iteration budgets) and compare the integrated system against production chiplet processors. Compared with state-of-the-art fixed-latency inter-chiplet links such as HeteroGarnet, DICE reshapes packet-latency composition and shifts system IPC by an average of 6.8% and up to 27.6%, revealing variability driven by realistic PHY link behaviors, enabling more accurate co-evaluation of performance, reliability, and design trade-offs in modern chiplet systems.

## 中文摘要

扩展单片多核处理器日益受到功耗/散热限制、良率以及不断上升的制造与测试成本的制约。Chiplet 设计通过将大芯片划分为更小的部分（通常为多个核心复合体 die 和一个 I/O die），并经高带宽物理层（PHY）互连，来应对这些挑战。然而，随着带宽和布线密度的提升，这些短距链路被推向其信号完整性极限，对噪声、串扰和信道损耗的敏感性增加，从而促使采用更强的链路级可靠性机制，如前向纠错（FEC）。尽管存在这一趋势，最先进的仿真基础设施往往使用过度简化的固定延迟模型来近似 chiplet 间链路。此类抽象忽略了 PHY 固有的、依赖于运行时状态的动态行为——包括信道条件（如信噪比变化、信号串扰、时钟抖动）、迭代译码器收敛与数据包重传，以及应用动态（如跨越 chiplet 边界的 LLC 缺失）——而这些都难以离线确定。我们表明，忽略这些效应会扭曲 chiplet 间数据包级时序以及 IPC 等高层次性能指标，导致仿真结果偏离趋势。我们提出 DICE，一个在 gem5 中实现的仿真内运行时 PHY 建模，它捕捉端到端的 chiplet 间数据通路，包括 QC-LDPC 编解码、PAM4 调制、有损信道传输、基于 LLR 的解调、自适应数据包重发以及 chiplet 间的 PHY 级流控。为保证保真度，我们通过硬件综合（如 QC-LDPC 译码路径和迭代预算）校准各组件延迟，并将集成后的系统与量产 chiplet 处理器进行比较。与 HeteroGarnet 等最先进的固定延迟 chiplet 间链路相比，DICE 重塑了数据包延迟构成，并使系统 IPC 平均偏移 6.8%、最高达 27.6%，揭示了由真实 PHY 链路行为所驱动的可变性，从而能够对现代 chiplet 系统中的性能、可靠性与设计权衡进行更准确的协同评估。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19428665）](https://zenodo.org/records/19428665)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
