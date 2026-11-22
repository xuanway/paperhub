---
title: "SMExplode: Cross-Core and Cache-Agnostic Side-Channel Attack on Apple Silicon via SME Engine"
description: "MICRO 2026 · Session 4B · SMExplode：利用 SME 引擎对 Apple Silicon 发起跨核心、与缓存无关的侧信道攻击"
tags:
  - "MICRO2026"
  - "Cache"
  - "Side-Channel Attack"
---

# SMExplode: Cross-Core and Cache-Agnostic Side-Channel Attack on Apple Silicon via SME Engine

**中文标题：** SMExplode：利用 SME 引擎对 Apple Silicon 发起跨核心、与缓存无关的侧信道攻击

**所属 Session：** [Session 4B](index.md) · [MICRO 2026](../index.md)

**作者：** Hongpei Zheng, Ben Chen, Hanyin Liu, Kaiyuan Rong, Yun Chen, Dongsheng Wang

**来源：** MICRO 2026，pp. 1444–1458；[DOI](https://doi.org/10.1109/MICRO67795.2026.00107)

## 英文摘要

Apple's M-series processors have become widely adopted across mobile and cloud platforms, yet their security implications remain underexplored. While prior work has exposed side channels in Apple-specific microarchitectural optimizations, they are largely limited to intra-process settings or depend on cache primitives for cross-core leakage. In this paper, we uncover a new attack surface: the Apple Scalable Matrix Extension (SME) Engine, an accelerator for AI/ML workloads. Through the first characterization of the SME Engine on Apple M4 and M5 processors, we show that it is shared across cores and exhibits measurable instruction-level contention. Building on these insights, we propose SMExplode, a novel, cache-agnostic side-channel primitive that exploits this contention to enable cross-core attacks. SMExplode achieves up to 1.22 Mbps covert-channel bandwidth across processes and 0.69 Mbps across virtual machines (VMs), outperforming the state-of-the-art on Apple silicon by 6x and representing the first cross-VM covert channel. In addition, SMExplode enables accurate DNN fingerprinting attacks (98.53% classification accuracy) and leaks fine-grained model details from the Apple Accelerate framework. Finally, we demonstrate that SMExplode can recover the secret key from the post-quantum cryptographic (PQC) implementation used in OpenSSL in 13 hours.

## 中文摘要

Apple 的 M 系列处理器已在移动和云平台上广泛采用，但其安全隐患仍未得到充分研究。虽然之前的工作已经暴露了 Apple 特定微架构优化中的侧通道，但它们很大程度上仅限于进程内设置或依赖于跨核心泄漏的缓存原语。在本文中，我们发现了一个新的攻击面：Apple 可扩展矩阵扩展 (SME) 引擎，它是 AI/ML 工作负载的加速器。通过对 Apple M4 和 M5 处理器上的 SME 引擎的首次表征，我们表明它是跨内核共享的，并表现出可测量的指令级争用。基于这些见解，我们提出了 SMExplode，这是一种新颖的、与缓存无关的侧通道原语，它利用这种争用来实现跨核心攻击。 SMExplode 跨进程实现高达 1.22 Mbps 的隐蔽通道带宽，跨虚拟机 (VM) 实现高达 0.69 Mbps 的隐蔽通道带宽，比 Apple 芯片上最先进的技术高出 6 倍，代表第一个跨 VM 隐蔽通道。此外，SMExplode 可实现准确的 DNN 指纹攻击（分类准确率达 98.53%），并从 Apple Accelerate 框架中泄漏细粒度的模型详细信息。最后，我们证明 SMExplode 可以在 13 小时内从 OpenSSL 中使用的后量子加密 (PQC) 实现中恢复密钥。

## 中文关键词

Apple Silicon；侧信道攻击；可扩展矩阵扩展；跨核攻击

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4B](index.md) · [MICRO 2026 主页](../index.md)
