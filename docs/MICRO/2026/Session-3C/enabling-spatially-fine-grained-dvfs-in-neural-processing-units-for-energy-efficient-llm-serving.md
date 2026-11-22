---
title: "Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving"
description: "MICRO 2026 · Session 3C · 在神经处理单元中实现空间细粒度 DVFS，以提高 LLM 服务能效"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Energy Efficiency"
  - "Neural Networks"
---

# Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving

**中文标题：** 在神经处理单元中实现空间细粒度 DVFS，以提高 LLM 服务能效

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Yuqi Xue, Jerry Wu, Corey Yu, Jian Huang

**来源：** MICRO 2026，pp. 1131–1149；[DOI](https://doi.org/10.1109/MICRO67795.2026.00088)

## 英文摘要

As neural processing units (NPUs) evolve rapidly to accommodate the ever-increasing compute demand of large language models (LLMs), their power consumption is becoming a limiting factor. Our study shows that using dynamic voltage and frequency scaling (DVFS) to exploit the service-level objective (SLO) slacks is a promising way to improve NPU energy efficiency for LLM services. As tensor operators in LLMs exhibit diverse bottlenecks across NPU components, it is desirable to configure the frequency separately for each component to maximize their energy efficiency. In this paper, we develop eNPU that enables hardware and software support for spatially fine-grained, component-level DVFS on NPUs. eNPU refactors the NPU core pipeline to partition components into separate V/f domains. It introduces lightweight cross-domain communication mechanisms to mitigate synchronization overheads across components, and extends the NPU ISA for sub-µs DVFS control. eNPU uses a compiler-driven two-level greedy search to co-optimize instruction scheduling and per-component V/f selection under SLO constraints. We implement eNPU's pipeline design on an open-source NPU core to verify its functionality and evaluate the energy savings with a production-level NPU simulator with various LLMs using production traces. eNPU reduces energy consumption of LLM services by 16.3%–20.5% with 2.20% projected area overhead on a TPUv4 chip, while preserving strict SLO guarantees.

## 中文摘要

随着神经处理单元 (NPU) 快速发展以适应大语言模型 (LLM) 不断增长的计算需求，其功耗正在成为一个限制因素。我们的研究表明，使用动态电压和频率缩放 (DVFS) 来利用服务级别目标 (SLO) 松弛是提高 LLM 服务的 NPU 能效的一种有前途的方法。由于 LLM 中的张量算子在 NPU 组件中表现出不同的瓶颈，因此需要为每个组件单独配置频率，以最大限度地提高其能效。在本文中，我们开发了 eNPU，它可以为 NPU 上的空间细粒度、组件级 DVFS 提供硬件和软件支持。 eNPU 重构了 NPU 核心管道，将组件划分为单独的 V/f 域。它引入了轻量级跨域通信机制来减轻组件之间的同步开销，并扩展了 NPU ISA 以实现亚微秒 DVFS 控制。 eNPU 使用编译器驱动的两级贪婪搜索来共同优化 SLO 约束下的指令调度和每个组件的 V/f 选择。我们在开源 NPU 内核上实现 eNPU 的管道设计，以验证其功能并使用生产级 NPU 模拟器（具有使用生产跟踪的各种 LLM）来评估节能情况。 eNPU 将 LLM 服务的能耗降低了 16.3%–20.5%，TPUv4 芯片上的投影面积开销为 2.20%，同时保留了严格的 SLO 保证。

## 中文关键词

动态电压频率调节；神经处理单元；大语言模型服务；能效；空间细粒度控制

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/platformxlab/NeuSim/tree/micro26ae](https://github.com/platformxlab/NeuSim/tree/micro26ae)（论文提供的地址；2026-11-10 检查返回 HTTP 404）
- 代码与复现实验仓库：[https://github.com/XZman/micro26ae_supplementary_files](https://github.com/XZman/micro26ae_supplementary_files)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
