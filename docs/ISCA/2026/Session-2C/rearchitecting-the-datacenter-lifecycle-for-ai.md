---
title: "Rearchitecting the Datacenter Lifecycle for AI"
description: "ISCA 2026 · Session 2C · Rearchitecting the Datacenter Lifecycle for AI"
tags:
  - "ISCA2026"
  - "Session 2C"
  - "Sustainability"
---

# Rearchitecting the Datacenter Lifecycle for AI

**中文标题：** 为 AI 重构数据中心生命周期

**所属 Session：** [Session 2C](index.md) · [ISCA 2026](../index.md)

**作者：** Jovan Stojkovic, Chaojie Zhang, Íñigo Goiri, Ricardo Bianchini

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The rapid rise of large language models (LLMs) has driven an enormous demand for AI inference infrastructure, mainly powered by high-end GPUs. While these accelerators offer immense computational power, they incur high capital and operational costs due to frequent upgrades, dense power consumption, and cooling demands, making total cost of ownership (TCO) for AI datacenters a critical concern for cloud providers. Unfortunately, traditional datacenter lifecycle management (designed for general-purpose workloads) struggles to keep pace with AI’s fast-evolving models, rising resource needs, and diverse hardware profiles. We rethink the AI datacenter lifecycle scheme across three stages (building, IT provisioning, and operation) highlighting how power, cooling, and networking decisions affect long-term TCO. We focus on hardware refresh strategies aligned with evolving hardware trends and evaluate operational software optimizations that further reduce cost. While these optimizations at each stage yield benefits, unlocking the full potential requires rethinking the entire lifecycle. We present a holistic lifecycle management framework that optimizes decisions across all three stages, accounting for workload dynamics, hardware evolution, and system aging. Our approach reduces TCO by 40% compared to traditional methods and offers guidelines for managing AI datacenter lifecycles in the future.

## 中文摘要

大语言模型（LLM）的迅速崛起驱动了对AI推理基础设施的巨大需求，主要由高端GPU提供算力。尽管这些加速器提供了强大的计算能力，但由于频繁升级、高密度功耗和散热需求，它们带来了高昂的资本和运营成本，使得AI数据中心的总拥有成本（TCO）成为云服务商关注的关键问题。不幸的是，传统的（为通用工作负载设计的）数据中心生命周期管理难以跟上AI快速演进的模型、不断增长的计算资源需求和多样化的硬件配置。我们重新思考了AI数据中心在三个阶段的（建设、IT部署和运营）生命周期方案，强调了电力、散热和网络决策如何影响长期TCO。我们重点关注与硬件演进趋势一致的硬件更新策略，并评估了进一步降低成本的运营软件优化。虽然各阶段的优化均能带来收益，但释放全部潜力需要重新思考整个生命周期。我们提出了一个整体生命周期管理框架，该框架优化了所有三个阶段的决策，综合考虑了工作负载动态、硬件演化和系统老化。与传统方法相比，我们的方法将TCO降低了40%，并为未来AI数据中心生命周期的管理提供了指导。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Azure/AI-Lifecycle-Compass](https://github.com/Azure/AI-Lifecycle-Compass)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2C](index.md) · [返回 ISCA 2026](../index.md)
