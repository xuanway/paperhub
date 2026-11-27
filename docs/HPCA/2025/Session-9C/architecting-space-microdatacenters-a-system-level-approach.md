---
title: "Architecting Space Microdatacenters: A System-level Approach"
description: "HPCA 2025 · Finding the Best Table"
tags:
  - "HPCA2025"
  - "Finding the Best Table"
---

# Architecting Space Microdatacenters: A System-level Approach

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Finding the Best Table。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Finding the Best Table</p>
</div>

**论文链接**：
**作者**：Nathaniel Bleier (University of Michigan), Rick Eason (University of Illinois at Urbana-Champaign), Michael Lembeck (University of Illinois at Urbana-Champaign), Rakesh Kumar (University of Illinois at Urbana-Champaign)
**会议**：HPCA 2025

---

## 中文标题

空间微数据中心架构设计：一种系统级方法

## 英文摘要

Server-based computing in space has been recently proposed due to potential benefits in terms of capability, latency, security, sustainability, and cost. Despite this, there has been no work asking the question: how should we architect systems for server-based computing in space when considering overall cost. This paper presents a Total Cost of Ownership (TCO)-based approach to architecture of server-based computing systems for space (Space Microdatacenters - SµDC) for processing data produced by low Earth orbit (LEO)- based Earth observation (EO) satellites. We show that power of compute is the primary factor in determining SµDC TCO, though the dependence is sublinear. Second, the impact of compute mass, monetary cost, and communication on TCO is relatively insignificant. Third, architectures with the highest FLOPs W provide much higher performance per TCO $ even if they have poor FLOPs $. We leverage these insights to advocate extreme heterogeneity designs for SµDCs. These designs reduce SµDC TCO by 116× in spite of poor FLOPs $ characteristics. We also show that (a) collaborative compute constellations — constellations in which EO satellites are also equipped with compute hardware — further improve SµDC TCO by 1.31 to 1.74×, (b) a distributed architecture reduces TCO by 10% over a monolithic architecture, and (c) low monetary cost of compute can be leveraged to provide near zero cost compute overprovisioning which improves an SµDC’s availability significantly and supports graceful degradation. Overall, this is the first paper on cost-aware architecture and optimization of a SµDC.

## 中文摘要

近期已有研究提出在太空中进行基于服务器的计算，因为其在能力、时延、安全性、可持续性与成本方面具有潜在优势。尽管如此，尚无工作提出这样的问题：在考虑总成本时，应如何为太空中的基于服务器的计算设计系统架构。本文提出一种基于总拥有成本（TCO）的方法，用于为处理低地球轨道（LEO）地球观测（EO）卫星所产生数据的太空基于服务器计算系统（空间微数据中心，SµDC）设计架构。我们表明，计算功率是决定 SµDC TCO 的首要因素，尽管这种依赖关系是次线性的。其次，计算硬件的质量、货币成本与通信对 TCO 的影响相对不重要。第三，具有最高 FLOPs W 的架构即便 FLOPs $ 表现较差，也能提供高得多的每 TCO 美元性能。我们利用这些洞察倡导 SµDC 的极端异构设计。这些设计尽管 FLOPs $ 特性较差，却将 SµDC 的 TCO 降低了 116×。我们还表明：（a）协作式计算星座，即 EO 卫星也搭载计算硬件的星座，可进一步将 SµDC 的 TCO 改善 1.31 至 1.74×；（b）分布式架构相较单体架构可将 TCO 降低 10%；（c）计算的低货币成本可用于提供近乎零成本的算力超额配置，显著提升 SµDC 的可用性并支持优雅降级。总体而言，这是首篇关于 SµDC 成本感知架构与优化的论文。
