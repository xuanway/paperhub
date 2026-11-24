---
title: "Hierarchical Prefetching, A Software-Hardware Instruction Prefetcher for Server Applications"
description: "ASPLOS 2025 · Session 5B · 层次化预取：面向服务器应用的软硬件指令预取器"
tags:
  - "ASPLOS2025"
  - "Session 5B"
  - "Microarchitecture"
---

# Hierarchical Prefetching, A Software-Hardware Instruction Prefetcher for Server Applications

**中文标题：** 层次化预取：面向服务器应用的软硬件指令预取器

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Tingji Zhang (Tsinghua University), Boris Grot (University of Edinburgh,Huawei Research), Wenjian He (Huawei Technologies Co., Ltd.), Yashuai Lv (Huawei Technologies Co., Ltd.), Peng Qu (Tsinghua University), Fang Su (Huawei Technologies Co., Ltd.), Wenxin Wang (Tsinghua University), Guowei Zhang (Huawei Technologies Co., Ltd.), Xuefeng Zhang (Tsinghua University), Youhui Zhang (Tsinghua University,Zhongguancun National Laboratory)

**单位：** Tsinghua University；University of Edinburgh,Huawei Research；Huawei Technologies Co., Ltd.；Tsinghua University,Zhongguancun National Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716260) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The large working set of instructions in server-side applications causes a significant bottleneck in the front-end, even for high-performance processors equipped with fetch-directed instruction prefetching (FDIP). Prefetchers specifically designed for server scenarios typically rely on a record-andreplay mechanism that exploits the repetitiveness of instruction sequences. However, the efficacy of these techniques is compromised by discrepancies between actual and predicted control flows, resulting in loss of coverage and timeliness. This paper proposes Hierarchical Prefetching, a novel approach that tackles the limitations of existing prefetchers. It identifies common coarse-grained functionality blocks (called Bundles) within the server code and prefetches them as a whole. Bundles are significantly larger than typical prefetch targets, encompassing tens to hundreds of kilobytes of code. The approach combines simple software analysis of code for bundle formation and light-weight hardware for record-and-replay prefetching. The prefetcher requires f the metadata in main memory. Experiments with 11 popular server workloads reveal that Hierarchical Prefetching significantly improves miss coverage and timeliness over prior techniques, achieving a 6.6% average performance gain over FDIP.

## 中文摘要

服务端应用中庞大的指令工作集即便对配备了取指导向指令预取（FDIP）的高性能处理器而言，也会造成显著的前端瓶颈。专为服务器场景设计的预取器通常依赖记录—重放（record-and-replay）机制，利用指令序列的重复性。然而，实际控制流与预测控制流之间的差异会损害这些技术的有效性，导致覆盖率与及时性损失。本文提出层次化预取（Hierarchical Prefetching），一种应对现有预取器局限性的新方法。它在服务器代码中识别常见的粗粒度功能块（称为 Bundle），并以整体方式预取它们。Bundle 远大于典型的预取目标，涵盖数十到数百 KB 的代码。该方法将用于 Bundle 构建的简单代码软件分析与用于记录—重放预取的轻量级硬件相结合。该预取器需要主存中的元数据。在 11 个流行服务器工作负载上的实验表明，层次化预取相比此前技术显著提升了缺失覆盖率与及时性，相对 FDIP 平均取得 6.6% 的性能提升。

## 英文关键词

Microarchitecture, Front-End Bottleneck, Instruction Prefetching

## 中文关键词

微体系结构；前端瓶颈；指令预取

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716260)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2025](../index.md)
