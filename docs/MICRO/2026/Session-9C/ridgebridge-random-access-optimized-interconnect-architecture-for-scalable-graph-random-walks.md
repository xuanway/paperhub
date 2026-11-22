---
title: "RidgeBridge: Random Access Optimized Interconnect Architecture for Scalable Graph Random Walks"
description: "MICRO 2026 · Session 9C · RidgeBridge：面向可扩展图随机游走的随机访问优化互连架构"
tags:
  - "MICRO2026"
  - "Graph Processing"
  - "Interconnect"
---

# RidgeBridge: Random Access Optimized Interconnect Architecture for Scalable Graph Random Walks

**中文标题：** RidgeBridge：面向可扩展图随机游走的随机访问优化互连架构

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Hongshi Tan, Yao Chen, Xinyu Chen, Qizhen Zhang, Weng-Fai Wong, Bingsheng He

**来源：** MICRO 2026，pp. 3429–3442；[DOI](https://doi.org/10.1109/MICRO67795.2026.00229)

## 英文摘要

Graph Random Walks (GRWs) are fundamental to applications such as recommendation, fraud detection, and graph-enhanced AI, creating an urgent need for distributed solutions that can keep pace with the exponential growth of real-world graphs. Existing scale-out frameworks predominantly rely on RDMA over Converged Ethernet, which performs well for bulk-transfer algorithms such as BFS and PageRank, but collapses to only 2-5% link utilization on GRWs due to the massive number of small, unpredictable requests. To address this gap, we propose RidgeBridge, the first interconnect architecture designed specifically for GRWs. RidgeBridge leverages a spine-leaf fabric with well-grounded randomized routing and timeout-driven batching to sustain near line-rate throughput on commodity high-speed Ethernet. We prototype RidgeBridge on FPGAs with 100 GbE and demonstrate linear scalability across nodes with near-optimal goodput utilization, enabling billion-scale GRW processing across multiple FPGAs. When scaling existing GRW accelerators, RidgeBridge scales linearly with the number of FPGAs, delivering a geometric-mean speedup of 20× over direct scale-out using a state-of-the-art multi-FPGA framework, and up to 3.5× higher throughput compared with the state-of-the-art multi-GPU solution.

## 中文摘要

图随机游走 (GRW) 是推荐、欺诈检测和图增强人工智能等应用的基础，迫切需要能够跟上现实世界图指数增长的分布式解决方案。现有的横向扩展框架主要依赖于融合以太网上的 RDMA，它对于 BFS 和 PageRank 等批量传输算法表现良好，但由于存在大量小型且不可预测的请求，GRW 上的链路利用率降至仅 2-5%。为了解决这一差距，我们提出了 RidgeBridge，这是第一个专为 GRW 设计的互连架构。 RidgeBridge 利用具有良好基础的随机路由和超时驱动批处理的脊叶结构来维持商用高速以太网上接近线速的吞吐量。我们在具有 100 GbE 的 FPGA 上构建了 RidgeBridge 原型，并展示了跨节点的线性可扩展性以及接近最佳的吞吐量利用率，从而实现了跨多个 FPGA 的十亿级 GRW 处理。在扩展现有 GRW 加速器时，RidgeBridge 可随 FPGA 数量线性扩展，与使用最先进的多 FPGA 框架的直接横向扩展相比，几何平均加速提高了 20 倍，与最先进的多 GPU 解决方案相比，吞吐量提高了 3.5 倍。

## 中文关键词

图随机游走；多 FPGA 系统；互连架构；横向扩展加速器；随机路由

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
