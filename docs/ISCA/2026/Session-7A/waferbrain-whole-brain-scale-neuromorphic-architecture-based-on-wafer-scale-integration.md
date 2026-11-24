---
title: "WaferBRAIN: Whole-Brain Scale Neuromorphic Architecture Based on Wafer-Scale Integration"
description: "ISCA 2026 · Session 7A · WaferBRAIN: Whole-Brain Scale Neuromorphic Architecture Based on Wafer-Scale Integration"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# WaferBRAIN: Whole-Brain Scale Neuromorphic Architecture Based on Wafer-Scale Integration

**中文标题：** WaferBRAIN: 基于晶圆级集成的全脑规模神经形态架构

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Yukun Feng, Hao Jia, Liangyu Gan, Haoming Chu, Yufan He, Jiaxin Yin, Lirong Zheng, Ning Ma, Yuxiang Huan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Scaling neuromorphic systems to whole-brain models is constrained by inefficient processing paradigms and long, sparse off-chip links in PCB integration. We present WaferBRAIN, a wafer-scale neuromorphic architecture that co-designs event representation, routing, storage, and topology for whole-brain scale cortical models. WaferBRAIN adopts a neuron–axon hybrid paradigm: local broadcast within brain regions, targeted unicast across regions, and boundary-triggered scheduling to mitigate hotspots, reducing router traffic by up to 300×, latency by up to 14×, and indexing storage by up to 7,400×. For further scaling-out of the single neuromorphic wafer chips, a switchless dragonfly inter-wafer network shortens paths and balances traffic, reducing inter-wafer congestion by 3.4–3.7×. Calibrated with a 12-inch prototype Lyra X, WaferBRAIN sustains the firing rates required for biological real-time simulation, achieving per-step communication latencies consistently below the 1 ms simulation time step. Furthermore, 3D Wafer-Scale Integration provides sufficient DRAM capacity to support 1B neurons and 256B synapses per wafer, and compared with neuromorphic processors by PCB-level integration, it improves sustainable firing rates by 13×. Together, these advances enable real-time whole-brain neuromorphic simulation on digital wafer-scale platforms.

## 中文摘要

将神经形态系统扩展到全脑模型，受到低效的处理范式以及 PCB 集成中长而稀疏的片外链路的制约。我们提出 WaferBRAIN，一种晶圆级神经形态架构，针对全脑规模皮层模型对事件表示、路由、存储和拓扑进行协同设计。WaferBRAIN 采用神经元–轴突混合范式：脑区内局部广播、跨脑区定向单播，以及边界触发调度以缓解热点，从而将路由器流量降低最多 300×、延迟降低最多 14×、索引存储降低最多 7,400×。为进一步横向扩展单块神经形态晶圆芯片，一种无交换机的蜻蜓（dragonfly）晶圆间网络缩短了路径并均衡了流量，使晶圆间拥塞降低 3.4–3.7×。基于 12 英寸原型 Lyra X 进行校准，WaferBRAIN 能够维持生物实时仿真所需的放电率，使每步通信延迟始终低于 1 ms 的仿真时间步长。此外，3D 晶圆级集成提供了充足的 DRAM 容量，每片晶圆可支持 10 亿个神经元和 2560 亿个突触；与采用 PCB 级集成的神经形态处理器相比，其可持续放电率提升了 13×。这些进展共同使在数字晶圆级平台上进行实时全脑神经形态仿真成为可能。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
