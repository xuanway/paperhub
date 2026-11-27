---
title: "Cooperative Warp Execution in Tensor Core for RISC-V GPGPU"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# Cooperative Warp Execution in Tensor Core for RISC-V GPGPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Abubakr Nada (imec), Giuseppe Maria Sarda (imec, KU Leuven), Erwan Lenormand (imec)
**会议**：HPCA 2025

---

## 中文标题

RISC-V GPGPU 中张量核心的协作式线程束（warp）执行

## 英文摘要

The rise of Deep Neural Networks (DNNs) has amplified the demand for efficient computation, with General Matrix Multiply (GEMM) operations at their core. While ASICs are efficient but inflexible, GPUs, especially NVIDIA GPUs, equipped with tensor cores, provide a flexible yet high-performance solution for GEMM-based workloads. Previous research and optimizations have largely centered on NVIDIA’s architecture and programming model, which, while effective, can obscure the rationale behind certain design decisions and limit flexibility for further improvements in tensor core designs. In this paper, we present the design and integration of a tensor core into the open-source RISC-V Vortex GPGPU platform, along with a suite of intrinsics designed for GEMM kernel generation. The analysis conducted on the integration elucidates the connections between GPU system architectural parameters and tensor core configuration. We find that the tensor core is severely under-utilized in many cases and that increased compute capacity does not always imply better performance. Hence, we propose a novel technique, cooperative warp execution in tensor core, which leverages hardware-supported warp cooperation within the tensor core to reduce memory requirements for GEMM operations and boost performance over the baseline tensor core implementation by up to 3x.

## 中文摘要

深度神经网络（DNN）的兴起放大了对高效计算的需求，而通用矩阵乘法（GEMM）运算正是其核心。ASIC 虽高效但缺乏灵活性，配备张量核心的 GPU（尤其是 NVIDIA GPU）则为基于 GEMM 的负载提供了灵活且高性能的方案。已有研究与优化大多围绕 NVIDIA 的体系结构与编程模型展开，这种做法虽然有效，却可能掩盖某些设计决策背后的依据，并限制张量核心设计进一步改进的灵活性。本文在开源 RISC-V Vortex GPGPU 平台上完成了张量核心的设计与集成，并提供了一组面向 GEMM 内核生成的 intrinsics。围绕该集成所做的分析阐明了 GPU 系统架构参数与张量核心配置之间的联系。我们发现，张量核心在许多情况下利用率严重不足，且计算能力的提升并不总是意味着性能提升。因此，我们提出一种新技术——张量核心内的协作式线程束（warp）执行，它利用张量核心内部由硬件支持的线程束协作，降低 GEMM 运算的内存需求，并将性能相较基线张量核心实现提升最多 3x。
