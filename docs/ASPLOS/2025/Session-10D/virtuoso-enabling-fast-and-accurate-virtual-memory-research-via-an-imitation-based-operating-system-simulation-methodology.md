---
title: "Virtuoso: Enabling Fast and Accurate Virtual Memory Research via an Imitation-based Operating System Simulation Methodology"
description: "ASPLOS 2025 · Session 10D · Virtuoso：基于模仿式操作系统模拟方法实现快速且准确的虚拟内存研究"
tags:
  - "ASPLOS2025"
  - "Session 10D"
  - "Memory Management"
---

# Virtuoso: Enabling Fast and Accurate Virtual Memory Research via an Imitation-based Operating System Simulation Methodology

**中文标题：** Virtuoso：基于模仿式操作系统模拟方法实现快速且准确的虚拟内存研究

**所属 Session：** [Session 10D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Konstantinos Kanellopoulos (ETH Zürich), Konstantinos Sgouras (ETH Zürich), Nisa Bostanci (ETH Zürich), Andreas Kosmas Kakolyris (ETH Zürich), Berkin Kerim Konar (ETH Zürich), Rahul Bera (ETH Zürich), Mohammad Sadrosadati (ETH Zürich), Rakesh Kumar (Norwegian University of Science and Technology (NTNU)), Nandita Vijaykumar (University of Toronto), Onur Mutlu (ETH Zürich)

**单位：** ETH Zürich；NTNU；University of Toronto

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716027) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The unprecedented growth in data demand from emerging applications has turned virtual memory (VM) into a major performance bottleneck. VM's overheads are expected to persist as memory requirements continue to increase. Researchers explore new hardware/OS co-designs to optimize VM across diverse applications and systems. To evaluate such designs, researchers rely on various simulation methodologies to model VM components. Unfortunately, current simulation tools (i) either lack the desired accuracy in modeling VM's software components or (ii) are too slow and complex to prototype and evaluate schemes that span across the hardware/software boundary. We introduce Virtuoso, a new simulation framework that enables quick and accurate prototyping and evaluation of the software and hardware components of the VM subsystem. The key idea of Virtuoso is to employ a lightweight userspace OS kernel, called MimicOS, that (i) accelerates simulation time by imitating only the desired kernel functionalities, (ii) facilitates the development of new OS routines that imitate real ones, using an accessible high-level programming interface, (iii) enables accurate and flexible evaluation of the application- and system-level implications of VM after integrating Virtuoso to a desired architectural simulator. In this work, we integrate Virtuoso into five diverse architectural simulators, each specializing in different aspects of system design, and heavily enrich it with multiple state-of-the-art VM schemes. This way, we establish a common ground for researchers to evaluate current VM designs and to develop and test new ones. We demonstrate Virtuoso's flexibility and versatility by evaluating five diverse use cases, yielding new insights into state-of-the-art VM techniques. Our validation shows that Virtuoso ported on top of Sniper, a state-of-the-art microarchitectural simulator, models (i) the memory management unit of a real high-end server-grade CPU with 82% accuracy, and (ii) the page fault latency of a real Linux kernel with up to 79% accuracy. Consequently, Virtuoso models the IPC performance of a real high-end servergrade CPU with 21% higher accuracy than the baseline version of Sniper. Virtuoso's accuracy benefits incur an average simulation time overhead of only 20%, on top of four baseline architectural simulators. The source code of Virtuoso is freely

## 中文摘要

新兴应用对数据需求的空前增长已使虚拟内存（VM）成为主要的性能瓶颈。随着内存需求持续增长，VM 的开销预计仍将存在。研究者在探索新的软硬件协同设计，以在多样化的应用与系统上优化 VM。为评估此类设计，研究者依赖各种模拟方法来对 VM 组件建模。遗憾的是，当前的模拟工具要么（i）在对 VM 软件组件建模时缺乏所需的准确性，要么（ii）过慢且过于复杂，难以对跨越硬件/软件边界的方案进行原型构建与评估。我们提出 Virtuoso，一个新的模拟框架，可对 VM 子系统的软件与硬件组件进行快速且准确的原型构建与评估。Virtuoso 的核心思想是采用一个名为 MimicOS 的轻量级用户态 OS 内核，它（i）仅模仿所需的内核功能，从而加速模拟时间，（ii）通过易用的高层编程接口，便于开发模仿真实例程的新 OS 例程，（iii）在将 Virtuoso 集成到目标体系结构模拟器后，能够准确而灵活地评估 VM 在应用层与系统层的影响。在本工作中，我们将 Virtuoso 集成到五个不同的体系结构模拟器中，每个模拟器专注于系统设计的不同方面，并用多种最先进的 VM 方案对其进行了大量充实。由此，我们为研究者建立了评估现有 VM 设计以及开发与测试新设计的共同基础。我们通过评估五个不同的用例展示了 Virtuoso 的灵活性与通用性，并对最先进的 VM 技术得出了新的洞见。我们的验证表明，将 Virtuoso 移植到最先进的微体系结构模拟器 Sniper 之上后，其建模（i）真实高端服务器级 CPU 的内存管理单元达到 82% 的准确度，（ii）真实 Linux 内核的缺页延迟达到最高 79% 的准确度。因此，Virtuoso 对真实高端服务器级 CPU 的 IPC 性能建模准确度比 Sniper 基线版本高 21%。Virtuoso 的准确性收益仅带来平均 20% 的模拟时间开销，且这是在四个基线体系结构模拟器之上额外付出的。Virtuoso 的源代码已免费提供。

## 英文关键词

Virtual Memory, Simulation, Operating Systems, Instrumentation, Address Translation, Memory Management

## 中文关键词

虚拟内存；模拟；操作系统；插桩；地址转换；内存管理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716027)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10D](index.md) · [返回 ASPLOS 2025](../index.md)
