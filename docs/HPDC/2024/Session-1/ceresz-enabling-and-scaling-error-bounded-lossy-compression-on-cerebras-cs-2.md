---
title: "CereSZ: Enabling and Scaling Error-bounded Lossy Compression on Cerebras CS-2"
description: "HPDC 2024 · Session 1 — Compression and AI"
tags:
  - "HPDC2024"
  - "Session 1"
  - "Compression and AI"
---

# CereSZ: Enabling and Scaling Error-bounded Lossy Compression on Cerebras CS-2

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 1</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658691)

**作者**：Shihui Song, Yafan Huang, Peng Jiang, Xiaodong Yu, Weijian Zheng, Sheng Di, Qinglei Cao, Yunhe Feng, Zhen Xie, Franck Cappello

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）

---

## 英文摘要

Today’s scientific applications running on supercomputers produce large volumes of data, leading to critical data storage and communication challenges. To tackle the challenges, error-bounded lossy compression is commonly adopted since it can reduce data size drastically within a user-defined error threshold. Previous work has shown that compression techniques can significantly reduce the storage and I/O overhead while retaining good data quality. However, the existing compressors are mainly designed for CPU and GPU. As new AI chips are being incorporated into supercomputers and increasingly used for accelerating scientific computing, there is a growing demand for efficient data compression on the new architecture. In this paper, we propose an efficient lossy compressor, CereSZ, based on the Cerebras CS-2 system. The compression algorithm is mapped onto Cerebras using both data parallelism and pipeline parallelism. In order to achieve a balanced workload on each processing unit, we propose an algorithm to evenly distribute the pipeline stages. Our experiments with six scientific datasets demonstrate that CereSZ can achieve a throughput from 227.93 GB/s to 773.8 GB/s, 2.43x to 10.98x faster than existing GPU compressors.

## 中文摘要

当今在超级计算机上运行的科学应用产生海量数据，带来严峻的数据存储与通信挑战。为应对这些挑战，误差有界有损压缩被普遍采用，因为它能在用户定义的误差阈值内大幅缩减数据规模。先前工作表明，压缩技术可在保持良好数据质量的同时显著降低存储与 I/O 开销。然而，现有压缩器主要面向 CPU 和 GPU 设计。随着新型 AI 芯片被纳入超级计算机并越来越多地用于加速科学计算，对新架构上高效数据压缩的需求日益增长。本文提出一种高效的基于 Cerebras CS-2 系统的有损压缩器 CereSZ。该压缩算法同时利用数据并行与流水线并行映射到 Cerebras 上。为在每个处理单元上实现负载均衡，我们提出一种均匀分配流水线阶段的算法。我们在六个科学数据集上的实验表明，CereSZ 可达到 227.93 GB/s 至 773.8 GB/s 的吞吐，比现有 GPU 压缩器快 2.43 倍至 10.98 倍。

## 英文关键词

Error-bounded Lossy Compression, AI-Optimized Architecture, Parallel Computing, Scientific Simulation, High-speed Compressor

## 中文关键词

误差有界有损压缩，AI 优化架构，并行计算，科学仿真，高速压缩器

---

[← 返回 Session 1 — Compression and AI](index.md)
