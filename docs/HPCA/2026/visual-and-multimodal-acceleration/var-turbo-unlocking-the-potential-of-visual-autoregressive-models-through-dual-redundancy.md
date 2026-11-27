---
title: "VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models through Dual Redundancy"
description: "HPCA 2026 · Visual and Multimodal Acceleration"
tags:
  - "HPCA2026"
  - "Visual and Multimodal Acceleration"
---

# VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models through Dual Redundancy

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Visual and Multimodal Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Visual and Multimodal Acceleration</p>
</div>

**论文链接**：
**作者**：Xujiang Xiang The Hong Kong University of Science and Technology , Fengbin Tu The Hong Kong University of Science and Technology
**会议**：HPCA 2026

---

## 中文标题

VAR-Turbo：通过双重冗余释放视觉自回归模型的潜力

## 英文摘要

Image synthesis task has recently drawn enormous attention from both the academia and the industry due to the recent advancements of generative models, which now can generate photorealistic images with conditional words from human. Among the generative models for image synthesis task, Visual AutoRegressive (VAR) model is a promising avenue due to its strong scalability. Nevertheless, its exorbitant computational cost poses a formidable obstacle to widespread adoption. To this end, we propose a dedicated software/hardware co-design framework dubbed VAR-Turbo for unlocking the potential of VAR models. Specifically, in the software level, we propose a Draft-Free Parallel Decoding scheme by exploiting the Image Redundancy, which can decrease the sample steps by > 80%, and a combination of Token Aggregation and Dynamic Bypass that capitalizes on the Model Redundancy introduced by the generative Transformer to reduce the computational load by > 60%. In the hardware level, we propose a dedicated accelerator featuring 1) A Unified Attention Core and 2) Radix Sort Core, which can support the aforementioned algorithm pipeline seamlessly and efficiently. Under the collaborative design and synergy of software and hardware, VAR-Turbo achieves averagely 5047.4x, 210.3x, 6.1x, 3.8x speedups and 24818.2x, 423.5x, 6.0x, 7.8x energy-efficiency improvements over Xeon 8168 CPU, Nvidia V100, ViTCoD and AdapTiV, while maintaining the generation quality.

## 中文摘要

近年来，生成模型的进展使图像合成受到学术界与工业界广泛关注，这类模型现已能根据人类给出的条件词生成逼真图像。在图像合成的各类生成模型中，视觉自回归（VAR）模型凭借强大可扩展性成为有前景的路线，但其高昂计算开销成为广泛应用的巨大障碍。为此，我们提出名为 VAR-Turbo 的专用软硬件协同设计框架，以释放 VAR 模型的潜力。软件层面，我们利用图像冗余提出无草稿并行解码方案，可将采样步数减少 80% 以上；并利用生成式 Transformer 带来的模型冗余，结合词元聚合与动态旁路，将计算量降低 60% 以上。硬件层面，我们提出包含统一注意力核心与基数排序核心的专用加速器，可无缝高效支撑上述算法流水线。在软硬件协同下，VAR-Turbo 相比 Xeon 8168 CPU、Nvidia V100、ViTCoD 与 AdapTiV 平均取得 5047.4 倍、210.3 倍、6.1 倍、3.8 倍加速比，以及 24818.2 倍、423.5 倍、6.0 倍、7.8 倍能效提升，同时保持生成质量。
