---
title: "AiF: Accelerating On-Device LLM Inference Using In-Flash Processing"
description: "ISCA 2025 · Session 4A · AiF: 利用片内闪存处理实现端侧LLM推理加速"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# AiF: Accelerating On-Device LLM Inference Using In-Flash Processing

**中文标题：** AiF: 利用片内闪存处理实现端侧LLM推理加速

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Jaeyong Lee, Hyunjoo Kim, Sanghoon Oh, Myoungjun Chun, Myungsuk Kim, Jihong Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731073) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

While large language models (LLMs) achieve remarkable perfor- mance across diverse application domains, their substantial memory demands present challenges, especially on personal devices with limited DRAM capacity. Recent LLM inference engines have in- troduced SSD offloading for model parameters to reduce memory footprint. However, the highly memory-bound nature of on-device LLMs makes inference speed heavily dependent on read bandwidth, leading to significant performance degradation due to the limited bandwidth of SSDs. In this paper, we propose an in-flash process- ing solution for on-device LLM, called Accelerator-in-Flash (AiF), which integrates matrix-vector multiplication (GEMV) operations directly into flash chips. By enabling in-flash GEMV operations, AiF leverages the high internal bandwidth of flash chips without being constrained by the limited external bandwidth. Building on this core structure, AiF employs two novel flash read techniques that were specifically optimized for reading LLM parameters stored in flash memory. AiF achieves a 4x boost in internal read band- width during inference with minimal implementation overhead, thanks to its streamlined error correction process. Evaluations on eight real-world LLMs reveal that AiF provides a 14.6x through- put improvement compared to baseline SSD offloading schemes. Furthermore, AiF surpasses in-memory inference, delivering 1.4x higher throughput with a significantly reduced memory footprint.

## 中文摘要

虽然大语言模型（LLM）在各类应用场景中表现出色，但其巨大的内存需求带来了难题，尤其对于DRAM容量有限的终端设备。近期的LLM推理引擎采用SSD卸载模型参数，以此降低内存占用。但终端侧LLM属于强访存密集型负载，推理速度高度依赖读带宽，SSD带宽有限会造成性能大幅下降。本文提出面向终端LLM的闪存内计算方案AiF（Accelerator-in-Flash），将矩阵-向量乘法（GEMV）直接集成在闪存芯片内部。借助闪存内GEMV运算，AiF利用闪存芯片的内部高带宽，不再受限于外部带宽瓶颈。基于该核心结构，AiF采用两项专门针对闪存中LLM参数读取优化的新型闪存读取技术。依托精简的纠错流程，AiF在推理时将内部读带宽提升4倍，实现开销极小。在八个真实大模型上的评测表明：相比基线SSD卸载方案，AiF吞吐量提升14.6倍；同时性能超越内存内推理，吞吐量提升1.4倍，内存占用大幅降低。

## 英文关键词

Flash Memory, In-Flash Processing, On-Device LLM Inference

## 中文关键词

闪存, 闪存内计算, 设备上 LLM 推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731073)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
