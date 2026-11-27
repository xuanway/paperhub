---
title: "Towards Resource-Efficient Serverless LLM Inference with SLINFER"
description: "HPCA 2026 · LLM Inference Serving Systems"
tags:
  - "HPCA2026"
  - "LLM Inference Serving Systems"
---

# Towards Resource-Efficient Serverless LLM Inference with SLINFER

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Inference Serving Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Inference Serving Systems</p>
</div>

**论文链接**：
**作者**：Chuhao Xu Shanghai Jiao Tong University , Zijun Li Shanghai Jiao Tong University , Quan Chen Shanghai Jiao Tong University, China , Han Zhao Shanghai Jiao Tong University , Xueyan Tang Nanyang Technological University , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

SLINFER：面向资源高效的无服务器 LLM 推理

## 英文摘要

The rise of LLMs has driven demand for private serverless deployments, characterized by moderate-sized models and infrequent requests. While existing serverless solutions follow exclusive GPU allocation, we take a step back to explore modern platforms and find that: Emerging CPU architectures with built-in accelerators are capable of serving LLMs but remain underutilized, and both CPUs and GPUs can accommodate multiple LLMs simultaneously. We propose SLINFER, a resource-efficient serverless inference scheme tailored for small- to mid-sized LLMs that enables elastic and on-demand sharing across heterogeneous hardware. SLINFER tackles three fundamental challenges: (1) precise, fine-grained compute resource allocation at token-level to handle fluctuating computational demands; (2) a coordinated and forward-looking memory scaling mechanism to detect out-of-memory hazards and reduce operational overhead; and (3) a dual approach that consolidates fragmented instances through proactive preemption and reactive bin-packing. Experimental results on 4 32-core CPUs and 4 A100 GPUs show that SLINFER improves serving capacity by 47% - 62% through sharing, while further leveraging CPUs boosts this to 86% - 154%.

## 中文摘要

LLM 的兴起推动了私有化无服务器部署的需求，其特点是模型规模中等且请求稀疏。既有无服务器方案采用独占式 GPU 分配，我们则退一步审视现代平台，发现：内置加速器的新型 CPU 架构具备服务 LLM 的能力却仍未被充分利用，并且 CPU 与 GPU 都能同时容纳多个 LLM。我们提出 SLINFER，一种面向中小型 LLM 的资源高效无服务器推理方案，可在异构硬件上实现弹性、按需的共享。SLINFER 应对三项基本挑战：(1) 在 Token 级别进行精确细粒度的计算资源分配，以应对波动的计算需求；(2) 协调且具备前瞻性的内存伸缩机制，用于检测内存溢出风险并降低运维开销；(3) 一种双重手段，通过主动抢占与被动装箱整合碎片化实例。在 4 个 32 核 CPU 与 4 块 A100 GPU 上的实验结果表明，SLINFER 通过共享将服务容量提升 47% - 62%，进一步利用 CPU 后更可提升至 86% - 154%。
