---
title: "Uni-Render: A Unified Accelerator for Real-Time Rendering Across Diverse Neural Renderers"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# Uni-Render: A Unified Accelerator for Real-Time Rendering Across Diverse Neural Renderers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Chaojian Li (Georgia Institute of Technology), Sixu Li (Georgia Institute of Technology), Linrui Jiang (Georgia Institute of Technology), Jingqun Zhang (Georgia Institute of Technology), Yingyan (Celine) Lin (Georgia Tech)
**会议**：HPCA 2025

---

## 中文标题

Uni-Render：面向多种神经渲染器的实时渲染统一加速器

## 英文摘要

Recent advancements in neural rendering technologies and their supporting devices have paved the way for immersive 3D experiences, significantly transforming human interaction with intelligent devices across diverse applications. However, achieving the desired real-time rendering speeds for immersive interactions is still hindered by (1) the lack of a universal algorithmic solution for different application scenarios and (2) the dedication of existing devices or accelerators to merely specific rendering pipelines. To overcome this challenge, we have developed a unified neural rendering accelerator that caters to a wide array of typical neural rendering pipelines, enabling real-time and on-device rendering across different applications while maintaining both efficiency and compatibility. Our accelerator design is based on the insight that, although neural rendering pipelines vary and their algorithm designs are continually evolving, they typically share common operators, predominantly executing similar workloads. Building on this insight, we propose a reconfigurable hardware architecture that can dynamically adjust dataflow to align with specific rendering metric requirements for diverse applications, effectively supporting both typical and the latest hybrid rendering pipelines. Benchmarking experiments and ablation studies on both synthetic and real-world scenes demonstrate the effectiveness of the proposed accelerator. It achieves real-time rendering speeds (> 30 FPS) and up to 119× speedups over state-of-the-art neural rendering hardware across varied rendering pipelines, while adhering to power consumption constraints of around 5 W, typical for edge devices. Consequently, the proposed unified accelerator stands out as the first solution capable of achieving real-time neural rendering across varied representative pipelines on edge devices, potentially paving the way for the next generation of neural graphics applications.

## 中文摘要

神经渲染技术及其支撑设备的近期进展为沉浸式 3D 体验铺平了道路，显著改变了人类在各类应用中与智能设备的交互方式。然而，要实现沉浸式交互所需的实时渲染速度，仍受两方面制约：(1) 缺乏适用于不同应用场景的通用算法解决方案；(2) 现有设备或加速器仅专用于特定的渲染流水线。为克服这一挑战，我们设计了一款统一的神经渲染加速器，可服务于多种典型的神经渲染流水线，在不同应用中实现实时且设备端侧的渲染，同时兼顾效率与兼容性。我们的设计基于这样的洞见：尽管神经渲染流水线各不相同且其算法设计持续演进，它们通常共享公共算子，主要执行相似的工作负载。基于此洞见，我们提出一种可重构硬件架构，能够动态调整数据流以匹配不同应用对渲染指标的具体要求，从而有效支持典型以及最新的混合渲染流水线。在合成场景与真实场景上的基准实验与消融实验证明了该加速器的有效性。它实现了实时渲染速度（> 30 FPS），在多种渲染流水线上相比最先进的神经渲染硬件最高可达 119 倍加速，同时满足边缘设备典型的约 5 W 功耗约束。因此，所提出的统一加速器是首个能够在边缘设备上跨多种代表性流水线实现实时神经渲染的方案，有望为下一代神经图形应用铺平道路。
