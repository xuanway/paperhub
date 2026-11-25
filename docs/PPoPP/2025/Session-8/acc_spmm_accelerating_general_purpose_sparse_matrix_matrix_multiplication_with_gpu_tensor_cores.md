---
title: "Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores"
description: "PPoPP 2025 Session 8（Tensor Cores）：四项系统优化，H100 上平均 1.58×、最高 3.60×"
tags:
  - "PPoPP2025"
  - "Session-8"
  - "Tensor Cores"
  - "SpMM"
  - "Load Balancing"
authors:
  - "Haisha Zhao"
  - "San Li"
  - "Jiaheng Wang"
  - "Chunbao Zhou"
  - "Jue Wang"
  - "Zhikuang Xin"
  - "Shunde Li"
  - "Zhiqiang Liang"
  - "Zhijie Pan"
  - "Fang Liu"
  - "Yan Zeng"
  - "Yangang Wang"
  - "Xuebin Chi"
session: "Session 8: Tensor Cores"
session_number: 8
session_chair: "Jeffrey Vetter"
date: "2025-03-04"
time: "14:20–14:40"
room: "Acacia D"
doi: "10.1145/3710848.3710888"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Acc-SpMM: Accelerating General-purpose Sparse Matrix-Matrix Multiplication with GPU Tensor Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出高性能 SpMM 库 Acc-SpMM，结合数据亲和重排序、内存高效压缩格式、高吞吐流水线与自适应稀疏感知负载均衡，充分释放 Tensor Core 性能。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 8: Tensor Cores</p>
</div>

**作者**：Haisha Zhao, San Li (Computer Network Information Center, Chinese Academy of Sciences, University of Chinese Academy of Sciences); Jiaheng Wang (Renmin University of China); Chunbao Zhou, Jue Wang, Zhikuang Xin, Shunde Li, Zhiqiang Liang (Computer Network Information Center, Chinese Academy of Sciences, University of Chinese Academy of Sciences); Zhijie Pan (Hangzhou Dianzi University); Fang Liu (Computer Network Information Center, Chinese Academy of Sciences, University of Chinese Academy of Sciences); Yan Zeng (Hangzhou Dianzi University); Yangang Wang (Computer Network Information Center, Chinese Academy of Sciences, University of Chinese Academy of Sciences); Xuebin Chi (Computer Network Information Center, Chinese Academy of Sciences; University of Chinese Academy of Sciences)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 14:20–14:40 · Session 8: Tensor Cores（主席：Jeffrey Vetter）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710888) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出高性能 SpMM 库 Acc-SpMM，结合数据亲和重排序、内存高效压缩格式、高吞吐流水线与自适应稀疏感知负载均衡，充分释放 Tensor Core 性能。

## 研究问题

Tensor Core 等新矩阵计算单元为 SpMM 加速带来机会，但要真正发挥硬件性能，需要系统性的优化设计。

## 方法简述

- 基于数据亲和性的重排序（data-affinity-based reordering）。
- 设计内存高效的压缩格式，并构建高吞吐流水线。
- 采用自适应稀疏感知的负载均衡策略。

## 主要结果

- 相比 cuSPARSE，RTX 4090 上平均加速 2.52×（最高 5.11×）。
- A800 上平均加速 1.91×（最高 4.68×），H100 上平均加速 1.58×（最高 3.60×）。

<details>
<summary>原文摘要（英文）</summary>

General-purpose Sparse Matrix-Matrix Multiplication (SpMM) is a fundamental kernel in scientific computing and deep learning. The emergence of new matrix computation units such as Tensor Cores (TCs) brings more opportunities for SpMM acceleration. However, in order to fully unleash the power of hardware performance, systematic optimization is required. In this paper, we propose Acc-SpMM, a high-performance SpMM library on TCs, with multiple optimizations, including data-affinity-based reordering, memory efficient compressed format, high-throughput pipeline, and adaptive sparsity-aware load balancing. In contrast to the state-of-the-art SpMM kernels on various NVIDIA GPU architectures with a diverse range of benchmark matrices, Acc-SpMM achieves significant performance improvements, on average 2.52x (up to 5.11x) speedup on RTX 4090, on average 1.91x (up to 4.68x) speedup on A800, and on average 1.58x (up to 3.60x) speedup on H100 over cuSPARSE.

</details>

---

> 所属 Session：[Session 8: Tensor Cores](index.md) · 返回 [PPoPP 2025 总览](../index.md)
