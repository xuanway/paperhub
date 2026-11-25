---
title: "SIVF: GPU-Resident IVF Index for Streaming Vector Analytics"
description: "HPDC 2026 · Session 10 — Data Systems for AI & Analytics"
tags:
  - "HPDC2026"
  - "Session 10"
  - "Data Systems for AI & Analytics"
---

# SIVF: GPU-Resident IVF Index for Streaming Vector Analytics

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 10</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807575)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#Zhao26](https://dblp.org/db/conf/hpdc/hpdc2026.html#Zhao26)

**作者**：Dongfang Zhao

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 10 — Data Systems for AI & Analytics（2026年7月16日 11:30–12:30 · Session Chair：Xiaoyi Lu）

---

## 英文摘要

GPU-accelerated Inverted File (IVF) index is one of the industry standards for large-scale vector search but relies on static VRAM layouts that hinder real-time mutability. Our benchmark and analysis reveal that existing designs of GPU IVF necessitate expensive CPU-GPU data transfers for index updates, causing system latency to spike from milliseconds to seconds in streaming scenarios. We present SIVF, a GPU-native index that enables high-velocity, in-place mutation via a series of new data structures and algorithms, such as conflict-free slab allocation and coalesced search on non-contiguous memory. SIVF has been implemented and integrated into the open-source vector search library, Faiss. Evaluation against baselines with diverse vector datasets demonstrates that SIVF reduces deletion latency by orders of magnitude compared to the state-of-the-arts. Furthermore, distributed experiments on a 12-GPU cluster demonstrate that SIVF exhibits near perfect linear scalability, achieving an aggregate ingestion throughput of 4.07 million vectors/s and a deletion throughput of 108.5 million vectors/s.

## 中文摘要

GPU 加速的倒排文件（IVF）索引是大规模向量搜索的行业标准之一，但其依赖静态显存布局，阻碍了实时可变性。我们的基准测试与分析表明，现有 GPU IVF 设计在索引更新时需要昂贵的 CPU-GPU 数据传输，导致流式场景下系统延迟从毫秒级飙升至秒级。我们提出 SIVF，一种 GPU 原生索引，通过无冲突 slab 分配、非连续内存上的合并搜索等一系列新数据结构与算法，实现高速原地变更。SIVF 已实现并集成到开源向量搜索库 Faiss 中。使用多样向量数据集与基线进行的评估表明，与最先进方法相比，SIVF 将删除延迟降低数个数量级。此外，在 12 块 GPU 集群上的分布式实验表明，SIVF 呈现近乎完美的线性扩展性，聚合摄取吞吐达到每秒 407 万个向量，删除吞吐达到每秒 1.085 亿个向量。

---

[← 返回 Session 10 — Data Systems for AI & Analytics](index.md)
