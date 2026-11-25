---
title: "A Fully GPU-Accelerated Framework for High-Performance Configuration Interaction Selection with Neural Network Quantum States"
description: "HPDC 2026 · Session 5 — Scientific Applications at Scale"
tags:
  - "HPDC2026"
  - "Session 5"
  - "Scientific Applications at Scale"
---

# A Fully GPU-Accelerated Framework for High-Performance Configuration Interaction Selection with Neural Network Quantum States

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 5</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807583)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#SunKLZLLZFHGLSZ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#SunKLZLLZFHGLSZ26)

**作者**：Daran Sun, Bowen Kan, Haoquan Long, Hairui Zhao, Haoxu Li, Yicheng Liu, Pengyu Zhou, Ankang Feng, Wenjing Huang, Yida Gu, Zhenyu Li, Honghui Shang, Yunquan Zhang, Dingwen Tao, Ninghui Sun, Guangming Tan

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）

---

## 英文摘要

AI-driven methods have demonstrated considerable success in tackling the central challenge of accurately solving the Schrödinger equation for complex many-body systems. Among neural network quantum state (NNQS) approaches, the NNQS-SCI (Selected Configuration Interaction) method stands out as a state-of-the-art technique, recognized for its high accuracy and scalability. However, its application to larger systems is severely constrained by a hybrid CPU-GPU architecture. Specifically, centralized CPU-based global de-duplication creates a severe scalability barrier due to communication bottlenecks, while host-resident coupled-configuration generation induces prohibitive computational overheads. We introduce QiankunNet-cuSCI, a fully GPU-accelerated SCI framework designed to overcome these bottlenecks. It first integrates a distributed, load-balanced global de-duplication algorithm to minimize redundancy and communication overhead at scale. To address compute limitations, it employs specialized, fine-grained CUDA kernels for exact coupled configuration generation. Finally, to break the single-GPU memory barrier exposed by this full acceleration, it incorporates a GPU memory-centric runtime featuring GPU-side pooling, streaming mini-batches, and overlapped offloading. This design enables much larger configuration spaces and shifts the bottleneck from host-side limitations back to on-device inference. Our evaluation demonstrates that our work fundamentally expands the scale of solvable problems. On an NVIDIA A100 cluster with 64 GPUs, our work achieves up to 2.32× end-to-end speedup over the highly-optimized NNQS-SCI baseline while preserving the same chemical accuracy. Furthermore, it demonstrates excellent distributed performance, maintaining over 90% parallel efficiency in strong scaling tests.

## 中文摘要

AI 驱动的方法在应对精确求解复杂多体系统薛定谔方程这一核心挑战上取得了相当的成功。在神经网络量子态（NNQS）方法中，NNQS-SCI（选择组态相互作用）方法作为一种最先进技术脱颖而出，以高精度和可扩展性著称。然而，其向更大系统的应用受到 CPU-GPU 混合架构的严重制约。具体而言，集中式的基于 CPU 的全局去重因通信瓶颈造成严重的可扩展性障碍，而驻留主机的耦合组态生成带来难以承受的计算开销。我们提出 QiankunNet-cuSCI，一个完全 GPU 加速的 SCI 框架，旨在克服这些瓶颈。它首先集成分布式的负载均衡全局去重算法，在大规模下最小化冗余与通信开销。为应对计算限制，它采用专门、细粒度的 CUDA 核进行精确的耦合组态生成。最后，为突破这种完全加速所暴露的单 GPU 显存壁垒，它引入以 GPU 显存为中心的运行时，具备 GPU 端池化、流式小批次与重叠卸载。该设计支持大得多的组态空间，并将瓶颈从主机侧限制转回设备端推理。我们的评估表明，本工作从根本上扩展了可求解问题的规模。在配备 64 块 GPU 的 NVIDIA A100 集群上，本工作相比高度优化的 NNQS-SCI 基线取得最高 2.32 倍端到端加速，同时保持相同的化学精度。此外，它展现出优异的分布式性能，在强扩展测试中保持 90% 以上的并行效率。

## 英文关键词

GPU, neural network quantum state, quantum chemistry, many-body Schrodinger equation.

## 中文关键词

GPU，神经网络量子态，量子化学，多体薛定谔方程。

---

[← 返回 Session 5 — Scientific Applications at Scale](index.md)
