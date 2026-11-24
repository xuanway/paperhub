---
title: "Aqua: Network-Accelerated Memory Offloading for LLMs in Scale-Up GPU Domains"
description: "ASPLOS 2025 · Session 10A · Aqua：面向纵向扩展 GPU 域中 LLM 的网络加速内存卸载"
tags:
  - "ASPLOS2025"
  - "Session 10A"
  - "GPGPU"
---

# Aqua: Network-Accelerated Memory Offloading for LLMs in Scale-Up GPU Domains

**中文标题：** Aqua：面向纵向扩展 GPU 域中 LLM 的网络加速内存卸载

**所属 Session：** [Session 10A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Abhishek Vijaya Kumar (Cornell University), Gianni Antichi (Politecnico di Milano), Rachee Singh (Cornell University)

**单位：** Cornell University；Politecnico di Milano

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715983) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Inference on large-language models (LLMs) is constrained by GPU memory capacity. A sudden increase in the number of inference requests to a cloud-hosted LLM can deplete GPU memory, leading to contention between multiple prompts for limited resources. Modern LLM serving engines deal with the challenge of limited GPU memory using admission control, which causes them to be unresponsive during request bursts. We propose that preemptive scheduling of prompts in time slices is essential for ensuring responsive LLM inference, especially under conditions of high load and limited GPU memory. However, preempting prompt inference incurs a high paging overhead, which reduces inference throughput. We present Aqa, a GPU memory management framework that significantly reduces the overhead of paging inference state; achieving both responsive and high throughput inference even under bursty request patterns. We evaluate Aqa by hosting several state-of-the-art large generative ML models of different modalities on servers with 8 Nvidia H100 80G GPUs. Aqa improves the responsiveness of LLM inference by 20× compared to the state-of-the-art. It improves LLM inference throughput over a single long prompt by 4×.1

## 中文摘要

大语言模型（LLM）的推理受限于 GPU 内存容量。发往云托管 LLM 的推理请求数量突然增加可能耗尽 GPU 内存，导致多个提示之间为有限资源而相互争用。现代 LLM 服务引擎利用准入控制来应对 GPU 内存有限的挑战，但这使它们在请求突发期间缺乏响应。我们提出，以时间片对提示进行抢占式调度对于确保 LLM 推理的响应性至关重要，尤其是在高负载且 GPU 内存受限的条件下。然而，抢占提示推理会带来高昂的分页开销，从而降低推理吞吐。我们提出 Aqa，一个 GPU 内存管理框架，它显著降低了推理状态分页的开销；即使在突发请求模式下也能同时实现响应性与高吞吐推理。我们通过在配备 8 块 Nvidia H100 80G GPU 的服务器上托管多个不同模态的最先进大型生成式机器学习模型来评估 Aqa。与最先进方案相比，Aqa 将 LLM 推理的响应性提升了 20 倍；针对单个长提示，它将 LLM 推理吞吐提升了 4 倍。1

## 英文关键词

Large language models; Generative AI; Paging; Virtual memory; GPU interconnects; Memory offloading

## 中文关键词

大语言模型；生成式人工智能；分页；虚拟内存；GPU 互连；内存卸载

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715983)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10A](index.md) · [返回 ASPLOS 2025](../index.md)
