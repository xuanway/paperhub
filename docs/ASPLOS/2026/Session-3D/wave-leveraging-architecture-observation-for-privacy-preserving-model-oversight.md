---
title: "WAVE: Leveraging Architecture Observation for Privacy-Preserving Model Oversight"
description: "ASPLOS 2026 · Session 3D · WAVE：利用架构观测实现隐私保护下的模型监管"
tags:
  - "ASPLOS2026"
  - "Session 3D"
  - "Trusted Execution Environments"
---

# WAVE: Leveraging Architecture Observation for Privacy-Preserving Model Oversight

**中文标题：** WAVE：利用架构观测实现隐私保护下的模型监管

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Haoxuan Xu (USC), Chen Gong (USC), Beijie Liu (USC), Haizhong Zheng (Carnegie Mellon University), Beidi Chen (Carnegie Mellon University), Mengyuan Li (USC)

**单位：** USC；Carnegie Mellon University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790247) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large Language Models (LLMs) inference increasingly require mechanisms that provide runtime visibility into what is actually executing, without exposing model weights or code. We present WAVE, a hardware-grounded monitoring framework that leverages GPU performance counters (PMCs) to observe LLM inference. WAVE is built on the insight that legitimate executions of a given model must satisfy hardware-constrained invariants, such as memory accesses, instruction mix, and tensor-core utilization, induced by the model's linear-algebraic structure. WAVE collects lightweight PMC traces and applies a two-stage pipeline: (1) inferring architectural properties (e.g., parameter count, layer depth, hidden dimension, batch size) from the observed traces; and (2) using an SMT-based consistency checker to assess whether the execution aligns with the provisioned compute and the claimed model's constraints. We evaluate WAVE on common opensource LLM architectures, such as LLaMA, GPT, and Qwen, across multiple GPU architectures, including NVIDIA Ada Lovelace, Hopper, and Blackwell. Results show that WAVE recovers key model parameters with an average error of 6.8% and identifies disguised executions under realistic perturbations. By grounding oversight in hardware invariants, WAVE provides a practical avenue for continuous, privacy-preserving runtime monitoring of LLM services.

## 中文摘要

大语言模型（LLM）推理日益需要这样的机制：它能够对实际正在执行的内容提供运行时可见性，同时不暴露模型权重或代码。我们提出 WAVE，一个以硬件为基础的监控框架，利用 GPU 性能计数器（PMC）来观测 LLM 推理。WAVE 建立在这样一个洞见之上：给定模型的合法执行必须满足由该模型的线性代数结构所诱发的、受硬件约束的不变量，例如内存访问、指令组合和张量核心利用率。WAVE 收集轻量级 PMC 轨迹，并应用两阶段流水线：（1）从观测到的轨迹中推断架构属性（例如参数量、层深度、隐藏维度、批大小）；（2）使用基于 SMT 的一致性检查器来评估执行是否与所配置的算力以及所声称模型的约束相符。我们在 LLaMA、GPT 和 Qwen 等常见开源 LLM 架构上、跨多种 GPU 架构（包括 NVIDIA Ada Lovelace、Hopper 和 Blackwell）评估 WAVE。结果表明，WAVE 以平均 6.8% 的误差恢复关键模型参数，并能在现实扰动下识别伪装的执行。通过将监管建立在硬件不变量之上，WAVE 为对 LLM 服务进行持续、隐私保护的运行时监控提供了一条切实可行的途径。

## 英文关键词

Verifiable Inference; GPU Performance Counters; Model Fingerprinting; Hardware-assisted Security

## 中文关键词

可验证推理；GPU 性能计数器；模型指纹识别；硬件辅助安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790247)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2026](../index.md)
