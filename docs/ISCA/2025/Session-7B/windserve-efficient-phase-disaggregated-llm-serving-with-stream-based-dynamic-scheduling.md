---
title: "WindServe: Efficient Phase-Disaggregated LLM Serving with Stream-based Dynamic Scheduling"
description: "ISCA 2025 · Session 7B · WindServe：基于流式动态调度的高效阶段解耦 LLM 服务"
tags:
  - "ISCA2025"
  - "Session 7B"
  - "Systems"
---

# WindServe: Efficient Phase-Disaggregated LLM Serving with Stream-based Dynamic Scheduling

**中文标题：** WindServe：基于流式动态调度的高效阶段解耦 LLM 服务

**所属 Session：** [Session 7B](index.md) · [ISCA 2025](../index.md)

**作者：** Jingqi Feng, Yukai Huang, Rui Zhang, Sicheng Liang, Ming Yan, Jie Wu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730999) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Existing large language model (LLM) serving systems typically batch the compute-bound prefill and I/O-bound decoding phases together. This co-location approach not only leads to significant interference between the two phases but also limits resource allo- cation and placements. To address these limitations, recent work proposes disaggregating the prefill and decoding phases to enhance performance. However, these works often rely on coarse-grained static scheduling strategies, resulting in imbalanced and insuffi- cient resource utilization. For instance, compute resources for the prefill phase may be overloaded while those for the decoding phase remain idle, resulting in performance bottlenecks. In this paper, we propose WindServe, an efficient phase dis- aggregated LLM serving system that leverages stream-based, fine- grained dynamic scheduling to enhance resource utilization and performance. WindServe features a global scheduler that monitors compute and memory resource usage to dynamically orchestrate cross-phase jobs, effectively reducing queuing delay and KV cache swapping overhead. We also introduce a stall-free rescheduling strategy to saturate the memory resources while minimizing the scheduling overhead from KV cache transfers. Furthermore, we design a stream-based approach to mitigate interference between prefill and decoding jobs. Our evaluation demonstrates that Wind- Serve achieves remarkable stability and SLO attainment under high- load scenarios, outperforming state-of-the-art phase-disaggregated LLM serving systems by delivering a 4.28×improvement in TTFT median latency and a 1.5×reduction in TPOT P99 latency.

## 中文摘要

现有大语言模型（LLM）服务系统通常将计算密集型的预填充阶段与IO密集型的解码阶段放在一起批量处理。这种混部方式不仅会造成两个阶段之间严重的资源干扰，还限制了资源分配与部署调度。为解决该问题，已有研究提出将预填充和解码阶段解耦部署以提升性能，但这类方案大多采用粗粒度静态调度，资源利用率不均衡。例如，预填充算力过载，而解码侧算力闲置，进而形成性能瓶颈。

本文提出WindServe，一套高效的阶段解耦LLM服务系统，采用基于流的细粒度动态调度，提升资源利用率与服务性能。WindServe包含全局调度器，监控算力与显存资源占用，动态调度跨阶段任务，降低排队延迟以及KV缓存换入换出开销。同时提出无停顿重调度策略，在打满显存资源的同时，减少KV缓存迁移带来的调度开销。此外，设计流式隔离机制，缓解预填充任务与解码任务之间的相互干扰。

评测结果表明：在高负载场景下，WindServe稳定性强、服务等级目标（SLO）达标率高，对比前沿阶段解耦LLM服务系统，中位首token延迟（TTFT）提升4.28倍，P99逐token生成延迟（TPOT）降低1.5倍。

## 英文关键词

Distributed LLM Inference, GPU Sharing, Scheduling Optimization

## 中文关键词

分布式LLM推理, GPU共享, 调度优化

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730999)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2025](../index.md)
