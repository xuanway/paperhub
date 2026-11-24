---
title: "MSCCL++: Rethinking GPU Communication Abstractions for AI Inference"
description: "ASPLOS 2026 · Session 2C · MSCCL++：为 AI 推理重新思考 GPU 通信抽象"
tags:
  - "ASPLOS2026"
  - "Session 2C"
  - "GPU Systems & Scheduling"
---

# MSCCL++: Rethinking GPU Communication Abstractions for AI Inference

**中文标题：** MSCCL++：为 AI 推理重新思考 GPU 通信抽象

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Changho Hwang (Microsoft Research), Peng Cheng (Microsoft Research), Roshan Dathathri (Microsoft Research), Abhinav Jangda (Microsoft Research), Saeed Maleki (Microsoft Research), Madan Musuvathi (Microsoft Research), Olli Saarikivi (Microsoft Research), Aashaka Shah (Microsoft Research), Ziyue Yang (Microsoft Research), Binyang Li (Microsoft Azure), Caio Rocha (Microsoft Azure), Qinghua Zhou (Microsoft Azure), Mahdieh Ghazimirsaeed (Microsoft Azure), Sreevatsa Anantharamu (Microsoft Azure), Jithin Jose (Microsoft Azure)

**单位：** Microsoft Research；Microsoft Azure

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790188) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

ions for AI Inference Changho Hwang Microsoft Research Vancouver, BC, Canada Peng Cheng Microsoft Research Redmond, WA, USA Roshan Dathathri Microsoft Research Redmond, WA, USA Abhinav Jangda Microsoft Research Redmond, WA, USA Saeed Maleki∗ Microsoft Research Redmond, WA, USA Madan Musuvathi Microsoft Research Redmond, WA, USA Olli Saarikivi† Microsoft Research Redmond, WA, USA Aashaka Shah Microsoft Research Redmond, WA, USA Ziyue Yang Microsoft Research Beijing, China Binyang Li Microsoft Azure Redmond, WA, USA Caio Rocha Microsoft Azure Redmond, WA, USA Qinghua Zhou Microsoft Azure Redmond, WA, USA Mahdieh Ghazimirsaeed Microsoft Azure Cambridge, MA, USA Sreevatsa Anantharamu Microsoft Azure Minneapolis, MN, USA Jithin Jose Microsoft Azure Austin, TX, USA Abstract AI applications increasingly run on fast-evolving, heterogeneous hardware to maximize performance, but general-purpose libraries lag in supporting these features. Performanceminded programmers often build custom communication stacks that are fast but error-prone and non-portable. This paper introduces MSCCL++, a design methodology for developing high-performance, portable communication kernels. It provides (1) a low-level, performance-preserving primitive interface that exposes minimal hardware abstractions while hiding the complexities of synchronization and consistency, (2) a higher-level DSL for application developers to implement workload-specific communication algorithms, and (3) a library of efficient algorithms implementing the standard collective API, enabling adoption by users with minimal expertise. Compared to state-of-the-art baselines, MSCCL++ achieves geomean speedups of 1.7× (up to 5.4×) for collective communication and 1.2× (up to 1.38×) for AI inference workloads. MSCCL++ is in production of multiple AI services provided by Microsoft Azure, and has also been adopted by RCCL, the GPU collective communication library maintained by AMD. MSCCL++ is open source and available at perience with MSCCL++ suggests that its abstractions are robust, enabling support for new hardware features, such as multimem, within weeks of development.

## 中文摘要

ions for AI Inference Changho Hwang Microsoft Research Vancouver, BC, Canada Peng Cheng Microsoft Research Redmond, WA, USA Roshan Dathathri Microsoft Research Redmond, WA, USA Abhinav Jangda Microsoft Research Redmond, WA, USA Saeed Maleki∗ Microsoft Research Redmond, WA, USA Madan Musuvathi Microsoft Research Redmond, WA, USA Olli Saarikivi† Microsoft Research Redmond, WA, USA Aashaka Shah Microsoft Research Redmond, WA, USA Ziyue Yang Microsoft Research Beijing, China Binyang Li Microsoft Azure Redmond, WA, USA Caio Rocha Microsoft Azure Redmond, WA, USA Qinghua Zhou Microsoft Azure Redmond, WA, USA Mahdieh Ghazimirsaeed Microsoft Azure Cambridge, MA, USA Sreevatsa Anantharamu Microsoft Azure Minneapolis, MN, USA Jithin Jose Microsoft Azure Austin, TX, USA 摘要 AI 应用越来越多地运行在快速演进、异构的硬件之上以最大化性能，但通用库在支持这些特性方面滞后。注重性能的程序员常常构建自定义通信栈，它们速度快，但易出错且不可移植。本文介绍 MSCCL++，一种用于开发高性能、可移植通信内核的设计方法。它提供：(1) 一个低层、保持性能的原语接口，暴露最少的硬件抽象，同时隐藏同步与一致性方面的复杂性；(2) 一个面向应用开发者的更高层 DSL，用于实现特定工作负载的通信算法；(3) 一个高效算法库，实现标准集合通信 API，使专业知识最少的用户也能采用。与最先进的基线相比，MSCCL++ 在集合通信上取得 1.7×（最高 5.4×）的几何平均加速，在 AI 推理工作负载上取得 1.2×（最高 1.38×）的几何平均加速。MSCCL++ 已用于 Microsoft Azure 提供的多项 AI 服务的生产环境，并且也被 AMD 维护的 GPU 集合通信库 RCCL 所采用。MSCCL++ 是开源的，可在 perience 处获取；在 MSCCL++ 上的经验表明，其抽象是稳健的，能够在数周开发周期内支持新的硬件特性，例如 multimem。

## 英文关键词

GPU Communication; Collective Communication; AI Inference; Multi-layered Programming Abstraction

## 中文关键词

GPU 通信；集合通信；AI 推理；多层编程抽象

## 代码与研究制品

- [代码仓库](https://github.com/microsoft/mscclpp)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790188)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2026](../index.md)
