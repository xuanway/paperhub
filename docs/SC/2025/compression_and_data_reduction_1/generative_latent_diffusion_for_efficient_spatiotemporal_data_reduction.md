---
title: "Generative Latent Diffusion for Efficient Spatiotemporal Data Reduction"
description: "SC 2025 · Compression and Data Reduction 1 · Xiao Li; Liangji Zhu; Anand Rangarajan; Sanjay Ranka"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# Generative Latent Diffusion for Efficient Spatiotemporal Data Reduction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Xiao Li; Liangji Zhu; Anand Rangarajan; Sanjay Ranka

**会议**：SC 2025 · St. Louis, MO

## 摘要

Generative models have demonstrated strong performance in conditional settings and can be viewed as a form of data compression, where the condition serves as a compact representation. However, their limited controllability and reconstruction accuracy restrict their practical application to data compression. In this work, we propose an efficient latent diffusion framework that bridges this gap by combining a variational autoencoder with a conditional diffusion model. Our method compresses a small number of keyframes into latent space and uses them as conditioning inputs to reconstruct the remaining frames via generative interpolation, eliminating the need to store latent representations for every frame. This approach enables accurate spatiotemporal reconstruction while significantly reducing storage costs. Experimental results across multiple datasets show that our method achieves up to 10× higher compression ratios than rule-based state-of-the-art compressors such as SZ3, and up to 63%

---

## 一句话总结

> 该工作属于 Compression and Data Reduction 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Compression and Data Reduction 1 领域贡献新的设计范式或评估框架。
