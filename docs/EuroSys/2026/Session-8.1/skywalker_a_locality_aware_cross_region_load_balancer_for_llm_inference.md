---
title: "SkyWalker: A Locality-Aware Cross-Region Load Balancer for LLM Inference"
description: "EuroSys 2026 · LLM Serving & Agents · Tian Xia (UC Berkeley), Ziming Mao (UC Berkeley), Jamison Kerney (UC Berkeley), "
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# SkyWalker: A Locality-Aware Cross-Region Load Balancer for LLM Inference

**中文标题：** SkyWalker：面向LLM推理的局部性感知跨区域负载均衡器

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Tian Xia (UC Berkeley), Ziming Mao (UC Berkeley), Jamison Kerney (UC Berkeley), Ethan J. Jackson (UC Berkeley), Zhifei Li (Renmin University of China), Jiarong Xing (Rice University and UC Berkeley), Scott Shenker (ICSI and UC Berkeley), Ion Stoica (UC Berkeley)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769353)

## 英文摘要

Serving Large Language Models (LLMs) efficiently in multi-region setups remains a challenge. Due to cost and GPU availability concerns, providers typically deploy LLMs in multiple regions using instance with long-term commitments, like reserved instances or on-premise clusters, which are often underutilized due to their region-local traffic handling and diurnal traffic variance. In this paper, we introduce SkyWalker, a multi-region load balancer for LLM inference that aggregates regional diurnal patterns through cross-region traffic handling. By doing so, SkyWalker enables providers to reserve instances based on expected global demand, rather than peak demand in each individual region. Meanwhile, SkyWalker preserves KV-Cache locality and load balancing, ensuring cost efficiency without sacrificing performance. SkyWalker achieves this with a cache-aware cross-region traffic handler and a selective pushing based load balancing mechanism. Our evaluation on real-world workloads shows that it achieves 1.12-2.06× higher throughput and 1.74-6.30× lower latency compared to existing load balancers, while reducing total serving cost by 25%.

## 中文摘要

在多区域环境中高效地服务大语言模型（LLM）仍是一项挑战。出于成本和GPU可获得性的考虑，提供商通常使用长期承诺的实例（如预留实例或本地集群）在多个区域部署LLM，而这些实例往往因其仅处理区域内流量以及流量的昼夜波动而利用不足。本文提出SkyWalker，一个面向LLM推理的多区域负载均衡器，通过跨区域流量处理汇聚各区域的昼夜模式。借此，SkyWalker使提供商能够依据预期的全局需求而非各区域的峰值需求来预留实例。同时，SkyWalker保持KV缓存局部性与负载均衡，在不牺牲性能的前提下确保成本效益。SkyWalker通过缓存感知的跨区域流量处理器和基于选择性推送的负载均衡机制实现这一点。我们在真实负载上的评估表明，与现有负载均衡器相比，它实现了1.12–2.06倍更高的吞吐和1.74–6.30倍更低的延迟，同时将总服务成本降低25%。

**英文关键词：** Load Balancing, AI Serving, Multi-Region, Cloud Computing

**中文关键词：** 负载均衡、AI服务、多区域、云计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
