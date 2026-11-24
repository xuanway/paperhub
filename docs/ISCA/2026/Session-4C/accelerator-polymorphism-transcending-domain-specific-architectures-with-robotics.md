---
title: "Accelerator Polymorphism: Transcending Domain-Specific Architectures with Robotics"
description: "ISCA 2026 · Session 4C · Accelerator Polymorphism: Transcending Domain-Specific Architectures with Robotics"
tags:
  - "ISCA2026"
  - "Session 4C"
  - "Domain Specific Accelerators 1"
---

# Accelerator Polymorphism: Transcending Domain-Specific Architectures with Robotics

**中文标题：** 加速器多态性：以机器人技术超越领域专用架构

**所属 Session：** [Session 4C](index.md) · [ISCA 2026](../index.md)

**作者：** Hanyang Xu, Seongryong Oh, Yubin Lee, Ashwin Rohit Alagiri Rajan, Rohan Mahapatra, Om Patil, Yuchuan Li, Jongse Park, Hadi Esmaeilzadeh

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Robotics is poised for a ChatGPT-like leap, but progress is constrained by the lack of a compute substrate suited to its cross-domain computational demands. Unlike LLMs and neural networks, which are largely confined to a single domain of tensor operations, robotics spans multiple algorithmic domains, including graph search, control theory, optimization, and more, often within a single application pipeline. This cross-domain diversity, coupled with stringent power, latency, and cost constraints, demands a new design point—one that transcends the siloed boundaries of domain-specific accelerators without reintroducing the overheads of general-purpose processing.

To address this challenge, we propose a novel architectural concept: accelerator polymorphism, whereby a single physical substrate dynamically shape-shifts itself from one specialized execution model to another without sacrificing the efficiency of specialization by reverting to general-purpose design. We instantiate this concept in a concrete microarchitecture, Morphatron, that dynamically shape-shifts across five execution morphas—queue-centric SIMD, graph, tree, vector, systolic—each tailored to distinct algorithmic domains in robotics. At the heart of Morphatron is Morpha Core, a novel SIMD processor specialized for queue-centric execution and built on a key algorithmic insight: queues are a unifying data structure across robotic workloads. Morpha Core elevates queues to first-class SIMD operands, integrates memory allocation directly into the pipeline as an architectural primitive, and thereby enables hardware acceleration of dynamically-sized data structures. Morphatron is a multi-core accelerator composed of a two-dimensional array of Morpha Cores, designed to support the diverse access and parallelism patterns revealed by our in-depth study of end-to-end robotic workloads. We evaluate the performance and power efficiency of Morphatron using six end-to-end robotic applications from the RoWild benchmarks [1]. Compared to the NVIDIA Jetson Orin Nano GPU, Morphatron achieves a 5.5× speedup and a 6.6× improvement in performance-per-watt, on average. Relative to the ARM A78 CPU, Morphatron delivers a 7.7× speedup and a 7.7× improvement in performance-per-watt.


## 中文摘要

机器人技术正处于类似 ChatGPT 的飞跃边缘，但缺乏适合其跨领域计算需求的硬件基础。与局限于张量操作的 LLM 和神经网络不同，机器人技术横跨图搜索、控制理论、优化等多个算法领域。本文提出加速器多态性的概念——单个物理硬件在不同专业化执行模型之间动态变形。我们将其实例化为 Morphatron 微架构，可在五种执行形态（以队列为中心的 SIMD、图、树、向量、脉动阵列）之间动态切换。其核心是 Morpha Core——一种以队列为中心的新型 SIMD 处理器，将队列提升为一等 SIMD 操作数并将内存分配集成到流水线中。相比 NVIDIA Jetson Orin Nano GPU，Morphatron 实现平均 5.5× 加速和 6.6× 性能-功耗比提升；相比 ARM A78 CPU，实现 7.7× 加速和 7.7× 性能-功耗比提升。

## 代码与研究制品

截至 2026-11-23，未在论文及公开检索中找到 Morphatron 对应的开源程序链接。已检查 [共同作者论文列表](https://www.ashwinrohit.com/)。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2026](../index.md)
