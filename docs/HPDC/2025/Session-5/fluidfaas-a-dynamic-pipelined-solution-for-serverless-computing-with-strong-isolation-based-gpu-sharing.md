---
title: "FluidFaaS: A Dynamic Pipelined Solution for Serverless Computing with Strong Isolation-based GPU Sharing"
description: "HPDC 2025 · Session 5 — Clouds and FaaS"
tags:
  - "HPDC2025"
  - "Session 5"
  - "Clouds and FaaS"
---

# FluidFaaS: A Dynamic Pipelined Solution for Serverless Computing with Strong Isolation-based GPU Sharing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 5</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731580) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/hui.pdf)

**作者**：Xinning Hui, Yuanchao Xu, Xipeng Shen

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）

---

## 英文摘要

Prompted by the rise of artificial intelligence (AI) or machine learning (ML), more serverless workloads demand efficient GPU support. Recent years have witnessed a shift of interest from weak isolation-based methods, such as Multi-Process Service (MPS), to strong isolation-based methods, such as Multi-Instance GPU (MIG), for GPU support on serverless platforms, thanks to concerns about performance interference and security. The current MIG-based solution for serverless computing is, however, subject to severe GPU resource fragmentation and under-utilization. This paper identifies the reason as the gap between current MIG supports in serverless computing and the rigid constraints in MIG (re)configurations. It proposes FluidFaaS, a solution that enables flexible MIG management for serverless computing. Through a novel programming system support, FluidFaaS enables fine-grained resource assignment to the components within a serverless function, based on which, it equips the invokers with runtime support that constructs pipelines on MIGs on the fly for a serverless function. The innovations, along with a hotness-aware eviction-based time sharing of MIG slices, significantly reduce GPU resource fragmentation and enhance system throughput. Evaluations demonstrate that FluidFaaS outperforms the state-of-the-art solutions by 25%-75% in throughput while achieving up to 90% higher SLO hit rates in various workloads.

## 中文摘要

在人工智能（AI）或机器学习（ML）兴起的推动下，越来越多的无服务器负载需要高效的 GPU 支持。近年来，出于对性能干扰与安全性的顾虑，无服务器平台上的 GPU 支持兴趣已从弱隔离方法（如多进程服务 MPS）转向强隔离方法（如多实例 GPU MIG）。然而，当前面向无服务器计算的基于 MIG 的方案受制于严重的 GPU 资源碎片化与利用率不足。本文指出其原因在于无服务器计算中现有 MIG 支持与 MIG（重）配置的刚性约束之间的差距。为此提出 FluidFaaS，一种为无服务器计算实现灵活 MIG 管理的方案。通过新颖的编程系统支持，FluidFaaS 能够为无服务器函数内部的各组件进行细粒度资源分配；在此基础上，它为调用器提供运行时支持，可即时在 MIG 上为无服务器函数构建流水线。这些创新，连同热感知、基于驱逐的 MIG 切片分时共享，显著减少了 GPU 资源碎片化并提升了系统吞吐。评估表明，FluidFaaS 在各种负载下吞吐优于最先进方案 25%–75%，同时 SLO 命中率最高提升 90%。

## 英文关键词

Cloud computing, Serverless Computing, Quality of Service, Function-as-a-Service, Resource Management, Resource Allocation, Resource Efficiency, Machine Learning for Systems, Deep Learning

## 中文关键词

云计算，无服务器计算，服务质量，函数即服务，资源管理，资源分配，资源效率，面向系统的机器学习，深度学习

---

[← 返回 Session 5 — Clouds and FaaS](index.md)
