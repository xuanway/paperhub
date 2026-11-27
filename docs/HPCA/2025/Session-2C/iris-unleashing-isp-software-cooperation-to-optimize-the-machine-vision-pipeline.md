---
title: "IRIS: Unleashing ISP-Software Cooperation to Optimize the Machine Vision Pipeline"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# IRIS: Unleashing ISP-Software Cooperation to Optimize the Machine Vision Pipeline

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Raúl Taranco (Universitat Politècnica de Catalunya), Jose Maria Arnau (Universitat Politècnica de Catalunya), Antonio Gonzalez (Universitat Politecnica de Catalunya)
**会议**：HPCA 2025

---

## 中文标题

IRIS：释放 ISP 与软件协同以优化机器视觉流水线

## 英文摘要

Contemporary Continuous Vision (CV) systems, crucial for robotics, Autonomous Driving (AD), and Extended Reality (XR), have challenging requirements in terms of performance and energy consumption. A standard CV System-on-a-Chip (SoC) pipeline includes an image capture frontend and a backend executing vision algorithms. The frontend typically samples the entire scene at a uniform high resolution (e.g., 4K). However, since not all image regions require this level of detail, this approach over-samples other less detailed areas that could be processed more efficiently at lower resolutions (e.g., 1080p). To address this inefficiency, we introduce IRIS (Image Region ISP-Software Cooperation). Our approach empowers the CV frontend to dynamically adjust the spatial resolution independently for each image region based on its content and backend application requirements. We augment the frontend’s Image Signal Processor (ISP) to adaptively downsample image regions using a Quadtree-like spatial division scheme guided by a low-overhead saliency scorer. The saliency scorer repurposes two valuable byproducts of the ISP—region edge density and perceived motion (optical flow)—that current ISPs already use to enhance image quality but discard afterward. IRIS saves memory bandwidth for image transmission and enables applications to process each image region at the most effective resolution, reducing latency and energy consumption. We validate our approach with both a state-of-the-art CV localization application and a standard Vision Transformer for image classification. IRIS significantly reduces tail latency, average latency, and energy consumption of modern mobile CV systems.

## 中文摘要

当代连续视觉（CV）系统对机器人、自动驾驶（AD）与扩展现实（XR）至关重要，在性能与能耗方面有着严苛要求。标准的 CV 片上系统（SoC）流水线包含图像采集前端与执行视觉算法的后端。前端通常以统一的高分辨率（如 4K）对整个场景采样。然而，并非所有图像区域都需要这种细节程度，这种做法会对其他细节较少的区域过采样，而这些区域本可以更低分辨率（如 1080p）更高效地处理。为消除这种低效，我们提出 IRIS（图像区域 ISP 与软件协同）。该方法使 CV 前端能够根据各图像区域的内容与后端应用需求，独立地动态调整该区域的空间分辨率。我们对前端的图像信号处理器（ISP）进行增强，借助低开销的显著性评分器，采用类四叉树的空间划分方案自适应地对图像区域降采样。显著性评分器复用了 ISP 的两项宝贵副产物——区域边缘密度与感知运动（光流），当前 ISP 已利用它们提升图像质量，但随后便将其丢弃。IRIS 节省了图像传输的内存带宽，并使应用能够以最有效的分辨率处理每个图像区域，从而降低时延与能耗。我们用一个最先进的 CV 定位应用和一个用于图像分类的标准 Vision Transformer 验证了该方法。IRIS 显著降低了现代移动 CV 系统的尾时延、平均时延与能耗。
