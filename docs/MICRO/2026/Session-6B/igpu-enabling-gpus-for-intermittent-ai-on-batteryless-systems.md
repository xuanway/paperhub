---
title: "iGPU: Enabling GPUs for Intermittent AI on Batteryless Systems"
description: "MICRO 2026 · Session 6B · iGPU：支持无电池系统中间歇式 AI 计算的 GPU"
tags:
  - "MICRO2026"
  - "GPU"
---

# iGPU: Enabling GPUs for Intermittent AI on Batteryless Systems

**中文标题：** iGPU：支持无电池系统中间歇式 AI 计算的 GPU

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Byounguk Min, Yilun Wu, Yuchen Zhou, Kasim Sinan Yildirim, Khakim Akhunov, Jianping Zeng, Jongouk Choi, Wenjie Xiong, Dongyoon Lee, Changhee Jung

**来源：** MICRO 2026，pp. 1998–2014；[DOI](https://doi.org/10.1109/MICRO67795.2026.00140)

## 英文摘要

This paper proposes iGPU, the first GPU proposal for energy harvesting systems (EHSs), enabling intermittent AI workloads where power failure is the norm. The key advantage of iGPU is that it completely eliminates the need for costly just-in-time (JIT) checkpointing of GPU's huge register file (RF). Instead, iGPU leverages compiler support to ensure correct recovery from power failure. The compiler divides the program into idempotent regions, each persisting only a small set of live-out register updates, allowing the vast RF to remain volatile. However, applying idempotent recovery to GPU's SIMT architecture poses a unique challenge because the standard post-dominator (PDOM) stack inherently discards the state of completed branch paths before divergent threads re-converge; if power failure occurs in between, the interrupted region may fail to re-execute correctly. To address this, iGPU lets the PDOM stack retain recovery metadata for all divergent subgroups until re-convergence, while aligning the idempotent region boundaries with divergence points. This hardware/software co-design keeps the PDOM hardware simple—still small enough for JIT checkpointing—while ensuring correct recovery even when power failure occurs while a warp is diverged. As a result, iGPU makes GPUs a viable and high-performance option for EHSs for the first time. Experimental results show that across 21 applications, iGPU delivers an average speedup of 2.40–2.74× over jGPU, which adopts JIT checkpointing, 7.82–8.93× over a CPU-based EHS, and 1.56–1.69× over MOUSE, an intermittent compute-in-memory accelerator.

## 中文摘要

本文提出了 iGPU，这是第一个针对能量收集系统 (EHS) 的 GPU 提案，可支持断电常见的间歇性 AI 工作负载。 iGPU 的主要优势在于它完全消除了对 GPU 巨大的寄存器文件 (RF) 进行成本高昂的即时 (JIT) 检查点的需要。相反，iGPU 利用编译器支持来确保从电源故障中正确恢复。编译器将程序划分为幂等区域，每个区域仅保留一小部分实时寄存器更新，从而允许庞大的 RF 保持易失性。然而，将幂等恢复应用于 GPU 的 SIMT 架构带来了独特的挑战，因为标准后支配者 (PDOM) 堆栈本质上会在发散的线程重新收敛之前丢弃已完成的分支路径的状态；如果中间发生电源故障，中断的区域可能无法正确重新执行。为了解决这个问题，iGPU 让 PDOM 堆栈保留所有发散子组的恢复元数据，直到重新收敛，同时将幂等区域边界与发散点对齐。这种硬件/软件协同设计使 PDOM 硬件保持简单，仍然足够小，适合 JIT 检查点，同时即使在线程束发散时发生电源故障，也能确保正确恢复。因此，iGPU 首次使 GPU 成为 EHS 的可行且高性能的选择。实验结果表明，在 21 个应用程序中，iGPU 比采用 JIT 检查点的 jGPU 平均加速 2.40–2.74 倍，比基于 CPU 的 EHS 平均加速 7.82–8.93 倍，比间歇性存内计算加速器 MOUSE 平均加速 1.56–1.69 倍。

## 中文关键词

间歇计算；无电池系统；图形处理器；人工智能；能量采集

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
