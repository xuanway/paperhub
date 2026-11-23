---
title: "LIA: A Single-GPU LLM Inference Acceleration with Cooperative AMX-Enabled CPU-GPU Computation and CXL Offloading"
description: "ISCA 2025 · Session 4A · LIA: 基于AMX的CPU-GPU协作与CXL卸载的单GPU LLM推理加速"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# LIA: A Single-GPU LLM Inference Acceleration with Cooperative AMX-Enabled CPU-GPU Computation and CXL Offloading

**中文标题：** LIA: 基于AMX的CPU-GPU协作与CXL卸载的单GPU LLM推理加速

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Hyungyo Kim, Nachuan Wang, Qirong Xia, Jinghan Huang, Amir Yazdanbakhsh, Nam Sung Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731092) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The limited memory capacity of single GPUs constrains large lan- guage model (LLM) inference, necessitating cost-prohibitive multi- GPU deployments or frequent performance-limiting CPU-GPU transfers over slow PCIe. In this work, we first benchmark re- cent Intel CPUs with Advanced Matrix Extensions (AMX), includ- ing 4th generation (Sapphire Rapids) and 6th generation (Gran- ite Rapids) Xeon Scalable Processors, demonstrating matrix multi- plication throughput of 20 TFLOPS and 40 TFLOPS, respectively— comparable to some recent GPUs. These findings unlock more extensive computation offloading to CPUs, reducing CPU-GPU transfers and alleviating throughput bottlenecks compared to prior- generation CPUs. Building on these insights, we design LIA, a single-GPU LLM inference acceleration framework leveraging coop- erative AMX-enabled CPU-GPU computation and CXL offloading. LIA systematically offloads computation to CPUs, optimizing both latency and throughput. The framework also introduces a memory- offloading policy that seamlessly integrates affordable CXL memory with DDR memory to enhance performance in throughput-driven tasks. On Saphhire Rapids (Granite Rapids) systems with a single H100 GPU, LIA achieves up to 5.1×(19×) lower latency and 3.7× (5.1×) higher throughput compared to the latest single-GPU of- floading framework. Furthermore, LIA deploying CXL offloading yields an additional 1.5×throughput improvement over LIA using only DDR memory with a 1.8×increase in maximum batch size (900→1.6K).

## 中文摘要

单GPU的内存容量限制制约了大语言模型（LLM）推理，要么需要成本高昂的多GPU部署，要么只能通过低速PCIe频繁进行CPU-GPU数据搬运，拖累性能。本文首先对搭载高级矩阵扩展（AMX）的新款Intel CPU开展基准测试，包括第四代（Sapphire Rapids）与第六代（Granite Rapids）至强可扩展处理器，二者矩阵乘法吞吐分别达到20 TFLOPS、40 TFLOPS，和部分新款GPU相当。该结论说明可以把更多计算卸载到CPU，相比上一代CPU，减少CPU-GPU之间的数据传输，缓解吞吐瓶颈。基于该发现，本文设计LIA，一个单GPU下的LLM推理加速框架，利用支持AMX的CPU-GPU协同计算以及CXL卸载。LIA将计算按策略卸载至CPU，同时优化延迟与吞吐。该框架还提出内存卸载策略，将高性价比的CXL内存与DDR内存无缝融合，提升吞吐型任务的性能。在搭载单张H100的Sapphire Rapids（Granite Rapids）平台上，对比最新单GPU卸载框架，LIA最高可将延迟降低至原来的1/5.1（1/19），吞吐提升3.7倍（5.1倍）。此外，启用CXL卸载的LIA相比仅使用DDR内存的LIA，吞吐再提升1.5倍，最大批大小提升1.8倍（从900提升至1600）。

## 英文关键词

LLM Inference, GPU-CPU Cooperative Computing, AMX, CXL

## 中文关键词

LLM 推理, GPU-CPU 协同计算, AMX, CXL

## 代码与研究制品

- [代码仓库](https://github.com/ece-fast-lab/ISCA-2025-LIA)
- [代码仓库](https://github.com/Hyungyo1/LIA_AMXGPU)
- [研究制品](https://zenodo.org/records/15104666)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731092)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
