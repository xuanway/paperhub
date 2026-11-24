---
title: "GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading"
description: "ASPLOS 2026 · Session 3C · GS-Scale：通过主机卸载释放大规模 3D 高斯泼溅训练"
tags:
  - "ASPLOS2026"
  - "Session 3C"
  - "3D Gaussian Splatting & Rendering"
---

# GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading

**中文标题：** GS-Scale：通过主机卸载释放大规模 3D 高斯泼溅训练

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Donghyun Lee (Seoul National University), Dawoon Jeong (Seoul National University), Jae W. Lee (Seoul National University), Hongil Yoon (Google)

**单位：** Seoul National University；Google

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790167) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The advent of 3D Gaussian Splatting has revolutionized graphics rendering by delivering high visual quality and fast rendering speeds. However, training large-scale scenes at high quality remains challenging due to the substantial memory demands required to store parameters, gradients, and optimizer states, which can quickly overwhelm GPU memory. To address these limitations, we propose GS-Scale, a fast and memory-efficient training system for 3D Gaussian Splatting. GS-Scale stores all Gaussians in host memory, transferring only a subset to the GPU on demand for each forward and backward pass. While this dramatically reduces GPU memory usage, it requires frustum culling and optimizer updates to be executed on the CPU, introducing slowdowns due to CPU's limited compute and memory bandwidth. To mitigate this, GS-Scale employs three system-level optimizations: (1) selective offloading of geometric parameters for fast frustum culling, (2) parameter forwarding to pipeline CPU optimizer updates with GPU computation, and (3) deferred optimizer update to minimize unnecessary memory accesses for Gaussians with zero gradients. Our extensive evaluations on large-scale datasets demonstrate that GS-Scale significantly lowers GPU memory demands by 3.3-5.6×, while achieving training speeds comparable to GPU without host offloading. This enables large-scale 3D Gaussian Splatting training on consumer-grade GPUs; for instance, GS-Scale can scale the number of Gaussians from 4 million to 18 million on an RTX 4070 Mobile GPU, leading to 23-35% LPIPS (learned perceptual image patch similarity) improvement.

## 中文摘要

3D 高斯泼溅的出现通过提供高视觉质量和快速渲染速度，彻底变革了图形渲染。然而，由于存储参数、梯度和优化器状态所需的大量内存需求会迅速压垮 GPU 内存，以高质量训练大规模场景仍然充满挑战。为解决这些限制，我们提出 GS-Scale，一个快速且内存高效的 3D 高斯泼溅训练系统。GS-Scale 将所有高斯存储在主机内存中，每次前向与反向传播时仅按需将其中一个子集传输到 GPU。尽管这大幅降低了 GPU 内存使用量，但它要求在 CPU 上执行视锥剔除和优化器更新，从而因 CPU 有限的计算能力与内存带宽而引入性能下降。为缓解这一问题，GS-Scale 采用三项系统级优化：（1）几何参数的选择性卸载，以实现快速视锥剔除；（2）参数转发，将 CPU 优化器更新与 GPU 计算流水线化；（3）延迟优化器更新，以最小化对零梯度高斯的非必要内存访问。我们在大规模数据集上的广泛评估表明，GS-Scale 将 GPU 内存需求显著降低 3.3-5.6×，同时达到与无主机卸载的 GPU 相当的训练速度。这使得在消费级 GPU 上进行大规模 3D 高斯泼溅训练成为可能；例如，GS-Scale 可以在 RTX 4070 Mobile GPU 上将高斯数量从 400 万扩展到 1800 万，从而带来 23-35% 的 LPIPS（学习感知图像块相似度）提升。

## 英文关键词

3D Gaussian Splatting; CPU Offloading; GPU

## 中文关键词

3D 高斯泼溅；CPU 卸载；GPU

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790167)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2026](../index.md)
