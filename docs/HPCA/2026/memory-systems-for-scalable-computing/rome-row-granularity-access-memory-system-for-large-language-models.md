---
title: "RoMe: Row Granularity Access Memory System for Large Language Models"
description: "HPCA 2026 · Memory Systems for Scalable Computing"
tags:
  - "HPCA2026"
  - "Memory Systems for Scalable Computing"
---

# RoMe: Row Granularity Access Memory System for Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory Systems for Scalable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory Systems for Scalable Computing</p>
</div>

**论文链接**：[https://arxiv.org/abs/2512.01541](https://arxiv.org/abs/2512.01541)
**作者**：Hwayong Nam Seoul National University , Seungmin Baek Seoul National University , Jumin Kim Seoul National University , Michael Jaemin Kim Meta , Jung Ho Ahn Seoul National University
**会议**：HPCA 2026

---

## 中文标题

RoMe：面向大语言模型的行粒度访存系统

## 英文摘要

Modern HBM-based memory systems have evolved over generations while retaining cache line granularity accesses. Preserving this fine granularity necessitated the introduction of bank groups and pseudo channels. These structures expand timing parameters and control overhead, significantly increasing memory controller scheduling complexity. Large language models (LLMs) now dominate deep learning workloads, streaming contiguous data blocks ranging from several kilobytes to megabytes per operation. In a conventional HBM-based memory system, these transfers are fragmented into hundreds of 32B cache line transactions. This forces the memory controller to employ unnecessarily intricate scheduling, leading to growing inefficiency. To address this problem, we propose RoMe. RoMe accesses DRAM at row granularity and removes columns, bank groups, and pseudo channels from the memory interface. This design simplifies memory scheduling, thereby requiring fewer pins per channel. The freed pins are aggregated to form additional channels, increasing overall bandwidth by 12.5% with minimal extra pins. RoMe demonstrates how memory scheduling logic can be significantly simplified for representative LLM workloads, and presents an alternative approach for next-generation HBM-based memory systems achieving increased bandwidth with minimal hardware overhead.

## 中文摘要

现代基于 HBM 的内存系统历经多代演进，却始终保留缓存行粒度的访问方式。为维持这种细粒度，必须引入 bank group 与伪通道，这些结构扩展了时序参数与控制开销，显著增加了内存控制器的调度复杂度。如今大语言模型（LLM）主导深度学习负载，每次操作都会流式传输从数千字节到数兆字节的连续数据块。在传统基于 HBM 的内存系统中，这些传输被切分为数百个 32B 缓存行事务，迫使内存控制器采用不必要的复杂调度，导致效率不断下降。为解决该问题，我们提出 RoMe。RoMe 以行粒度访问 DRAM，并从内存接口中移除列、bank group 与伪通道。该设计简化了内存调度，从而减少每通道所需的引脚数；释放出的引脚被聚合形成额外通道，在仅增加极少引脚的情况下将整体带宽提升 12.5%。RoMe 展示了如何针对代表性 LLM 负载显著简化内存调度逻辑，并为下一代基于 HBM 的内存系统提供了一条以极小硬件开销提升带宽的替代路径。
