---
title: "Push Multicast: A Speculative and Coherent Interconnect for Mitigating Manycore CPU Communication Bottleneck"
description: "HPCA 2025 · Colluding to Even the Odds"
tags:
  - "HPCA2025"
  - "Colluding to Even the Odds"
---

# Push Multicast: A Speculative and Coherent Interconnect for Mitigating Manycore CPU Communication Bottleneck

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Colluding to Even the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Colluding to Even the Odds</p>
</div>

**论文链接**：
**作者**：Jiayi Huang (HKUST(GZ)), Yanhua Chen (HKUST(GZ)), Zhe Wang (Intel Labs), Christopher J. Hughes (Intel), Yufei Ding (UCSD), Yuan Xie (HKUST)
**会议**：HPCA 2025

---

## 中文标题

Push Multicast：缓解众核 CPU 通信瓶颈的推测式一致性互连

## 英文摘要

As CPUs scale up to many cores, the bandwidth of the network-on-chip (NoC) and cache can soon become the performance bottleneck. In modern processors, the cache hierarchy plays a reactive role to supply data upon request. In parallel programs, shared data accesses from different cores at different times can consume large cache and NoC bandwidth for the same data. These same-data accesses inherently have redundancy and lead to inefficient cache and NoC bandwidth utilization. In this work, we propose Push Multicast, a speculative and coherent interconnect. We transform the last-level cache into a proactive agent to push data to other sharers upon replying to the demand requester. Pushing enables effective multicasting to reduce LLC and NoC bandwidth consumption. A coherent in-network filter is proposed to prune the outstanding requests in the routers along the way of the pushed data delivery. Moreover, a dynamic mechanism is designed to pause and resume pushing adaptively. Compared with a system with an L1 Bingo data prefetcher and an L2 Stride prefetcher, Push Multicast achieves an average of 33% NoC bandwidth saving, a geomean of 1.02× and a maximum of 1.56× speedup in a 16-core system. In a 64-core system, it further achieves an average of 43% NoC bandwidth saving, along with a geomean of 1.11× and a maximum of 2.08× speedup.

## 中文摘要

随着 CPU 扩展到众多核心，片上网络（NoC）与缓存的带宽很快就会成为性能瓶颈。在现代处理器中，缓存层次结构扮演被动响应的角色，在收到请求时提供数据。在并行程序中，不同核心在不同时刻对共享数据的访问会为同一数据消耗大量缓存与 NoC 带宽。这些对同一数据的访问本质上具有冗余性，导致缓存与 NoC 带宽利用效率低下。在本工作中，我们提出 Push Multicast，一种推测式且一致的互连。我们把末级缓存转变为主动代理，在回复需求请求方时把数据推送给其他共享者。推送使有效的多播成为可能，从而降低 LLC 与 NoC 的带宽消耗。我们提出一种一致性网内过滤器，用于剪除沿推送数据传递路径的路由器中未完成的请求。此外，设计了一种动态机制来自适应地暂停与恢复推送。与带有 L1 Bingo 数据预取器与 L2 Stride 预取器的系统相比，Push Multicast 在 16 核系统中平均节省 33% 的 NoC 带宽，几何平均加速 1.02 倍、最高 1.56 倍。在 64 核系统中，它进一步平均节省 43% 的 NoC 带宽，几何平均加速 1.11 倍、最高 2.08 倍。
