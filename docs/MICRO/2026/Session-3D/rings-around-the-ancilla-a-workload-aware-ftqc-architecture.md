---
title: "Rings Around the Ancilla: A Workload-Aware FTQC Architecture"
description: "MICRO 2026 · Session 3D · Rings Around the Ancilla：面向工作负载的容错量子计算架构"
tags:
  - "MICRO2026"
---

# Rings Around the Ancilla: A Workload-Aware FTQC Architecture

**中文标题：** Rings Around the Ancilla：面向工作负载的容错量子计算架构

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Archisman Ghosh, Avimita Chatterjee, Swaroop Ghosh

**来源：** MICRO 2026，pp. 1299–1312；[DOI](https://doi.org/10.1109/MICRO67795.2026.00098)

## 英文摘要

Obtaining a quantum advantage in practical applications over classical machines requires a fault-tolerant model of computation. However, the resource overhead of developing a fault-tolerant quantum computer (FTQC) architecture is quite high. Current state-of-the-art architecture designs promise constant-time access to logical qubits at the expense of a high qubit overhead, or qubit-dense layouts at the expense of increased latency in the execution of a quantum workload. In this paper, we propose (a) an architecture design that balances the tradeoff of execution time of workloads with the density of logical qubits by placing the surface code patches around the ancilla region, giving almost equal access of the ancilla region to all the data qubits, (b) design a novel algorithm to leverage the T-gate characteristics of the user workload to suggest the optimal placement strategy in the floorplan of our architecture, (c) a workload-selective fast-Y optimization knob that accelerates Y-basis measurements only for qubits whose Y-gate demand justifies the additional tile cost, and (d) explore the scope of executing multiple programs concurrently, which enhances the reconfigurability of our proposed design. Through numerical evaluation, we observe that the proposed architecture design maintains the cycles per instruction time close to optimal while using up to ~21% fewer data tiles, and up to ~90% efficiency under a 10-way concurrency.

## 中文摘要

在实际应用中获得相对于经典机器的量子优势需要容错计算模型。然而，开发容错量子计算机（FTQC）架构的资源开销相当高。当前最先进的架构设计承诺以高量子位开销为代价对逻辑量子位进行恒定时间访问，或者以增加量子工作负载执行时延为代价实现量子位密集布局。在本文中，我们提出了（a）一种架构设计，通过将表面码补丁放置在辅助区域周围，为所有数据量子位提供几乎平等的辅助区域访问权，从而平衡工作负载执行时间与逻辑量子位密度之间的权衡，（b）设计一种新颖的算法，利用用户工作负载的 T 门特性来建议架构布局中的最佳放置策略，（c）加速 Y 基础的工作负载选择性快速 Y 优化旋钮仅对其 Y 门需求证明额外切片成本合理的量子位进行测量，并且（d）探索同时执行多个程序的范围，这增强了我们提出的设计的可重构性。通过数值评估，我们观察到所提出的架构设计使每条指令时间的周期保持接近最佳状态，同时使用的数据块减少了约 21%，并且在 10 路并发下效率高达约 90%。

## 中文关键词

容错量子计算；量子计算架构；表面码；量子纠错；辅助量子比特

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
