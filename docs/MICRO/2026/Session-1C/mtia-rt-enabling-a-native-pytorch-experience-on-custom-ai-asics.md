---
title: "MTIA-RT: Enabling a Native PyTorch Experience on Custom AI ASICs"
description: "MICRO 2026 · Session 1C · MTIA-RT：在定制 AI ASIC 上提供原生 PyTorch 体验"
tags:
  - "MICRO2026"
---

# MTIA-RT: Enabling a Native PyTorch Experience on Custom AI ASICs

**中文标题：** MTIA-RT：在定制 AI ASIC 上提供原生 PyTorch 体验

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Hangchen Yu, Adam Belay, Jun Luo, Chunqiang Tang, Roman Levenstein, Yige Hu, Anirudh Shaktawat, Alex Mastro, David Reiss, Tim Sham, Jaesoo Lee, Anirban Banerjee, Hyunho Yeo, Youlin Zhang, Wushi Dong, Rumit Desai, Wang Xu, Jack Montgomery, Kaustubh Gondkar, Ajit Mathews

**来源：** MICRO 2026，pp. 253–268；[DOI](https://doi.org/10.1109/MICRO67795.2026.00033)

## 英文摘要

The rapid evolution of AI workloads has driven the need for specialized accelerators that provide both exceptional computational efficiency and easy-to-use software interfaces. This paper presents the host runtime (MTIA-RT) for Meta's custom AI accelerator (MTIA), which manages kernel launches, buffer lifecycles, and other critical functions. To our knowledge, MTIA-RT is the first publicly documented runtime for an AI accelerator deployed at hyperscale. Despite MTIA's fundamentally different architecture compared to GPUs, MTIA-RT exposes APIs that are functionally compatible with the CUDA runtime, ensuring application portability. It provides a familiar, native PyTorch experience for developers, supporting both high-performance graph mode and flexible eager mode. Currently, it manages accelerators in production and serves diverse models at scale. By sharing MTIA-RT's design and deployment experience, we aim to provide concrete, field-tested knowledge about production accelerator runtime development.

## 中文摘要

人工智能工作负载的快速发展推动了对专用加速器的需求，这些加速器既提供卓越的计算效率，又提供易于使用的软件界面。本文介绍了 Meta 的自定义 AI 加速器 (MTIA) 的主机运行时 (MTIA-RT)，它管理内核启动、缓冲区生命周期和其他关键功能。据我们所知，MTIA-RT 是第一个公开记录的超大规模部署的 AI 加速器运行时。尽管 MTIA 的架构与 GPU 根本不同，但 MTIA-RT 公开了在功能上与 CUDA 运行时兼容的 API，确保了应用程序的可移植性。它为开发人员提供了熟悉的原生 PyTorch 体验，支持高性能图形模式和灵活的 Eager 模式。目前，它管理生产中的加速器并大规模服务于多种模型。通过分享 MTIA-RT 的设计和部署经验，我们的目标是提供有关生产加速器运行时开发的具体、经过现场测试的知识。

## 中文关键词

运行时系统；专用集成电路；加速器；即时执行模式；PyTorch；MTIA

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
