---
title: "NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-Based Request Placement"
description: "MICRO 2026 · Session 8A · NELSSA：通过基于长度的请求放置实现混合长度 LLM 服务的 GPU-PNM 异构系统"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
  - "Near-Memory Computing"
---

# NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-Based Request Placement

**中文标题：** NELSSA：通过基于长度的请求放置实现混合长度 LLM 服务的 GPU-PNM 异构系统

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Sookyung Choi, Seungyong Lee, Kangkyu Park, Yunseo Chun, Junseok Lee, Hyeongseok Gwak, Myunghyun Rhee, Euiseok Kim, Donguk Moon, Kwangsik Shin, Guseul Heo, Youngpyo Joo, Hoshik Kim, Jongse Park

**来源：** MICRO 2026，pp. 2755–2769；[DOI](https://doi.org/10.1109/MICRO67795.2026.00187)

## 英文摘要

Modern LLMs and their agentic applications are broadening the range of serving workloads, spanning context lengths from a few hundred tokens to hundreds of thousands. As these requests frequently interleave within the same serving window, LLM serving systems must handle highly heterogeneous mixed-length workloads. These workloads expose fundamental inefficiencies in GPU-centric serving architectures, whose throughput depends on large, memory-constrained batches. In this paper, we present NELSSA (Processing-NEar-Memory for Long Sequences with Sparse Attention), an LLM serving system that integrates GPUs with real-world Processing-near-Memory (PNM) accelerator devices to efficiently support mixed-length workloads. NELSSA employs length-based request placement to route short-context requests to GPUs and long-context requests to the PNM tier, incorporating runtime migration to accommodate dynamic context growth without recomputation. We prototype NELSSA as an end-to-end system, implementing device-level sparse attention on PNM, GPU decode kernels, and a host-side runtime that orchestrates scheduling and crosstier memory movement over a CXL-enabled infrastructure with RPC and RDMA support. Across mixed-length LLM workloads, NELSSA improves decode throughput by up to 5.5× in tokens/sec and reduces P99 latency by up to 15× compared to GPU-only baselines. Our end-to-end prototype and experimental results demonstrate how workload-aware heterogeneous composition of GPU and PNM resources can reduce the resource inefficiencies of homogeneous GPU provisioning, suggesting a promising path toward scalable and resource-efficient LLM infrastructures.

## 中文摘要

现代大语言模型及其代理应用程序正在扩大服务工作负载的范围，将上下文长度从几百个词元扩展到数十万个。由于这些请求经常在同一服务窗口内交错，LLM 服务系统必须处理高度异构的混合长度工作负载。这些工作负载暴露了以 GPU 为中心的服务架构中根本性的低效率，其吞吐量取决于内存受限的大批量。在本文中，我们提出了 NELSSA（具有稀疏注意力的长序列处理近存），这是一种 LLM 服务系统，它将 GPU 与现实世界的近存处理（PNM）加速器设备集成，以有效支持混合长度工作负载。 NELSSA 采用基于长度的请求放置，将短上下文请求路由到 GPU，将长上下文请求路由到 PNM 层，并结合运行时迁移来适应动态上下文增长，而无需重新计算。我们将 NELSSA 原型化为端到端系统，在 PNM、GPU 解码内核和主机端运行时上实现设备级稀疏注意力，该主机端运行时在具有 RPC 和 RDMA 支持的 CXL 基础设施上协调调度和跨层内存移动。在混合长度的 LLM 工作负载中，与仅使用 GPU 的基准相比，NELSSA 将解码吞吐量提高了高达 5.5 倍（以词元/秒为单位），并将 P99 时延降低了高达 15 倍。我们的端到端原型和实验结果展示了 GPU 和 PNM 资源的工作负载感知异构组合如何降低同构 GPU 配置的资源效率低下问题，为可扩展且资源高效的 LLM 基础设施提供了一条有希望的道路。

## 中文关键词

大语言模型服务；近存处理；异构系统；混合长度请求；请求放置

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
