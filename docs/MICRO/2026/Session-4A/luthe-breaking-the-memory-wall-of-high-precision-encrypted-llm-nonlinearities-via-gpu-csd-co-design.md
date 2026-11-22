---
title: "LUTHE: Breaking the Memory Wall of High-Precision Encrypted LLM Nonlinearities via GPU-CSD Co-Design"
description: "MICRO 2026 · Session 4A · LUTHE：通过 GPU-CSD 协同设计突破高精度加密 LLM 非线性运算的内存墙"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
  - "Cryptography"
  - "HW-SW Co-design"
---

# LUTHE: Breaking the Memory Wall of High-Precision Encrypted LLM Nonlinearities via GPU-CSD Co-Design

**中文标题：** LUTHE：通过 GPU-CSD 协同设计突破高精度加密 LLM 非线性运算的内存墙

**所属 Session：** [Session 4A](index.md) · [MICRO 2026](../index.md)

**作者：** Xiurui Pan, Guoci Chen, Guangyu Sun, Mingzhe Zhang, Jie Zhang

**来源：** MICRO 2026，pp. 1365–1380；[DOI](https://doi.org/10.1109/MICRO67795.2026.00102)

## 英文摘要

Cloud-based Large Language Model (LLM) inference raises severe privacy concerns, motivating end-to-end encrypted inference with Fully Homomorphic Encryption (FHE). However, practical encrypted inference is bottlenecked by high precision nonlinear operators (e.g., Softmax and GELU). TFHE’s Without-Padding Programmable Bootstrapping (WoP-PBS) enables exact high-precision nonlinear computation on encrypted data, but each invocation streams hundreds of megabytes to gigabytes of cryptographic keys. Once the key working set exceeds on-device memory capacity, execution hits a sharp capacity cliff: repeated streaming of KSK-family keys over PCIe dominates end-to-end execution time. To address this, we propose LUTHE, a heterogeneous architecture that co-designs a GPU with a Computational Storage Drive (CSD). Specifically, LUTHE partitions the WoP-PBS chain at primitive granularity: key bound primitives that consume the dominant KSK-family keys execute on the CSD near flash-resident keys, while compute bound primitives that consume the compact BSK remain on the GPU. LUTHE introduces a unified kernel that fuses all three WoP-PBS evaluation stages to eliminate cross-mode arbitration bubbles, and an FTL-bypass key-stream subsystem for jitter-free key delivery. Evaluations demonstrate that when key working sets exceed on-device memory, LUTHE reduces the latency of en crypted high-precision nonlinear computation by up to 16 &times; over the GPU-spill baseline for single-request nonlinear workloads.

## 中文摘要

基于云的大语言模型 (LLM) 推理引起了严重的隐私问题，激发了使用完全同态加密 (FHE) 进行端到端加密推理。然而，实际的加密推理受到高精度非线性算子（例如 Softmax 和 GELU）的瓶颈。 TFHE 的无填充可编程引导 (WoP-PBS) 可对加密数据进行精确的高精度非线性计算，但每次调用都会传输数百兆字节到千兆字节的加密密钥。一旦密钥工作集超过设备上的内存容量，执行就会遇到急剧的容量悬崖：通过 PCIe 重复传输 KSK 系列密钥将主导端到端执行时间。为了解决这个问题，我们提出了 LUTHE，这是一种异构架构，可共同设计 GPU 与计算存储驱动器 (CSD)。具体来说，LUTHE 在基元粒度上对 WoP-PBS 链进行分区：使用主要 KSK 系列密钥的键绑定基元在靠近闪存驻留密钥的 CSD 上执行，而使用紧凑 BSK 的计算绑定基元则保留在 GPU 上。 LUTHE 引入了一个统一内核，该内核融合了所有三个 WoP-PBS 评估阶段以消除跨模式仲裁泡沫，以及一个用于无抖动密钥传送的 FTL 旁路密钥流子系统。评估表明，当关键工作集超出设备内存时，LUTHE 可以将加密高精度非线性计算的时延降低至单请求非线性工作负载的 GPU 溢出基线的 16 倍。

## 中文关键词

全同态加密；加密大语言模型推理；可编程自举；计算存储；GPU 与计算存储设备协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4A](index.md) · [MICRO 2026 主页](../index.md)
