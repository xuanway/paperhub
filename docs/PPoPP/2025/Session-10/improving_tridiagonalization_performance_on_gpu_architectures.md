---
title: "Improving Tridiagonalization Performance on GPU Architectures"
description: "PPoPP 2025 Session 10（GPU II）：双重分块 band reduction + GPU bulge chasing，最高 19.6 TFLOPs"
tags:
  - "PPoPP2025"
  - "Session-10"
  - "GPU II"
  - "Tridiagonalization"
  - "Eigenvalue Decomposition"
  - "GPU"
authors:
  - "Hansheng Wang"
  - "Zhekai Duan"
  - "Zitian Zhao"
  - "Siqi Wu"
  - "Saiqi Zheng"
  - "Qiao Li"
  - "Xu Jiang"
  - "Shaoshuai Zhang"
session: "Session 10: GPU II"
session_number: 10
session_chair: "Zhijia Zhao"
date: "2025-03-05"
time: "11:00–11:20"
room: "Acacia D"
doi: "10.1145/3710848.3710894"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Improving Tridiagonalization Performance on GPU Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出新的双重分块 band reduction 算法与 GPU 上的 bulge chasing 实现，大幅提升对称特征值分解中 FP64 三对角化的性能。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 10: GPU II</p>
</div>

**作者**：Hansheng Wang (University of Electronic Science and Technology of China); Zhekai Duan (University of Edinburgh); Zitian Zhao, Siqi Wu (University of Electronic Science and Technology of China); Saiqi Zheng (Xi’an Jiaotong-Liverpool University); Qiao Li, Xu Jiang, Shaoshuai Zhang (University of Electronic Science and Technology of China)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 11:00–11:20 · Session 10: GPU II（主席：Zhijia Zhao）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710894) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出新的双重分块 band reduction 算法与 GPU 上的 bulge chasing 实现，大幅提升对称特征值分解中 FP64 三对角化的性能。

## 研究问题

在 cuSOLVER 中，FP64 三对角化在 H100 上仅达到 2.1 TFLOPs（峰值 67 TFLOPs），却占整个 EVD 过程 97% 以上的时间。

## 方法简述

- 系统分析三对角化在 GPU 架构上性能次优的原因。
- 提出新的 double blocking band reduction 算法，并实现 GPU-based bulge chasing。

## 主要结果

- FP64 三对角化最高达到 19.6 TFLOPs。
- 相比 cuSOLVER 快 9.3×，相比 MAGMA 快 5.2×。

<details>
<summary>原文摘要（英文）</summary>

Tridiagonalization, which is a key step in symmetric eigenvalue decomposition (EVD), aims to convert a symmetric matrix to a tridiagonal form. In Nvidia’s cuSOLVER library, the FP64 precision tridiagonalization process only reach 2.1 TFLOPs out of 67 TFLOPs on H100 GPU, and it consumes a significant portion of the elapsed time in the entire EVD process, accounting for over 97%. Thus, improving the tridiagonalization performance is crucial on accelerating EVD. In this paper, we analyze the reasons behind the suboptimal performance of tridiagonalization on GPU architectures, and we propose a new double blocking band reduction algorithm along with an implementation of GPU-based bulge chasing to improve the tridiagonalization performance. Through experimental evaluation, the proposed FP64 precision tridiagonalization method yields up to 19.6 TFLOPs which is 9.3x and 5.2x faster compared cuSOVLER and MAGMA, respectively.

</details>

---

> 所属 Session：[Session 10: GPU II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
