---
title: "NeRArch-Sim: A Unified Simulator for Benchmarking and DSE of Neural Rendering Accelerators"
description: "ISCA 2026 · Session 7B · NeRArch-Sim: A Unified Simulator for Benchmarking and DSE of Neural Rendering Accelerators"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# NeRArch-Sim: A Unified Simulator for Benchmarking and DSE of Neural Rendering Accelerators

**中文标题：** NeRArch-Sim: 面向神经渲染加速器基准评测与 DSE 的统一仿真器

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Cheng-Jhih Shih, Chaojian Li, Chihao Yu, Hsuan-Chen Fang, Sixu Li, Wei-Po Hsin, Lexington Whalen, Hyewon Suh, Greg Eisenhauer, Ling Liu, Yingyan (Celine) Lin

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Recent breakthroughs in neural rendering promise numerous real-time 3D intelligence applications, e.g., AR/VR, robotics, and digital twins. To satisfy real-time requirements, various neural rendering accelerators have been developed, with each employing a different rendering algorithm pipeline and designed for a specific hardware target. Such one-off specialization, representing only a single design point, creates two gaps: (i) fair, extensible cross-accelerator benchmarking, and (ii) design-space exploration (DSE) that retargets designs across pipelines or hardware budgets. We present NeRArch-Sim, an open-source simulator purpose-built for neural rendering accelerators with module-accurate models and validated end-to-end schedules (error ≤9.4%). NeRArch-Sim follows two principles: (1) modular abstractions for software workflows and hardware, enabling extensible benchmarking across diverse algorithmic pipelines and accelerator designs; and (2) a dataflow-aware two-level scheduler for rapid, effective DSE. Across eleven accelerators and two datasets, NeRArch-Sim reproduces prior designs with minimal changes (modeling error ≤9.4%) and guides new accelerators that achieve up to 1.3× efficiency gains. To our knowledge, NeRArch-Sim is the first open-source simulator that models a wide range of neural rendering accelerators, providing timely infrastructure for this emerging domain. The simulator is publicly available at https://github.com/GATECH-EIC/NeRArch-Sim.

## 中文摘要

神经渲染领域近期的突破有望催生大量实时 3D 智能应用，例如 AR/VR、机器人和数字孪生。为满足实时性要求，研究者开发了多种神经渲染加速器，每种都采用不同的渲染算法流水线，并针对特定的硬件目标设计。这种一次性专门化只代表单一设计点，造成了两方面空白：(i) 公平、可扩展的跨加速器基准评测；(ii) 可在不同流水线或硬件预算之间重新定向设计的设计空间探索（DSE）。我们提出 NeRArch-Sim，一个专为神经渲染加速器打造的开源仿真器，具有模块级精确模型和经过验证的端到端调度（误差 ≤9.4%）。NeRArch-Sim 遵循两条原则：(1) 对软件工作流和硬件采用模块化抽象，从而支持跨多样算法流水线与加速器设计的可扩展基准评测；(2) 采用数据流感知的两级调度器，以实现快速有效的 DSE。在 11 个加速器和两个数据集上，NeRArch-Sim 以极小改动复现了既有设计（建模误差 ≤9.4%），并指导新的加速器实现最高 1.3× 的效率提升。据我们所知，NeRArch-Sim 是首个能建模多种神经渲染加速器的开源仿真器，为这一新兴领域提供了及时的基础设施。该仿真器已公开于 https://github.com/GATECH-EIC/NeRArch-Sim。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：GATECH-EIC/NeRArch-Sim](https://github.com/GATECH-EIC/NeRArch-Sim)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
