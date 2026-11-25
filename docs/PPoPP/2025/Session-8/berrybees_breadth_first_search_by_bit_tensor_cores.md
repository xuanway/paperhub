---
title: "BerryBees: Breadth First Search by Bit-Tensor-Cores"
description: "PPoPP 2025 Session 8（Tensor Cores）：位图 BRS + TCU MMA，较 SOTA 平均最高 5.05×；获两项大奖"
tags:
  - "PPoPP2025"
  - "Session-8"
  - "Tensor Cores"
  - "BFS"
  - "Bit-Tensor-Cores"
  - "Graph Algorithms"
authors:
  - "Yuyao Niu"
  - "Marc Casas"
session: "Session 8: Tensor Cores"
session_number: 8
session_chair: "Jeffrey Vetter"
date: "2025-03-04"
time: "14:40–15:00"
room: "Acacia D"
doi: "10.1145/3710848.3710859"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
award: "Distinguished Paper Award · Best Artifact Award"
---

# BerryBees: Breadth First Search by Bit-Tensor-Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出基于位张量核的代数 BFS 算法 BerryBees，用 Binarized Row Slice 位图格式编码邻接矩阵，并以 warp 级 TCU 算法加速 SpMV 与 SpMSpV。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 8: Tensor Cores</p>
</div>

**作者**：Yuyao Niu, Marc Casas (Barcelona Supercomputing Center (BSC) - Universitat Politècnica de Catalunya (UPC))

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 14:40–15:00 · Session 8: Tensor Cores（主席：Jeffrey Vetter）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710859) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

> 🏆 **Distinguished Paper Award · Best Artifact Award**

---

## 一句话总结

> 提出基于位张量核的代数 BFS 算法 BerryBees，用 Binarized Row Slice 位图格式编码邻接矩阵，并以 warp 级 TCU 算法加速 SpMV 与 SpMSpV。

## 研究问题

现有 BFS 实现（包括方向优化版本）仍存在内存占用高、位图轻量表示利用不足，以及现代 Tensor Core 未被充分利用三大问题。

## 方法简述

- 提出 Binarized Row Slice（BRS）格式，用位图表示非空行段来编码邻接矩阵。
- 设计 warp 级算法，利用 TCU 的 MMA 指令同时加速 SpMV 与 SpMSpV。

## 主要结果

- 在三款最新 NVIDIA GPU 上优于 GAP、Gunrock、Enterprise、GSWITCH、GraphBLAST，平均加速分别为 1.42×、1.97×、5.05×、1.24×、3.74×（最高 9.99×、13.66×、114.07×、13.97×、24.74×）。
- 获 PPoPP 2025 Distinguished Paper Award 与 Best Artifact Award。

<details>
<summary>原文摘要（英文）</summary>

Breadth First Search (BFS) plays a key role in computational science, networking, and artificial intelligence applications. Although the BFS approach has been extensively studied, particularly in its direction-optimized form, existing implementations still present three main issues: (1) high memory footprint; (2) the under-realized lightweight representations using bitmaps; and (3) the underuse of modern hardware such as Tensor Cores Units (TCUs). In this paper, we propose BerryBees, an efficient algebraic BFS algorithm that leverages the Matrix Multiply-Accumulate (MMA) instructions of TCUs. The novelty of BerryBees lies in (1) the Binarized Row Slice (BRS) format, which encodes the adjacency matrix by using bitmaps to represent non-empty row segments; and (2) a warp-level algorithm that leverages TCUs for accelerating both SpMV and SpMSpV operations for enhanced BFS performance. The experimental results on three latest NVIDIA GPUs show that BerryBees outperforms five state-of-the-art BFS methods: GAP, Gunrock, Enterprise, GSWITCH, and GraphBLAST, and delivers average speedups of 1.42 ×, 1.97×, 5.05×, 1.24×, and 3.74× (up to 9.99×, 13.66×, 114.07×, 13.97×, and 24.74×), respectively.

</details>

---

> 所属 Session：[Session 8: Tensor Cores](index.md) · 返回 [PPoPP 2025 总览](../index.md)
