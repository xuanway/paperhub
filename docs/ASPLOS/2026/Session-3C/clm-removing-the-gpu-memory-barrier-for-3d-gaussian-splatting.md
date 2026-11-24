---
title: "CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting"
description: "ASPLOS 2026 · Session 3C · CLM：消除 3D 高斯泼溅的 GPU 内存壁垒"
tags:
  - "ASPLOS2026"
  - "Session 3C"
  - "3D Gaussian Splatting & Rendering"
---

# CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting

**中文标题：** CLM：消除 3D 高斯泼溅的 GPU 内存壁垒

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hexu Zhao (NYU), Xiwen Min (NYU), Xiaoteng Liu (NYU), Moonjun Gong (NYU), Yiming Li (NYU), Ang Li (PNNL and UW), Saining Xie (NYU), Jinyang Li (NYU), Aurojit Panda (NYU)

**单位：** NYU；PNNL and UW

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790140) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

3D Gaussian Splatting (3DGS) is an increasingly popular novel view synthesis approach due to its fast rendering time, and high-quality output. However, scaling 3DGS to large (or intricate) scenes is challenging due to its substantial memory requirement, which exceeds the memory capacity of most GPUs. In this paper, we describe CLM, a system that allows 3DGS to render large scenes using a single consumer-grade GPU, e.g., RTX4090. It does so by offloading Gaussians to CPU memory, and loading them into GPU memory only when necessary. To improve performance and reduce communication overheads, CLM uses a novel offloading strategy based on insights into 3DGS's memory access patterns. This strategy enables efficient pipelining, which overlaps GPU-to-CPU communication, GPU computation and CPU computation. Furthermore, CLM exploits these access patterns to reduce communication volume. Our evaluation shows that the resulting implementation can render a large scene that requires 102 million Gaussians on a single RTX4090 and achieve state-of-the-art reconstruction quality.

## 中文摘要

3D 高斯泼溅（3DGS）因其渲染时间快、输出质量高，正成为一种日益流行的新视角合成方法。然而，由于 3DGS 的内存需求很大且超出大多数 GPU 的内存容量，将其扩展到大型（或复杂）场景仍具有挑战性。在本文中，我们介绍 CLM，一个使 3DGS 能够使用单块消费级 GPU（例如 RTX4090）渲染大型场景的系统。它通过将高斯卸载到 CPU 内存，并仅在必要时将其加载到 GPU 内存来实现这一点。为了提升性能并降低通信开销，CLM 采用了一种基于对 3DGS 内存访问模式洞察的新型卸载策略。该策略实现了高效的流水线化，将 GPU 到 CPU 的通信、GPU 计算与 CPU 计算相互重叠。此外，CLM 利用这些访问模式来降低通信量。我们的评估表明，由此得到的实现可以在单块 RTX4090 上渲染需要 1.02 亿个高斯的大型场景，并达到最先进的重建质量。

## 英文关键词

GPU memory offloading; Heterogeneous systems for ML; 3D Gaussian Splatting

## 中文关键词

GPU 内存卸载；面向机器学习的异构系统；3D 高斯泼溅

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790140)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2026](../index.md)
