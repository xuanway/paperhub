---
title: "PRISM: A Miss-Attribution-Guided Temporal Prefetcher Beyond Metadata Management"
description: "MICRO 2026 · Session 2B · PRISM：超越元数据管理的缓存未命中归因驱动时序预取器"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# PRISM: A Miss-Attribution-Guided Temporal Prefetcher Beyond Metadata Management

**中文标题：** PRISM：超越元数据管理的缓存未命中归因驱动时序预取器

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Yiquan Lin, Jianxiang Liu, Yiquan Chen, Wenhai Lin, Zonghui Wang, Wenzhi Chen

**来源：** MICRO 2026，pp. 592–608；[DOI](https://doi.org/10.1109/MICRO67795.2026.00054)

## 英文摘要

Temporal prefetching is a promising solution for handling complex, irregular memory access patterns. Recent studies have transitioned to cache-resident metadata designs and made significant progress by optimizing metadata management. In this paper, we conduct a systematic miss attribution analysis to explore the performance bottlenecks of temporal prefetching. This analysis decomposes cache misses persisting under a baseline temporal prefetcher into four distinct categories: compulsory misses, unseen correlations, late prefetches, and metadata evictions. Our quantitative breakdown reveals that the performance bottlenecks are highly workload-dependent. While metadata management remains critical, other categories frequently emerge as the primary bottlenecks under specific scenarios. This underscores the necessity to jointly address all three non-compulsory miss categories. To this end, we propose PRISM, a miss-attribution-guided temporal prefetcher with three key innovations: (1) PC-Triggered Prefetching (PCTP): PCTP constructs PC-address correlations and establishes an auxiliary PC-triggered prefetching path to mitigate misses that elude traditional address-to-address tracking. (2) Timeliness-Guaranteed Prefetching (TGP): TGP synergistically combines static lookahead with adaptive degree adjustment to enhance timeliness without compromising accuracy. It further leverages redundancy filtering to minimize metadata traffic. (3) Utility-Aware Management (UAM): UAM optimizes metadata efficiency by integrating Bimodal Metadata Partitioning, which dynamically toggles between conservative and aggressive allocation modes, with a selective insertion policy to filter redundant metadata and a fine-tuned SHiP variant to prolong the residency of high-utility correlations. Evaluation across five benchmark suites shows that PRISM outperforms state-of-the-art temporal prefetchers, Triangel and Prophet, by 5.8% and 7.8%, respectively. The source code of PRISM is freely available at https://github.com/YIQUAN-LIN/prism.

## 中文摘要

时间预取是处理复杂、不规则内存访问模式的一种很有前景的解决方案。最近的研究已经转向缓存驻留元数据设计，并通过优化元数据管理取得了重大进展。在本文中，我们进行了系统的缺失归因分析，以探索时间预取的性能瓶颈。此分析将基线时间预取器下持续存在的缓存未命中分解为四个不同的类别：强制未命中、未见的相关性、时延预取和元数据逐出。我们的定量分析表明，性能瓶颈高度依赖于工作负载。虽然元数据管理仍然很重要，但在特定场景下，其他类别经常成为主要瓶颈。这强调了共同解决所有三个非强制性失误类别的必要性。为此，我们提出了 PRISM，一种由未命中归因引导的时间预取器，具有三个关键创新：（1）PC 触发预取（PCTP）：PCTP 构建 PC 地址相关性并建立辅助 PC 触发预取路径，以减少传统地址到地址跟踪的未命中。 (2)及时性保证预取(TGP)：TGP将静态前瞻与自适应程度调整协同结合，以在不影响准确性的情况下增强及时性。它进一步利用冗余过滤来最大限度地减少元数据流量。 (3) 效用感知管理 (UAM)：UAM 通过集成双模态元数据分区来优化元数据效率，双模态元数据分区在保守和激进的分配模式之间动态切换，并通过选择性插入策略来过滤冗余元数据，并通过微调的 SHiP 变体来延长高效用相关性的驻留时间。对五个基准套件的评估表明，PRISM 的性能分别优于最先进的时间预取器 Triangel 和 Prophet 5.8% 和 7.8%。 PRISM 的源代码可以在 https://github.com/YIQUAN-LIN/prism 上免费获取。

## 中文关键词

微架构；数据预取；硬件预取器；时序预取；未命中归因

## 代码与研究制品

- 代码仓库：[https://github.com/YIQUAN-LIN/prism](https://github.com/YIQUAN-LIN/prism)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
