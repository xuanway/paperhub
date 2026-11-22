---
title: "Pistil - A Decoupled Pipeline Architecture for Sustained Memory Bandwidth Across a 20-Chiplet 2.5D SiP for Edge SLM Inference"
description: "MICRO 2026 · Session 3C · Pistil：面向端侧小语言模型推理、在 20 芯粒 2.5D 系统级封装中维持内存带宽的解耦流水线架构"
tags:
  - "MICRO2026"
---

# Pistil - A Decoupled Pipeline Architecture for Sustained Memory Bandwidth Across a 20-Chiplet 2.5D SiP for Edge SLM Inference

**中文标题：** Pistil：面向端侧小语言模型推理、在 20 芯粒 2.5D 系统级封装中维持内存带宽的解耦流水线架构

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Matthew Joseph Adiletta, Nestor Cuevas, Haebin Do, Yun-Chen Lo, Kevin Kim, Gu-Yeon Wei, David Brooks

**来源：** MICRO 2026，pp. 1181–1195；[DOI](https://doi.org/10.1109/MICRO67795.2026.00091)

## 英文摘要

Small language model (SLM) reasoning on edge devices is decode-latency sensitive and requires sustained high token throughput under strict cost and power constraints. SLM decode is memory-bandwidth bound, and conventional edge platforms fail to deliver sufficient bandwidth per capacity to support interactive reasoning rates. Achieving practical on-device reasoning therefore requires architectures that sustain high memory utilization while remaining area- and energy-efficient. We present Pistil, a scalable, chiplet-based System-in-Package accelerator that sustains near-roofline memory bandwidth. Pistil employs a novel architecture which decouples memory, compute, and network pipelines through hardware-managed synchronization and integrates on-the-fly MXFP dequantization to efficiently support low-precision weights. Across representative dense SLM workloads, Pistil sustains >98% of peak memory bandwidth during decode and delivers 80-250 tokens/s within a 5W edge-system power and area budgets, achieving up to 7.6× lower latency and 7.8× lower energy per token than a Jetson Nano.

## 中文摘要

边缘设备上的小语言模型 (SLM) 推理对解码时延敏感，并且需要在严格的成本和功耗限制下持续高词元吞吐量。 SLM 解码受内存带宽限制，传统边缘平台无法为每容量提供足够的带宽来支持交互式推理速率。因此，实现实用的设备上推理需要架构能够维持高内存利用率，同时保持面积和能效。我们推出了 Pistil，这是一种可扩展、基于小芯片的系统级封装加速器，可维持接近极限的内存带宽。 Pistil 采用新颖的架构，通过硬件管理的同步来解耦内存、计算和网络管道，并集成动态 MXFP 反量化以有效支持低精度权重。在具有代表性的密集 SLM 工作负载中，Pistil 在解码期间可维持超过 98% 的峰值内存带宽，并在 5W 边缘系统功耗和面积预算内提供 80-250 个词元/秒，与 Jetson Nano 相比，时延降低高达 7.6 倍，每个词元能耗降低 7.8 倍。

## 中文关键词

边缘推理；分布式计算；可扩展内存带宽；芯粒；解耦流水线

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
