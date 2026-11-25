---
title: "TurboFFT: Co-Designed High-Performance and Fault-Tolerant Fast Fourier Transform on GPUs"
description: "PPoPP 2025 Session 2（GPU I）：架构感知 FFT 模板 + 两级 ABFT，容错开销仅 7%–15%"
tags:
  - "PPoPP2025"
  - "Session-2"
  - "GPU I"
  - "FFT"
  - "Fault Tolerance"
  - "ABFT"
authors:
  - "Shixun Wu"
  - "Yujia Zhai"
  - "Jinyang Liu"
  - "Jiajun Huang"
  - "Zizhe Jian"
  - "Huangliang Dai"
  - "Sheng Di"
  - "Franck Cappello"
  - "Zizhong Chen"
session: "Session 2: GPU I"
session_number: 2
session_chair: "Xipeng Shen"
date: "2025-03-03"
time: "12:00–12:20"
room: "Acacia D"
doi: "10.1145/3710848.3710853"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# TurboFFT: Co-Designed High-Performance and Fault-Tolerant Fast Fourier Transform on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 TurboFFT，一个兼顾高性能与在线容错的 GPU FFT 原型：以架构感知的模板化实现逼近 cuFFT，并用线程/线程块两级 ABFT 实现在线纠错。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 2: GPU I</p>
</div>

**作者**：Shixun Wu, Yujia Zhai (University of California, Riverside); Jinyang Liu (University of Houston); Jiajun Huang, Zizhe Jian, Huangliang Dai (University of California, Riverside); Sheng Di, Franck Cappello (Argonne National Laboratory); Zizhong Chen (University of California, Riverside)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 12:00–12:20 · Session 2: GPU I（主席：Xipeng Shen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710853) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 TurboFFT，一个兼顾高性能与在线容错的 GPU FFT 原型：以架构感知的模板化实现逼近 cuFFT，并用线程/线程块两级 ABFT 实现在线纠错。

## 研究问题

现有 GPU FFT 库效率仍有提升空间，且普遍缺乏针对软错误的容错机制，难以满足大规模科学计算对可靠性的要求。

## 方法简述

- 设计架构感知、无 padding 的模板化 FFT 实现，最大化硬件资源利用率。
- 在线程与线程块两级应用 ABFT 以减少额外内存，并用带位置编码的双侧 ABFT 抑制错误传播。
- 把线程块级 FFT 从单事务改为多事务，为 ABFT 提供更多并行度并摊薄归约开销。

## 主要结果

- 无容错版本与 cuFFT 相当或最高快 300%，并优于 VkFFT。
- 开启容错后额外开销仅 7%–15%，在每分钟数十次错误注入下仍能在线纠正。

<details>
<summary>原文摘要（英文）</summary>

GPU-based fast Fourier transform (FFT) is extremely important for scientific computing and signal processing. However, we find the inefficiency of existing FFT libraries and the absence of fault tolerance against soft error. To address these issues, we introduce TurboFFT, a new FFT prototype co-designed for high performance and online fault tolerance. For FFT, we propose an architecture-aware, padding-free, and template-based prototype to maximize hardware resource utilization, achieving a competitive or superior performance compared to the state-of-the-art closed-source library, cuFFT. For fault tolerance, we 1) explore algorithm-based fault tolerance (ABFT) at the thread and threadblock levels to reduce additional memory footprint, 2) address the error propagation by introducing a two-side ABFT with location encoding, and 3) further modify the threadblock-level FFT from 1-transaction to multi-transaction in order to bring more parallelism for ABFT. Our two-side strategy enables online correction without additional global memory while our multi-transaction design averages the expensive threadblock-level reduction in ABFT with zero additional operations. Experimental results on an NVIDIA A100 server GPU and a Tesla Turing T4 GPU demonstrate that TurboFFT without fault tolerance is comparable to or up to 300% faster than cuFFT and outperforms VkFFT. TurboFFT with fault This work is licensed under tolerance maintains an overhead of 7% to 15%, even under tens of error injections per minute for both FP32 and FP64.

</details>

---

> 所属 Session：[Session 2: GPU I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
