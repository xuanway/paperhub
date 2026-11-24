---
title: "MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems"
description: "ISCA 2026 · Session 10A · MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems"
tags:
  - "ISCA2026"
  - "Session 10A"
  - "LLM 5"
---

# MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems

**中文标题：** MoE-Hub: 在多 GPU 系统上驾驭软件复杂性，以硬件加速通信实现无缝 MoE 重叠

**所属 Session：** [Session 10A](index.md) · [ISCA 2026](../index.md)

**作者：** Zhuoshan Zhou, Chen Zhang, Shuyi Zhang, Qijun Zhang, Haibo Wang, Zhe Zhou, Zhipeng Tu, Guangyu Sun, Yijia Diao, Zhigang Ji, Jingwen Leng, Guanghui He, Minyi Guo

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The Mixture-of-Experts (MoE) architecture is crucial for scaling large language models, but its scalability is severely limited by inter-GPU communication bottlenecks in multi-GPU systems. Although overlapping communication with computation is a widely recognized optimization, its effective deployment still remains challenging, both in terms of performance and programmability. In this work, we identify the root cause as a fundamental abstraction mismatch between MoE’s dynamic, irregular token-to-expert mapping and the static, address-centric communication model of modern GPUs, which necessitates a complex software mediation phase to resolve addresses before data transfers, limiting performance and software flexibility. To resolve this, we propose MoE-Hub, a hardware-software co-design that introduces a destination-agnostic communication paradigm. MoE-Hub decouples data transmission from address management, allowing producers to send data immediately after routing using only a logical destination, while address allocation and data-flow orchestration are handled transparently by lightweight hardware in the GPU hub. By hardware-accelerating the entire communication control plane, MoE-Hub enables seamless and transparent overlap. Our evaluation shows that MoE-Hub achieves 1.40×–3.08× per-layer and 1.21×–1.98× end-to-end speedup over state-of-the-art systems.

## 中文摘要

混合专家（MoE）架构对于扩展大语言模型至关重要，但其可扩展性受到多GPU系统中GPU间通信瓶颈的严重限制。尽管将通信与计算重叠是一种广泛认可的优化方法，但在性能和可编程性方面，其有效部署仍然具有挑战性。在本工作中，我们将根本原因确定为MoE动态、不规则的令牌到专家映射与现代GPU静态、以地址为中心的通信模型之间的根本性抽象不匹配，这需要在数据传输之前通过复杂的软件中介阶段来解析地址，从而限制了性能和软件灵活性。为解决这一问题，我们提出了MoE-Hub，一种软硬件协同设计方案，引入了一种目的地无关的通信范式。MoE-Hub将数据传输与地址管理解耦，允许生产者在路由后仅使用逻辑目的地立即发送数据，而地址分配和数据流编排则由GPU中枢中的轻量级硬件透明处理。通过对整个通信控制平面进行硬件加速，MoE-Hub实现了无缝且透明的重叠。评估表明，与最先进的系统相比，MoE-Hub实现了每层1.40×–3.08×和端到端1.21×–1.98×的加速。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2026](../index.md)
