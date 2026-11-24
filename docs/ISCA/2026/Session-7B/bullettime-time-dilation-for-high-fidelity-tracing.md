---
title: "BULLETTIME: Time Dilation for High-Fidelity Tracing"
description: "ISCA 2026 · Session 7B · BULLETTIME: Time Dilation for High-Fidelity Tracing"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# BULLETTIME: Time Dilation for High-Fidelity Tracing

**中文标题：** BULLETTIME: 面向高保真追踪的时间膨胀

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Michael Wu, Sibren Isaacman, Abhishek Bhattacharjee, Anurag Khandelwal

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Much of computer systems and architecture research depends on accurate, high-fidelity program tracing for simulation, profiling, and debugging. Unfortunately, with significant improvements in compute and memory instruction execution speeds, tracing frameworks incur frequent I/O to persist traced events to disk. We find that such delays can be bursty and asymmetric across application threads, resulting in an inadvertent reordering of application and system operations relative to untraced execution. In our analysis, such reordering often leads to significant changes in the behavior of the studied application, thereby contaminating insights from simulation and profiling studies of the corresponding captured traces. In this work, we formalize the application behavior under study to establish correctness requirements for traced application execution in the presence of tracing-induced delays. We propose a novel time dilation approach that strategically slows execution for application and system threads while meeting correctness requirements. We implement the time-dilation approach in BULLETTIME, a tracing framework built atop Pin, the de facto binary instrumentation tool. We evaluate BULLETTIME for memory-contiguity and synchronization studies on real-world applications and workloads. Our results show that while existing tracing approaches can cause application behavior to deviate by as much as 20× compared to untraced execution, BULLETTIME’s deviations are < 10% even in extreme cases of asymmetric tracing delays.

## 中文摘要

计算机系统与体系结构研究的许多工作都依赖于准确、高保真的程序追踪，以用于仿真、性能剖析和调试。然而，随着计算与内存指令执行速度的大幅提升，追踪框架会因频繁的 I/O 而将追踪事件持久化到磁盘。我们发现，这类延迟可能呈现突发性，并在应用线程之间不对称，从而导致应用与系统操作相对于未追踪执行发生意外重排序。在我们的分析中，这种重排序常常导致所研究应用的行为发生显著变化，从而污染基于相应捕获轨迹的仿真与性能剖析研究所得到的洞见。在本工作中，我们对所研究的应用行为进行形式化，以确立在存在追踪引发延迟的情况下被追踪应用执行的正确性要求。我们提出一种新颖的时间膨胀（time dilation）方法，在满足正确性要求的同时，策略性地放慢应用线程和系统线程的执行。我们在 BULLETTIME 中实现了该时间膨胀方法，这是一个构建于事实上的二进制插桩工具 Pin 之上的追踪框架。我们针对真实应用与工作负载，在内存连续性和同步研究中评估了 BULLETTIME。结果表明，现有追踪方法可能使应用行为相对于未追踪执行偏离高达 20×，而 BULLETTIME 即使在追踪延迟严重不对称的极端情况下，偏离也小于 10%。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：ysarch-lab/BulletTime](https://github.com/ysarch-lab/BulletTime)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
