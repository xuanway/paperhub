---
title: "AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving"
description: "MICRO 2026 · Session 8A · AMMA：面向百万长度上下文低时延注意力服务的多芯粒内存中心架构"
tags:
  - "MICRO2026"
---

# AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving

**中文标题：** AMMA：面向百万长度上下文低时延注意力服务的多芯粒内存中心架构

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Zhongkai Yu, Haotian Ye, Chenyang Zhou, Ohm Rishabh Venkatachalam, Zaifeng Pan, Zhengding Hu, Junsung Kim, Won Woo Ro, Po-An Tsai, Shuyi Pei, Yangwook Kang, Yufei Ding

**来源：** MICRO 2026，pp. 2738–2754；[DOI](https://doi.org/10.1109/MICRO67795.2026.00186)

## 英文摘要

All current LLM serving systems place the GPU at the center, from production-level attention-FFN disaggregation to NVIDIA's Rubin GPU-LPU heterogeneous platform. Even academic PIM/PNM proposals still treat the GPU as the central hub for cross-device communication. Yet the GPU's compute-rich architecture is fundamentally mismatched with the memory-bound nature of decode-phase attention, inflating serving latency while wasting power and die area on idle compute units. The problem is compounded as reasoning and agentic workloads push context lengths toward one million tokens, making attention latency the primary user-facing bottleneck. To address these inefficiencies, we present AMMA, a multi-chiplet, memory-centric architecture for low-latency long-context attention. AMMA replaces GPU compute dies with HBM-PNM cubes, roughly doubling the available memory bandwidth to better serve memory-bound attention workloads. To translate this bandwidth into proportional performance gains, we introduce (i) a logic-die microarchitecture that fully exploits per-cube internal bandwidth for decode attention under a minimal power and area budget, (ii) a two-level hybrid parallelism scheme, and (iii) a reordered collective flow that reduces intra-chip die-to-die communication overhead. We further conduct a design-space exploration over per-cube compute power and intra-chip D2D link bandwidth, providing actionable guidance for hardware designers. Evaluations show that AMMA achieves 15.5X lower latency and 6.9X lower energy consumption compared with the NVIDIA H100. Our code is available at https://github.com/zhongkaiyu/AMMA.

## 中文摘要

当前所有的 LLM 服务系统都将 GPU 置于中心，从生产级注意力 FFN 分解到 NVIDIA 的 Rubin GPU-LPU 异构平台。即使学术 PIM/PNM 提案仍然将 GPU 视为跨设备通信的中心枢纽。然而，GPU 的计算丰富的架构从根本上与解码阶段注意力的内存限制性质不匹配，从而增加了服务时延，同时浪费了空闲计算单元上的功率和芯片面积。随着推理和代理工作负载将上下文长度推向一百万个词元，使注意力时延成为面向用户的主要瓶颈，问题变得更加复杂。为了解决这些低效率问题，我们提出了 AMMA，一种多芯片、以内存为中心的架构，用于低时延长上下文注意力。 AMMA 用 HBM-PNM 立方体取代了 GPU 计算芯片，将可用内存带宽大致增加了一倍，以更好地服务于内存受限的注意力工作负载。为了将此带宽转化为成比例的性能增益，我们引入了（i）一种逻辑芯片微架构，该架构充分利用每立方体内部带宽在最小功率和面积预算下进行解码注意力，（ii）一种两级混合并行方案，以及（iii）一种重新排序的集体流，可减少芯片内芯片到芯片的通信开销。我们进一步对每立方体的计算能力和芯片内 D2D 链路带宽进行设计空间探索，为硬件设计人员提供可行的指导。评估表明，与 NVIDIA H100 相比，AMMA 的时延降低了 15.5 倍，能耗降低了 6.9 倍。我们的代码可在 https://github.com/zhongkaiyu/AMMA 获取。

## 中文关键词

近存处理；高带宽内存；大语言模型；长上下文注意力；芯粒；内存中心架构

## 代码与研究制品

- 代码仓库：[https://github.com/zhongkaiyu/AMMA](https://github.com/zhongkaiyu/AMMA)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21540779](https://doi.org/10.5281/zenodo.21540779)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
