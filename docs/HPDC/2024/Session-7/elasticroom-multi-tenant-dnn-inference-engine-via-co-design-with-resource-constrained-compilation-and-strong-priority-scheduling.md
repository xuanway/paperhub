---
title: "ElasticRoom: Multi-Tenant DNN Inference Engine via Co-design with Resource-constrained Compilation and Strong Priority Scheduling"
description: "HPDC 2024 · Session 7 — Resource Management"
tags:
  - "HPDC2024"
  - "Session 7"
  - "Resource Management"
---

# ElasticRoom: Multi-Tenant DNN Inference Engine via Co-design with Resource-constrained Compilation and Strong Priority Scheduling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 7</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658654)

**作者**：Lixian Ma, Haoruo Chen, En Shao, Leping Wang, Quan Chen, Guangming Tan

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）

---

## 英文摘要

GPU partition mechanisms in run-time software have been widely used in job scheduler and multi-tenant computing system to improve resource utilization and throughput. The latency requirements of different DNN requests, such as real-time and best-effort requests, often exhibit variations in computational systems that handle batch tasks for DNN inference. However, the existing GPU partition mechanisms and state-of-the-art scheduling approaches face challenges in effectively promising both high throughput and low latency for real-time requests. The current limitation lies in the inability of existing GPU partition mechanisms to enhance GPU resource utilization and ensure job priority simultaneously. In this paper, we present an innovative multi-tenant DNN inference engine, ElasticRoom, which relies on the co-design with resource-constrained compilation and strong priority scheduling to achieve high GPU utilization and low latency of real-time requests simultaneously. To ensure portability across diverse manufacturers’ accelerator hardware, ElasticRoom does not rely on any customization or pre-set features in the hardware or operating system. To quantify the ability of DNN inference computing systems to process and meet performance requirements for a batch of real-time DNN inference requests within a valid time, we define the concept of Goodput for each batch of inference requests. The performance of ElasticRoom was assessed on both NVIDIA GPUs (A100) and AMD GPUs (MI100), revealing significant enhancements in Goodput ranging from 14% to 49% compared to well-established state-of-the-art methods.

## 中文摘要

运行时软件中的 GPU 分区机制已广泛用于作业调度器与多租户计算系统，以提升资源利用率与吞吐。处理 DNN 推理批处理任务的计算系统中，不同 DNN 请求（如实时请求与尽力而为请求）的延迟需求往往存在差异。然而，现有 GPU 分区机制与最先进调度方法难以同时有效保证高吞吐与实时请求的低延迟。当前局限在于现有 GPU 分区机制无法同时提升 GPU 资源利用率并确保作业优先级。本文提出一种创新的多租户 DNN 推理引擎 ElasticRoom，它依赖与资源受限编译及强优先级调度的协同设计，同时实现高 GPU 利用率与实时请求的低延迟。为确保跨不同厂商加速器硬件的可移植性，ElasticRoom 不依赖硬件或操作系统中的任何定制或预置特性。为量化 DNN 推理计算系统在有效时间内处理并满足一批实时 DNN 推理请求性能需求的能力，我们为每批推理请求定义了吞吐（Goodput）概念。ElasticRoom 的性能在 NVIDIA GPU（A100）与 AMD GPU（MI100）上均进行了评估，相比成熟的最先进方法，Goodput 显著提升 14%–49%。

## 英文关键词

DNN Inference, GPU, Compiling, Scheduling

## 中文关键词

DNN 推理，GPU，编译，调度

---

[← 返回 Session 7 — Resource Management](index.md)
