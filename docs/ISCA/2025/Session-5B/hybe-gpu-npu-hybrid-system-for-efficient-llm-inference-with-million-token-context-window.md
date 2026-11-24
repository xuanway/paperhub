---
title: "Hybe: GPU-NPU Hybrid System for Efficient LLM Inference with Million-Token Context Window"
description: "ISCA 2025 · Session 5B · Hybe：面向百万词元上下文高效 LLM 推理的 GPU-NPU 混合系统"
tags:
  - "ISCA2025"
  - "Session 5B"
  - "HPC for ML/AI"
---

# Hybe: GPU-NPU Hybrid System for Efficient LLM Inference with Million-Token Context Window

**中文标题：** Hybe：面向百万词元上下文高效 LLM 推理的 GPU-NPU 混合系统

**所属 Session：** [Session 5B](index.md) · [ISCA 2025](../index.md)

**作者：** Seungjae Moon, Junseo Cha, Hyunjun Park, Joo-Young Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731051) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The growth of context window size in large language model (LLM) inference poses a very distinct computational challenge of hard- ware inefficiency. The inefficiency arises from the computational imbalance during LLM inference between the compute-intensive prefill stage, and memory-intensive decode stage. The predominant inference hardware, GPU, boasts large number of cores to excel in the prefill stage, which processes the entire input context at once, but suffers from hardware underutilization in the decode stage, which iteratively generates one output token at a time. In conven- tional LLM, batching has been able to alleviate the underutilization by generating multiple tokens of different requests. However, batch- ing becomes infeasible in models with large context windows over 100K tokens because the Key-Value (KV) activations dominate the physical memory capacity, surpassing the entire model size. In this paper, we propose Hybe, a GPU-NPU hybrid system for effi- cient LLM inference with a million-token context window. Hybe utilizes the preexisting GPU for the prefill stage and employs light- weight NPUs during the decode stage. Each NPU includes only the necessary computing resources to fully utilize the given memory bandwidth, thereby achieving maximum hardware efficiency. Fur- thermore, Hybe introduces fine-grained KV transmission, a kernel scheduling method that immediately offloads partial KV produced from the GPU to the NPU, which significantly reduces the KV mem- ory required in the GPU. Lastly, Hybe scheduler applies stage-wise pipelining that dynamically assigns queued requests to idle hard- ware to minimize stalls. Hybe utilizes NVIDIA H100 GPU with inference-optimized vLLM library and implement Hybe NPU in 4nm process with equal HBM specification. Hybe achieves 2.1× speedup for Phi-3 with 100K-token context window and 3.9×en- ergy efficiency for Llama-3 with 1M-token context window, over H100 GPUs with equal total device count.

## 中文摘要

大语言模型 (LLM) 推理中上下文窗口大小的增长对硬件低效率提出了非常明显的计算挑战。效率低下是由于 LLM 推理过程中计算密集型预填充阶段和内存密集型解码阶段之间的计算不平衡造成的。主要的推理硬件 GPU 拥有大量核心，在预填充阶段表现出色，可一次性处理整个输入上下文，但在解码阶段却存在硬件利用率不足的问题，该阶段一次迭代地生成一个输出令牌。在传统的 LLM 中，批处理能够通过生成不同请求的多个令牌来缓解利用率不足的情况。然而，在具有超过 100K token 的大上下文窗口的模型中，批处理变得不可行，因为键值 (KV) 激活占据了物理内存容量，超过了整个模型的大小。

在本文中，我们提出了 Hybe，这是一种 GPU-NPU 混合系统，用于通过百万个令牌上下文窗口进行高效的 LLM 推理。 Hybe 在预填充阶段使用预先存在的 GPU，并在解码阶段使用轻量级 NPU。每个NPU仅包含充分利用给定内存带宽所需的计算资源，从而实现最大的硬件效率。此外，Hybe还引入了细粒度KV传输，这是一种内核调度方法，可以立即将GPU产生的部分KV卸载到NPU，从而显著减少GPU中所需的KV内存。最后，Hybe 调度程序应用分阶段流水线技术，将排队的请求动态分配给空闲硬件，以最大限度地减少停顿。

Hybe 利用 NVIDIA H100 GPU 和推理优化的 vLLM 库，并在 4nm 工艺中实现具有相同 HBM 规格的 Hybe NPU。与具有相同总设备数量的 H100 GPU 相比，Hybe 使具有 100K 令牌上下文窗口的 Phi-3 实现了 2.1 倍的加速，并为具有 1M 令牌上下文窗口的 Llama-3 实现了 3.9 倍的能效。

## 英文关键词

Large language model (LLM), Context window, Heterogeneous (hybrid) system, Neural processing unit (NPU), Scheduling

## 中文关键词

大语言模型（LLM）, 上下文窗口, 异构（混合）系统, 神经网络处理单元（NPU）, 调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731051)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2025](../index.md)
