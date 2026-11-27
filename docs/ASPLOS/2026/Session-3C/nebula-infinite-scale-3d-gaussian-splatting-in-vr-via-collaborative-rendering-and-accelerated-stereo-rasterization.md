---
title: "Nebula: Infinite-Scale 3D Gaussian Splatting in VR via Collaborative Rendering and Accelerated Stereo Rasterization"
description: "ASPLOS 2026 · Session 3C · Nebula：通过协同渲染与加速立体光栅化在 VR 中实现无限规模 3D 高斯泼溅"
tags:
  - "ASPLOS2026"
  - "Session 3C"
  - "3D Gaussian Splatting & Rendering"
---

# Nebula: Infinite-Scale 3D Gaussian Splatting in VR via Collaborative Rendering and Accelerated Stereo Rasterization

**中文标题：** Nebula：通过协同渲染与加速立体光栅化在 VR 中实现无限规模 3D 高斯泼溅

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2026](../index.md)

**作者：** He Zhu (Shanghai Jiao Tong University), Zheng Liu (Shanghai Jiao Tong University), Xingyang Li (Shanghai Jiao Tong University), Anbang Wu (Shanghai Jiao Tong University), Jieru Zhao (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Fangxin Liu (Shanghai Jiao Tong University), Yiming Gan (ICT, Chinese Academy of Sciences), Jingwen Leng (Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；Department of Computer Science and Engineering, Shanghai Jiao Tong University；ICT, Chinese Academy of Sciences

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790190) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

3D Gaussian splatting (3DGS) has drawn significant attention in the architectural community recently. However, current architectural designs often overlook the 3DGS scalability, making them fragile for extremely large-scale 3DGS. Meanwhile, the VR bandwidth requirement makes it impossible to deliver high-fidelity and smooth VR content from the cloud. We present Nebula, a coherent acceleration framework for large-scale 3DGS collaborative rendering. Instead of streaming videos, Nebula streams intermediate results after the LoD search, reducing 1925% data communication between the cloud and the client. To further enhance the motionto-photon experience, we introduce a temporal-aware LoD search in the cloud that tames the irregular memory access and reduces redundant data access by exploiting temporal coherence across frames. On the client side, we propose a novel stereo rasterization that enables two eyes to share most computations during the stereo rendering with bit-accurate quality. With minimal hardware augmentations, Nebula achieves 2.7× motion-to-photon speedup and reduces 1925% bandwidth over lossy video streaming.

## 中文摘要

3D 高斯泼溅（3DGS）近来在体系结构领域引起了广泛关注。然而，当前的体系结构设计往往忽视 3DGS 的可扩展性，使其面对极大规模 3DGS 时变得脆弱。同时，VR 带宽需求使得无法从云端传输高保真且流畅的 VR 内容。我们提出 Nebula，一个面向大规模 3DGS 协同渲染的一致性加速框架。Nebula 不传输视频流，而是传输 LoD 搜索之后的中间结果，将云端与客户端之间的数据通信减少 1925%。为进一步增强运动到光子（motion-to-photon）体验，我们在云端引入时序感知的 LoD 搜索，它利用跨帧的时序一致性来抑制不规则内存访问并减少冗余数据访问。在客户端，我们提出一种新颖的立体光栅化，使两只眼睛在立体渲染过程中共享大部分计算，同时保持比特精确的质量。借助极少的硬件增强，Nebula 实现了 2.7× 的运动到光子加速，并且相比有损视频流减少了 1925% 的带宽。

## 英文关键词

3D Gaussian Splatting, Neural Rendering Acceleration, Cloud-Client Collaborative Rendering, algorithm-hardware Co-Design

## 中文关键词

3D 高斯泼溅；神经渲染加速；云-客户端协同渲染；算法-硬件协同设计

## 相关链接
- [code](https://github.com/SJTU-MVCLab/Nebula)
- [website](https://stonesix16.github.io/Nebula/)
- [论文 DOI](https://doi.org/10.1145/3779212.3790190)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2026](../index.md)
