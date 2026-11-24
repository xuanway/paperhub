---
title: "Orion: A Fully Homomorphic Encryption Framework for Deep Learning"
description: "ASPLOS 2025 · Session 1D · Orion：面向深度学习的全同态加密框架"
tags:
  - "ASPLOS2025"
  - "Session 1D"
  - "Homomorphic Encryption"
---

# Orion: A Fully Homomorphic Encryption Framework for Deep Learning

**中文标题：** Orion：面向深度学习的全同态加密框架

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Austin Ebel (Tandon School of Engineering, New York University), Karthik Garimella (Tandon School of Engineering, New York University), Brandon Reagen (Tandon School of Engineering, New York University)

**单位：** Tandon School of Engineering, New York University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716008) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Fully Homomorphic Encryption (FHE) has the potential to substantially improve privacy and security by enabling computation directly on encrypted data. This is especially true with deep learning, as today, many popular user services are powered by neural networks in the cloud. Beyond its well-known high computational costs, one of the major challenges facing wide-scale deployment of FHE-secured neural inference is effectively mapping these networks to FHE primitives. FHE poses many programming challenges including packing large vectors, managing accumulated noise, and translating arbitrary and general-purpose programs to the limited instruction set provided by FHE. These challenges make building large FHE neural networks intractable using the tools available today. In this paper we address these challenges with Orion, a fully-automated framework for private neural inference using FHE. Orion accepts deep neural networks written in PyTorch and translates them into efficient FHE programs. We achieve this by proposing a novel single-shot multiplexed packing strategy for arbitrary convolutions and through a new, efficient technique to automate bootstrap placement and scale management. We evaluate Orion on common benchmarks used by the FHE deep learning community and outperform state-of-the-art by 2.38× on ResNet-20, the largest network they report. Orion's techniques enable processing much deeper and larger networks. We demonstrate this by evaluating ResNet-50 on ImageNet and present the first highresolution FHE object detection experiments using a YOLOv1 model with 139 million parameters. Orion is open-source for all to use at:

## 中文摘要

全同态加密（FHE）通过支持直接在加密数据上进行计算，有望大幅提升隐私性与安全性。在深度学习场景下尤其如此，因为如今许多流行的用户服务都由云端的神经网络提供支持。除了众所周知的高计算开销之外，FHE 安全神经推理大规模部署所面临的主要挑战之一是：如何有效地将这些网络映射到 FHE 原语上。FHE 带来了诸多编程挑战，包括打包大向量、管理累积噪声，以及将任意且通用的程序转换为 FHE 所提供的有限指令集。这些挑战使得使用当今可用的工具构建大型 FHE 神经网络变得难以实施。在本文中，我们通过 Orion 应对这些挑战，Orion 是一个使用 FHE 进行隐私神经推理的全自动框架。Orion 接受以 PyTorch 编写的深度神经网络，并将其翻译为高效的 FHE 程序。我们通过为任意卷积提出一种新颖的单次多路复用打包策略，以及通过一种新的高效技术来自动化自举放置与尺度管理，从而实现了这一目标。我们在 FHE 深度学习社区常用的基准上评估 Orion，在其报告的最大网络 ResNet-20 上性能超过最先进水平 2.38×。Orion 的技术能够处理更深、更大的网络。我们通过在 ImageNet 上评估 ResNet-50，并使用拥有 1.39 亿参数的 YOLOv1 模型首次给出高分辨率 FHE 目标检测实验，来证明这一点。Orion 已开源供所有人使用，地址为：

## 英文关键词

fully homomorphic encryption, compilers, cryptography, privacy-preserving machine learning

## 中文关键词

全同态加密；编译器；密码学；隐私保护机器学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716008)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2025](../index.md)
