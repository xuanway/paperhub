---
title: "TiNA: Tiered Network Buffer Architecture for Fast Networking in Chiplet-based CPU"
description: "ASPLOS 2026 · Session 9D · TiNA：面向基于 Chiplet 的 CPU 中快速网络的分层网络缓冲区架构"
tags:
  - "ASPLOS2026"
  - "Session 9D"
  - "Network & Cloud Infrastructure"
---

# TiNA: Tiered Network Buffer Architecture for Fast Networking in Chiplet-based CPU

**中文标题：** TiNA：面向基于 Chiplet 的 CPU 中快速网络的分层网络缓冲区架构

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Siddharth Agarwal (UIUC), Tianchen Wang (UIUC), Jinghan Huang (UIUC), Saksham Agarwal (UIUC), Nan Sung Kim (UIUC)

**单位：** UIUC

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762224) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** TiNA: Tiered Network Buffer Architecture for Fast Networking in Chiplet-based CPUs

## 英文摘要

To manufacture a large CPU cost-effectively, the industry has begun exploiting emerging packaging technologies that integrate multiple chiplets—each comprising a subset of cores and/or memory and I/O subsystems—into a single package. However, such a CPU experiences longer memory access latency with more pronounced variance, especially when its cores in one chiplet access LLC slices1 or DRAM controllers in other chiplets. This creates unique challenges in µs-scale networking, which is highly sensitive to memory access latency. In this work, we start by proposing exploiting a little-known mode, known as Sub-NUMA Clustering (SNC), in the latest chiplet-based CPUs. As it restricts receiving and processing packets to a particular chiplet unless explicitly specified otherwise, it offers shorter memory access latency and, consequently, lower networking latency than the default mode (non-SNC). Nonetheless, when receiving long bursts of packets2, SNC incurs higher networking latency than non-SNC, as it provides less LLC capacity for CPU cores processing the packets, making Direct Cache Access (DCA)— a commonly used CPU feature to reduce memory access latency for packet processing—ineffective. To address this 1A slice is a subset of the LLC directly connected with a CPU core. The CPU core can access the LLC slices of other CPU cores through interconnects but at longer latency than its own LLC slice. 2A burst is defined as the period during which the NIC receives packets at line rate, and bursts lasting hundreds of microsec drawback, we propose TiNA, a tiered network buffer architecture consisting of an enhanced NIC and networking stack, which opportunistically uses LLC slices in other chiplets for DCA only when receiving long bursts of packets. On average, TiNA reduces the mean (tail) latency by 25% (18%) and 28% (22%), compared to SNC and non-SNC, respectively, across diverse network applications and traces.

## 中文摘要

为了以经济高效的方式制造大型 CPU，业界已开始利用新兴封装技术，将多颗 chiplet——每颗包含一部分核心和/或内存与 I/O 子系统——集成到单个封装中。然而，这样的 CPU 会经历更长的内存访问延迟，且方差更为明显，尤其是当某颗 chiplet 中的核心访问其他 chiplet 中的 LLC slice1 或 DRAM 控制器时。这给对内存访问延迟高度敏感的 µs 级网络带来了独特挑战。在本工作中，我们首先提出利用最新基于 chiplet 的 CPU 中一个鲜为人知的模式——Sub-NUMA Clustering（SNC）。由于除非显式指定，它会把数据包的接收与处理限制在特定 chiplet 内，因此相比默认模式（non-SNC），它能提供更短的内存访问延迟，并由此带来更低的网络延迟。然而，在接收长突发数据包2时，SNC 的网络延迟高于 non-SNC，因为它为处理数据包的 CPU 核心提供的 LLC 容量更少，使得 Direct Cache Access（DCA）——一种常用于降低数据包处理内存访问延迟的 CPU 特性——失效。为解决这一缺陷，我们提出 TiNA，一种由增强的 NIC 与网络栈组成的分层网络缓冲区架构，仅在接收长突发数据包时机会性地使用其他 chiplet 中的 LLC slice 进行 DCA。在多样化的网络应用与轨迹上，与 SNC 和 non-SNC 相比，TiNA 平均将平均（尾部）延迟分别降低 25%（18%）和 28%（22%）。

1 一个 slice 是与某个 CPU 核心直接相连的 LLC 子集。CPU 核心可以通过互连访问其他 CPU 核心的 LLC slice，但延迟高于访问自身的 LLC slice。2 突发定义为 NIC 以线速接收数据包的时段，持续数百微秒的突发

## 英文关键词

Sub-NUMA Clustering, Direct Cache Access, Chiplet, Direct Memory Access, Non Uniform Cache Access

## 中文关键词

Sub-NUMA Clustering；直接缓存访问（Direct Cache Access）；Chiplet；直接内存访问（Direct Memory Access）；非一致缓存访问（Non Uniform Cache Access）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762224)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2026](../index.md)
