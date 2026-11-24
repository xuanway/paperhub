---
title: "Generative Latent Diffusion for Efficient Spatiotemporal Data Reduction"
description: "SC 2025 · Compression and Data Reduction 1 · Xiao Li; Liangji Zhu; Anand Rangarajan; Sanjay Ranka"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# Generative Latent Diffusion for Efficient Spatiotemporal Data Reduction

**中文标题：** 利用生成式潜在扩散实现高效时空数据约简

**所属 Session：** [Compression and Data Reduction 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Xiao Li; Liangji Zhu; Anand Rangarajan; Sanjay Ranka

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap517&sess=sess162)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Generative models have demonstrated strong performance in conditional settings and can be viewed as a form of data compression, where the condition serves as a compact representation. However, their limited controllability and reconstruction accuracy restrict their practical application to data compression. In this work, we propose an efficient latent diffusion framework that bridges this gap by combining a variational autoencoder with a conditional diffusion model. Our method compresses a small number of keyframes into latent space and uses them as conditioning inputs to reconstruct the remaining frames via generative interpolation, eliminating the need to store latent representations for every frame. This approach enables accurate spatiotemporal reconstruction while significantly reducing storage costs. Experimental results across multiple datasets show that our method achieves up to 10× higher compression ratios than rule-based state-of-the-art compressors such as SZ3, and up to 63%

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
