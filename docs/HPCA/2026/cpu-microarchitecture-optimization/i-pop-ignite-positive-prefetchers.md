---
title: "I-POP: Ignite Positive Prefetchers"
description: "HPCA 2026 · CPU Microarchitecture Optimization"
tags:
  - "HPCA2026"
  - "CPU Microarchitecture Optimization"
---

# I-POP: Ignite Positive Prefetchers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: CPU Microarchitecture Optimization。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · CPU Microarchitecture Optimization</p>
</div>

**论文链接**：
**作者**：Yiquan Lin Zhejiang University and Alibaba Group , Wenhai Lin Alibaba Group , Yiquan Chen Alibaba Group , Jiexiong Xu Zhejiang University and Alibaba Group , Shishun Cai Alibaba Group , Jiarong Ye Zhejiang University , Zonghui Wang Zhejiang University , Wenzhi Chen Zhejiang University
**会议**：HPCA 2026

---

## 中文标题

I-POP：点燃正向预取器

## 英文摘要

Hardware prefetching is a well-established technique for bridging the processor-memory performance gap. To improve cache miss coverage, modern processors often integrate multiple prefetchers. However, multi-prefetcher systems without proper management often suffer from suboptimal performance due to a surge of useless prefetches. Several techniques have been proposed to select appropriate prefetchers for issuing requests, but they all face limitations. Specifically, existing (1) static schemes lack feedback regulation mechanisms and suffer from inflexible prefetcher selections; (2) reinforcement learning (RL)- based schemes incur high overhead and suffer from adjustment lag; and (3) performance-counter-based schemes rely on inefficient runtime metrics that fail to accurately and clearly reflect a prefetcher’s true impact on performance. In this paper, we propose I-POP, a high-performance and low-overhead prefetcher management scheme for multi-prefetcher systems. I-POP introduces a novel runtime metric, Prefetch Effectiveness (PE), which aggregates each prefetch request’s beneficial and harmful effects to precisely quantify the impact of a prefetcher on performance, effectively overcoming the limitations of prior metrics. To compute and leverage this metric, I-POP incorporates two key components: the Metric Collector, which periodically calculates each prefetcher’s PE, and the Control Engine, which dynamically manages all prefetchers based on their PE values. Specifically, I-POP ignites (enables) prefetchers with positive PE values, adaptively tuning their aggressiveness, and disables those with non-positive PE. We evaluated I-POP on numerous workloads, and the results show I-POP outperforms two state-of-the-art approaches, Bandit and Alecto, by 4.2% and 3.5% across three benchmark suites in a single-core system, and 6.6% and 8.6% in a 16-core system, while incurring only 1.46 KB of storage overhead.

## 中文摘要

硬件预取是弥合处理器与内存性能差距的成熟技术。为提升缓存缺失覆盖率，现代处理器常集成多个预取器。然而，缺乏有效管理的多预取器系统常因无用预取激增而性能欠佳。已有若干技术通过挑选合适的预取器来发出请求，但都存在局限：静态方案缺少反馈调节机制，预取器选择不够灵活；基于强化学习（RL）的方案开销高且存在调节滞后；基于性能计数器的方案依赖低效的运行时指标，无法准确清晰地反映预取器对性能的真实影响。本文提出 I-POP，一种面向多预取器系统的高性能、低开销预取器管理方案。I-POP 引入新的运行时指标——预取有效性（PE），它汇总每个预取请求的有益与有害影响，以精确量化预取器对性能的影响，有效克服了以往指标的局限。为计算并利用该指标，I-POP 包含两个关键组件：定期计算各预取器 PE 的指标收集器，以及基于 PE 值动态管理所有预取器的控制引擎。具体而言，I-POP 点燃（启用）PE 为正的预取器并自适应调整其激进度，关闭 PE 非正的预取器。我们在大量负载上评估 I-POP，结果表明在单核系统中，I-POP 在三个基准测试集上分别比两种最先进方法 Bandit 与 Alecto 高出 4.2% 与 3.5%，在 16 核系统中高出 6.6% 与 8.6%，而仅带来 1.46 KB 的存储开销。
