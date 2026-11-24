---
title: "COSM: A Cooperative Scheduling Framework for Concurrent PIM and CPU Execution on Mobile Devices"
description: "ISCA 2026 · Session 1A · COSM: A Cooperative Scheduling Framework for Concurrent PIM and CPU Execution on Mobile Devices"
tags:
  - "ISCA2026"
  - "Session 1A"
  - "Best Paper Candidate Session"
---

# COSM: A Cooperative Scheduling Framework for Concurrent PIM and CPU Execution on Mobile Devices

**中文标题：** COSM: 移动设备上 PIM 与 CPU 并发执行的协同调度框架

**所属 Session：** [Session 1A](index.md) · [ISCA 2026](../index.md)

**作者：** Yilong Zhao, Fangxin Liu, Onur Mutlu, Mingyu Gao, Jian Liu, Haibing Guan, Li Jiang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The development of on-device large language models (LLMs) is driven by the need for privacy and fast response times. Energy-intensive data transfer on mobile devices makes Processing-in-Memory (PIM) an effective solution. Due to stringent DRAM cost constraints, limited physical footprint on circuit boards, and the interaction between applications and LLMs, it is imperative for the CPU and PIM to operate concurrently within a shared memory space. However, challenges such as bank conflicts and bus congestion can arise, potentially diminishing the performance and energy benefits of PIM To address this challenge, we introduce COSM, a cooperative scheduling framework designed to facilitate the concurrent operation of PIM and CPU tasks on mobile platforms. Our key innovations include: 1) a low-interference PIM control interface that generates the maximum number of PIM commands without disrupting CPU memory accesses; 2) an idleness-aware scheduling method that integrates PIM commands into available idle time windows within the CPU’s access sequence. COSM not only hides PIM execution latency from the CPU, but also overlaps PIM execution with data transfer. Experiments on concurrent execution of LLMs and mobile workloads, including mobile applications and compute-intensive kernels, demonstrate that COSM improves PIM throughput by up to 2.8× compared to the baseline scheduling method with less than 2.0% CPU performance loss.

## 中文摘要

端侧大语言模型（LLM）的发展是由对隐私和快速响应时间需求驱动的。移动设备上高能耗的数据传输使得存内处理（PIM）成为一种有效的解决方案。由于严格的 DRAM 成本限制、电路板上有限的物理空间以及应用程序与 LLM 之间的交互，CPU 和 PIM 必须在一个共享内存空间内并发运行。然而，可能会产生存储体冲突和总线拥塞等挑战，从而可能降低 PIM 的性能和能效优势。为解决这一挑战，我们引入了 COSM，一种协同调度框架，旨在促进移动平台上 PIM 和 CPU 任务的并发运行。我们的关键创新包括：1）一种低干扰的 PIM 控制接口，能在不干扰 CPU 内存访问的情况下生成最大数量的 PIM 命令；2）一种空闲感知的调度方法，将 PIM 命令集成到 CPU 访问序列中的可用空闲时间窗口内。COSM 不仅向 CPU 隐藏了 PIM 执行延迟，还使 PIM 执行与数据传输重叠。在对 LLM 与移动工作负载（包括移动应用程序和计算密集型内核）的并发执行实验中，与基线调度方法相比，COSM 将 PIM 吞吐量提高了高达 2.8×，同时 CPU 性能损失小于 2.0%。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19660293）](https://zenodo.org/records/19660293)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2026](../index.md)
