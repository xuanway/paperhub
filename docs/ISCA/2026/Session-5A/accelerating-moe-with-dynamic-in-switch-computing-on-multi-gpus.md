---
title: "Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs"
description: "ISCA 2026 · Session 5A · Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs"
tags:
  - "ISCA2026"
  - "Session 5A"
  - "LLM 3"
---

# Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs

**中文标题：** 在多 GPU 上以动态交换机内计算加速 MoE

**所属 Session：** [Session 5A](index.md) · [ISCA 2026](../index.md)

**作者：** Qijun Zhang, Chen Zhang, Zhuoshan Zhou, Haibo Wang, Zhe Zhou, Zhipeng Tu, Guangyu Sun, Zhiyao Xie, Yijia Diao, Zhigang Ji, Jingwen Leng, Guanghui He, Minyi Guo

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Mixture-of-Experts (MoE) has been adopted by many leading large models to reduce computational requirements. However, frequent inter-GPU communication in MoE expert parallelism (EP) becomes a performance challenge. We observe substantial redundant inter-GPU data transfers in MoE that can be potentially addressed by in-switch computing. Unfortunately, the existing solution, NVLink SHARP (NVLS), can only support static collectives with regular patterns, incapable of dynamic communication with irregular patterns in MoE.

To bridge the functionality gap, we propose DySHARP, an integral dynamic in-switch computing solution to accelerate MoE, encompassing both communication primitives and communication-aware scheduling: 1) Dynamic multimem addressing co-designs ISA, architecture, and runtime, as a dynamic extension to NVLS, reducing redundant traffic. However, the resulting traffic reduction is inherently asymmetric between two directions, preventing it from directly translating into speedup. 2) Token-centric kernel fusion deeply fuses the dispatch-computation-combine pipeline, resolving this asymmetry to translate traffic reduction into actual speedup. Compared with the state-of-the-art solution, DySHARP achieves up to 1.79× speedup.

## 中文摘要

混合专家（MoE）已被众多领先的大模型采用，以降低计算需求。然而，MoE 专家并行（EP）中频繁的跨 GPU 通信成为性能瓶颈。我们观察到 MoE 中存在大量冗余的跨 GPU 数据传输，而交换机内计算有望解决这一问题。遗憾的是，现有方案 NVLink SHARP（NVLS）仅能支持具有规则模式的静态集合通信，无法胜任 MoE 中不规则模式的动态通信。

为弥补这一功能差距，我们提出 DySHARP——一套完整的动态交换机内计算方案以加速 MoE，涵盖通信原语与通信感知调度：1）动态多播寻址（Dynamic multimem addressing）协同设计指令集、体系结构与运行时，作为 NVLS 的动态扩展，减少冗余流量。然而由此产生的流量削减在两个方向上本质不对称，使其无法直接转化为性能提升。2）以 Token 为中心的内核融合（Token-centric kernel fusion）将分发—计算—合并流水线深度融合，化解上述不对称性，从而把流量削减转化为实际的加速。与最先进方案相比，DySHARP 最高实现 1.79× 的加速。

## 代码与研究制品

截至 2026-11-23，未在论文及公开检索中找到 DySHARP 对应的开源程序链接。已检查 [第一作者主页](https://zqj2333.github.io/)。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2026](../index.md)
