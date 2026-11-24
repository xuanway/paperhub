---
title: "FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations"
description: "ASPLOS 2026 · Session 5B · FlashMem：通过 GPU 内存层次优化在移动端支持现代 DNN 工作负载"
tags:
  - "ASPLOS2026"
  - "Session 5B"
  - "On-Device & Edge AI"
---

# FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations

**中文标题：** FlashMem：通过 GPU 内存层次优化在移动端支持现代 DNN 工作负载

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhihao Shu (University of Georgia), Md Musfiqur Rahman Sanim (University of Georgia), Hangyu Zheng (University of Georgia), Kunxiong Zhu (University of Georgia), Miao Yin (University of Texas at Arlington), Gagan Agrawal (University of Georgia), Wei Niu (University of Georgia)

**单位：** University of Georgia；University of Texas at Arlington

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790164) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The increasing size and complexity of modern deep neural networks (DNNs) pose significant challenges for on-device inference on mobile GPUs, with limited memory and computational resources. Existing DNN acceleration frameworks primarily deploy a weight preloading strategy, where all model parameters are loaded into memory before execution on mobile GPUs. We posit that this approach is not adequate for modern DNN workloads that comprise very large model(s) and possibly execution of several distinct models in succession. In this work, we introduce FlashMem, a memory streaming framework designed to efficiently execute large-scale modern DNNs and multi-DNN workloads while minimizing memory consumption and reducing inference latency. Instead of fully preloading weights, FlashMem statically determines model loading schedules and dynamically streams them on demand, leveraging 2.5D texture memory to minimize data transformations and improve execution efficiency. Experimental results on 11 models demonstrate that FlashMem achieves 2.0× to 8.4× memory reduction and 1.7× to 75.0× speedup compared to existing frameworks, enabling efficient execution of large-scale models and multi-DNN support on resource-constrained mobile GPUs.

## 中文摘要

现代深度神经网络（DNN）规模与复杂度的不断增长，为在内存和计算资源有限的移动 GPU 上进行端侧推理带来了重大挑战。现有的 DNN 加速框架主要采用权重预加载策略，即在移动 GPU 上执行之前将所有模型参数加载到内存中。我们认为，对于包含超大模型、且可能连续执行多个不同模型的现代 DNN 工作负载而言，这种做法并不充分。在本工作中，我们提出 FlashMem，一个内存流式传输框架，旨在高效执行大规模现代 DNN 与多 DNN 工作负载，同时最小化内存占用并降低推理延迟。FlashMem 并不完整预加载权重，而是静态确定模型加载调度并按需动态流式传输，利用 2.5D 纹理内存来最小化数据变换并提升执行效率。在 11 个模型上的实验结果表明，与现有框架相比，FlashMem 实现了 2.0× 至 8.4× 的内存缩减和 1.7× 至 75.0× 的加速，从而能够在资源受限的移动 GPU 上高效执行大规模模型并支持多 DNN。

## 英文关键词

Multi-Model Co-running, Machine Learning, Mobile, Memory Management

## 中文关键词

多模型协同运行；机器学习；移动端；内存管理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790164)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2026](../index.md)
