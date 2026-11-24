---
title: "Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management"
description: "ASPLOS 2025 · Session 7A · 通过高效资源管理加速多轮对话的大语言模型服务"
tags:
  - "ASPLOS2025"
  - "Session 7A"
  - "Serving LLMs"
---

# Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management

**中文标题：** 通过高效资源管理加速多轮对话的大语言模型服务

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jinwoo Jeong (Korea University), Jeongseob Ahn (Korea University)

**单位：** Korea University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716245) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Although there have been significant efforts to make LLM serving efficient, we observe two limitations of current state-of-the-art serving frameworks in handling multi-turn dialogues between users and assistants, particularly in chat scenarios. First, existing LLM frameworks incur substantial computational overhead in recomputing attention keys and values (KVs) for understanding context across multiple turns of user queries. Second, as the prompt length of user queries is amplified due to multi-turns, a first-come-firstserved (FCFS) scheduling policy often causes head-of-line blocking issues, leading to underutilization of GPU resources. To address these limitations, we present FlashGen to rapidly complete multi-turn queries by efficiently utilizing the compute and memory resources of GPUs as well as the host hardware (e.g., DRAM and SSD). We introduce a multi-level KV cache comprised of GPU, CPU, and SSD, to efficiently retain attention KVs from prior turns. Our approach employs low-cost cache restoration techniques to avoid the recomputation burden. Further, we propose a request reordering technique to effectively utilize GPU memory. This scheduling technique carefully adjusts the request order without compromising fairness. Our proposed techniques outperform the vLLM framework in terms of both latency and throughput. For OPT 30B and Llama-2 70B models with the ShareGPT dataset, we achieve 1.63× and 2.85× better throughput, respectively while in a similar latency boundary.

## 中文摘要

尽管在提升 LLM 服务效率方面已有大量工作，但我们观察到当前最先进的服务框架在处理用户与助手之间的多轮对话（尤其是聊天场景）时存在两点局限。首先，现有 LLM 框架在理解多轮用户查询的上下文时，需要重新计算注意力的键和值（KV），带来大量计算开销。其次，随着用户查询的提示长度因多轮交互而不断增长，先来先服务（FCFS）调度策略常常导致队头阻塞问题，使 GPU 资源利用不足。为解决这些局限，我们提出 FlashGen，通过高效利用 GPU 的计算与内存资源以及主机硬件（如 DRAM 和 SSD）来快速完成多轮查询。我们引入由 GPU、CPU 和 SSD 构成的多级 KV cache，以高效保留先前轮次的注意力 KV。我们的方法采用低成本缓存恢复技术来避免重计算负担。此外，我们提出请求重排序技术以有效利用 GPU 内存。该调度技术在不损害公平性的前提下谨慎调整请求顺序。所提技术在时延和吞吐方面均优于 vLLM 框架。对于使用 ShareGPT 数据集的 OPT 30B 和 Llama-2 70B 模型，在相近的时延边界下，我们分别实现了 1.63× 和 2.85× 的吞吐提升。

## 英文关键词

LLM Serving; Multi-turn Dialogues; KV Cache Management; Request Reordering

## 中文关键词

LLM 服务；多轮对话；KV cache 管理；请求重排序

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716245)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2025](../index.md)
