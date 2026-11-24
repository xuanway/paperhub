---
title: "IroKnight: Ownership-Preserving Neural Acceleration for Inference Serving"
description: "ISCA 2026 · Session 5C · IroKnight: Ownership-Preserving Neural Acceleration for Inference Serving"
tags:
  - "ISCA2026"
  - "Session 5C"
  - "Crypto and Security"
---

# IroKnight: Ownership-Preserving Neural Acceleration for Inference Serving

**中文标题：** IroKnight: 面向推理服务的保所有权神经加速

**所属 Session：** [Session 5C](index.md) · [ISCA 2026](../index.md)

**作者：** Harsha Santhanam, Ashwin Rohit Alagiri Rajan, Hadi Esmaeilzadeh

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

With the rise of Large Language Models (LLMs), cloud-hosted inference serving has become the norm, requiring users to relinquish data ownership to the ethereal cloud. This surrender of ownership is particularly concerning, as citizens’ data is exposed to the cloud en masse and LLMs are increasingly deployed in highly regulated domains. Yet, existing approaches to preserving data ownership are either insufficient or impractical. Trusted Execution Environments (TEEs) incur modest overheads but expose plaintext in on-chip storage, thereby failing to preserve ownership and also presenting a well-exploited attack surface. Fully Homomorphic Encryption (FHE) keeps data encrypted on-chip and thus theoretically provides cryptographic data ownership, but it remains impractical due to immense overheads. FHE’s overheads stem from performing Arithmetic Logic Unit (ALU) operations directly on encrypted data. However, transient electrical signals within ALU wires and combinational logic gates are unobservable unless they are stored in registers or other on-chip storage in plaintext. Thus, if plaintext assets never persist beyond these transient ALU signals and all stored values remain encrypted on-chip, FHE-level data ownership becomes attainable. Our work proposes this new paradigm for ownership-preserving inference, instantiated in a novel design point called the IroKnight Neural Processing Unit (NPU). IroKnight exposes plaintext only ephemerally within the wires and gates of ALUs—flashing for a literal nanosecond—while all on-chip storage (e.g., pipe-registers, buffers, etc.) remains encrypted and integrity-protected. To make this practical, IroKnight leverages two domain-specific insights: (1) the regular accesses in fine-grained tiled and vectored neural calculations enable same-cycle in-ALU encryption and decryption; (2) the mathematics of integrity checks mirrors the multiply-and-accumulate flow of neural operators, enabling mid-execution data authentication. By leveraging these LLM-specific properties, IroKnight achieves near-FHE-level data ownership with just 3.3% runtime and 15.2% energy overheads, whereas FHE NPUs increase runtime and energy by 1110× and 2872×, respectively.

## 中文摘要

随着大语言模型（LLM）的兴起，云端托管的推理服务已成为常态，这要求用户将数据所有权让渡给虚无缥缈的云。这种所有权的让渡尤其令人担忧，因为公民数据被大规模暴露给云端，而 LLM 正越来越多地部署在高度受监管的领域。然而，现有的数据所有权保护方法要么不充分，要么不实用。可信执行环境（TEE）带来的开销不大，但会在片上存储中以明文暴露数据，从而既无法保持所有权，又构成了一个已被充分挖掘的攻击面。全同态加密（FHE）使数据在片上保持加密，因而理论上提供了密码学意义上的数据所有权，但由于巨大开销而仍不实用。FHE 的开销源于直接在加密数据上执行算术逻辑单元（ALU）运算。然而，ALU 连线与组合逻辑门内部的瞬态电信号，除非以明文存入寄存器或其他片上存储，否则不可观测。因此，若明文资产从不留存于这些瞬态 ALU 信号之外，且所有被存储的值在片上始终保持加密，那么 FHE 级别的数据所有权便可实现。我们的工作提出了这种面向保所有权推理的新范式，并将其实例化为一个新颖的设计点——IroKnight 神经网络处理单元（NPU）。IroKnight 仅在 ALU 的连线与逻辑门内以瞬态方式暴露明文——字面意义上仅闪现一纳秒——而所有片上存储（如流水寄存器、缓冲区等）始终保持加密并受完整性保护。为使这一方案实用，IroKnight 利用了两项领域相关洞见：(1) 细粒度分块与向量化神经计算中的规则访问模式，使同周期内的 ALU 加密与解密成为可能；(2) 完整性校验的数学运算与神经算子的乘累加数据流同构，从而支持执行中途的数据认证。借助这些 LLM 特有的性质，IroKnight 仅以 3.3% 的运行时间开销和 15.2% 的能耗开销便达到近乎 FHE 级别的数据所有权，而 FHE NPU 会使运行时间和能耗分别增加 1110× 和 2872×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2026](../index.md)
