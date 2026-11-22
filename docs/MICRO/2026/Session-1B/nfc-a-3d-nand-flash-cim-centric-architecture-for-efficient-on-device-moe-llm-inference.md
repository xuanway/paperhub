---
title: "NFC: A 3D NAND Flash-CIM Centric Architecture for Efficient On-Device MoE LLM Inference"
description: "MICRO 2026 · Session 1B · NFC：以三维 NAND 闪存存内计算为核心的高效端侧 MoE 大语言模型推理架构"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# NFC: A 3D NAND Flash-CIM Centric Architecture for Efficient On-Device MoE LLM Inference

**中文标题：** NFC：以三维 NAND 闪存存内计算为核心的高效端侧 MoE 大语言模型推理架构

**所属 Session：** [Session 1B](index.md) · [MICRO 2026](../index.md)

**作者：** Siyuan Chen, Ao Shi, Shiyang Li, Jiaqi Li, Haozhang Yang, Haobin Shang, Lianliang Wu, Ruiqi Chen, Yiyang Chen, Lixia Han, Lifeng Liu, Peng Huang

**来源：** MICRO 2026，pp. 174–190；[DOI](https://doi.org/10.1109/MICRO67795.2026.00028)

## 英文摘要

Large language models (LLMs) utilizing mixture-of-experts (MoE) achieve high performance with low computational overhead, yet their massive memory footprint hinders on-device deployment. While recent research leverages high-density 3D NAND flash to address this through offloading and near-data processing (NDP), these approaches suffer from limited memory bandwidth, particularly in offloading scenarios. Furthermore, current NDP designs fail to provide sufficient computational throughput, even for the low-batch workloads typical of edge inference. Therefore, we present NFC, a 3D NAND flash computing-in-memory (CIM) centric architecture to overcome memory bottlenecks and enable efficient on-device MoE LLM inference. To fully exploit the computing potential of NFC, we first develop an offline module-aware resource allocation (MARA) strategy, which optimizes weight mapping on flash-CIM based on the distinct characteristics of MoE LLM modules to enhance inference throughput. Second, we introduce conflict-aware token parallelism (CATP) to maximize flash-CIM utilization through efficient online token scheduling. Finally, we propose a two-phase adaptive bitline charging scheme to reduce the intrinsic computing latency of flash-CIM by introducing a voltage source and relevant circuitry for fast charging. Experimental results show that NFC achieves up to 171.3x and 26.6x higher decoding throughput compared to state-of-the-art offloading and flash-NDP baselines, highlighting the significant potential of 3D NAND flash-CIM for on-device MoE LLM inference.

## 中文摘要

利用专家混合 (MoE) 的大语言模型 (LLM) 以较低的计算开销实现高性能，但其巨大的内存占用阻碍了设备上的部署。虽然最近的研究利用高密度 3D NAND 闪存通过卸载和近数据处理 (NDP) 来解决这个问题，但这些方法受到内存带宽有限的影响，特别是在卸载场景中。此外，当前的 NDP 设计无法提供足够的计算吞吐量，即使对于边缘推理典型的小批量工作负载也是如此。因此，我们提出了 NFC，一种以 3D NAND 闪存存内计算 (CIM) 为中心的架构，以克服内存瓶颈并实现高效的设备上 MoE LLM 推理。为了充分发挥 NFC 的计算潜力，我们首先开发了一种离线模块感知资源分配 (MARA) 策略，该策略根据 MoE LLM 模块的独特特征优化 flash-CIM 上的权重映射，以提高推理吞吐量。其次，我们引入冲突感知词元并行性 (CATP)，通过高效的在线词元调度来最大限度地提高 flash-CIM 利用率。最后，我们提出了一种两阶段自适应位线充电方案，通过引入电压源和相关快速充电电路来减少 flash-CIM 的固有计算时延。实验结果表明，与最先进的卸载和闪存 NDP 基准相比，NFC 的解码吞吐量分别提高了 171.3 倍和 26.6 倍，凸显了 3D NAND 闪存 CIM 在设备上 MoE LLM 推理方面的巨大潜力。

## 中文关键词

三维 NAND 闪存；存内计算；混合专家模型；端侧大语言模型推理

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1B](index.md) · [MICRO 2026 主页](../index.md)
