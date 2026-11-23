---
title: "Debunking the CUDA Myth Towards GPU-based AI Systems: Evaluation of the Performance and Programmability of Intel’s Gaudi NPU for AI Model Serving"
description: "ISCA 2025 · Session 9B · 破除 GPU AI 系统的 CUDA 迷思：英特尔 Gaudi NPU 在 AI 模型服务中的性能与可编程性评估"
tags:
  - "ISCA2025"
  - "Session 9B"
  - "HPC"
---

# Debunking the CUDA Myth Towards GPU-based AI Systems: Evaluation of the Performance and Programmability of Intel’s Gaudi NPU for AI Model Serving

**中文标题：** 破除 GPU AI 系统的 CUDA 迷思：英特尔 Gaudi NPU 在 AI 模型服务中的性能与可编程性评估

**所属 Session：** [Session 9B](index.md) · [ISCA 2025](../index.md)

**作者：** Yunjae Lee, Juntaek Lim, Jehyeon Bang, Eunyeong Cho, Huijong Jeong, Taesu Kim, Hyungjun Kim, Joonhyung Lee, Jinseop Im, Ranggi Hwang, Se Jung Kwon, Dongsoo Lee, Minsoo Rhu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731050) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

This paper presents a comprehensive evaluation of Intel Gaudi NPUs as an alternative to NVIDIA GPUs, which is currently the de facto standard in AI system design. First, we create microbench- marks to compare Intel Gaudi-2 with NVIDIA A100, showing that Gaudi-2 achieves competitive performance not only in primitive AI compute, memory, and communication operations but also in executing several important AI workloads end-to-end. We then as- sess Gaudi NPU’s programmability by discussing several software- level optimization strategies to employ for implementing critical FBGEMM operators and vLLM, evaluating their efficiency against GPU-optimized counterparts. Results indicate that Gaudi-2 achieves energy efficiency comparable to A100, though there are notable areas for improvement in terms of software maturity. Overall, we conclude that, with effective integration into high-level AI frame- works, Gaudi NPUs could challenge NVIDIA GPU’s dominance in the AI server market, though further improvements are necessary to fully compete with NVIDIA’s robust software ecosystem.

## 中文摘要

本文针对Intel Gaudi系列NPU开展全面评测，探究其能否替代当前AI系统设计里事实上的标准——NVIDIA GPU。首先，我们搭建微基准测试，对比Intel Gaudi-2与NVIDIA A100。结果显示，Gaudi-2不仅在AI基础计算、访存、通信原语上具备有竞争力的性能，在多个重要AI负载的端到端执行中也表现不俗。

随后，本文评估Gaudi NPU的可编程性：探讨在其上实现核心FBGEMM算子、vLLM时用到的多种软件层优化策略，并和GPU优化版本对比效率。实验表明，Gaudi-2的能效可以比肩A100，但软件成熟度仍存在明显短板。

总体结论：如果能良好接入高层AI框架，Gaudi NPU有机会冲击NVIDIA GPU在AI服务器市场的主导地位；但想要和NVIDIA完善的软件生态正面竞争，仍需要持续改进。

## 英文关键词

Artificial intelligence, domain-specific architecture, GPU, NPU

## 中文关键词

人工智能, 领域专用架构, 图形处理器, 神经网络处理器

## 代码与研究制品

- [代码仓库](https://github.com/VIA-Research/Intel-Gaudi-AI-benchmarks)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731050)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9B](index.md) · [返回 ISCA 2025](../index.md)
