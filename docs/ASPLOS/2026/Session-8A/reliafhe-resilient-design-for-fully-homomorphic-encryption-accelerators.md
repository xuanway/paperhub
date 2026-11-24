---
title: "ReliaFHE: Resilient Design for Fully Homomorphic Encryption Accelerators"
description: "ASPLOS 2026 · Session 8A · ReliaFHE：面向全同态加密加速器的弹性设计"
tags:
  - "ASPLOS2026"
  - "Session 8A"
  - "GPU Programming"
---

# ReliaFHE: Resilient Design for Fully Homomorphic Encryption Accelerators

**中文标题：** ReliaFHE：面向全同态加密加速器的弹性设计

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Fan Li (University of Central Florida), Mayank Kumar (University of Central Florida), Ruizhi Zhu (University of Central Florida), Mengxin Zheng (University of Central Florida), Qian Lou (University of Central Florida), Xin Xin (University of Central Florida)

**单位：** University of Central Florida

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790211) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The significant computational complexity of Fully Homomorphic Encryption (FHE) has prompted numerous accelerator designs. However, existing FHE accelerators often implicitly assume that all computations are executed reliably, overlooking the fact that modern FHE schemes can be highly vulnerable to hardware faults: even a single-bit error in a ciphertext can cascade into widespread plaintext corruption. In this paper, we present ReliaFHE, a resilient framework that integrates both storage- and computation-oriented protection for FHE accelerators. It leverages the large ciphertext polynomials inherent in FHE and employs lightweight, checksum-based schemes to construct efficient codewords. ReliaFHE is tailored to the three dominant arithmetic kernels: number theoretic transform, base conversion, and elementwise operations. Our evaluation shows that ReliaFHE improves reliability by more than 104 (in terms of primitive operations), with either ∼1.5% performance overhead or ∼1.9% area overhead. The parity storage overhead is below 1%.

## 中文摘要

全同态加密（FHE）极高的计算复杂度催生了众多加速器设计。然而，现有的 FHE 加速器往往隐含地假设所有计算都被可靠地执行，从而忽视了现代 FHE 方案可能极易受硬件故障影响这一事实：密文中的哪怕一个比特错误也可能级联造成大范围的明文损坏。在本文中，我们提出 ReliaFHE，一个为 FHE 加速器同时集成面向存储与面向计算保护的弹性框架。它利用 FHE 中固有的大密文多项式，并采用轻量级、基于校验和的方案来构造高效的码字。ReliaFHE 针对三种主要算术内核进行了定制：数论变换、基转换和逐元素运算。我们的评估表明，ReliaFHE 将可靠性提升 104 以上（以原始操作计），而性能开销约为 1.5%，或面积开销约为 1.9%。奇偶校验存储开销低于 1%。

## 英文关键词

Resilient design; fully homomorphic encryption

## 中文关键词

弹性设计；全同态加密

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790211)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2026](../index.md)
