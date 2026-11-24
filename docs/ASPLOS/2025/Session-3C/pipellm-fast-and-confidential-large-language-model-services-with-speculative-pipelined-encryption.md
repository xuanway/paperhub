---
title: "PipeLLM: Fast and Confidential Large Language Model Services with Speculative Pipelined Encryption"
description: "ASPLOS 2025 · Session 3C · PipeLLM：基于推测式流水线加密的快速保密大语言模型服务"
tags:
  - "ASPLOS2025"
  - "Session 3C"
  - "ML Security"
---

# PipeLLM: Fast and Confidential Large Language Model Services with Speculative Pipelined Encryption

**中文标题：** PipeLLM：基于推测式流水线加密的快速保密大语言模型服务

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yifan Tan (Institute of Parallel and Distributed Systems, SEIEE, Shanghai Jiao Tong University), Cheng Tan (Northeastern University), Zeyu Mi (Institute of Parallel and Distributed Systems, SEIEE, Shanghai Jiao Tong University), Haibo Chen (Institute of Parallel and Distributed Systems, SEIEE, Shanghai Jiao Tong University)

**单位：** Institute of Parallel and Distributed Systems, SEIEE, Shanghai Jiao Tong University；Northeastern University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707224) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Confidential computing on GPUs, like NVIDIA H100, mitigates the security risks of outsourced Large Language Models (LLMs) by implementing strong isolation and data encryption. Nonetheless, this encryption incurs a significant performance overhead, reaching up to 52.8% and 88.2% throughput drop when serving OPT-30B and OPT-66B, respectively. To address this challenge, we introduce PipeLLM, a usertransparent runtime system. PipeLLM removes the overhead by overlapping the encryption and GPU computation through pipelining—an idea inspired by the CPU instruction pipelining—thereby effectively concealing the latency increase caused by encryption. The primary technical challenge is that, unlike CPUs, the encryption module lacks prior knowledge of the specific data needing encryption until it is requested by the GPUs. To this end, we propose speculative pipelined encryption to predict the data requiring encryption by analyzing the serving patterns of LLMs. Further, we have developed an efficient, low-cost pipeline relinquishing approach for instances of incorrect predictions. Our experiments show that compared with vanilla systems without confidential computing (e.g., vLLM, PEFT, and FlexGen), PipeLLM incurs modest overhead (<19.6% in throughput) across various LLM sizes, from 13B to 175B. PipeLLM's source code is available at PipeLLM.

## 中文摘要

GPU 上的机密计算（如 NVIDIA H100）通过实现强隔离与数据加密，缓解了外包大语言模型（LLM）的安全风险。然而，这种加密带来了显著的性能开销：在服务 OPT-30B 和 OPT-66B 时，吞吐量分别下降高达 52.8% 和 88.2%。为应对这一挑战，我们提出 PipeLLM，一个对用户透明的运行时系统。PipeLLM 通过流水线将加密与 GPU 计算重叠——这一思路受 CPU 指令流水线启发——从而有效隐藏加密所导致的延迟增加。主要技术挑战在于：与 CPU 不同，加密模块在 GPU 请求之前并不掌握需要加密的具体数据。为此，我们提出推测式流水线加密，通过分析 LLM 的服务模式来预测需要加密的数据。此外，我们针对预测错误的情形开发了一种高效、低成本的流水线让渡方法。我们的实验表明，与不带机密计算的原始系统（如 vLLM、PEFT 和 FlexGen）相比，PipeLLM 在 13B 到 175B 的各种 LLM 规模下只带来适度的开销（吞吐开销 <19.6%）。PipeLLM 的源代码可在 PipeLLM 获取。

## 英文关键词

Nvidia Confidential Computing; Large Language Model; Confidential Virtual Machine

## 中文关键词

Nvidia 机密计算；大语言模型；机密虚拟机

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707224)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2025](../index.md)
