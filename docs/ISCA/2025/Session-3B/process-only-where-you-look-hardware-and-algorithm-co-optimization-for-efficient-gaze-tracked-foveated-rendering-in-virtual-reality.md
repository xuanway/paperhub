---
title: "Process Only Where You Look: Hardware and Algorithm Co-optimization for Efficient Gaze-Tracked Foveated Rendering in Virtual Reality"
description: "ISCA 2025 · Session 3B · 只处理注视区域：面向虚拟现实高效眼动追踪注视点渲染的软硬件协同优化"
tags:
  - "ISCA2025"
  - "Session 3B"
  - "Domain Specific Accelerators I"
---

# Process Only Where You Look: Hardware and Algorithm Co-optimization for Efficient Gaze-Tracked Foveated Rendering in Virtual Reality

**中文标题：** 只处理注视区域：面向虚拟现实高效眼动追踪注视点渲染的软硬件协同优化

**所属 Session：** [Session 3B](index.md) · [ISCA 2025](../index.md)

**作者：** Haiyu Wang, Wenxuan Liu, Kenny Chen, Qi Sun, Sai Qian Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731110) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Virtual reality (VR) plays a crucial role in advancing immersive, in-

teractive experiences that transform learning, work, and entertain-

ment by enhancing user engagement and expanding possibilities

across various fields. Image rendering is one of the most crucial ap-

plication in VR, as it produces high-quality, realistic visuals that are

vital for maintaining immersive user experiences and preventing

visual discomfort or motion sickness. However, the cost of image

rendering in VR environment is considerable, primarily due to the

demands of high-quality visual experiences from users. This chal-

lenge is even greater in real-time applications, where maintaining

low latency further increases the complexity of the rendering pro-

cess. On the other hand, VR devices, such as head-mounted displays

(HMDs), are intrinsically linked to human behavior, using insights

from perception and cognition to enhance user experience.

In this work, we aim to reduce the high computational costs of

the rendering process in VR by leveraging natural human eye dy-

namics and focusing on processing only where you look (POLO). This

involves co-optimizing AI algorithms with underlying hardware

for greater efficiency. We introduce POLONet, an efficient multitask

deep learning framework designed to track human eye movements

with minimal latency. Integrated with the POLO accelerator as a

plug-in for VR HMD SoCs, this approach significantly lowers image

rendering costs, achieving up to a 3.9×reduction in end-to-end

latency compared to the latest gaze tracking methods.

## 中文摘要

虚拟现实 (VR) 在推进沉浸式互动体验方面发挥着至关重要的作用，通过增强用户参与度和扩展各个领域的可能性来改变学习、工作和娱乐。图像渲染是 VR 中最重要的应用之一，因为它可以产生高质量、逼真的视觉效果，这对于维持沉浸式用户体验和防止视觉不适或晕动病至关重要。然而，VR环境下的图像渲染成本相当高，这主要是由于用户对高质量视觉体验的需求。在实时应用程序中，这一挑战甚至更大，其中保持低延迟进一步增加了渲染过程的复杂性。另一方面，头戴式显示器 (HMD) 等 VR 设备与人类行为有着内在的联系，利用感知和认知的洞察来增强用户体验。

在这项工作中，我们的目标是通过利用自然的人眼动力学并专注于仅在您看到的地方进行处理（POLO）来降低 VR 渲染过程的高计算成本。这涉及到人工智能算法与底层硬件的共同优化，以提高效率。我们推出 POLONet，这是一种高效的多任务深度学习框架，旨在以最小的延迟跟踪人眼运动。这种方法与 POLO 加速器集成作为 VR HMD SoC 的插件，可显著降低图像渲染成本，与最新的视线跟踪方法相比，端到端延迟最多可减少 3.9 倍。

## 英文关键词

Foveated Rendering, Gaze Tracking, Saccade Detection, Hardware Accelerator, Virtual Reality

## 中文关键词

焦点渲染, 眼动追踪, 扫视检测, 硬件加速器, 虚拟现实

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731110)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2025](../index.md)
