---
title: "MetaSapiens: Real-Time Neural Rendering with Efficiency-Aware Pruning and Accelerated Foveated Rendering"
description: "ASPLOS 2025 · Session 3B · MetaSapiens：基于效率感知剪枝与加速注视点渲染的实时神经渲染"
tags:
  - "ASPLOS2025"
  - "Session 3B"
  - "Graphics"
---

# MetaSapiens: Real-Time Neural Rendering with Efficiency-Aware Pruning and Accelerated Foveated Rendering

**中文标题：** MetaSapiens：基于效率感知剪枝与加速注视点渲染的实时神经渲染

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Weikai Lin (University of Rochester), Yu Feng (Shanghai Jiao Tong University), Yuhao Zhu (University of Rochester)

**单位：** University of Rochester；Shanghai Jiao Tong University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707227) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Point-Based Neural Rendering (PBNR) is emerging as a promising class of rendering techniques, which are permeating all aspects of society, driven by a growing demand for real-time, photorealistic rendering in AR/VR and digital twins. Achieving real-time PBNR on mobile devices is challenging. This paper proposes MetaSapiens, a PBNR system that for the first time delivers real-time neural rendering on mobile devices while maintaining human visual quality. MetaSapiens combines three techniques. First, we present an efficiencyaware pruning technique to optimize rendering speed. Second, we introduce a Foveated Rendering (FR) method for PBNR, leveraging humans' low visual acuity in peripheral regions to relax rendering quality and improve rendering speed. Finally, we propose an accelerator design for FR, addressing the load imbalance issue in (FR-based) PBNR. Our evaluation shows that our system achieves an order of magnitude speedup over existing PBNR models without sacrificing subjective visual quality, as confirmed by a user study. The code and demo are

## 中文摘要

基于点的神经渲染（Point-Based Neural Rendering，PBNR）正在成为一类颇具前景的渲染技术；在 AR/VR 与数字孪生对实时、照片级真实感渲染需求日益增长的驱动下，它正渗透到社会的各个方面。在移动设备上实现实时 PBNR 颇具挑战。本文提出 MetaSapiens，这是一个首次在移动设备上实现实时神经渲染、同时保持人类视觉质量的 PBNR 系统。MetaSapiens 结合了三项技术。第一，我们提出一种效率感知的剪枝技术以优化渲染速度。第二，我们为 PBNR 引入一种注视点渲染（Foveated Rendering，FR）方法，利用人类在周边区域较低的视觉锐度来放宽渲染质量并提升渲染速度。最后，我们提出面向 FR 的加速器设计，解决（基于 FR 的）PBNR 中的负载不均衡问题。我们的评估表明，该系统相较于现有 PBNR 模型取得了数量级的加速，且未牺牲主观视觉质量，这一点已由用户研究证实。代码与演示见

## 英文关键词

Gaussian Splatting, Foveated Rendering, Hardware Accelerator

## 中文关键词

高斯泼溅；注视点渲染；硬件加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707227)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2025](../index.md)
