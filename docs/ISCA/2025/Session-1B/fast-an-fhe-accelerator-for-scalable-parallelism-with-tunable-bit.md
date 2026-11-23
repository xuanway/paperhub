---
title: "FAST: An FHE Accelerator for Scalable-parallelism with Tunable-bit"
description: "ISCA 2025 · Session 1B · FAST: 支持可调精度与可扩展并行的FHE加速器"
tags:
  - "ISCA2025"
  - "Session 1B"
  - "Crypto & Fully Homomorphic Encryption"
---

# FAST: An FHE Accelerator for Scalable-parallelism with Tunable-bit

**中文标题：** FAST: 支持可调精度与可扩展并行的FHE加速器

**所属 Session：** [Session 1B](index.md) · [ISCA 2025](../index.md)

**作者：** Shengyu Fan, Xianglong Deng, Liang Kong, Guiming Shi, Guang Fan, Rui Hou, Dan Meng, Mingzhe Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731407) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Fully Homomorphic Encryption (FHE) enables direct computation on encrypted data, providing substantial security advantages in cloud-based modern society. However, FHE suffers from significant computational overhead compared to plaintext computation, hindering its adoption in real-world applications. While many accelerators have been designed to address performance bottlenecks, most do not fully leverage cryptographic optimization technologies, leaving room for further performance enhancements.

In this work, we propose FAST, an FHE accelerator incorporating recent cryptographic optimizations, including hoisting technology and the gadget decomposition key-switching method (named KLSS method). We analyze ciphertext level consumption throughout application execution and observe that workload requirements vary significantly with different ciphertext levels for both hybrid and KLSS key-switching methods. Additionally, we note the differing computational precision requirements for these key-switching methods. Based on these observations, we designed a versatile framework that supports multiple key-switching methods during a single application execution and integrates hoisting technology.

## 中文摘要

全同态加密（FHE）支持直接对密文进行计算，在云服务普及的当下具备极高的安全价值。但相较于明文计算，FHE存在巨大的计算开销，制约了其在实际场景中的落地。尽管已有大量加速器工作用于缓解性能瓶颈，多数方案并未充分利用密码学层面的优化手段，仍存在较大的性能提升空间。

本文提出FAST，一款融合前沿密码优化技术的FHE加速器，集成了提升技术（hoisting technology）以及基于 gadget 分解的密钥切换方案（KLSS方案）。我们分析应用运行全过程中的密文层级开销，发现在混合密钥切换与KLSS密钥切换两种方式下，不同密文层级对应的计算负载差异显著；同时两类密钥切换方案对计算精度的需求也各不相同。基于上述发现，我们构建了一套通用框架，能够在单次应用执行过程中支持多种密钥切换方式，并集成提升优化技术。

## 英文关键词

Fully homomorphic encryption, CKKS, key switching, gadget decomposition, hoisting, tunable-bit multiplier

## 中文关键词

全同态加密, CKKS, 密钥切换, Gadget 分解, 提升优化, 可调位宽乘法器

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731407)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1B](index.md) · [返回 ISCA 2025](../index.md)
