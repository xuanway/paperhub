---
title: "Nyx: Virtualizing Dataflow Execution on Shared FPGA Platforms"
description: "ISCA 2025 · Session 7B · Nyx：在共享 FPGA 平台上虚拟化数据流执行"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# Nyx: Virtualizing Dataflow Execution on Shared FPGA Platforms

**中文标题：** Nyx：在共享 FPGA 平台上虚拟化数据流执行

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Panagiotis Miliadis, Dimitris Theodoropoulos, Nectarios Koziris, Dionisios Pnevmatikatos

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731094) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

As FPGAs become more widespread for improving computing per- formance within cloud infrastructure, researchers aim to equip them with virtualization features to enable resource sharing in both temporal and spatial domains, thereby improving hardware utiliza- tion. Existing multi-tenant solutions focus on task-parallel models, where tasks are assigned to distinct regions to process separate sets of data. However, this model introduces waiting times between dependent and pipelined tasks, leading to longer response times for applications. The root cause is the lack of support for dataflow execution -a key potential of FPGAs and a crucial optimization for applications. Dataflow allows direct data streaming between operators, forming a task-pipelined model that reduces application latency by overlapping task operations within its workflow. This paper presents Nyx, the first system to enable dataflow exe- cution in a task-based virtualized and shared FPGA environment. Nyx enables efficient resource sharing by dividing the FPGA into dis- tinct reconfigurable regions. At its core, Nyx employs virtual FIFOs, independent channels that allow seamless communication between pipelined tasks. Its approach ensures smooth task operation even when the predecessor or successor tasks are not simultaneously scheduled in the FPGA, making them agnostic to their dependencies, communication channels or data locations. An FPGA hypervisor is designed to handle all data dependencies and efficiently dispatch pipelined tasks across regions at high throughput. Nyx outperforms existing state of the art virtualized task-parallel approaches by 1.26x-8.87x across a series of real-world benchmarks. Furthermore, it reduces response times by 2.8x - 3.28x during low-demand periods, decreasing also deadline violations by up to 76.5%. Under high- demand conditions, Nyx delivers 2x - 2.75x reduction, 34.5% fewer violations, and up to 1.9x reduced tail response time.

## 中文摘要

随着FPGA在云基础设施中广泛用于提升计算性能，研究者为FPGA增加虚拟化能力，以支持时间域与空间域的资源共享，提升硬件利用率。现有的多租户方案大多基于任务并行模型：任务分配到不同区域，分别处理独立数据集。但该模型会带来存在依赖关系、流水线任务之间的等待开销，拉长应用响应时间。根源在于这类方案不支持数据流执行——而数据流正是FPGA的核心优势，也是应用优化的关键手段。数据流允许算子之间直接流式传输数据，构建任务流水线模型，通过工作流内任务重叠执行，降低应用延迟。

本文提出Nyx，首个在基于任务的虚拟化共享FPGA环境中支持数据流执行的系统。Nyx将FPGA划分为多个独立可重构区域，实现高效资源共享。Nyx的核心是虚拟FIFO机制：一组独立通道，保障流水线任务之间流畅通信。即使上游或下游任务没有同时调度到FPGA上运行，该机制仍能保证任务正常执行，使任务本身无需感知依赖关系、通信通道与数据位置。本文设计FPGA虚拟化管理程序（hypervisor），统一处理所有数据依赖，并以高吞吐在不同区域调度流水线任务。

在一系列真实基准测试集上，Nyx对比前沿虚拟化任务并行方案，性能提升1.26–8.87倍。低负载场景下，响应时间降低2.8–3.28倍，截止时间违规最多减少76.5%；高负载场景下，响应时间降低2–2.75倍，违规数量减少34.5%，尾延迟最高下降1.9倍。

## 英文关键词

Virtualization, Reconfigurable Computing, FPGAs, Dataflow, Run-time Systems

## 中文关键词

虚拟化, 可重构计算, FPGA, 数据流, 运行时系统

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15102799)
- [代码仓库](https://github.com/cslab-ntua/Nyx-ISCA2025)
- [研究制品](https://doi.org/10.5281/zenodo.15274814)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731094)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
