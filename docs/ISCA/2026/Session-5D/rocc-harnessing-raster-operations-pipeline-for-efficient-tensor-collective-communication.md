---
title: "RoCC: Harnessing Raster Operations Pipeline for Efficient Tensor Collective Communication"
description: "ISCA 2026 · Session 5D · RoCC: Harnessing Raster Operations Pipeline for Efficient Tensor Collective Communication"
tags:
  - "ISCA2026"
  - "Session 5D"
  - "Potpourri"
---

# RoCC: Harnessing Raster Operations Pipeline for Efficient Tensor Collective Communication

**中文标题：** RoCC: 利用光栅操作流水线实现高效张量集合通信

**所属 Session：** [Session 5D](index.md) · [ISCA 2026](../index.md)

**作者：** Yuan Feng, Daniel Wong, Hyeran Jeon

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

This paper introduces RoCC, which enables fine-grained overlapping between compute and collective communication (CC) phases of LLM computing on GPUs, by offloading the CC to underutilized raster operations pipelines (ROPs). ROPs can provide fruitful performance for CC as they reside near the memory and have reduction computation capability. We first reverse engineer the ROP microarchitecture of two GPU architectures to model ROPs and add small logics to enable asynchronous computing and messaging for CC. We also decompose any CC operations into a sequence of ROP micro-operations. In our cycle-level simulations of a 4- to 8-GPU node with LLM training workloads, RoCC delivers an average of 51% and 23% speedups over the non-overlapping baseline and oracle kernel fusion, with only 2.4% L2 cache worth of area. On larger systems with 32 to 256 GPUs, RoCC consistently achieves speedups from 13 – 21%.

## 中文摘要

本文提出 RoCC，它通过将集合通信（CC）卸载到利用不足的光栅操作流水线（ROP），实现 GPU 上 LLM 计算中计算阶段与集合通信阶段的细粒度重叠。ROP 可为 CC 提供可观的性能，因为它们紧邻内存并具备归约计算能力。我们首先对两种 GPU 架构的 ROP 微架构进行逆向工程以对其建模，并加入少量逻辑以支持 CC 的异步计算与消息传递。我们还将任意 CC 操作分解为一系列 ROP 微操作。在针对 4 至 8 个 GPU 节点、使用 LLM 训练负载的周期级仿真中，RoCC 相比无可重叠基线平均加速 51%，相比理想内核融合（oracle kernel fusion）加速 23%，而仅占用相当于 2.4% L2 缓存的面积。在 32 至 256 个 GPU 的更大规模系统上，RoCC 稳定实现 13–21% 的加速。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：MoCALabUCM/rocc](https://github.com/MoCALabUCM/rocc)
- [实验材料归档（Zenodo 19489039）](https://zenodo.org/records/19489039)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5D](index.md) · [返回 ISCA 2026](../index.md)
