---
title: "Lazy-LLC: Reducing GPU LLC Thrashing with Shared-Data and Reusability Filters"
description: "MICRO 2026 · Session 5C · Lazy-LLC：利用共享数据与可复用性过滤器减少 GPU 末级缓存抖动"
tags:
  - "MICRO2026"
  - "GPU"
---

# Lazy-LLC: Reducing GPU LLC Thrashing with Shared-Data and Reusability Filters

**中文标题：** Lazy-LLC：利用共享数据与可复用性过滤器减少 GPU 末级缓存抖动

**所属 Session：** [Session 5C](index.md) · [MICRO 2026](../index.md)

**作者：** Sina Darabi, Ahmad Javadi-Nezhad, Hajar Falahati, Negin Mahani, Adrian Cristal, Osman Unsal, Hamid Sarbazi-Azad

**来源：** MICRO 2026，pp. 1784–1798；[DOI](https://doi.org/10.1109/MICRO67795.2026.00127)

## 英文摘要

Graphics Processing Units (GPUs) are engineered for massive parallelism, supporting high-computation applications, such as deep learning and graphics rendering. The Last Level Cache (LLC) in modern GPUs is pivotal in managing off-chip memory requests. However, excessive LLC requests can lead to cache thrashing, which reduces cache hits and increases off-chip memory writes. Despite the increase in LLC sizes in recent GPU generations, handling LLC pressure remains challenging due to the proportional growth in application input datasets. Current studies predominantly focus on balancing LLC pressure rather than directly reducing it through bypassing. In this paper, we make a key observation that LLC Miss Status Holding Register (MSHR) and L1 data (L1D) cache inherently act as two filters to identify shared and reusable (LLC-friendly) data within and across Streaming Multiprocessors (SMs). We introduce Lazy-LLC, a novel approach that utilizes these two filters to selectively load data, improving efficiency for LLC management. Lazy-LLC increases effective bandwidth by 32.54%, reduces the LLC miss rate by 27.03%, and achieves 27.38% higher performance and 21.67% better energy efficiency compared to the NVIDIA A100 GPU in memory-bound applications, with less than 1% increase in thermal design power (TDP) and 0.01% additional die area.

## 中文摘要

图形处理单元 (GPU) 专为大规模并行性而设计，支持深度学习和图形渲染等高计算应用程序。现代 GPU 中的末级缓存 (LLC) 对于管理片外内存请求至关重要。然而，过多的 LLC 请求可能会导致缓存抖动，从而减少缓存命中并增加片外内存写入。尽管最近几代 GPU 的 LLC 大小有所增加，但由于应用程序输入数据集的比例增长，处理 LLC 压力仍然具有挑战性。目前的研究主要集中在平衡 LLC 压力，而不是通过旁路直接降低压力。在本文中，我们进行了一个关键观察，即 LLC 未命中状态保持寄存器 (MSHR) 和 L1 数据 (L1D) 缓存本质上充当两个过滤器，用于识别流式多处理器 (SM) 内部和之间的共享和可重用（LLC 友好）数据。我们引入了 Lazy-LLC，这是一种利用这两个过滤器有选择地加载数据的新颖方法，从而提高 LLC 管理的效率。与内存受限应用中的 NVIDIA A100 GPU 相比，Lazy-LLC 将有效带宽提高了 32.54%，将 LLC 未命中率降低了 27.03%，性能提高了 27.38%，能效提高了 21.67%，热设计功耗 (TDP) 增加了不到 1%，芯片面积增加了 0.01%。

## 中文关键词

GPU 架构；末级缓存；缓存抖动；缓存旁路；未命中状态处理寄存器；能效

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5C](index.md) · [MICRO 2026 主页](../index.md)
