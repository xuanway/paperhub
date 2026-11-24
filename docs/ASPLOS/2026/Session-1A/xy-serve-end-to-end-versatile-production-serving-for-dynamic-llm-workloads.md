---
title: "XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads"
description: "ASPLOS 2026 · Session 1A · XY-Serve：面向动态 LLM 工作负载的端到端通用型生产服务系统"
tags:
  - "ASPLOS2026"
  - "Session 1A"
  - "LLM Serving: Throughput Optimization"
---

# XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads

**中文标题：** XY-Serve：面向动态 LLM 工作负载的端到端通用型生产服务系统

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Mingcong Song (Huawei Technologies Co., Ltd.), Xinru Tang (Tsinghua University, BNRist), Fengfan Hou (Huawei Technologies Co., Ltd.), Jing Li (Huawei Technologies Co., Ltd.), Wei Wei (Huawei Technologies Co., Ltd.), Yipeng Ma (Huawei Technologies Co., Ltd.), Runqiu Xiao (Huawei Technologies Co., Ltd.), Hongjie Si (Huawei Technologies Co., Ltd.), Dingcheng Jiang (Tsinghua University, BNRist), Shouyi Yin (Tsinghua University, BNRist and Shanghai AI Laboratory), Yang Hu (Tsinghua University, BNRist), Guoping Long (Huawei Technologies Co., Ltd.)

**单位：** Huawei Technologies Co., Ltd.；Tsinghua University, BNRist；Tsinghua University, BNRist and Shanghai AI Laboratory

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762228) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Meeting growing demands for low latency and cost efficiency in production-grade large language model (LLM) serving systems requires integrating advanced optimization techniques. However, dynamic and unpredictable input-output lengths of LLM, compounded by these optimizations, exacerbate the issues of workload variability, making it difficult to maintain high efficiency on AI accelerators, especially DSAs with tile-based programming models. To address this challenge, we introduce XY-Serve, a versatile, Ascend NPU native, end-to-end production LLM-serving system. The core idea is an abstraction mechanism that smooths out the workload variability by decomposing computations into unified, hardware-friendly, fine-grained meta primitives. Then, kernels can efficiently execute without concerning the irregularity of workload. After this abstraction mechanism, for Attention, we propose a meta-kernel that computes the basic For Linear, we introduce a virtual padding scheme that adapts to dynamic shape changes while using highly efficient GEMM primitives with assorted fixed tile sizes. XYServe sits harmoniously with vLLM. Experimental results show up to 95% end-to-end throughput improvement compared with current publicly available baselines on Ascend NPUs. We also set a new performance record for Linear (average 14.6% faster) and Attention (average 21.5% faster) kernels relative to existing libraries. Lastly, we demonstrate the generality of our technologies on GPU platform.

## 中文摘要

在生产级大语言模型（LLM）服务系统中满足日益增长的低延迟与成本效益需求，需要融合多种先进优化技术。然而，LLM 动态且不可预测的输入输出长度，叠加这些优化，进一步加剧了工作负载波动问题，使得在 AI 加速器上——尤其是采用基于 tile 编程模型的 DSA 上——难以保持高效率。为应对这一挑战，我们提出 XY-Serve，一个通用、Ascend NPU 原生的端到端生产级 LLM 服务系统。其核心思想是一种抽象机制：通过将计算分解为统一的、硬件友好的细粒度元原语（meta primitives）来平滑工作负载波动。由此，内核可以高效执行，而无需关注工作负载的不规则性。在该抽象机制之上，针对 Attention，我们提出一个计算基础的元内核；针对 Linear，我们引入一种虚拟填充（virtual padding）方案，在适配动态形状变化的同时使用具备各种固定 tile 尺寸的高效 GEMM 原语。XY-Serve 与 vLLM 能够和谐共存。实验结果表明，在 Ascend NPU 上，与当前公开可用的基线相比，端到端吞吐提升最高可达 95%。同时，相对于现有库，我们在 Linear（平均快 14.6%）与 Attention（平均快 21.5%）内核上创造了新的性能纪录。最后，我们在 GPU 平台上验证了这些技术的通用性。

## 英文关键词

Inference System; AI Accelerator; Large Language Model

## 中文关键词

推理系统；AI 加速器；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762228)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2026](../index.md)
