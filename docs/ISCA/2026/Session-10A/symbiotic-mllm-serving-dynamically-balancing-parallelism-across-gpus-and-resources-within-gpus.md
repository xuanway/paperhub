---
title: "Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs"
description: "ISCA 2026 · Session 10A · Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs"
tags:
  - "ISCA2026"
  - "Session 10A"
  - "LLM 5"
---

# Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs

**中文标题：** 共生 MLLM 服务：在 GPU 之间与 GPU 内部资源间动态平衡并行度

**所属 Session：** [Session 10A](index.md) · [ISCA 2026](../index.md)

**作者：** Zhicheng Li, Jiacheng Zhao, Yangyu Zhang, Zhaolin Duan, Xinyu Liu, Siqi Li, Shuoming Zhang, Shuaijiang Li, Donglin Yu, Yuan Wen, Chunwei Xia, Xiyu Shi, Huimin Cui

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Multimodal Large Language Models (MLLMs) present a key serving challenge. Existing systems usually extend text-only LLM stacks. They either co-locate the vision encoder with the decoder on the same GPUs or move it to a fixed GPU pool. Both choices rely on ahead-of-time, static decisions for parallelism and GPU allocation. They ignore a key asymmetry in MLLMs: the encoder has a small memory footprint but input-dependent, often quadratic, compute cost, while the decoder is both memory- and compute-intensive. With mixed high-and low-resolution requests, this leads to interference between encoder and decoder, persistent SM and HBM slack, poor GPU utilization, and frequent SLO violations. In this paper, we propose RESONATOR, an efficient MLLM serving system that uses fine-grained runtime scheduling along two axes. First, an intra-GPU sharing engine manages SM and HBM sharing between encoder and decoder. It exploits stage-level complementarity and kernel-level slack to run compute-bound encoder kernels and memory-bound LLM kernels in a work-conserving way on the same GPU. Second, an inter-GPU parallelism engine selects the encoder’s data-parallel and tensor-parallel plan at runtime based on input resolution, batch composition, and a lightweight Performance Atlas, and switches plans with near-zero overhead. Evaluation on three state-of-the-art MLLMs against strong baselines shows that RESONATOR improves mean TTFT by up to 5.1×, TPOT by up to 3.0×, mean end-to-end latency by up to 4.9×, and overall throughput by up to 3.4×, while adapting efficiently to highly concurrent and dynamic workloads.

## 中文摘要

多模态大语言模型（MLLM）带来了关键的 serving 挑战。现有系统通常扩展纯文本 LLM 技术栈——它们要么将视觉编码器与解码器放在同一 GPU 上，要么将其迁移到一个固定的 GPU 池中。这两种选择都依赖于提前做出的静态并行性和 GPU 分配决策，忽略了 MLLM 中的一个关键不对称性：编码器内存占用小但计算成本随输入变化（通常呈二次增长），而解码器则同时是内存和计算密集型。面对混合的高分辨率和低分辨率请求，这会导致编码器与解码器之间的干扰、持续的 SM 和 HBM 闲置、低 GPU 利用率以及频繁的 SLO 违反。在本文中，我们提出 RESONATOR，一个高效的 MLLM serving 系统，沿两个维度进行细粒度的运行时调度。首先，一个 GPU 内共享引擎管理编码器与解码器之间的 SM 和 HBM 共享，利用阶段级互补性和内核级闲置，以工作守恒的方式在同一 GPU 上运行计算密集型的编码器内核和内存密集型的 LLM 内核。其次，一个 GPU 间并行性引擎根据输入分辨率、批次组合和轻量级性能图谱在运行时选择编码器的数据并行和张量并行方案，并以近乎零开销切换方案。在三个最先进的 MLLM 上进行的评估表明，与强基线相比，RESONATOR 将平均 TTFT 提升高达 5.1 倍，TPOT 提升高达 3.0 倍，平均端到端延迟降低高达 4.9 倍，总体吞吐量提升高达 3.4 倍，同时高效地适应高并发和动态的工作负载。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2026](../index.md)
