---
title: "A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs"
description: "ASPLOS 2026 · Session 4D · 面向长上下文 LLM 离线推理的高性价比近存储处理方案"
tags:
  - "ASPLOS2026"
  - "Session 4D"
  - "Processing-in-Memory"
---

# A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs

**中文标题：** 面向长上下文 LLM 离线推理的高性价比近存储处理方案

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hongsun Jang (Seoul National University), Jaeyong Song (Seoul National University), Changmin Shin (Seoul National University), Si Ung Noh (Seoul National University), Jaewon Jung (Seoul National University), Jisung Park (POSTECH (Pohang University of Science and Technology)), Jinho Lee (Seoul National University)

**单位：** Seoul National University；POSTECH (Pohang University of Science and Technology)

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790119) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The computational and memory demands of large language models for generative inference present significant challenges for practical deployment. One promising solution targeting offline inference is offloading-based batched inference, which extends the GPU's memory hierarchy with host memory and storage. However, it often suffers from substantial I/O overhead, primarily due to the large KV cache sizes that scale with batch size and context window length. In this paper, we introduce HILOS, a framework that boosts offline inference throughput using near-storage processing. The core of HILOS is attention near storage, which offloads memory-intensive attention operations to near-storage accelerators, reducing traffic across the system interconnect. Building on attention near storage, HILOS incorporates three additional optimizations. First, cooperative X-cache minimizes KV cache I/O by exploiting available host resources after offloading. Second, delayed KV cache writeback hides storage write latency and mitigates storage write amplification. Finally, a memory-efficient attention accelerator sustains high throughput for long sequences within the resource constraints of NSP devices. We implemented and evaluated HILOS on a real system equipped with 16 SmartSSDs. Compared to state-of-the-art offloading-based inference frameworks, HILOS achieves up to 7.86× throughput while reducing energy consumption by up to 85%. The source code for HILOS is

## 中文摘要

大语言模型生成式推理的计算与存储需求给实际部署带来了重大挑战。面向离线推理的一种有前景的方案是基于卸载（offloading）的批量推理，它利用主机内存和存储扩展 GPU 的存储层次。然而，由于 KV cache 大小随批量大小和上下文窗口长度增长，该方案常常承受巨大的 I/O 开销。本文提出 HILOS，一个利用近存储处理提升离线推理吞吐量的框架。HILOS 的核心是近存储注意力（attention near storage），它将访存密集的注意力操作卸载到近存储加速器，从而减少跨系统互连的流量。在近存储注意力的基础上，HILOS 还包含三项额外优化。第一，协作式 X-cache 通过利用卸载后空闲的主机资源，最小化 KV cache 的 I/O。第二，延迟的 KV cache 写回（delayed KV cache writeback）隐藏存储写延迟并缓解存储写放大。最后，一个访存高效的注意力加速器在 NSP 设备的资源约束下为长序列维持高吞吐量。我们在配备 16 块 SmartSSD 的真实系统上实现并评估了 HILOS。与最先进的基于卸载的推理框架相比，HILOS 实现最高 7.86× 的吞吐量，同时将能耗降低最高 85%。HILOS 的源代码可在

## 英文关键词

Near-Storage Processing, Transformer-Based Generative Model, FPGA, Batch Inference

## 中文关键词

近存储处理；基于 Transformer 的生成模型；FPGA；批量推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790119)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2026](../index.md)
