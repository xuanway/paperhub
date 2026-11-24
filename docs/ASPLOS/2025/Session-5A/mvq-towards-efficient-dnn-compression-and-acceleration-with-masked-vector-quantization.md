---
title: "MVQ: Towards Efficient DNN Compression and Acceleration with Masked Vector Quantization"
description: "ASPLOS 2025 · Session 5A · MVQ：基于掩码向量量化的高效 DNN 压缩与加速"
tags:
  - "ASPLOS2025"
  - "Session 5A"
  - "ML Systems 1"
---

# MVQ: Towards Efficient DNN Compression and Acceleration with Masked Vector Quantization

**中文标题：** MVQ：基于掩码向量量化的高效 DNN 压缩与加速

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shuaiting Li (Zhejiang University), Chengxuan Wang (Zhejiang University), Juncan Deng (Zhejiang University), Zeyu Wang (Zhejiang University), Zewen Ye (Zhejiang University), Zongsheng Wang (Zhejiang University), Haibin Shen (Zhejiang University), Kejie Huang (Zhejiang University)

**单位：** Zhejiang University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707268) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Vector quantization(VQ) is a hardware-friendly DNN compression method that can reduce the storage cost and weightloading datawidth of hardware accelerators. However, conventional VQ techniques lead to significant accuracy loss because the important weights are not well preserved. To tackle this problem, a novel approach called MVQ is proposed, which aims at better approximating important weights with a limited number of codewords. At the algorithm level, our approach removes the less important weights through N:M pruning and then minimizes the vector clustering error between the remaining weights and codewords by the masked k-means algorithm. Only distances between the unpruned weights and the codewords are computed, which are then used to update the codewords. At the architecture level, our accelerator implements vector quantization on an EWS (Enhanced weight stationary) CNN accelerator and proposes a sparse systolic array design to maximize the benefits brought by masked vector quantization. Our algorithm is validated on various models for image classification, object detection, and segmentation tasks. Experimental results demonstrate that MVQ not only outperforms conventional vector quantization methods at comparable compression ratios but also reduces FLOPs. Under ASIC evaluation, our MVQ accelerator boosts energy efficiency by 2.3× and reduces the size of the systolic array by 55% when compared with the base EWS accelerator. Compared to the previous sparse accelerators, MVQ achieves 1.73× higher energy efficiency.

## 中文摘要

向量量化（VQ）是一种对硬件友好的 DNN 压缩方法，能够降低硬件加速器的存储开销与权重加载数据位宽。然而，传统 VQ 技术会导致显著的精度损失，因为重要权重未能得到良好保留。为解决这一问题，本文提出一种称为 MVQ 的新方法，旨在用有限的码字数更好地逼近重要权重。在算法层面，我们的方法先通过 N:M 剪枝去除较不重要的权重，然后利用 masked k-means 算法最小化剩余权重与码字之间的向量聚类误差。只计算未剪枝权重与码字之间的距离，并用这些距离来更新码字。在体系结构层面，我们的加速器在 EWS（Enhanced weight stationary）CNN 加速器上实现向量量化，并提出一种稀疏脉动阵列设计，以最大化掩码向量量化带来的收益。我们的算法在图像分类、目标检测与分割任务的多种模型上得到验证。实验结果表明，MVQ 不仅在相近压缩率下优于传统向量量化方法，而且还能减少 FLOPs。在 ASIC 评估下，与基础 EWS 加速器相比，我们的 MVQ 加速器将能效提升 2.3×，并将脉动阵列面积减小 55%。与先前的稀疏加速器相比，MVQ 实现了 1.73× 更高的能效。

## 英文关键词

neural networks; vector quantization; pruning; systolic arrays

## 中文关键词

神经网络；向量量化；剪枝；脉动阵列

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707268)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2025](../index.md)
