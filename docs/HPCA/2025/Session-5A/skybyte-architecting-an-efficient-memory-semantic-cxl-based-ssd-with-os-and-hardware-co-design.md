---
title: "SkyByte: Architecting An Efficient Memory-Semantic CXL-based SSD with OS and Hardware Co-design"
description: "HPCA 2025 · Stashing your Winnings"
tags:
  - "HPCA2025"
  - "Stashing your Winnings"
---

# SkyByte: Architecting An Efficient Memory-Semantic CXL-based SSD with OS and Hardware Co-design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stashing your Winnings。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stashing your Winnings</p>
</div>

**论文链接**：
**作者**：Haoyang Zhang (University of Illinois Urbana Champaign), Yuqi Xue (University of Illinois Urbana Champaign), Yirui Eric Zhou (University of Illinois Urbana Champaign), Shaobo Li (University of Illinois Urbana Champaign), Jian Huang (University of Illinois Urbana Champaign)
**会议**：HPCA 2025

---

## 中文标题

SkyByte：操作系统与硬件协同设计的高效内存语义 CXL SSD

## 英文摘要

The CXL-based solid-state drive (CXL-SSD) provides a promising approach towards scaling the main memory capacity at low cost. However, the CXL-based SSD faces performance challenges due to the long flash access latency and unpredictable events such as garbage collection in the SSD device, stalling the host processor and wasting compute cycles. Although the CXL interface enables the byte-granular data access to the SSD, accessing flash chips is still at page granularity due to physical limitations. The mismatch of access granularity causes significant unnecessary I/O traffic to flash chips, worsening the suboptimal end-to-end data access performance. In this paper, we present SkyByte, an efficient CXL-based SSD that employs a holistic approach to address the aforementioned challenges by co-designing the host operating system (OS) and SSD controller. To alleviate the long memory stall when accessing the CXL-SSD, SkyByte revisits the OS context switch mechanism and enables opportunistic context switches upon the detection of long access delays. To accommodate byte-granular data accesses, SkyByte architects the internal DRAM of the SSD controller into a cacheline-level write log and a page-level data cache, and enables data coalescing upon log cleaning to reduce the I/O traffic to flash chips. SkyByte also employs optimization techniques that include adaptive page migration for exploring the performance benefits of fast host memory by promoting hot pages in CXL-SSD to the host. We implement SkyByte with a CXL-SSD simulator and evaluate its efficiency with various data-intensive applications. Our experiments show that SkyByte outperforms current CXL-based SSD by 6.11×, and reduces the I/O traffic to flash chips by 23.08× on average. SkyByte also reaches 75% of the performance of the ideal case that assumes unlimited DRAM capacity in the host, which offers an attractive cost-effective solution.

## 中文摘要

基于 CXL 的固态盘（CXL-SSD）为低成本扩展主存容量提供了有前景的途径。然而，长闪存访问时延以及垃圾回收等不可预测事件会阻塞主机处理器、浪费计算周期，使 CXL-SSD 面临性能挑战。CXL 接口虽支持字节粒度访问 SSD，但受物理限制，访问闪存芯片仍以页为粒度；粒度不匹配造成大量不必要的闪存 I/O 流量，进一步劣化端到端访问性能。本文提出 SkyByte，通过协同设计主机操作系统（OS）与 SSD 控制器，以整体化方法应对上述挑战：为缓解访问 CXL-SSD 的长内存停顿，SkyByte 重新审视 OS 上下文切换机制，在检测到长访问延迟时启用机会性上下文切换；为适应字节粒度访问，SkyByte 将 SSD 控制器内部 DRAM 构建为缓存行级写日志与页级数据缓存，并在日志清理时合并数据以减少闪存 I/O 流量；它还采用自适应页迁移，将 CXL-SSD 中的热页提升至主机，以挖掘快速主机内存的性能收益。我们用 CXL-SSD 模拟器实现 SkyByte，并在多种数据密集型应用中评估其效率。实验表明，SkyByte 相比现有基于 CXL 的 SSD 快 6.11 倍，对闪存芯片的 I/O 流量平均降低 23.08 倍，并达到假设主机 DRAM 容量无限这一理想情况性能的 75%，是高性价比的方案。
