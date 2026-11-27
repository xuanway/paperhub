---
title: "HDPAT: Hierarchical Distributed Page Address Translation for Wafer-Scale GPUs"
description: "HPCA 2026 · Memory Systems for Scalable Computing"
tags:
  - "HPCA2026"
  - "Memory Systems for Scalable Computing"
---

# HDPAT: Hierarchical Distributed Page Address Translation for Wafer-Scale GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory Systems for Scalable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory Systems for Scalable Computing</p>
</div>

**论文链接**：
**作者**：daoxuan xu William & Mary , Ying Li William & Mary , Yuwei Sun UIUC , Jie Ren William & Mary , Yifan Sun William&Mary
**会议**：HPCA 2026

---

## 中文标题

HDPAT：面向晶圆级 GPU 的分层分布式页地址转换

## 英文摘要

A Wafer-scale GPU connects a large number of chiplets via a high-bandwidth, low-latency interposer-based network, promising to overcome the communication bottleneck of traditional multi-GPU systems. While prior work has prototyped wafer-scale GPUs to demonstrate technical feasibility, scaling to massive chiplet counts creates new bottlenecks: virtual-to-physical address translation becomes severely constrained by massive concurrent requests and long multi-hop network latencies. We propose HDPAT, a hardware-accelerated distributed address translation system that addresses this challenge through three complementary techniques: (1) Concentric caching converts near-IOMMU chiplets into hierarchical translation caches based on their distance to the IOMMU. A lightweight rotation mechanism ensures that there is always a nearby chiplet that can provide translation caching. (2) The redirection table further reduces the burden of IOMMU by delegating translations to caching chiplets, and (3) Prefetching proactively delivers potentially needed address translation into the chiplet to improve translation cache hit rate. Experimental results on 14 representative workloads show that HDPAT improves overall performance by an average of 1.57×.

## 中文摘要

晶圆级 GPU 通过基于中介层的高带宽、低时延网络连接大量芯粒，有望突破传统多 GPU 系统的通信瓶颈。尽管已有工作通过原型验证了晶圆级 GPU 的技术可行性，但扩展到海量芯粒数量会带来新的瓶颈：虚拟到物理地址转换受制于海量并发请求和长距离多跳网络时延。我们提出 HDPAT，一种硬件加速的分布式地址转换系统，通过三项互补技术应对该挑战：（1）同心缓存根据芯粒到 IOMMU 的距离，将靠近 IOMMU 的芯粒转变为分层转换缓存，并采用轻量轮转机制保证总有邻近芯粒可提供转换缓存；（2）重定向表将转换委托给缓存芯粒，进一步减轻 IOMMU 的负担；（3）预取主动将可能需要的地址转换送达芯粒，以提高转换缓存命中率。在 14 个代表性负载上的实验结果表明，HDPAT 平均提升整体性能 1.57 倍。
