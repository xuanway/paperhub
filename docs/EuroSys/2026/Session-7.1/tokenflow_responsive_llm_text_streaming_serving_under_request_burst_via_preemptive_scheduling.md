---
title: "TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling"
description: "EuroSys 2026 · LLM Inference · Junyi Chen (Shanghai Jiao Tong University), Chuheng Du (Shanghai Jiao Tong Unive"
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling

**中文标题：** TokenFlow：通过抢占式调度在请求突发下实现响应式 LLM 文本流式服务

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Junyi Chen (Shanghai Jiao Tong University), Chuheng Du (Shanghai Jiao Tong University), Renyuan Liu (George Mason University), Shuochao Yao (George Mason University), Dingtian Yan (China Telecom Corporation Limited Shanghai Branch), Jiang Liao (China Telecom Corporation Limited Shanghai Branch), Shengzhong Liu (Shanghai Jiao Tong University), Fan Wu (Shanghai Jiao Tong University), Guihai Chen (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769328)

## 英文摘要

Real-time LLM interactions demand streamed token generations, where text tokens are progressively generated and delivered to users while balancing two objectives: responsiveness (i.e., low time-to-first-token) and steady generation (i.e., required time-between-tokens). Standard LLM serving systems suffer from the inflexibility caused by non-preemptive request scheduling and reactive memory management, leading to poor resource utilization and low request processing parallelism under request bursts. Therefore, we present TokenFlow, a novel LLM serving system with enhanced text streaming performance via preemptive request scheduling and proactive key-value (KV) cache management. TokenFlow dynamically prioritizes requests based on real-time token buffer occupancy and token consumption rate, while actively transferring KV cache between GPU and CPU memory in the background and overlapping I/O with computation to minimize request preemption overhead. Extensive experiments on Llama3-8B and Qwen2.5-32B across multiple GPUs (RTX 4090, A6000, H200) demonstrate that TokenFlow achieves up to 82.5% higher effective throughput (accounting for actual user consumption) while reducing P99 TTFT by up to 80.2%, without degrading overall token throughput.

## 中文摘要

实时的 LLM 交互需要流式 token 生成，即文本 token 被逐步生成并交付给用户，同时需平衡两个目标：响应性（即低首 token 时延）与稳定生成（即所需的 token 间时延）。标准 LLM 服务系统受非抢占式请求调度与被动式内存管理所导致的僵化性困扰，在请求突发时造成资源利用率低下和请求处理并行度不足。因此，我们提出 TokenFlow，一种通过抢占式请求调度与主动式键值（KV）缓存管理来增强文本流式性能的新型 LLM 服务系统。TokenFlow 基于实时 token 缓冲区占用率与 token 消费速率动态确定请求优先级，同时在后台主动在 GPU 与 CPU 内存之间迁移 KV 缓存，并将 I/O 与计算重叠，以最小化请求抢占开销。在多种 GPU（RTX 4090、A6000、H200）上针对 Llama3-8B 与 Qwen2.5-32B 的大量实验表明，TokenFlow 将有效吞吐量（按用户实际消费计）最高提升 82.5%，同时将 P99 TTFT 最多降低 80.2%，且不降低整体 token 吞吐量。

**英文关键词：** LLM Serving, Text Streaming, KV Cache Management, Scheduling Optimization

**中文关键词：** LLM 服务、文本流式生成、KV Cache 管理、调度优化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
