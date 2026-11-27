---
title: "RPU - A Reasoning Processing Unit"
description: "HPCA 2026 · Best Paper Candidates"
tags:
  - "HPCA2026"
  - "Best Paper Candidates"
---

# RPU - A Reasoning Processing Unit

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Best Paper Candidates。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Best Paper Candidates</p>
</div>

**论文链接**：
**作者**：Matthew Adiletta Harvard University , David Brooks Harvard University , Gu-Yeon Wei Harvard University
**会议**：HPCA 2026

---

## 中文标题

RPU：推理处理单元

## 英文摘要

Large language model (LLM) inference performance is increasingly bottlenecked by the memory wall. While GPUs continue to scale raw compute throughput, they struggle to deliver scalable performance for memory bandwidth bound workloads. This challenge is amplified by emerging reasoning LLM applications, where long output sequences, low arithmetic intensity, and tight latency constraints demand significantly higher memory bandwidth. As a result, system utilization drops and energy per inference rises, highlighting the need for an optimized system architecture for scalable memory bandwidth. To address these challenges we present the Reasoning Processing Unit (RPU), a chiplet-based architecture designed to address the challenges of the modern memory wall. RPU introduces: (1) A Capacity-Optimized High-Bandwidth Memory (HBM-CO) that trades capacity for lower energy and cost; (2) a scalable chiplet architecture featuring a bandwidth-first power and area provisioning design; and (3) a decoupled microarchitecture that separates memory, compute, and communication pipelines to sustain high bandwidth utilization. Simulation results show that RPU performs up to 45.3× lower latency and 18.6× higher throughput over an H100 system at ISO-TDP on Llama3-405B.

## 中文摘要

大语言模型（LLM）推理性能日益受内存墙制约。GPU 的原始计算吞吐仍在提升，却难以在受内存带宽约束的负载上提供可扩展性能。新兴的推理型 LLM 应用放大了这一挑战：长输出序列、低算术强度与严格时延约束要求显著更高的内存带宽，导致系统利用率下降、每次推理能耗上升，凸显出为可扩展内存带宽设计优化系统架构的必要性。为应对这些挑战，我们提出推理处理单元（RPU），一种面向现代内存墙挑战的芯粒架构。RPU 引入：（1）容量优化的高带宽内存（HBM-CO），以容量换取更低能耗与成本；（2）可扩展芯粒架构，采用带宽优先的功耗与面积供给设计；（3）解耦微架构，将内存、计算与通信流水线分离，以维持高带宽利用率。模拟结果显示，在 ISO-TDP 下运行 Llama3-405B 时，RPU 相较 H100 系统最高实现 45.3 倍更低时延与 18.6 倍更高吞吐。
