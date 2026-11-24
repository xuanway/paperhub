---
title: "Towards Unified Analysis of GPU Consistency"
description: "ASPLOS 2025 · Session 10A · 迈向 GPU 一致性的统一分析"
tags:
  - "ASPLOS2025"
  - "Session 10A"
  - "GPGPU"
---

# Towards Unified Analysis of GPU Consistency

**中文标题：** 迈向 GPU 一致性的统一分析

**所属 Session：** [Session 10A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Haining Tong (University of Helsinki), Natalia Gavrilenko (Huawei Dresden Research Center), Hernan Ponce de Leon (Huawei Dresden Research Center), Keijo Heljanko (University of Helsinki,Helsinki Institute for Information Technology)

**单位：** University of Helsinki；Huawei Dresden Research Center；University of Helsinki,Helsinki Institute for Information Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674174) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

After more than 30 years of research, there is a solid understanding of the consistency guarantees given by CPU systems. Unfortunately, the same is not yet true for GPUs. The growing popularity of general purpose GPU programming has been a call for action which industry players like Nvidia and Khronos have answered by formalizing their Ptx and Vulkan consistency models. These models give precise answers to questions about program's correctness. However, interpreting them still requires a level of expertise that escapes most developers, and the current tool support is insufficient. To remedy this, we translated and integrated the Ptx and Vulkan models into the Dartagnan verification tool. This makes Dartagnan the first analysis tool for multiple GPU consistency models that can analyze real GPU code. During the validation of the translated models, we discovered two bugs in the original Ptx and Vulkan consistency models.

## 中文摘要

经过三十多年的研究，人们对 CPU 系统所提供的一致性保证已有扎实的理解。遗憾的是，GPU 的情况尚非如此。通用 GPU 编程的日益普及构成了一种行动号召，Nvidia 与 Khronos 等行业参与者通过形式化各自的 Ptx 与 Vulkan 一致性模型作出了回应。这些模型为关于程序正确性的问题给出了精确答案。然而，解读它们仍然需要大多数开发者所不具备的专业知识水平，且当前的工具支持仍然不足。为弥补这一不足，我们将 Ptx 与 Vulkan 模型翻译并集成到 Dartagnan 验证工具中。这使 Dartagnan 成为首个能够分析真实 GPU 代码、支持多种 GPU 一致性模型的分析工具。在验证翻译后模型的过程中，我们在原始的 Ptx 与 Vulkan 一致性模型中发现了两个缺陷。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674174)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10A](index.md) · [返回 ASPLOS 2025](../index.md)
