---
title: "Shared Metadata Field: A Dynamic ECC/DBI Allocation to Improve Reliability and I/O Power Efficiency for LPDDR6"
description: "MICRO 2026 · Session 8B · 共享元数据字段：动态分配 ECC 与 DBI 以提高 LPDDR6 可靠性及 I/O 能效"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# Shared Metadata Field: A Dynamic ECC/DBI Allocation to Improve Reliability and I/O Power Efficiency for LPDDR6

**中文标题：** 共享元数据字段：动态分配 ECC 与 DBI 以提高 LPDDR6 可靠性及 I/O 能效

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Jongwoo Jeon, Youngbae Kong, Junki Lee, Jae-Youn Hong, Joon-Sung Yang

**来源：** MICRO 2026，pp. 2879–2894；[DOI](https://doi.org/10.1109/MICRO67795.2026.00195)

## 英文摘要

LPDDR6 deploys metadata for Error Correcting Code (ECC) to enhance reliability and Data Bus Inversion (DBI) to reduce I/O power. However, the limited 32-bit metadata field budget of LPDDR6 constrains the simultaneous enhancement of both functions. In most cases, DRAM READ operations are error-free, which allows more metadata bits to be used for DBI to further reduce I/O power. Conversely, when an error is detected, metadata bits can instead be used for ECC to maintain reliability. Motivated by this asymmetry, this paper proposes the Shared Metadata Field (SMF), which dynamically reconfigures the metadata field between ECC and DBI. SMF allows both ECC and DBI to utilize more metadata bits according to error conditions, improving reliability and I/O power efficiency without requiring additional pins or transfer cycles. During prevalent error-free operations, the metadata field is allocated for finer-grained DBI flags (DBI-26/24) to maximize I/O power savings. Otherwise, when an error is detected on the memory die, DRAM transmits Reed-Solomon double-symbol-correcting (RS-DSC) parity to maintain system-level data integrity. To enable this dynamic operation under LPDDR6's strict hardware constraints, the SMF architecture places a lightweight Encoder and Error Detector on the memory-side, offloading the complex Decoder logic to the memory controller-side. Evaluation results show that SMF reduces I/O power by 3.8%–7.6% relative to the LPDDR6 standard DBI baseline across CPU and GPU workloads. Moreover, SMF corrects all random double-bit errors and single-byte peripheral faults while reducing on-die ECC area by 13% compared to a conventional SEC-DED implementation.

## 中文摘要

LPDDR6 部署纠错码 (ECC) 元数据以增强可靠性，并部署数据总线反转 (DBI) 以降低 I/O 功耗。然而，LPDDR6有限的32位元数据字段预算限制了这两种功能的同时增强。在大多数情况下，DRAM READ 操作是无错误的，这允许将更多元数据位用于 DBI，以进一步降低 I/O 功耗。相反，当检测到错误时，元数据位可以改为用于 ECC 以保持可靠性。受这种不对称性的启发，本文提出了共享元数据字段（SMF），它动态地重新配置 ECC 和 DBI 之间的元数据字段。 SMF 允许 ECC 和 DBI 根据错误情况利用更多元数据位，从而提高可靠性和 I/O 功率效率，而无需额外的引脚或传输周期。在普遍的无错误操作期间，元数据字段被分配给更细粒度的 DBI 标志 (DBI-26/24)，以最大限度地节省 I/O 功耗。否则，当在内存芯片上检测到错误时，DRAM 会传输里德-所罗门双符号校正 (RS-DSC) 奇偶校验以维持系统级数据完整性。为了在 LPDDR6 严格的硬件限制下实现这种动态操作，SMF 架构在内存侧放置了轻量级编码器和错误检测器，将复杂的解码器逻辑卸载到内存控制器侧。评估结果显示，相对于 LPDDR6 标准 DBI 基准，SMF 在 CPU 和 GPU 工作负载方面将 I/O 功耗降低了 3.8%–7.6%。此外，与传统的 SEC-DED 实现相比，SMF 可以纠正所有随机双位错误和单字节外设故障，同时将片上 ECC 面积减少 13%。

## 中文关键词

LPDDR6；共享元数据字段；纠错码；数据总线反转；内存可靠性；输入输出功耗

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
