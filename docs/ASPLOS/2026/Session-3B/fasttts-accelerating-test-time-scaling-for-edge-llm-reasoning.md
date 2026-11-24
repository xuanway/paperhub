---
title: "FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning"
description: "ASPLOS 2026 · Session 3B · FastTTS：加速边缘 LLM 推理的测试时扩展"
tags:
  - "ASPLOS2026"
  - "Session 3B"
  - "Mixture-of-Experts & Efficient Inference"
---

# FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning

**中文标题：** FastTTS：加速边缘 LLM 推理的测试时扩展

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hao (Mark) Chen (Imperial College London), Zhiwen Mo (Imperial College London), Guanxi Lu (Imperial College London), Shuang Liang (Imperial College London), Lingxiao Ma (Microsoft Research), Wayne Luk (Imperial College London), Hongxiang Fan (Imperial College London)

**单位：** Imperial College London；Microsoft Research

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790161) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Recent advances in reasoning Large Language Models (LLMs) are driving the emergence of agentic AI systems. Edge deployment of LLM agents near end users is increasingly necessary to protect data privacy, enable offline use, and provide responsive interaction with local context. However, strict memory constraints on edge devices limit deployment to smaller LLMs, whose reasoning capabilities are much weaker than those of large cloud models, hindering practical deployment of edge agentic AI. Test-Time Scaling (TTS) offers a promising solution by allocating more compute during inference to enhance the reasoning capability of edge LLMs. However, current TTS methods introduce heavy hardware performance overhead on resource-constrained devices, making them impractical for real applications. To address this challenge, we present FastTTS, a serving system that enables fast and efficient TTS for memory-constrained LLM reasoning. After analyzing common patterns across various TTS methods and identifying their performance bottlenecks, we introduce three novel techniques: i) Speculative Beam Extension, which mitigates system stragglers caused by irregular reasoning paths, ii) Asymmetric Multi-Model Memory Allocation, which dynamically balances memory usage between token generation and reasoning-step verification, and iii) Dynamic Prefix-Aware Scheduling, which across search paths. FastTTS offers a plug-and-play third-party library on top of vLLM, enabling edge LLMs (≤7B) on a single consumer GPU (24 GB) to match cloud-model accuracy and cloud-measured latency. Comprehensive evaluation shows that FastTTS achieves an average 2.2× higher goodput and reduces latency by 38%-68% compared to the vLLM baseline; it pushes the boundaries of low-latency Test-Time Scaling on memory-constrained edge devices and highlights the potential for democratizing agentic AI.

## 中文摘要

推理大语言模型（LLM）的最新进展正在推动智能体式 AI 系统的兴起。为保护数据隐私、支持离线使用并提供与本地上下文的快速响应交互，在终端用户附近进行 LLM 智能体的边缘部署日益必要。然而，边缘设备严格的内存约束使部署只能局限于较小的 LLM，其推理能力远弱于云端大模型，阻碍了边缘智能体 AI 的实际部署。测试时扩展（TTS）通过在推理期间分配更多计算来增强边缘 LLM 的推理能力，提供了一种有前景的解决方案。但是，当前的 TTS 方法会在资源受限的设备上带来沉重的硬件性能开销，使其难以用于实际应用。为应对这一挑战，我们提出 FastTTS，这是一个为内存受限的 LLM 推理提供快速且高效 TTS 的服务系统。在分析各类 TTS 方法的共同模式并识别其性能瓶颈之后，我们引入了三项新技术：i) Speculative Beam Extension，用于缓解由不规则推理路径导致的系统拖尾；ii) Asymmetric Multi-Model Memory Allocation，用于在 token 生成与推理步验证之间动态平衡内存使用；iii) Dynamic Prefix-Aware Scheduling，其跨搜索路径。FastTTS 在 vLLM 之上提供了一个即插即用的第三方库，使单块消费级 GPU（24 GB）上的边缘 LLM（≤7B）能够达到与云端模型相当的准确率和云端实测的延迟。综合评估表明，与 vLLM 基线相比，FastTTS 平均取得了 2.2× 的更高 goodput，并将延迟降低了 38%-68%；它拓展了内存受限边缘设备上低延迟测试时扩展的边界，并凸显了智能体 AI 普惠化的潜力。

## 英文关键词

machine learning system; LLM reasoning; test-time scaling (TTS); resource-constrained inference

## 中文关键词

机器学习系统；LLM 推理；测试时扩展（TTS）；资源受限推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790161)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2026](../index.md)
