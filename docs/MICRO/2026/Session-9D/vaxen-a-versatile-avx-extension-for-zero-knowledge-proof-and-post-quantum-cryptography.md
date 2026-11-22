---
title: "VAXEN: A Versatile AVX Extension for Zero-Knowledge Proof and Post-Quantum Cryptography"
description: "MICRO 2026 · Session 9D · VAXEN：面向零知识证明与后量子密码学的多功能 AVX 扩展"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Cryptography"
---

# VAXEN: A Versatile AVX Extension for Zero-Knowledge Proof and Post-Quantum Cryptography

**中文标题：** VAXEN：面向零知识证明与后量子密码学的多功能 AVX 扩展

**所属 Session：** [Session 9D](index.md) · [MICRO 2026](../index.md)

**作者：** Jipeng Zhang, Hao Cheng, Tao Lu, Jiaheng Zhang

**来源：** MICRO 2026，pp. 3515–3529；[DOI](https://doi.org/10.1109/MICRO67795.2026.00234)

## 英文摘要

The Intel Advanced Vector eXtension (AVX) family provides multiply-high instructions (e.g., vpmulhw) for 16-bit lanes, but no corresponding support exists for 32-bit lanes in either AVX2 or AVX-512. This gap inflates the cost of 32-bit integer arithmetic in both zero-knowledge proof (ZKP) and post-quantum cryptography (PQC), and it also impacts the efficiency of Philox pseudorandom number generation (PRNG). To address this, we present VAXEN, a Versatile AVX Extension, which introduces signed and unsigned 32-bit multiply-high instructions, vpmulhd and vpmulhud, while preserving the existing AVX2/AVX-512 programming model. VAXEN targets per-lane arithmetic and therefore does not require carry-propagation support. We evaluate VAXEN using proxy ISA (PISA): proxy binaries are measured on Intel Rocket Lake, Intel Core Ultra 5 228V P/E cores, and AMD Zen 5, then interpreted under explicit implementation mappings. Under a balanced 32-bit multiply mapping, projected results show up to 1.86 times (resp. 2.14 times) speedup for BabyBear (resp. ML-DSA) Montgomery multiplication, 1.84 times for ML-DSA NTT, 1.51 times for Rust-level Plonky3 Poseidon2, and 2.83 times for Philox PRNG. We also report a complete Intel PISA matrix that separates the benefit of the proposed high-half instructions from improvements to existing vpmulld. To strengthen trustworthiness, we use CryptoLine to formally verify the projected implementations of Montgomery multiplication and Philox PRNG. We also develop an ASIC evaluation library and show low marginal cost: a 4.50 percent increase of the modeled vector-integer cluster post-synthesis, 0.017 percent of an AMD Zen 5 core area including private L2, and a post-route core-normalized upper bound below 0.1 percent. These results suggest that a minimal fix to AVX2 and AVX-512 can deliver meaningful cross-domain speedups at low hardware cost.

## 中文摘要

英特尔高级矢量扩展 (AVX) 系列为 16 位通道提供乘高指令（例如 vpmulhw），但 AVX2 或 AVX-512 中不存在对 32 位通道的相应支持。这一差距增加了零知识证明 (ZKP) 和后量子密码学 (PQC) 中 32 位整数算术的成本，并且还影响了 Philox 伪随机数生成 (PRNG) 的效率。为了解决这个问题，我们推出了 VAXEN，一种多功能 AVX 扩展，它引入了有符号和无符号 32 位乘高指令 vpmulhd 和 vpmulhud，同时保留了现有的 AVX2/AVX-512 编程模型。 VAXEN 针对每通道算术，因此不需要进位传播支持。我们使用代理 ISA (PISA) 评估 VAXEN：代理二进制文件在 Intel Rocket Lake、Intel Core Ultra 5 228V P/E 核心和 AMD Zen 5 上进行测量，然后在显式实现映射下进行解释。在平衡的 32 位乘法映射下，预计结果显示 BabyBear（分别为 ML-DSA）蒙哥马利乘法加速高达 1.86 倍（分别为 2.14 倍），ML-DSA NTT 加速为 1.84 倍，Rust 级 Plonky3 Poseidon2 加速为 1.51 倍，Philox PRNG 加速为 2.83 倍。我们还报告了完整的英特尔 PISA 矩阵，该矩阵将提议的高半指令的优势与对现有 vpmulld 的改进分开。为了增强可信度，我们使用 CryptoLine 来正式验证蒙哥马利乘法和 Philox PRNG 的预计实现。我们还开发了一个 ASIC 评估库，并显示出较低的边际成本：综合后建模的向量整数簇增加了 4.50%，包括专用 L2 的 AMD Zen 5 核心面积增加了 0.017%，布线后核心归一化上限低于 0.1%。这些结果表明，对 AVX2 和 AVX-512 进行最小程度的修复可以以较低的硬件成本提供有意义的跨域加速。

## 中文关键词

指令集扩展；AVX2；AVX-512；代理指令集；后量子密码学；零知识证明

## 代码与研究制品

- 代码仓库：[https://github.com/Ji-Peng/VAXEN_Artifact](https://github.com/Ji-Peng/VAXEN_Artifact)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9D](index.md) · [MICRO 2026 主页](../index.md)
