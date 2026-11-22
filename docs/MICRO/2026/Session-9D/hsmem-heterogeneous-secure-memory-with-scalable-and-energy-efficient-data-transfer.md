---
title: "HSMEM: Heterogeneous Secure Memory with Scalable and Energy-Efficient Data Transfer"
description: "MICRO 2026 · Session 9D · HSMEM：支持可扩展高能效数据传输的异构安全内存"
tags:
  - "MICRO2026"
  - "Energy Efficiency"
---

# HSMEM: Heterogeneous Secure Memory with Scalable and Energy-Efficient Data Transfer

**中文标题：** HSMEM：支持可扩展高能效数据传输的异构安全内存

**所属 Session：** [Session 9D](index.md) · [MICRO 2026](../index.md)

**作者：** Sheng Qiang, Shulin Fan, Jinyu Gu, Zhichao Hua, Yubin Xia

**来源：** MICRO 2026，pp. 3479–3496；[DOI](https://doi.org/10.1109/MICRO67795.2026.00232)

## 英文摘要

The growing deployment of large language models (LLMs) and other AI applications has made GPU trusted execution environments (TEEs) critical for protecting valuable model weights and sensitive user data. Secure memory is essential for these TEEs to guarantee memory confidentiality, integrity, and freshness against physical attacks. While specialized secure memory architectures have been developed for CPUs and GPUs to optimize performance on each side, their architectural differences—distinct encryption schemes, integrity trees, and cacheline sizes—complicate CPU-GPU data transfers. Specifically, transferring data between the CPU and GPU requires switching protection modes, resulting in severely limited transfer bandwidth and increased energy consumption. For example, the NVIDIA H100's CPU-GPU secure memory transfer bandwidth is only 4 GB/s, whereas the theoretical bandwidth of PCIe 7.0 reaches 242 GB/s. Moreover, this switching introduces a 26.16× energy overhead to PCIe memory transfers, even with a dedicated hardware switching engine. We observe that protection mode switching is analogous to a pair of secure memory read and write operations. Building on this insight, we propose HSMEM, a heterogeneous secure memory architecture that defers and merges mode switching with subsequent read and write accesses to the transferred region. HSMEM introduces Multi-mode Memory Protection to enable state-of-the-art secure memory designs on both the CPU and GPU, and Mode-preserved Transfer to facilitate CPU-GPU memory transfers without protection mode switching. Our prototype demonstrates that HSMEM achieves efficient CPU-GPU memory transfer that scales with interconnect bandwidth while conserving energy. HSMEM attains 92.7% of the interconnect bandwidth. With PCIe 7.0, HSMEM improves transfer throughput by 8.96× and reduces the energy consumption of data transfers by 98.2% on average compared to dedicated hardware strawman designs.

## 中文摘要

大语言模型 (LLM) 和其他人工智能应用程序的部署不断增加，使得 GPU 可信执行环境 (TEE) 对于保护宝贵的模型权重和敏感用户数据至关重要。安全内存对于这些 TEE 来说至关重要，以确保内存机密性、完整性和新鲜度以抵御物理攻击。虽然已经为 CPU 和 GPU 开发了专门的安全内存架构来优化双方的性能，但它们的架构差异（不同的加密方案、完整性树和缓存行大小）使 CPU-GPU 数据传输变得复杂。具体来说，CPU和GPU之间传输数据需要切换保护模式，导致传输带宽严重受限，能耗增加。例如，NVIDIA H100的CPU-GPU安全内存传输带宽仅为4GB/s，而PCIe 7.0的理论带宽达到242GB/s。此外，即使使用专用的硬件交换引擎，这种交换也会给 PCIe 内存传输带来 26.16 倍的能量开销。我们观察到保护模式切换类似于一对安全存储器读写操作。基于这一见解，我们提出了 HSMEM，这是一种异构安全内存架构，它推迟并合并模式切换与对传输区域的后续读写访问。 HSMEM 引入了多模式内存保护，可在 CPU 和 GPU 上实现最先进的安全内存设计，并引入模式保留传输，以促进 CPU-GPU 内存传输，而无需保护模式切换。我们的原型表明，HSMEM 实现了高效的 CPU-GPU 内存传输，可根据互连带宽进行扩展，同时节省能源。 HSMEM 获得了 92.7% 的互连带宽。借助 PCIe 7.0，与专用硬件稻草人设计相比，HSMEM 将传输吞吐量提高了 8.96 倍，并将数据传输能耗平均降低了 98.2%。

## 中文关键词

机密计算；安全内存；异构系统；可扩展数据传输；能效

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21507078](https://doi.org/10.5281/zenodo.21507078)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9D](index.md) · [MICRO 2026 主页](../index.md)
