---
title: "VR-Pipe: Streamlining Hardware Graphics Pipeline for Volume Rendering"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# VR-Pipe: Streamlining Hardware Graphics Pipeline for Volume Rendering

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Junseo Lee (Seoul National University), Jaisung Kim (Seoul National University), Junyong Park (Seoul National University), Jaewoong Sim (Seoul National University)
**会议**：HPCA 2025

---

## 中文标题

VR-Pipe：精简面向体渲染的硬件图形流水线

## 英文摘要

Graphics rendering that builds on machine learning and radiance fields is gaining significant attention due to its outstanding quality and speed in generating photorealistic images from novel viewpoints. However, prior work has primarily focused on evaluating its performance through software-based rendering on programmable shader cores, leaving its performance when exploiting fixed-function graphics units largely unexplored. In this paper, we investigate the performance implications of performing radiance field rendering on the hardware graphics pipeline. In doing so, we implement the state-of-the-art radiance field method, 3D Gaussian splatting, using graphics APIs and evaluate it across synthetic and real-world scenes on today’s graphics hardware. Based on our analysis, we present VR-Pipe, which seamlessly integrates two innovations into graphics hardware to streamline the hardware pipeline for volume rendering, such as radiance field methods. First, we introduce native hardware support for early termination by repurposing existing special-purpose hardware in modern GPUs. Second, we propose multi-granular tile binning with quad merging, which opportunistically blends fragments in shader cores before passing them to fixed-function blending units. Our evaluation shows that VR-Pipe greatly improves rendering performance, achieving up to a 2.78× speedup over the conventional graphics pipeline with negligible hardware overhead.

## 中文摘要

基于机器学习与辐射场的图形渲染因其在从新视角生成逼真图像方面出色的质量与速度而备受关注。然而，先前工作主要通过在可编程着色器核心上的软件渲染来评估其性能，对利用固定功能图形单元时的性能则基本未做探索。本文研究了在硬件图形流水线上执行辐射场渲染的性能影响。为此，我们使用图形 API 实现了最先进的辐射场方法 3D 高斯泼溅，并在当今的图形硬件上跨合成与真实场景对其进行评估。基于分析，我们提出 VR-Pipe，将两项创新无缝集成到图形硬件中，以精简面向体渲染（如辐射场方法）的硬件流水线。首先，我们通过改造现代 GPU 中已有的专用硬件，为提前终止引入原生硬件支持。其次，我们提出带四边形合并的多粒度分块（tile binning），在着色器核心中择机合并片元，再将其送往固定功能混合单元。评估表明，VR-Pipe 大幅提升了渲染性能，相比传统图形流水线最高实现 2.78 倍加速，且硬件开销可忽略。
