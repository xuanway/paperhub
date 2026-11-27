---
title: "ASPA: Reassigning DDR5 Parity Bandwidth"
description: "HPCA 2026 · Memory System Reliability"
tags:
  - "HPCA2026"
  - "Memory System Reliability"
---

# ASPA: Reassigning DDR5 Parity Bandwidth

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory System Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory System Reliability</p>
</div>

**论文链接**：
**作者**：Fan Li University of Central Florida , Qiufeng Li George Washington University , Yanan Guo University of Rochester , Weidong Cao George Washington University , Xin Xin University of Central Florida
**会议**：HPCA 2026

---

## 中文标题

ASPA：重新分配 DDR5 的奇偶校验带宽

## 英文摘要

Recent memory advancements, such as DDR5, HBM3, and emerging memory-centric accelerators, primarily focus on increasing bandwidth capacity, yet often omit the significance of effective bandwidth utilization, i.e., bandwidth efficiency. Motivated by the suboptimal channel allocation in DDR5, where parity accounts for 25% bandwidth overhead, we propose ASPA, an efficiency-oriented solution that reallocates parity bandwidth to boost regular data transfer. The objective of ASPA is to enhance bandwidth efficiency without compromising reliability while maintaining low hardware overhead. In particular, we leverage existing CRC (Cyclic Redundancy Check) units in DRAM chips to opportunistically generate second-tier parity for the existing ECC (Error Correction Code) parity. For bulk-sized memory accesses, only the small second-tier parity is transmitted. This reduces the parity bandwidth consumption, allowing data chips to reuse the freed parity bandwidth for data transfer. Our observation indicates that the protection capability is sufficient when the second-tier parity (with a 64-bit size) is used exclusively for error detection. Furthermore, by exploiting underutilized resources in high-performance memory systems, ASPA is implemented with negligible hardware overhead.

## 中文摘要

近期的内存技术进步，如 DDR5、HBM3 以及新兴的以内存为中心的加速器，主要着眼于提升带宽总量，却往往忽视了有效带宽利用率（即带宽效率）的重要性。受 DDR5 中通道分配欠佳（奇偶校验占 25% 带宽开销）的启发，我们提出 ASPA，一种以效率为导向的方案，通过重新分配校验带宽来提升常规数据传输。ASPA 的目标是在不损害可靠性的同时提升带宽效率，并保持较低的硬件开销。具体而言，我们利用 DRAM 芯片中已有的 CRC（循环冗余校验）单元，为现有的 ECC（纠错码）校验机会性地生成第二级校验。对于大块内存访问，只需传输少量第二级校验，从而减少校验带宽消耗，使数据芯片能够把释放出的校验带宽复用于数据传输。我们的观察表明，当第二级校验（64 位）仅用于错误检测时，其保护能力已足够。此外，通过利用高性能内存系统中未被充分利用的资源，ASPA 的硬件开销可忽略不计。
