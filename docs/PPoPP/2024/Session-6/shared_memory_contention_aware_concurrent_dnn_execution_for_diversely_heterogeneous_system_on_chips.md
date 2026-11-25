---
title: "Shared Memory-contention-aware Concurrent DNN Execution for Diversely Heterogeneous System-on-Chips"
description: "PPoPP 2024 Session ML Workloads：按层映射异构加速器，内存竞争降 45%、延迟降 32%、吞吐升 29%"
tags:
  - "PPoPP2024"
  - "Session-6"
  - "ML Workloads"
  - "Concurrent DNN inference"
  - "Shared memory contention"
  - "Heterogeneous SoCs"
authors:
  - "Ismet Dagli"
  - "Mehmet E. Belviranli"
session: "Session 6: ML Workloads"
session_number: 6
session_chair: "Xipeng Shen"
date: "2024-03-05"
time: "11:50–12:10"
room: "Moorfoot"
doi: "10.1145/3627535.3638502"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Shared Memory-contention-aware Concurrent DNN Execution for Diversely Heterogeneous System-on-Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">HaX-CoNN 对并发 DNN 推理逐层刻画并映射到 SoC 异构加速器，联合考虑共享内存竞争与加速器切换，内存竞争最多降 45%。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 6: ML Workloads</p>
</div>

**作者**：Ismet Dagli, Mehmet E. Belviranli (Colorado School of Mines)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 11:50–12:10 · Session 6: ML Workloads（主席：Xipeng Shen）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638502) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Two distinguishing features of state-of-the-art mobile and autonomous systems are: 1) There are often multiple workloads, mainly deep neural network (DNN) inference, running concurrently and continuously. 2) They operate on shared memory System-on-Chips (SoC) that embed heterogeneous accelerators tailored for specific operations. State-of-the-art systems lack efficient performance and resource management techniques necessary to either maximize total system throughput or minimize end-to-end workload latency. In this work, we propose HaX-CoNN, a novel scheme that characterizes and maps layers in concurrently executing DNN inference workloads to a diverse set of accelerators within an SoC. Our scheme uniquely takes per-layer execution characteristics, shared memory (SM) contention, and inter-accelerator transitions into account to find optimal schedules. We evaluate HaX-CoNN on NVIDIA Orin, NVIDIA Xavier, and Qualcomm Snapdragon 865 SoCs. Our experimental results indicate that HaX-CoNN can minimize memory contention by up to 45% and improve total latency and throughput by up to 32% and 29%, respectively, compared to the state-of-the-art.

## 中文摘要

当前最先进的移动与自主系统有两个显著特征：1）通常有多个工作负载（主要是深度神经网络（DNN）推理）并发且持续地运行；2）它们运行在共享内存的片上系统（SoC）上，这些 SoC 内嵌了针对特定操作定制的异构加速器。现有系统缺乏高效的性能与资源管理技术，而这些技术对于最大化系统总吞吐或最小化端到端工作负载延迟是必需的。在本工作中，我们提出 HaX-CoNN，一种新方案，它对并发执行的 DNN 推理工作负载中的层进行刻画，并将其映射到 SoC 内多样化的加速器集合上。我们的方案独特地考虑了逐层执行特征、共享内存（SM）竞争以及加速器间切换，以寻找最优调度。我们在 NVIDIA Orin、NVIDIA Xavier 和 Qualcomm Snapdragon 865 SoC 上评估 HaX-CoNN。实验结果表明，与最先进方法相比，HaX-CoNN 可将内存竞争最多降低 45%，并将总延迟与吞吐分别最多改善 32% 和 29%。

## 英文关键词

Concurrent DNN inference, Shared memory contention, Heterogeneous SoCs

## 中文关键词

并发 DNN 推理；共享内存竞争；异构 SoC

---

## 一句话总结

> HaX-CoNN 对并发 DNN 推理逐层刻画并映射到 SoC 异构加速器，联合考虑共享内存竞争与加速器切换，内存竞争最多降 45%。

## 研究问题

移动与自主系统上多个 DNN 推理并发持续运行于共享内存 SoC，但现有系统缺乏性能与资源管理技术，既无法最大化系统总吞吐，也无法最小化端到端工作负载延迟。

## 方法简述

- 对并发执行的 DNN 推理工作负载逐层刻画执行特征，并将各层映射到 SoC 内多样化的加速器集合。
- 将逐层执行特征、共享内存（SM）竞争与加速器间切换开销一并纳入考量，以搜索最优调度方案。

## 主要结果

- 与最先进方法相比，内存竞争最多降低 45%。
- 总延迟与吞吐分别最多改善 32% 和 29%。
- 在 NVIDIA Orin、NVIDIA Xavier 与 Qualcomm Snapdragon 865 三类 SoC 上完成评估。

---

> 所属 Session：[Session 6: ML Workloads](index.md) · 返回 [PPoPP 2024 总览](../index.md)
