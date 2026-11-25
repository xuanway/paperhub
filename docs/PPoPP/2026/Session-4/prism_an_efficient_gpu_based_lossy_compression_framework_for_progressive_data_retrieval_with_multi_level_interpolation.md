---
title: "PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation"
description: "PPoPP 2026 Session 4（GPU and Heterogeneous Computing）：多重插值+位平面+符号-绝对值编码，吞吐高 20.1×"
tags:
  - "PPoPP2026"
  - "Session-4"
  - "GPU and Heterogeneous Computing"
  - "Lossy Compression"
  - "GPU"
  - "Progressive Retrieval"
authors:
  - "Bing Lu"
  - "Zedong Liu"
  - "Hairui Zhao"
  - "Dejun Luo"
  - "Wenjing Huang"
  - "Yida Gu"
  - "Jinyang Liu"
  - "Guangming Tan"
  - "Dingwen Tao"
session: "Session 4: GPU and Heterogeneous Computing"
session_number: 4
session_chair: "Frank Mueller"
date: "2026-02-02"
time: "15:50–16:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786438"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Nominee"
---

# PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 GPU 渐进式有损压缩器 PRISM，融合多重插值预测、位平面提取与符号-绝对值编码的增强无损压缩，相同误差界下吞吐最高提升 20.1×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 4: GPU and Heterogeneous Computing</p>
</div>

**作者**：Bing Lu, Zedong Liu, Hairui Zhao, Dejun Luo, Wenjing Huang, Yida Gu, Jinyang Liu, Guangming Tan, and Dingwen Tao — Institute of Computing Technology at Chinese Academy of Sciences, China; Jilin University, China; University of Chinese Academy of Sciences, China; University of California at Riverside, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 15:50–16:10 · Session 4: GPU and Heterogeneous Computing（主席：Frank Mueller）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786438) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Nominee**

---

## 英文摘要

With the exponential growth of computing power, large-scale scientific simulations are producing massive volumes of data, leading to critical storage and I/O challenges. Error-bounded lossy compression has become one of the most effective solutions for reducing data size while preserving accuracy. Leveraging GPU is increasingly essential for high-performance compression on such large datasets, but GPU-based lossy compressors usually support only single-precision decompression, limiting their ability to meet the diverse accuracy requirements of scientific workflows. Progressive compressors can address this limitation by enabling on-demand precision retrieval. However, existing progressive lossy compressors on GPU still suffer from low throughput. To overcome these challenges, we present PRISM, a GPU-based progressive lossy compressor that achieves both high throughput and multi-precision retrieval, which introduces a high performance progressive framework that integrates the multiple interpolation predictors, efficient bitplane extraction, and an enhanced lossless compression that combines sign-absolute coding with zero-aware parallel algorithms. Evaluations on representative real-world datasets from five scientific domains show that PRISM significantly outperforms state-of-the-art progressive compressors on GPU, reducing retrieval data volume by over 15.6× and achieving up to 20.1× higher throughput on the NVIDIA H100 GPU under the same error bounds.

## 中文摘要

随着算力的指数级增长，大规模科学仿真正产生海量数据，带来严峻的存储与 I/O 挑战。误差有界的有损压缩已成为在保持精度的同时减小数据规模的最有效方案之一。在此类超大规模数据集上实现高性能压缩，愈发依赖 GPU；但基于 GPU 的有损压缩器通常仅支持单精度解压，难以满足科学工作流多样化的精度需求。渐进式压缩器可通过按需的精度检索来缓解这一局限。然而，GPU 上现有的渐进式有损压缩器仍存在吞吐量低的问题。为应对这些挑战，我们提出 PRISM，一个基于 GPU 的渐进式有损压缩器，可同时实现高吞吐与多精度检索；它引入了一个高性能渐进式框架，集成了多插值预测器、高效的位平面提取，以及结合符号-绝对值编码与零感知并行算法的增强无损压缩。在来自五个科学领域的代表性真实数据集上的评测表明，PRISM 显著优于 GPU 上最先进的渐进式压缩器：在相同误差界下，检索数据量降低 15.6 倍以上，并在 NVIDIA H100 GPU 上取得最高 20.1 倍的吞吐提升。

## 英文关键词

Lossy compressor, Progressive decompression, High performance

## 中文关键词

有损压缩器；渐进式解压；高性能

---

## 一句话总结

> 提出 GPU 渐进式有损压缩器 PRISM，融合多重插值预测、位平面提取与符号-绝对值编码的增强无损压缩，相同误差界下吞吐最高提升 20.1×。

## 研究问题

GPU 有损压缩器通常只支持单精度解压，难以满足科学工作流多样的精度需求；而现有 GPU 渐进式有损压缩器吞吐偏低，无法兼顾高吞吐与多精度检索。

## 方法简述

- 提出高性能渐进式压缩框架，集成多重插值预测器以支持按需的多精度渐进重构。
- 设计高效的位平面提取方法。
- 采用结合符号-绝对值编码与零感知并行算法的增强无损压缩阶段。

## 主要结果

- 在来自五个科学领域的代表性真实数据集上，相同误差界下检索数据量减少 15.6× 以上。
- 在 NVIDIA H100 GPU 上吞吐最高提升 20.1×，显著优于最先进的 GPU 渐进式压缩器。

---

> 所属 Session：[Session 4: GPU and Heterogeneous Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
