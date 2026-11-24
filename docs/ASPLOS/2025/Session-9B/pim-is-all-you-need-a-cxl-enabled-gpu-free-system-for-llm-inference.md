---
title: "PIM is All You Need: A CXL-Enabled GPU-Free System for LLM Inference"
description: "ASPLOS 2025 · Session 9B · PIM 就是全部所需：一种基于 CXL 的无 GPU 大语言模型推理系统"
tags:
  - "ASPLOS2025"
  - "Session 9B"
  - "Processing in Memory"
---

# PIM is All You Need: A CXL-Enabled GPU-Free System for LLM Inference

**中文标题：** PIM 就是全部所需：一种基于 CXL 的无 GPU 大语言模型推理系统

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yufeng Gu (University of Michigan), Alireza Khadem (University of Michigan), Sumanth Umesh (University of Michigan), Ning Liang (University of Michigan), Xavier Servot (ETH Zurich), Onur Mutlu (ETH Zurich), Ravi Iyer (Google), Reetuparna Das (University of Michigan)

**单位：** University of Michigan；ETH Zurich；Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716267) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Large Language Model (LLM) inference uses an autoregressive manner to generate one token at a time, which exhibits notably lower operational intensity compared to earlier Machine Learning (ML) models such as encoder-only transformers and Convolutional Neural Networks. At the same time, LLMs possess large parameter sizes and use key-value caches to store context information. Modern LLMs support context windows with up to 1 million tokens to generate versatile text, audio, and video content. A large key-value cache unique to each prompt requires a large memory capacity, limiting the inference batch size. Both low operational intensity and limited batch size necessitate a high memory bandwidth. However, contemporary hardware systems for ML model deployment, such as GPUs and TPUs, are primarily optimized for compute throughput. This mismatch challenges the efficient deployment of advanced LLMs and makes users to pay for expensive compute resources that are poorly utilized for the memory-bound LLM inference tasks. We propose CENT, a CXL-ENabled GPU-Free sysTem for LLM inference, which harnesses CXL memory expansion capabilities to accommodate substantial LLM sizes, and utilizes near-bank processing units to deliver high memory bandwidth, eliminating the need for expensive GPUs. CENT ∗Yufeng Gu r-to-peer and collective communication primitives across CXL devices. We implement various parallelism strategies to distribute LLMs across these devices. Compared to GPU baselines with maximum supported batch sizes and similar average power, CENT achieves 2.3× higher throughput and consumes 2.3× less energy. CENT reduces the Total Cost of Ownership (TCO), generating 5.2× more tokens per dollar than GPUs.

## 中文摘要

大语言模型（LLM）推理采用自回归方式逐个生成 token，与早期的机器学习（ML）模型（如仅编码器 Transformer 和卷积神经网络）相比，其运算强度明显更低。与此同时，LLM 拥有庞大的参数规模，并使用键值缓存（key-value cache）存储上下文信息。现代 LLM 支持多达 100 万个 token 的上下文窗口，以生成多样化的文本、音频和视频内容。每个提示（prompt）独有的庞大键值缓存需要很大的内存容量，从而限制了推理的批大小（batch size）。低运算强度与受限的批大小这两者都要求高内存带宽。然而，当代用于 ML 模型部署的硬件系统（如 GPU 和 TPU）主要针对计算吞吐量进行优化。这种不匹配使先进 LLM 的高效部署面临挑战，并迫使用户为昂贵却难以被内存受限型 LLM 推理任务充分利用的计算资源付费。我们提出 CENT，一种面向 LLM 推理的 CXL 使能无 GPU 系统（CXL-ENabled GPU-Free sysTem），它利用 CXL 内存扩展能力来容纳规模可观的 LLM，并利用近 bank（near-bank）处理单元提供高内存带宽，从而消除对昂贵 GPU 的需求。CENT 支持跨 CXL 设备的对等（peer-to-peer）与集合通信原语。我们在这些设备上实现多种并行策略以分布 LLM。与采用最大支持批大小和相近平均功耗的 GPU 基线相比，CENT 实现了 2.3× 的吞吐提升，并消耗 2.3× 更少的能耗。CENT 降低了总拥有成本（TCO），每美元生成的 token 数比 GPU 多 5.2×。

## 英文关键词

Computer Architecture, Processing-In-Memory, Compute Express Link, Generative Artificial Intelligence, Large Language Models

## 中文关键词

计算机体系结构；存内计算；Compute Express Link；生成式人工智能；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716267)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2025](../index.md)
