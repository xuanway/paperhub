---
title: "MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs"
description: "ASPLOS 2025 · Session 6C · MoE-Lightning：面向显存受限 GPU 的高吞吐 MoE 推理"
tags:
  - "ASPLOS2025"
  - "Session 6C"
  - "Mixture of Experts"
---

# MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs

**中文标题：** MoE-Lightning：面向显存受限 GPU 的高吞吐 MoE 推理

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shiyi Cao (UC Berkeley), Shu Liu (UC Berkeley), Tyler Griggs (UC Berkeley), Peter Schafhalter (UC Berkeley), Xiaoxuan Liu (UC Berkeley), Ying Sheng (Stanford University), Joseph E. Gonzalez (UC Berkeley), Matei Zaharia (UC Berkeley), Ion Stoica (UC Berkeley)

**单位：** UC Berkeley；Stanford University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707267) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Efficient deployment of large language models, particularly Mixture of Experts (MoE) models, on resource-constrained platforms presents significant challenges in terms of computational efficiency and memory utilization. The MoE architecture, renowned for its ability to increase model capacity without a proportional increase in inference cost, greatly reduces the token generation latency compared with dense models. However, the large model size makes MoE models inaccessible to individuals without high-end GPUs. In this paper, we propose a high-throughput MoE batch inference system, MoE-Lightning, that significantly outperforms past work. MoE-Lightning introduces a novel CPU-GPU-I/O pipelining schedule, CGOPipe, with paged weights to achieve high resource utilization, and a performance model, HRM, based on a Hierarchical Roofline Model we introduce to help find policies with higher throughput than existing systems. MoE-Lightning can achieve up to 10.3× higher throughput than state-of-the-art offloading-enabled LLM inference systems for Mixtral 8x7B on a single T4 GPU (16GB). When the theoretical system throughput is bounded by the GPU memory, MoE-Lightning can reach the throughput upper bound with 2–3× less CPU memory, significantly increasing resource utilization. MoE-Lightning also supports efficient batch inference for much larger MoEs (e.g., Mixtral 8x22B and DBRX) on multiple low-cost GPUs (e.g., 2–4 T4s). Attribution International 4.0 License.

## 中文摘要

在资源受限平台上高效部署大语言模型，尤其是混合专家（MoE）模型，在计算效率与内存利用率方面都面临显著挑战。MoE 架构以能够在不按比例增加推理成本的前提下提升模型容量而著称，相比稠密模型大幅降低了 token 生成延迟。然而，庞大的模型体量使得没有高端 GPU 的个人难以使用 MoE 模型。本文提出一个高吞吐的 MoE 批量推理系统 MoE-Lightning，其性能显著优于以往工作。MoE-Lightning 引入了一种新的 CPU-GPU-I/O 流水线调度方案 CGOPipe，并配合分页权重以实现高资源利用率；同时提出性能模型 HRM，它基于我们提出的分层 Roofline 模型（Hierarchical Roofline Model），用于帮助寻找吞吐高于现有系统的策略。在单块 T4 GPU（16GB）上对 Mixtral 8x7B 进行推理时，MoE-Lightning 的吞吐最高可达最先进的、支持卸载的 LLM 推理系统的 10.3 倍。当理论系统吞吐受 GPU 内存限制时，MoE-Lightning 可以用少 2–3 倍的 CPU 内存达到吞吐上界，显著提升资源利用率。MoE-Lightning 还支持在多块低成本 GPU（例如 2–4 块 T4）上对更大的 MoE 模型（如 Mixtral 8x22B 和 DBRX）进行高效批量推理。本文采用 Attribution International 4.0 License 许可协议。

## 英文关键词

MoE, Batch Inference, CPU Offloading

## 中文关键词

MoE；批量推理；CPU 卸载

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707267)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2025](../index.md)
