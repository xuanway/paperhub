---
title: "Segment Only Where You Look: Leveraging Human Gaze Behavior for Efficient Computer Vision Applications in Augmented Reality"
description: "ASPLOS 2026 · Session 5A · 只在你注视之处分割：利用人类注视行为实现增强现实中高效的计算机视觉应用"
tags:
  - "ASPLOS2026"
  - "Session 5A"
  - "Generative Model Serving"
---

# Segment Only Where You Look: Leveraging Human Gaze Behavior for Efficient Computer Vision Applications in Augmented Reality

**中文标题：** 只在你注视之处分割：利用人类注视行为实现增强现实中高效的计算机视觉应用

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tianhua Xia (New York University), Haiyu Wang (New York University), Sai Qian Zhang (New York University)

**单位：** New York University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790216) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Augmented reality (AR) comprises groundbreaking technologies that are reshaping the landscape of human interaction. Image segmentation, which divides a user front-scene frame into more manageable parts for analysis, is of paramount importance since this technique enables AR systems to extract digital information precisely from the real world by identifying and isolating specific objects in the user's surroundings. Despite its importance, the segmentation task imposes substantial computational demands and processing delays on AR devices, significantly degrading the user experience. In this work, we aim to reduce the high computational costs of the segmentation task in AR by leveraging natural human eye dynamics and focusing on segmenting only where you look (SOLO). This involves co-optimizing image segmentation algorithms with underlying hardware for greater efficiency. We introduce SOLO algorithm, an efficient deep learning framework that takes high-resolution input images and user eye images to effectively segment only the instance of interest. Integrated with the saliency-based sensing (SBS) and SOLO accelerator as a plug-in for SoCs of the AR device, SOLO significantly lowers the computational costs for image segmentation, achieving up to a 12× reduction in end-to-end latency compared to other baselines.

## 中文摘要

增强现实（AR）包含正在重塑人类交互格局的突破性技术。图像分割将用户前视场景帧划分为更易管理的部分以进行分析，该技术具有至关重要的意义，因为它使 AR 系统能够通过识别并分离用户周围环境中的特定对象，从现实世界中精确地提取数字信息。尽管其重要性显著，分割任务仍给 AR 设备带来了巨大的计算需求和处理延迟，显著降低了用户体验。在本工作中，我们的目标是通过利用人类自然的眼动动态、聚焦于只在注视之处进行分割（SOLO），来降低 AR 中分割任务的高计算成本。这涉及将图像分割算法与底层硬件进行协同优化以获得更高的效率。我们提出 SOLO 算法，这是一个高效的深度学习框架，它接收高分辨率输入图像和用户眼部图像，从而有效地仅分割感兴趣的实例。通过与基于显著性的感知（SBS）以及作为 AR 设备 SoC 插件的 SOLO 加速器相结合，SOLO 显著降低了图像分割的计算成本，相比其他基线实现了高达 12× 的端到端延迟降低。

## 英文关键词

Computer Vision; Video Segmentation; Gaze Tracking; Saccade Detection; Hardware Accelerator; Augmented Reality

## 中文关键词

计算机视觉；视频分割；注视追踪；眼跳检测；硬件加速器；增强现实

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790216)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2026](../index.md)
