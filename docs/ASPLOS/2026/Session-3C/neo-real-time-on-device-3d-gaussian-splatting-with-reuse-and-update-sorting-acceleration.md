---
title: "Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration"
description: "ASPLOS 2026 · Session 3C · Neo：基于复用与更新排序加速的实时端侧 3D 高斯泼溅"
tags:
  - "ASPLOS2026"
  - "Session 3C"
  - "3D Gaussian Splatting & Rendering"
---

# Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration

**中文标题：** Neo：基于复用与更新排序加速的实时端侧 3D 高斯泼溅

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Changhun Oh (KAIST), Seongryong Oh (KAIST), Jinwoo Hwang (KAIST), Yoonsung Kim (KAIST), Hardik Sharma (Meta), Jongse Park (KAIST)

**单位：** KAIST；Meta

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790192) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

While 3D Gaussian Splatting (3DGS) has emerged as a promising technique for immersive AR/VR experiences, its practical adoption critically depends on whether real-time rendering can be achieved on resource-constrained devices, such as Meta Ray-Ban Display and Google Android XR Glasses. However, existing solutions struggle to achieve high frame rates, especially for high-resolution rendering. Our analysis identifies the sorting stage in the 3DGS rendering pipeline as the major bottleneck due to its high memory bandwidth demand. This paper presents Neo, which introduces a reuseand-update sorting algorithm that exploits temporal redundancy in Gaussian ordering across consecutive frames and devises a hardware accelerator optimized for this algorithm. By efficiently tracking and updating Gaussian depth ordering instead of re-sorting from scratch, Neo significantly reduces redundant computations and memory bandwidth pressure. Experimental results show that Neo achieves up to 12.4× and 5.5× higher throughput than state-of-the-art edge GPU and ASIC solution, respectively, while reducing DRAM traffic by 94.6% and 81.4%. These improvements make high-quality and low-latency on-device 3D rendering more practical.

## 中文摘要

尽管 3D 高斯泼溅（3DGS）已成为实现沉浸式 AR/VR 体验的一项有前景的技术，但其实际应用在很大程度上取决于能否在资源受限的设备（如 Meta Ray-Ban Display 和 Google Android XR Glasses）上实现实时渲染。然而，现有解决方案难以达到高帧率，尤其是在高分辨率渲染下。我们的分析指出，由于内存带宽需求高，3DGS 渲染流水线中的排序阶段是主要瓶颈。本文提出 Neo，它引入一种复用与更新排序算法，该算法利用连续帧之间高斯排序的时序冗余，并设计了针对该算法优化的硬件加速器。通过高效地跟踪与更新高斯深度顺序，而非从头重新排序，Neo 显著减少了冗余计算与内存带宽压力。实验结果表明，Neo 的吞吐量分别比最先进的边缘 GPU 和 ASIC 方案高出最高 12.4× 和 5.5×，同时将 DRAM 流量降低 94.6% 和 81.4%。这些改进使高质量、低延迟的端侧 3D 渲染更加实用。

## 英文关键词

Domain Specific Architecture (DSA), Accelerator, Neural Rendering, 3D Gaussian Splatting (3DGS)

## 中文关键词

领域专用体系结构（DSA）；加速器；神经渲染；3D 高斯泼溅（3DGS）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790192)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2026](../index.md)
