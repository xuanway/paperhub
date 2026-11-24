---
title: "COMET: Towards Practical W4A4KV4 LLMs Serving"
description: "ASPLOS 2025 · Session 7A · COMET：迈向实用的 W4A4KV4 大语言模型服务"
tags:
  - "ASPLOS2025"
  - "Session 7A"
  - "Serving LLMs"
---

# COMET: Towards Practical W4A4KV4 LLMs Serving

**中文标题：** COMET：迈向实用的 W4A4KV4 大语言模型服务

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Lian Liu (Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Long Cheng (North China Electric Power University), Haimeng Ren (ShanghaiTech University), Zhaohui Xu (ShanghaiTech University), Yudong Pan (Institute of Computing Technology, CAS,University of Chinese Academy of Sciences), Mengdi Wang (Institute of Computing Technology, CAS), Xiaowei Li (Institute of Computing Technology, CAS,Zhongguancun Laboratory), Yinhe Han (Institute of Computing Technology, CAS), Ying Wang (Institute of Computing Technology, CAS)

**单位：** Institute of Computing Technology, CAS,University of Chinese Academy of Sciences；North China Electric Power University；ShanghaiTech University；Institute of Computing Technology, CAS；Institute of Computing Technology, CAS,Zhongguancun Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716252) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Quantization is a widely-used compression technology to reduce the overhead of serving large language models (LLMs) on terminal devices and in cloud data centers. However, prevalent quantization methods, such as 8-bit weight-activation or 4-bit weight-only quantization, achieve limited performance improvements due to poor support for low-precision (e.g., 4-bit) activation. This work, for the first time, realizes practical W4A4KV4 serving for LLMs, fully utilizing the INT4 tensor cores on modern GPUs and reducing the memory bottleneck caused by the KV cache. Specifically, we propose a novel fine-grained mixed-precision quantization algorithm (FMPQ) that compresses most activations into 4bit with negligible accuracy loss. To support mixed-precision matrix multiplication for W4A4 and W4A8, we develop a highly optimized W4Ax kernel. Our approach introduces a novel mixed-precision data layout to facilitate access and fast dequantization for activation and weight tensors, utilizing the GPU's software pipeline to hide the overhead of data loading and conversion. Additionally, we propose fine-grained streaming multiprocessor (SM) scheduling to achieve load balance across different SMs. We integrate the optimized T, and provide efficient management to support popular LLMs such as LLaMA-3-70B. Extensive evaluations demonstrate that, when running LLaMA family models on a single A100-80GSMX4, COMET achieves a kernel-level speedup of 2.88× over cuBLAS and a 2.02× throughput improvement compared to TensorRT-LLM from an end-to-end framework perspective.

## 中文摘要

量化是一种被广泛使用的压缩技术，用于降低在终端设备和云数据中心中服务大语言模型（LLM）的开销。然而，主流量化方法（如 8 位权重-激活量化或 4 位权重仅量化）由于对低精度（如 4 位）激活的支持不佳，取得的性能提升有限。本工作首次为 LLM 实现了实用的 W4A4KV4 服务，充分利用现代 GPU 上的 INT4 张量核心，并减少 KV cache 带来的内存瓶颈。具体而言，我们提出一种新颖的细粒度混合精度量化算法（FMPQ），可将大多数激活压缩到 4 位，而精度损失可忽略。为支持 W4A4 与 W4A8 的混合精度矩阵乘法，我们开发了高度优化的 W4Ax 内核。我们的方法引入一种新颖的混合精度数据布局，以便对激活和权重张量进行访问与快速反量化，并利用 GPU 的软件流水线隐藏数据加载与转换的开销。此外，我们提出细粒度的流式多处理器（SM）调度，以实现不同 SM 之间的负载均衡。我们集成了优化后的 T，并提供高效管理以支持 LLaMA-3-70B 等流行 LLM。大量评估表明，在单台 A100-80GSMX4 上运行 LLaMA 系列模型时，COMET 相较 cuBLAS 实现了 2.88× 的内核级加速，从端到端框架角度看相较 TensorRT-LLM 实现了 2.02× 的吞吐提升。

## 英文关键词

Large Language Models (LLM) Serving, LLM Quantization, Algorithm-System Co-design

## 中文关键词

大语言模型（LLM）服务；LLM 量化；算法-系统协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716252)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2025](../index.md)
