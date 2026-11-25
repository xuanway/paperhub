---
title: "ATLAS: Efficient Out-of-Core Inference for Billion-Scale Graph Neural Networks"
description: "HPDC 2026 · Session 10 — Data Systems for AI & Analytics"
tags:
  - "HPDC2026"
  - "Session 10"
  - "Data Systems for AI & Analytics"
---

# ATLAS: Efficient Out-of-Core Inference for Billion-Scale Graph Neural Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 10</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807597)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#NamanS26](https://dblp.org/db/conf/hpdc/hpdc2026.html#NamanS26)

**作者**：Pranjal Naman, Yogesh Simmhan

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）

---

## 英文摘要

Graph Neural Network (GNN) inference on billion-scale graphs is critical for domains like fintech and recommendation systems. Full-graph inference on these large graphs can be challenging due to high communication costs in distributed settings and high I/O costs in disk-backed Out-of-Core (OOC) settings. Existing OOC systems, operating across disk and memory, primarily focus on GNN training and perform poorly for full-graph inference due to massive read amplification, irregular I/O and memory pressure. We present ATLAS, a disk-based GNN inference framework that enables efficient full-graph, layer-wise inference on graphs whose topologies, features and intermediate embeddings exceed the available memory on single machines. ATLAS replaces gather-based execution with a broadcast-based model that enables sequential, single-pass streaming reads of features and embeddings per layer. A tiered memory–disk hierarchy with minimum-pending-message eviction, graph reordering and a GPU-accelerated pipeline sustains high throughput within 128 GiB RAM and 2 TiB SSD. Across out-of-core graphs with up to 4B edges and 550 GiB features and multiple GNN architectures, ATLAS improves end-to-end inference time by ≈ 12–30× over State-of-the-Art (SOTA) OOC baselines on a single workstation, while remaining within ≈ 5% when features fit in memory.

## 中文摘要

十亿规模图上的图神经网络（GNN）推理对金融科技、推荐系统等领域至关重要。在这类大图上进行全图推理颇具挑战，原因在于分布式环境下的高通信成本以及磁盘支撑的外存（OOC）环境下的高 I/O 成本。现有跨磁盘与内存运行的 OOC 系统主要面向 GNN 训练，由于大量读放大、不规则 I/O 和内存压力，在全图推理上表现不佳。我们提出 ATLAS，一个基于磁盘的 GNN 推理框架，可在拓扑、特征和中间嵌入超出单机可用内存的图上实现高效的全图、逐层推理。ATLAS 用基于广播的模型取代基于聚合（gather）的执行，从而支持对每层特征与嵌入的顺序、单遍流式读取。具备最小待处理消息逐出、图重排序和 GPU 加速流水线的分级内存-磁盘层次结构，在 128 GiB 内存和 2 TiB SSD 内维持高吞吐。在边数多达 40 亿、特征达 550 GiB 的外存图以及多种 GNN 架构上，ATLAS 在单台工作站上将端到端推理时间相比最先进（SOTA）OOC 基线提升约 12–30 倍，而在特征可放入内存时性能差距保持在约 5% 以内。

## 英文关键词

Graph Neural Network (GNN), Disk-based Inference, Memory management, Out-of-Core (OOC) Computation

## 中文关键词

图神经网络（GNN），基于磁盘的推理，内存管理，外存（OOC）计算

---

[← 返回 Session 10 — Data Systems for AI & Analytics](index.md)
