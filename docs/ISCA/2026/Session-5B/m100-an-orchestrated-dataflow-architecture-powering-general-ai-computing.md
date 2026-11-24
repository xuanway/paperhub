---
title: "M100: An Orchestrated Dataflow Architecture Powering General AI Computing"
description: "ISCA 2026 · Session 5B · M100: An Orchestrated Dataflow Architecture Powering General AI Computing"
tags:
  - "ISCA2026"
  - "Session 5B"
  - "Industry Track 2"
---

# M100: An Orchestrated Dataflow Architecture Powering General AI Computing

**中文标题：** M100: 支撑通用 AI 计算的编排式数据流架构

**所属 Session：** [Session 5B](index.md) · [ISCA 2026](../index.md)

**作者：** Yan Xie, Changkui Mao, Changsong Wu, Chao Lu, Chao Suo, Cheng Qian, Chun Yang, Danyang Zhu, Hengchang Xiong, Hongzhan Lu, Hongzhen Liu, Jiafu Liu, Jie Chen, Jie Dai, Junfeng Tang, Kai Liu, Kun Li, Lipeng Ge, Meng Sun, Min Luo, Peng Chen, Peng Wang, Shaodong Yang, Shibin Tang, Shibo Chen, Weikang Zhang, Xiao Ling, Xiaobo Du, Xin Wu, Yang Liu, Yi Jiang, Yihua Jin, Yin Huang, Yuli Zhang, Zhen Yuan, Zhiyuan Man, Zhongxiao Yao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As deep learning-based AI technologies gain momentum across nearly all aspects of life, the demand for a general-purpose AI computing architecture continues to grow. While current GPGPU-based architectures offer exceptional versatility to diverse AI workloads, they often fall short in efficiency and cost-effectiveness. Conversely, various Domain-Specific Architectures (DSAs) excel at particular AI tasks but struggle to extend their capabilities across a broader range of applications, let alone adapt to the rapidly evolving landscape of AI algorithms. M100 is Li Auto’s response to this challenge: a performant and cost-effective architecture designed to meet the AI inference demands of Autonomous Driving (AD), Large Language Models (LLMs), and intelligent human interactions. These domains are crucial to build today’s most competitive automobile platforms. M100 employs a dataflow parallel architecture, where compiler-architecture co-design orchestrates not only computation but, more critically, data movement across time and space. Leveraging the inherent efficiency of dataflow computing, our integrated hardware-software approach improves overall system performance while significantly reducing hardware complexity and cost. In line with the dataflow paradigm, M100 largely eliminates caching. Tensor computations are driven by compiler-and runtime-managed data streams flowing between computing elements and on/off-chip memories, resulting in greater efficiency and scalability compared to conventional cache-based systems. Another key design principle was selecting the right operational granularity for scheduling, issuing, and execution—across the compiler, firmware, and hardware. Recognizing commonalities in AI workloads, we chose the tensor, large or small, as the fundamental data element in the M100 architecture. M100 has demonstrated general AI computing capability across diverse inference applications, including UniAD (for AD) and LLaMA (for LLMs). Benchmark results show that M100 outperforms GPGPU architectures in AD applications, with higher hardware utilization. We believe that M100 represents a promising direction for the future convergence of general AI computing architectures.

## 中文摘要

随着基于深度学习的 AI 技术在人类生活的几乎各个方面不断取得进展，对通用 AI 计算架构的需求持续增长。当前基于 GPGPU 的架构为各类 AI 负载提供了卓越的通用性，但在效率与成本效益上往往不足。相反，各类领域专用架构（DSA）在特定 AI 任务上表现出色，却难以将能力扩展到更广泛的应用，更不用说适应快速演进的 AI 算法格局。M100 是理想汽车对这一挑战的回应：一个兼顾性能与成本的架构，旨在满足自动驾驶（AD）、大语言模型（LLM）与智能人机交互的 AI 推理需求，而这些领域对于构建当今最具竞争力的汽车平台至关重要。M100 采用数据流并行架构，通过编译器—架构协同设计，不仅编排计算，更关键的是编排跨越时间与空间的数据移动。借助数据流计算固有的效率，我们的软硬件一体化方法在提升整体系统性能的同时，显著降低了硬件复杂度与成本。遵循数据流范式，M100 在很大程度上消除了缓存。张量计算由编译器和运行时管理的数据流驱动，这些数据流在计算单元与片上／片外存储器之间流动，相比传统的基于缓存的系统带来更高的效率与可扩展性。另一个关键设计原则是为调度、发射和执行选择合适的操作粒度——这一选择贯穿编译器、固件与硬件。基于对 AI 负载共性的认识，我们选择张量（无论大小）作为 M100 架构中的基本数据元素。M100 已在多种推理应用中展现出通用 AI 计算能力，包括面向 AD 的 UniAD 与面向 LLM 的 LLaMA。基准结果表明，M100 在 AD 应用中优于 GPGPU 架构，并具有更高的硬件利用率。我们相信，M100 代表了通用 AI 计算架构未来融合的一个有前景的方向。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2026](../index.md)
