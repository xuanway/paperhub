---
title: "FlashFFTStencil: Bridging Fast Fourier Transforms to Memory-Efficient Stencil Computations on Tensor Core Units"
description: "PPoPP 2025 Session 8（Tensor Cores）：HBM/SMEM/TCU 三层优化，平均加速 2.57×"
tags:
  - "PPoPP2025"
  - "Session-8"
  - "Tensor Cores"
  - "Stencil Computation"
  - "FFT"
authors:
  - "Haozhi Han"
  - "Kun Li"
  - "Wei Cui"
  - "Donglin Bai"
  - "Yiwei Zhang"
  - "Liang Yuan"
  - "Yifeng Chen"
  - "Yunquan Zhang"
  - "Ting Cao"
  - "Mao Yang"
session: "Session 8: Tensor Cores"
session_number: 8
session_chair: "Jeffrey Vetter"
date: "2025-03-04"
time: "15:00–15:20"
room: "Acacia D"
doi: "10.1145/3710848.3710897"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# FlashFFTStencil: Bridging Fast Fourier Transforms to Memory-Efficient Stencil Computations on Tensor Core Units

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FlashFFTStencil，把 FFT 与全稠密 stencil 计算桥接到 Tensor Core，通过 HBM、SMEM 与 TCU 三个层次的协同优化实现无稀疏化的 bound shifting。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 8: Tensor Cores</p>
</div>

**作者**：Haozhi Han (Peking University); Kun Li, Wei Cui, Donglin Bai (Microsoft Research); Yiwei Zhang (University of Chinese Academy of Sciences); Liang Yuan (Chinese Academy of Sciences); Yifeng Chen (Peking University); Yunquan Zhang (Chinese Academy of Sciences); Ting Cao, Mao Yang (Microsoft Research)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 15:00–15:20 · Session 8: Tensor Cores（主席：Jeffrey Vetter）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710897) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 FlashFFTStencil，把 FFT 与全稠密 stencil 计算桥接到 Tensor Core，通过 HBM、SMEM 与 TCU 三个层次的协同优化实现无稀疏化的 bound shifting。

## 研究问题

Tensor Core 在 AI 任务中表现优异，但用于 stencil 等 HPC 算法时受稀疏性拖累导致利用率低，并进一步放大内存受限问题。

## 方法简述

- Kernel Tailoring on HBM：融合不同 kernel，提高并行度并减少数据传输与内存占用。
- Architecture Aligning on SMEM：把基于 FFT 的 stencil 计算重构为适配共享内存架构的稠密矩阵乘。
- Computation Streamlining on TCU：减少流水停顿、最大化寄存器复用，提升 TCU 利用率与线程并行度。

## 主要结果

- 实现有效的无稀疏 bound shifting，相比 SOTA 平均加速 2.57×。
- 借助 FFT 支持理论上无限制的时间维融合（temporal fusion）。

<details>
<summary>原文摘要（英文）</summary>

While Tensor Core Units (TCUs) excel in AI tasks, their application to HPC algorithms like stencil computations faces significant challenges due to sparsity, which leads to underutilization and exacerbates memory-bound limitations. This paper introduces FlashFFTStencil1, a memory-efficient stencil computing system designed to bridge FFT to fully-dense stencil computations on TCUs. Aimed at bound shifting, FlashFFTStencil comprises three key techniques: Kernel Tailoring on HBM fuses distinct kernels to enhance parallelism while reducing memory transfer and footprint; Architecture Aligning on SMEM restructures FFT-based stencil computations into dense matrix multiplications tailored for shared memory architecture; Computation Streamlining on TCU optimizes TCU utilization and thread parallelism by minimizing pipeline stalls and maximizing register reuse. Notably, a distinctive extension is FlashFFTStencil’s ability to enable theoretically unrestricted temporal fusion by FFT. Results show that FlashFFTStencil achieves effective sparsity-free bound shifting, with an average speedup of 2.57x over the state-of-the-art. FlashFFTStencil pioneers a new era in unifying computational patterns within the HPC landscape and bridges them with cutting-edge AI-driven hardware innovations like TCUs.

</details>

---

> 所属 Session：[Session 8: Tensor Cores](index.md) · 返回 [PPoPP 2025 总览](../index.md)
