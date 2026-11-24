---
title: "AutoFHE: An Automatic Hardware Generation Framework for Domain-Specific FHE Accelerators"
description: "ISCA 2026 · Session 5C · AutoFHE: An Automatic Hardware Generation Framework for Domain-Specific FHE Accelerators"
tags:
  - "ISCA2026"
  - "Session 5C"
  - "Crypto and Security"
---

# AutoFHE: An Automatic Hardware Generation Framework for Domain-Specific FHE Accelerators

**中文标题：** AutoFHE: 面向领域专用 FHE 加速器的自动硬件生成框架

**所属 Session：** [Session 5C](index.md) · [ISCA 2026](../index.md)

**作者：** Yibo Du, Cangyuan Li, Bing Li, Mengdi Wang, Lian Liu, Shixin Zhao, Yinhe Han, Ying Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Fully Homomorphic Encryption (FHE) is a transformative technology that enables computation directly on encrypted data, unlocking secure applications such as privacy inference, encrypted databases, and privacy-preserving analytics. As the demand for high-performance FHE computation grows, domain-specific FHE accelerators have emerged to improve efficiency across different application domains. However, designing these accelerators remains prohibitively difficult. It requires implementing specialized ciphertext processing elements (CPEs) and navigating a vast design space tightly coupled to cryptographic operations, demanding rare dual-domain expertise in both hardware architecture and FHE algorithms. In this paper, we propose AutoFHE, the first automatic hardware generation framework that transforms conventional domain-specific RTL accelerator designs into encrypted accelerators that operate on FHE ciphertexts. AutoFHE decouples FHE complexity from architecture design, empowering hardware designers without FHE expertise to implement FHE accelerators with significantly reduced design effort. To achieve this, (1) AutoFHE raises the abstraction level of encrypted signals, allowing designers to declaratively specify encrypted signals in a hardware construction language (Chisel) without manually modifying the underlying hardware. (2) AutoFHE operates on FIRRTL (Flexible Intermediate Representation for Register Transfer Level) to automatically identify encrypted PEs and synthesize them using optimized CPE templates. (3) To address the prohibitive resource cost, AutoFHE introduces a CPE-virtualization strategy that virtualizes a pool of physical CPEs for the identified encrypted PEs. AutoFHE develops a heuristic algorithm to search for the optimal schedule from logically identified encrypted PEs to physical CPEs, and embeds this algorithm into its design space exploration. Evaluations on multiple TFHE design cases show that AutoFHE-generated FHE accelerators outperform handcrafted designs while drastically reducing design effort.

## 中文摘要

全同态加密（FHE）是一项变革性技术，它使得可以直接在加密数据上完成计算，从而开启隐私推理、加密数据库和隐私保护分析等安全应用。随着对高性能 FHE 计算需求的增长，领域专用 FHE 加速器应运而生，以提升不同应用领域的效率。然而，设计这类加速器依然极其困难：需要实现专用的密文处理单元（CPE），并在与密码学操作紧密耦合的庞大设计空间中探索，要求同时具备硬件架构与 FHE 算法这两方面罕见跨领域专业知识。本文提出 AutoFHE，这是首个自动硬件生成框架，可将传统的领域专用 RTL 加速器设计转化为直接在 FHE 密文上运行的加密加速器。AutoFHE 将 FHE 的复杂性从架构设计中解耦，使不具备 FHE 专业知识的硬件设计者也能以大幅降低的设计工作量实现 FHE 加速器。为此，(1) AutoFHE 提升了加密信号的抽象层次，使设计者能够在硬件构建语言（Chisel）中以声明方式指定加密信号，而无需手动修改底层硬件；(2) AutoFHE 基于 FIRRTL（面向寄存器传输级的灵活中间表示）工作，自动识别加密 PE 并使用优化的 CPE 模板对其进行综合；(3) 为应对高昂的资源开销，AutoFHE 引入了 CPE 虚拟化策略，为已识别的加密 PE 虚拟化一个物理 CPE 池。AutoFHE 提出一种启发式算法，用于搜索从逻辑上已识别的加密 PE 到物理 CPE 的最优调度，并将该算法嵌入其设计空间探索之中。在多个 TFHE 设计案例上的评估表明，AutoFHE 生成的 FHE 加速器优于手工设计，同时大幅降低了设计工作量。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2026](../index.md)
