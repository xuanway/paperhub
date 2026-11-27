---
title: "NOVA: A Novel Vertex Management Architecture For Scalable Graph Processing"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# NOVA: A Novel Vertex Management Architecture For Scalable Graph Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Marjan Fariborz (University of California, Davis), Mahyar Samani (University of California, Davis), Austin York (University of California, Davis), S. J. Ben Yoo (University of California, Davis; Lawrence Berkeley National Laboratory), Jason Lowe-Power (University of California, Davis; Lawrence Berkeley National Laboratory), Venkatesh Akella (University of California, Davis)
**会议**：HPCA 2025

---

## 中文标题

NOVA：面向可扩展图处理的新型顶点管理架构

## 英文摘要

We propose a scalable graph processing hardware accelerator called NOVA that is based on a novel vertex management architecture that decouples the execution of reduction and propagation operations in the popular vertex-centric graph processing paradigm. This allows us to store the working set in off-chip memory and utilize the available on-chip memory as a buffer to hide the latency of DRAM accesses instead of a traditional cache. This overcomes one of the key drawbacks of almost all the prior works which require temporal partitioning of graphs to scale to large graphs. We develop a cycle-accurate model of the architecture in gem5 and demonstrate that NOVA exhibits near-perfect weak and strong scaling while scaling to large graphs by spatially tiling multiple nodes. In addition, our simulations show that NOVA is 2.35× better than a state-of-the-art graph accelerator (PolyGraph) while using a fraction of the on-chip memory on a synthetic graph with 134M vertices and over 2.14B edges.

## 中文摘要

我们提出了一种名为 NOVA 的可扩展图处理硬件加速器，它基于一种新型顶点管理架构，该架构将主流以顶点为中心的图处理范式中的规约操作与传播操作的执行解耦。这使我们能够把工作集存放在片外内存中，并将可用的片上内存用作缓冲区来隐藏 DRAM 访问时延，而不是用作传统缓存。这克服了几乎所有先前工作的一个关键缺陷，即需要按时间对图进行划分才能扩展到大规模图。我们在 gem5 中为该架构开发了周期精确模型，并证明 NOVA 通过在多节点上进行空间分块扩展到大规模图时，表现出近乎完美的弱扩展性和强扩展性。此外，仿真表明，在包含 134M 个顶点、超过 2.14B 条边的合成图上，NOVA 仅使用一小部分片上内存，性能就比最先进的图加速器（PolyGraph）好 2.35 倍。
