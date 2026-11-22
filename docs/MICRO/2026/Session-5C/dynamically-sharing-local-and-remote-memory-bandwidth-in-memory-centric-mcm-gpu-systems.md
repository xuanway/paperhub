---
title: "Dynamically Sharing Local and Remote Memory Bandwidth in Memory-Centric MCM-GPU Systems"
description: "MICRO 2026 · Session 5C · 以内存为中心的多芯片模块 GPU 系统中本地与远端内存带宽的动态共享"
tags:
  - "MICRO2026"
  - "GPU"
---

# Dynamically Sharing Local and Remote Memory Bandwidth in Memory-Centric MCM-GPU Systems

**中文标题：** 以内存为中心的多芯片模块 GPU 系统中本地与远端内存带宽的动态共享

**所属 Session：** [Session 5C](index.md) · [MICRO 2026](../index.md)

**作者：** Hossein SeyyedAghaei, Xin Wang, Mahmood Naderan-Tahan, Guy Torfs, Magnus Jahre, Lieven Eeckhout

**来源：** MICRO 2026，pp. 1799–1814；[DOI](https://doi.org/10.1109/MICRO67795.2026.00128)

## 英文摘要

The growing demand for computational power and memory bandwidth in modern applications, including artificial intelligence, data analytics and scientific computing, has made GPUs indispensable for high-performance, high-throughput computing. To meet these demands, industry has recently adopted Multi-Chip Module (MCM) GPU architectures, which integrate multiple GPU chiplets on an interposer substrate for continued performance scaling. Conventional MCM-GPU architectures follow a GPU-centric design in which GPU chiplets are connected to High-Bandwidth Memory (HBM) stacks for local memory accesses and other GPU chiplets for remote memory accesses. Unfortunately, GPU-centric architectures statically (at design time) partition off-chip GPU bandwidth between local and remote memory accesses, which fails to adapt to the diverse and dynamically varying bandwidth characteristics observed in modern-day applications. To overcome these challenges, we propose the memory-centric MCM-GPU architecture. The key insight is to dynamically share GPU off-chip bandwidth for local and remote memory accesses by connecting GPU chiplets to bridge chiplets that are interconnected to each other on the underlying interposer. A bridge chiplet is connected to an HBM stack (for local memory accesses) and other bridge chiplets (for remote memory accesses in other HBM stacks). A useful side-effect of the memory-centric architecture is that it also enables adding more HBM stacks per GPU chiplet, thereby increasing memory bandwidth and capacity. The memory-centric design improves GPU off-chip bandwidth utilization and effective memory bandwidth, which ultimately leads to improved performance. Our experimental evaluation reports an average 1.39× (and up to 2.27×) speedup for the memory-centric MCM-GPU over a conventional GPU-centric design, while incurring modest power and chip area overheads.

## 中文摘要

现代应用（包括人工智能、数据分析和科学计算）对计算能力和内存带宽的需求不断增长，使得 GPU 对于高性能、高吞吐量计算不可或缺。为了满足这些需求，业界最近采用了多芯片模块 (MCM) GPU 架构，该架构在中介层基板上集成了多个 GPU 小芯片，以实现持续的性能扩展。传统的 MCM-GPU 架构遵循以 GPU 为中心的设计，其中 GPU 小芯片连接到高带宽内存 (HBM) 堆栈以进行本地内存访问，并连接到其他 GPU 小芯片以进行远程内存访问。不幸的是，以 GPU 为中心的架构（在设计时）在本地和远程内存访问之间静态地划分片外 GPU 带宽，这无法适应现代应用中观察到的多样化且动态变化的带宽特征。为了克服这些挑战，我们提出了以内存为中心的 MCM-GPU 架构。关键见解是通过将 GPU 小芯片连接到在底层中介层上相互互连的桥接小芯片，动态共享用于本地和远程内存访问的 GPU 片外带宽。桥接小芯片连接到 HBM 堆栈（用于本地内存访问）和其他桥接小芯片（用于其他 HBM 堆栈中的远程内存访问）。以内存为中心的架构的一个有用的副作用是，它还可以为每个 GPU 小芯片添加更多 HBM 堆栈，从而增加内存带宽和容量。以内存为中心的设计提高了 GPU 片外带宽利用率和有效内存带宽，最终提高性能。我们的实验评估报告显示，与传统的以 GPU 为中心的设计相比，以内存为中心的 MCM-GPU 平均加速 1.39 倍（最高可达 2.27 倍），同时会产生适度的功耗和芯片面积开销。

## 中文关键词

多芯片 GPU；以内存为中心；本地与远端内存；带宽共享

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5C](index.md) · [MICRO 2026 主页](../index.md)
