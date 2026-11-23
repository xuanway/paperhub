---
title: "Synchronization for Fault-Tolerant Quantum Computers"
description: "ISCA 2025 · Session 7C · 容错量子计算机的同步机制"
tags:
  - "ISCA2025"
  - "Session 7C"
  - "Quantum II"
---

# Synchronization for Fault-Tolerant Quantum Computers

**中文标题：** 容错量子计算机的同步机制

**所属 Session：** [Session 7C](index.md) · [ISCA 2025](../index.md)

**作者：** Satvik Maurya, Swamit Tannu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730991) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Quantum Error Correction (QEC) codes store information reliably in logical qubits by encoding them in a larger number of less reliable qubits. The surface code, known for its high resilience to physical errors, is a leading candidate for fault-tolerant quantum computing (FTQC). Logical qubits encoded with the surface code can be in different phases of their syndrome generation cycle, thereby in- troducing desynchronization in the system. This can occur due to the production of non-Clifford states, dropouts due to fabrica- tion defects, and the use of other QEC codes with the surface code to reduce resource requirements. Logical operations require the syndrome generation cycles of the logical qubits involved to be syn- chronized. This requires the leading qubit to pause or slow down its cycle, allowing more errors to accumulate before the next cycle, thereby increasing the risk of uncorrectable errors. To synchronize the syndrome generation cycles of logical qubits, we define three policies - Passive, Active, and Hybrid. The Passive policy is the baseline, and the simplest, wherein the leading logical qubits idle until they are synchronized with the remaining logical qubits. On the other hand, the Active policy aims to slow the lead- ing logical qubits down gradually, by inserting short idle periods before multiple code cycles. This approach reduces the logical er- ror rate (LER) by up to 2.4×compared to the Passive policy. The Hybrid policy further reduces the LER by up to 3.4×by reducing the synchronization slack and running a few additional rounds of error correction. Furthermore, the reduction in the logical error rate with the proposed synchronization policies enables a speedup in decoding latency of up to 2.2×with a circuit-level noise model.

## 中文摘要

量子纠错（QEC）通过将信息编码到大量可靠性更低的物理量子比特中，利用逻辑量子比特实现可靠的信息存储。表面码对物理错误具备很强的抵御能力，是容错量子计算（FTQC）的主流方案。
采用表面码编码的逻辑量子比特，其校验子生成周期可能处于不同相位，造成系统失步。引发失步的原因包括：生成非克利福德态、工艺缺陷导致量子比特失效、以及表面码和其他纠错码混合使用以降低资源开销。
执行逻辑运算时，参与运算的所有逻辑量子比特的校验子生成周期必须同步。这就要求进度更快的量子比特暂停或放慢周期，等待其余比特；但等待期间会累积更多错误，提升不可纠正错误的发生概率。

为实现逻辑量子比特校验子生成周期的同步，本文定义三种同步策略：被动策略（Passive）、主动策略（Active）、混合策略（Hybrid）。 被动策略是基线方案，实现最简单：进度超前的逻辑量子比特保持空闲，直到和其余逻辑量子比特对齐。 主动策略则在多个纠错周期前插入短时空闲，逐步拖慢超前比特，相比被动策略，逻辑错误率（LER）最高降低2.4倍。 混合策略进一步压缩同步余量，额外增加少量纠错轮次，逻辑错误率最高降低3.4倍。 在电路级噪声模型下，这套同步策略带来的逻辑错误率下降，还能让解码延迟最高提速2.2倍。

## 英文关键词

Synchronization, Surface Code, Lattice Surgery, Quantum Error Correction, Fault Tolerance, Quantum Computing Systems

## 中文关键词

同步, 表面码, 晶格手术, 量子纠错, 容错, 量子计算系统

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15092177)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730991)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2025](../index.md)
