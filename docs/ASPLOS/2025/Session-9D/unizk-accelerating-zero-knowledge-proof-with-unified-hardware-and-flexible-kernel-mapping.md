---
title: "UniZK: Accelerating Zero-Knowledge Proof with Unified Hardware and Flexible Kernel Mapping"
description: "ASPLOS 2025 · Session 9D · UniZK：以统一硬件与灵活内核映射加速零知识证明"
tags:
  - "ASPLOS2025"
  - "Session 9D"
  - "Trust"
---

# UniZK: Accelerating Zero-Knowledge Proof with Unified Hardware and Flexible Kernel Mapping

**中文标题：** UniZK：以统一硬件与灵活内核映射加速零知识证明

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Cheng Wang (Xi'an Jiaotong University,Institute for Interdisciplinary Information Core Technology), Mingyu Gao (Tsinghua University,Shanghai Qi Zhi Institute)

**单位：** Xi'an Jiaotong University,Institute for Interdisciplinary Information Core Technology；Tsinghua University,Shanghai Qi Zhi Institute

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707228) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Zero-knowledge proof (ZKP) is an important cryptographic tool that sees wide applications in real-world scenarios where privacy must be protected, including privacy-preserving blockchains and zero-knowledge machine learning. Existing ZKP acceleration approaches using GPUs, FPGAs, and ASICs focus only on classic protocols that rely on expensive elliptic curve arithmetics. Emerging ZKP protocols based on hash functions can greatly reduce the algorithmic complexity, but they also introduce much more diverse computation kernels that cannot be efficiently handled by a single accelerator chip if dedicated units for each kernel are used. Our approach is to leverage a unified hardware architecture that is able to efficiently support the common primitives in ZKP, and then use smart mapping strategies to flexibly map various kernels to such hardware while ensuring high resource utilization. We design UniZK as such a ZKP accelerator, with a systolic-array-based hardware architecture enhanced with extra local links and a new vector processing mode. We propose novel mapping strategies to support diverse kernels including number theoretic transforms, hash functions, and general polynomial computations. UniZK provides 97× and 46× speedups on average compared to the CPU and GPU implementations of the same protocols, and is also 840× faster than previous ZKP accelerators using different protocols.

## 中文摘要

零知识证明（ZKP）是一种重要的密码学工具，在隐私保护区块链和零知识机器学习等必须保护隐私的真实场景中得到广泛应用。现有的基于 GPU、FPGA 和 ASIC 的 ZKP 加速方法仅关注依赖昂贵椭圆曲线运算的经典协议。基于哈希函数的新兴 ZKP 协议能够大幅降低算法复杂度，但也引入了更加多样的计算内核；若为每个内核配置专用单元，单一加速器芯片将无法高效处理。我们的思路是利用一种能够高效支持 ZKP 中常见原语的统一硬件架构，再借助智能映射策略将各类内核灵活映射到该硬件上，同时保证高资源利用率。我们据此设计了 UniZK 这一 ZKP 加速器，其采用基于脉动阵列的硬件架构，并增强了额外的局部链路与一种新的向量处理模式。我们提出了新颖的映射策略，以支持包括数论变换、哈希函数和通用多项式计算在内的多样内核。与相同协议的 CPU 和 GPU 实现相比，UniZK 平均分别取得 97× 和 46× 的加速，并且比此前采用不同协议的 ZKP 加速器快 840×。

## 英文关键词

domain-specific acceleration, zero-knowledge proof, mapping

## 中文关键词

领域专用加速；零知识证明；映射

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707228)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2025](../index.md)
