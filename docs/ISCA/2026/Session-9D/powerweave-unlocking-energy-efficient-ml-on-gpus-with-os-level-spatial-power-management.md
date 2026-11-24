---
title: "PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management"
description: "ISCA 2026 · Session 9D · PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management"
tags:
  - "ISCA2026"
  - "Session 9D"
  - "Sustainability and Energy Efficiency"
---

# PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management

**中文标题：** PowerWeave: 以 OS 级空间功耗管理释放 GPU 上的高能效 ML

**所属 Session：** [Session 9D](index.md) · [ISCA 2026](../index.md)

**作者：** Vasilis Kypriotis, Eric Dubberstein, Patrick H. Coppock, Eliot H. Solomon, Rayyan Zamir, Tathagata Srimani, Dimitrios Skarlatos

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

GPU power consumption has become a central systems challenge as modern AI datacenters increasingly rely on accelerators whose power footprints reach unprecedented scales. A single NVIDIA B200 already draws around 1000 W, making large multi-GPU nodes among the most power-hungry computing platforms ever deployed. Despite this, GPUs still expose only a single, device-wide DVFS domain. This coarse control is increasingly mismatched to modern AI inference, where power demand is highly non-uniform across models, phases, and workloads. LLMs alternate between compute-bound prefill and memory-bound decode phases, models exhibit widely varying kernel behavior, and emerging agentic pipelines chain together models with sharply different computational profiles. As GPUs shift toward multi-die designs and multi-model stacking becomes essential for utilization, a single global frequency increasingly leads to unnecessary and wasteful high-power operation. We introduce PowerWeave, the first spatial DVFS mechanism for GPUs, built around an OS-level power-management control plane. PowerWeave dynamically learns per-stream frequency-scaling behavior from kernel latencies and uses a global governor to react to request-rate changes, tail-latency behavior, and SLO slack. This design enables adaptive, fine-grained, kernel-aware power management that preserves SLOs while improving energy efficiency across diverse ML workloads. We build PowerWeave in Rust as a fully transparent power-governor layer atop the GPU driver and evaluate it across diverse LLM scenarios and agentic workloads on B200 GPUs. PowerWeave reduces energy consumption by 28% on average in both disaggregated-prefill and multitenant settings, achieving up to an 8× improvement over device-wide DVFS in disaggregated prefill. For agentic workflows, PowerWeave reduces energy consumption by 19% on average without compromising throughput. PowerWeave eliminates thermal throttling across all evaluated workloads while maintaining zero SLO violations. Finally, our hardware analysis shows that spatial DVFS is practical: even per-SM clock domains add less than 0.5% GPU die area overhead.

## 中文摘要

随着现代 AI 数据中心日益依赖功耗足迹达到前所未有规模的加速器，GPU 功耗已成为核心的系统级挑战。单个 NVIDIA B200 的功耗已达约 1000 W，使大型多 GPU 节点成为有史以来部署的最耗电的计算平台之一。尽管如此，GPU 仍然只提供一个设备范围的 DVFS 域。这种粗粒度控制与现代 AI 推理日益不匹配，因为后者对电力的需求在模型、阶段和工作负载之间高度不均匀。LLM 在计算受限的预填充阶段和内存受限的解码阶段之间交替，模型表现出差异很大的内核行为，而新兴的智能体流水线将具有截然不同计算特征的模型串联在一起。随着 GPU 转向多裸片设计，且多模型堆叠对利用率提升变得至关重要，单一全局频率日益导致不必要和浪费的高功耗运行。我们提出 PowerWeave，首个面向 GPU 的空间 DVFS 机制，它围绕操作系统级功耗管理控制平面构建。PowerWeave 从内核延迟中动态学习每个流的频率缩放行为，并使用全局调控器对请求速率变化、尾延迟行为和 SLO 松弛做出反应。该设计实现了自适应、细粒度、内核感知的功耗管理，在保持 SLO 的同时提高各种 ML 工作负载的能效。我们用 Rust 在 GPU 驱动之上将 PowerWeave 构建为一个完全透明的功耗调控层，并在 B200 GPU 上跨各种 LLM 场景和智能体工作负载对其进行评估。PowerWeave 在分离式预填充和多租户设置中平均将能耗降低 28%，在分离式预填充中相对于设备范围 DVFS 实现了高达 8 倍的改进。对于智能体工作流，PowerWeave 在不影响吞吐量的情况下平均将能耗降低 19%。PowerWeave 在所有评估的工作负载中消除了热节流，同时保持零 SLO 违规。最后，我们的硬件分析表明，空间 DVFS 是可行的：即使是每个 SM 的时钟域也只增加不到 0.5% 的 GPU 裸片面积开销。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9D](index.md) · [返回 ISCA 2026](../index.md)
