---
title: "GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering"
description: "HPCA 2026 · 3D Graphics and Rendering Acceleration"
tags:
  - "HPCA2026"
  - "3D Graphics and Rendering Acceleration"
---

# GRTX: Efficient Ray Tracing for 3D Gaussian-Based Rendering

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: 3D Graphics and Rendering Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 3D Graphics and Rendering Acceleration</p>
</div>

**论文链接**：
**作者**：Junseo Lee Seoul National University , Sangyun Jeon Seoul National University , Jungi Lee Seoul National University , Junyong Park Seoul National University , Jaewoong Sim Seoul National University
**会议**：HPCA 2026

---

## 中文标题

GRTX：面向基于 3D 高斯渲染的高效光线追踪

## 英文摘要

3D Gaussian Splatting has gained widespread adoption across diverse applications due to its exceptional rendering performance and visual quality. While most existing methods rely on rasterization to render Gaussians, recent research has started investigating ray tracing approaches to overcome the fundamental limitations inherent in rasterization. However, current Gaussian ray tracing methods suffer from inefficiencies such as bloated acceleration structures and redundant node traversals, which greatly degrade ray tracing performance. In this work, we present GRTX, a set of software and hardware optimizations that enable efficient ray tracing for 3D Gaussian-based rendering. First, we introduce a novel approach for constructing streamlined acceleration structures for Gaussian primitives. Our key insight is that anisotropic Gaussians can be treated as unit spheres through ray space transformations, which substantially reduces BVH size and traversal overhead. Second, we propose dedicated hardware support for traversal checkpointing within ray tracing units. This eliminates redundant node visits during multi-round tracing by resuming traversal from checkpointed nodes rather than restarting from the root node in each subsequent round. Our evaluation shows that GRTX significantly improves ray tracing performance compared to the baseline ray tracing method with a negligible hardware cost.

## 中文摘要

3D 高斯泼溅凭借优异的渲染性能与视觉质量，已在多种应用中得到广泛采用。现有方法大多依赖光栅化来渲染高斯，近期研究则开始探索光线追踪方法，以突破光栅化固有的根本性局限。然而，当前的高斯光线追踪方法存在加速结构臃肿、节点遍历冗余等低效问题，严重削弱了光线追踪性能。本文提出 GRTX——一套使 3D 高斯渲染的光线追踪得以高效执行的软硬件优化方案。首先，我们提出一种为高斯基元构建精简加速结构的新方法。其核心洞见在于：借助光线空间变换，可将各向异性高斯视为单位球，从而大幅缩减 BVH 规模与遍历开销。其次，我们提出光线追踪单元内遍历检查点（traversal checkpointing）的专用硬件支持。该方法在多轮追踪中从检查点节点恢复遍历，而非在后续每一轮都从根节点重新开始，从而消除冗余的节点访问。评估表明，相较于基线光线追踪方法，GRTX 以可忽略的硬件开销显著提升了光线追踪性能。
