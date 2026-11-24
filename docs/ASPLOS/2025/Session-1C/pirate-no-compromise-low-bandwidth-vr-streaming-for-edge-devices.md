---
title: "Pirate: No Compromise Low-Bandwidth VR Streaming for Edge Devices"
description: "ASPLOS 2025 · Session 1C · Pirate：面向边缘设备的无妥协低带宽 VR 流式传输"
tags:
  - "ASPLOS2025"
  - "Session 1C"
  - "Edge Computing"
---

# Pirate: No Compromise Low-Bandwidth VR Streaming for Edge Devices

**中文标题：** Pirate：面向边缘设备的无妥协低带宽 VR 流式传输

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yingtian Zhang (The Pennsylvania State University), Yan Kang (The Pennsylvania State University), Ziyu Ying (The Pennsylvania State University), Wanhang Lu (The Pennsylvania State University), Sijie Lan (The Pennsylvania State University), Huijuan Xu (The Pennsylvania State University), Kiwan Maeng (The Pennsylvania State University), Anand Sivasubramaniam (The Pennsylvania State University), Mahmut T. Kandemir (The Pennsylvania State University), Chita R. Das (The Pennsylvania State University)

**单位：** The Pennsylvania State University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716268) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Due to the limited compute power and storage capabilities of edge platforms, “streaming” often provides a better VR experience compared to “rendering”. Yet, achieving high-quality VR streaming faces two significant challenges, namely, bandwidth limitations and the need for real-time operation with high frames per second (FPS). Previous efforts have tended to prioritize either conserving bandwidth without real-time performance or ensuring real-time operation without substantial bandwidth savings. In this work, we incorporate the concept of “stereo similarity” to develop a novel real-time stereo video compression framework for streaming, called Pirate. Unlike the previously proposed approaches that rely on large machine learning-based models for synthesizing stereo pairs from both eyes with disparity maps (which can be impractical for most edge platforms due to their high computational cost), Pirate iteratively synthesizes the target eye view using only a single eye view and its corresponding disparity and optical flow information, with alternating left or right eye transmission. This enables us to generate target view at an extremely low computational cost, even under bandwidth constraints as low as 0.1 bits per pixel (bpp), while maintaining a high frame rate of 90 FPS. Our evaluations also reveal that, the proposed approach not only achieves realtime VR streaming with a 20%-40% reduction in bandwidth usage, but also maintains similar superior quality standards.

## 中文摘要

由于边缘平台的计算能力与存储能力有限，与“渲染”相比，“流式传输”往往能提供更好的 VR 体验。然而，实现高质量的 VR 流式传输面临两大挑战，即带宽限制以及需要以高帧率（FPS）实时运行。已有工作往往偏向其一：要么在牺牲实时性的情况下节省带宽，要么在未显著节省带宽的情况下保证实时运行。在本工作中，我们引入“立体相似性”（stereo similarity）概念，开发了一种用于流式传输的新型实时立体视频压缩框架 Pirate。与以往依赖大型机器学习模型、借助视差图从双眼合成立体图像对的做法（其高计算开销对大多数边缘平台并不现实）不同，Pirate 仅使用单眼视图及其对应的视差与光流信息，并交替传输左眼或右眼，从而迭代地合成目标眼视图。这使我们能够以极低计算开销生成目标视图，即使在低至 0.1 比特每像素（bpp）的带宽约束下，仍能保持 90 FPS 的高帧率。我们的评估还表明，所提方法不仅实现了实时 VR 流式传输并将带宽占用降低 20%–40%，而且保持了同等出色的质量水准。

## 英文关键词

Virtual Reality, Edge Computing, Game Streaming

## 中文关键词

虚拟现实；边缘计算；游戏流式传输

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716268)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2025](../index.md)
