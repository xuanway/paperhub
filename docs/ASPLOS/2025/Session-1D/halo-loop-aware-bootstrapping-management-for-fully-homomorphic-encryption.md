---
title: "HALO: Loop-aware Bootstrapping Management for Fully Homomorphic Encryption"
description: "ASPLOS 2025 · Session 1D · HALO：面向全同态加密的循环感知自举管理"
tags:
  - "ASPLOS2025"
  - "Session 1D"
  - "Homomorphic Encryption"
---

# HALO: Loop-aware Bootstrapping Management for Fully Homomorphic Encryption

**中文标题：** HALO：面向全同态加密的循环感知自举管理

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Seonyoung Cheon (Yonsei University), Yongwoo Lee (Yonsei University), Hoyun Youm (Yonsei University), Dongkwan Kim (Yonsei University), Sungwoo Yun (Yonsei University), Kunmo Jeong (Yonsei University), Dongyoon Lee (Stony Brook University), Hanjun Kim (Yonsei University)

**单位：** Yonsei University；Stony Brook University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707275) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Thanks to the computation ability on encrypted data, fully homomorphic encryption (FHE) is an attractive solution for privacy-preserving computation. Despite its advantages, FHE suffers from limited applicability in small programs because repeated FHE multiplications deplete the level of a ciphertext, which is finite. Bootstrapping reinitializes the level, thus allowing support for larger programs. However, its high computational overhead and the risk of level underflow require sophisticated bootstrapping placement, thereby increasing the programming burden. Although a recently proposed compiler automatizes the bootstrapping placement, its applicability is still limited due to lack of loop support. This work proposes the first loop-aware bootstrapping management compiler, called HALO, which optimizes bootstrapping placement in an FHE program with a loop. To correctly support bootstrapping-enabled loops, HALO matches encryption status and levels between live-in and loop-carried ciphertexts in the loops. To reduce the bootstrapping overheads, HALO decreases the number of bootstrapping within a loop body by packing the loop-carried variables to a single ciphertext, reduces wasted levels in a short loop body by unrolling the loop, and optimizes the bootstrapping latency by adjusting the target level of bootstrapping as needed. For seven machine learning programs with flat and nested loops, HALO shows 27% performance speedup compared to the state-of-the-art compiler that places bootstrapping operations on fully unrolled loops. In addition, HALO reduces Attribution International 4.0 License. c means of 209.12× and 11.0× compared to the compiler, respectively.

## 中文摘要

得益于在加密数据上进行计算的能力，全同态加密（FHE）成为隐私保护计算的一种颇具吸引力的解决方案。尽管具有优势，FHE 在小程序中的适用性仍然受限，因为反复的 FHE 乘法会耗尽密文的层级（level），而该层级是有限的。自举（bootstrapping）会重新初始化层级，从而支持更大的程序。然而，自举的高计算开销以及层级下溢的风险要求精细的自举放置，从而加重了编程负担。尽管最近提出的编译器可以自动完成自举放置，但由于缺乏对循环的支持，其适用性仍然有限。本工作提出了首个循环感知的自举管理编译器 HALO，它可优化带循环的 FHE 程序中的自举放置。为了正确支持启用自举的循环，HALO 在循环中匹配活入（live-in）密文与循环携带（loop-carried）密文之间的加密状态和层级。为降低自举开销，HALO 通过将循环携带变量打包到单个密文中来减少循环体内的自举次数，通过展开循环来减少短循环体中浪费的层级，并根据需要调整自举的目标层级来优化自举延迟。对于七个包含平坦循环和嵌套循环的机器学习程序，与在完全展开的循环上放置自举操作的最先进编译器相比，HALO 取得了 27% 的性能加速。此外，与该编译器相比，HALO 还分别将其开销降低了 209.12× 和 11.0×。

## 英文关键词

Fully homomorphic encryption, CKKS, Bootstrapping, Loop optimization, Compiler, Privacy-preserve machine learning

## 中文关键词

全同态加密；CKKS；自举；循环优化；编译器；隐私保护机器学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707275)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2025](../index.md)
