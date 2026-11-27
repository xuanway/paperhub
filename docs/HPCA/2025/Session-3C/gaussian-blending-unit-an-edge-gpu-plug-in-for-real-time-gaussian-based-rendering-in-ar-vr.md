---
title: "Gaussian Blending Unit: An Edge GPU Plug-in for Real-Time Gaussian-Based Rendering in AR/VR"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# Gaussian Blending Unit: An Edge GPU Plug-in for Real-Time Gaussian-Based Rendering in AR/VR

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Zhifan Ye (Georgia Institute of Technology), Yonggan Fu (Georgia Institute of Technology), Jingqun Zhang (Georgia Institute of Technology), Leshu Li (Georgia Institute of Technology), Yongan Zhang (Georgia Institute of Technology), Sixu Li (Georgia Institute of Technology), Cheng Wan (Georgia Institute of Technology), Chenxi Wan (Georgia Institute of Technology), Chaojian Li (Georgia Institute of Technology), Sreemanth Prathipati (Georgia Institute of Technology), Yingyan (Celine) Lin (Georgia Tech)
**会议**：HPCA 2025

---

## 中文标题

高斯混合单元：面向 AR/VR 实时高斯渲染的边缘 GPU 插件

## 英文摘要

The rapidly advancing field of Augmented and Virtual Reality (AR/VR) demands real-time, photorealistic rendering on resource-constrained platforms. 3D Gaussian Splatting, delivering state-of-the-art (SOTA) performance in rendering efficiency and quality, has emerged as a promising solution across a broad spectrum of AR/VR applications. However, despite its effectiveness on high-end GPUs, it struggles on edge systems like the Jetson Orin NX Edge GPU, achieving only 7-17 FPS—well below the over 60 FPS standard required for truly immersive AR/VR experiences. Addressing this challenge, we perform a comprehensive analysis of Gaussian-based AR/VR applications and identify the Gaussian Blending Stage, which intensively calculates each Gaussian’s contribution at every pixel, as the primary bottleneck. In response, we propose a Gaussian Blending Unit (GBU), an edge GPU plug-in module for real-time rendering in AR/VR applications. Notably, our GBU can be seamlessly integrated into conventional edge GPUs and collaboratively supports a wide range of AR/VR applications. Specifically, GBU incorporates an intra-row sequential shading (IRSS) dataflow that shades each row of pixels sequentially from left to right, utilizing a two-step coordinate transformation. This transformation enables (1) the sharing of intermediate values between adjacent pixels, reducing pixel-wise computation costs by up to 5.5×, and (2) the early identification and skipping of Gaussians that minimally contribute to the pixels, reducing per-pixel computation by up to 93%. When directly deployed on a GPU, the proposed dataflow achieved a non-trivial 1.72× speedup on real-world static scenes, though still falls short of real-time rendering performance. Recognizing the limited compute utilization in the GPU-based implementation, GBU enhances rendering speed with a dedicated rendering engine that balances the workload across rows by aggregating computations from multiple Gaussians. Additionally, GBU integrates a Gaussian Reuse Cache, reducing off-chip memory accesses by 44.9% and resulting in a 1.14× speedup in rendering. Experiments across representative AR/VR applications demonstrate that our GBU provides a unified solution for on-device real-time rendering while maintaining SOTA rendering quality.

## 中文摘要

快速发展的增强现实与虚拟现实（AR/VR）领域要求在资源受限平台上实现实时、照片级真实感渲染。3D 高斯泼溅在渲染效率与质量上达到最先进水平，已成为广泛 AR/VR 应用中颇具前景的方案。然而，尽管其在高性能 GPU 上效果出色，在 Jetson Orin NX 边缘 GPU 等边缘系统上却仅达 7-17 FPS，远低于真正沉浸式 AR/VR 所需的 60 FPS 以上标准。为此我们全面分析了基于高斯的 AR/VR 应用，发现主要瓶颈在于高斯混合阶段——它在每个像素上密集计算每个高斯的贡献。我们提出高斯混合单元（GBU），一种用于 AR/VR 实时渲染的边缘 GPU 插件模块，可无缝集成到常规边缘 GPU 中并协同支持广泛的 AR/VR 应用。GBU 采用行内顺序着色（IRSS）数据流，借助两步坐标变换从左到右依次着色每行像素，使（1）相邻像素可共享中间值，将逐像素计算开销最多降低 5.5×；（2）可提前识别并跳过贡献极小的高斯，将逐像素计算最多减少 93%。直接部署在 GPU 上时，该数据流在真实静态场景中实现 1.72× 的显著加速，但仍未达实时性能。针对 GPU 实现中计算利用率有限的问题，GBU 以专用渲染引擎聚合多个高斯的计算，在行间平衡负载以提升渲染速度；它还集成高斯复用缓存，将片外内存访问减少 44.9%，带来 1.14× 的渲染加速。在代表性 AR/VR 应用上的实验表明，GBU 在保持最先进渲染质量的同时为端侧实时渲染提供了统一方案。
