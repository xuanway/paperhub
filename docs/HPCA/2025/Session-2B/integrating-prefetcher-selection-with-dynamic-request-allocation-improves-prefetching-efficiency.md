---
title: "Integrating Prefetcher Selection with Dynamic Request Allocation Improves Prefetching Efficiency"
description: "HPCA 2025 · Speculating in Vegas"
tags:
  - "HPCA2025"
  - "Speculating in Vegas"
---

# Integrating Prefetcher Selection with Dynamic Request Allocation Improves Prefetching Efficiency

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Speculating in Vegas。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Speculating in Vegas</p>
</div>

**论文链接**：
**作者**：Mengming Li (Hong Kong University of Science and Technology), Qijun Zhang (Hong Kong University of Science and Technology), Yongqing Ren (Intel Corporation), Zhiyao Xie (Hong Kong University of Science and Technology)
**会议**：HPCA 2025

---

## 中文标题

将预取器选择与动态请求分配相结合以提升预取效率

## 英文摘要

Hardware prefetching plays a critical role in hiding the off-chip DRAM latency. The complexity of applications results in a wide variety of memory access patterns, prompting the development of numerous cache-prefetching algorithms. Consequently, commercial processors often employ a hybrid of these algorithms to enhance the overall prefetching performance. Nonetheless, since these prefetchers share hardware resources, conflicts arising from competing prefetching requests can negate the benefits of hardware prefetching. Under such circumstances, several prefetcher selection algorithms have been proposed to mitigate conflicts between prefetchers. However, these prior solutions suffer from two limitations. First, the input demand request allocation is inaccurate. Second, the prefetcher selection criteria are coarse-grained. In this paper, we address both limitations by introducing an efficient and widely applicable prefetcher selection algorithm— Alecto1, which tailors the demand requests for each prefetcher. Every demand request is first sent to Alecto to identify suitable prefetchers before being routed to prefetchers for training and prefetching. Our analysis shows that Alecto is adept at not only harmonizing prefetching accuracy, coverage, and timeliness but also significantly enhancing the utilization of the prefetcher table, which is vital for temporal prefetching. Alecto outperforms the state-of-the-art RL-based prefetcher selection algorithm— Bandit by 2.76% in single-core, and 7.56% in eight-core. For memory-intensive benchmarks, Alecto outperforms Bandit by 5.25%. Alecto consistently delivers state-of-the-art performance in scheduling various types of cache prefetchers. In addition to the performance improvement, Alecto can reduce the energy consumption associated with accessing the prefetchers’ table by 48% (7% energy reduction on the entire memory hierarchy), while only adding less than 1 KB of storage overhead.

## 中文摘要

硬件预取对隐藏片外 DRAM 时延至关重要。应用复杂性带来多样的访存模式，催生了众多缓存预取算法，商用处理器因此常采用多种算法的混合来提升整体预取性能。然而这些预取器共享硬件资源，竞争性请求引发的冲突会抵消预取收益，于是出现了若干缓解冲突的预取器选择算法。但这些方案有两个局限：输入的需求请求分配不准确，预取器选择准则过于粗粒度。本文通过引入高效且通用的预取器选择算法 Alecto 同时解决这两个局限，它为每个预取器定制需求请求：每个需求请求先送到 Alecto 识别合适的预取器，再路由给预取器进行训练与预取。分析表明 Alecto 不仅能协调预取准确率、覆盖率与及时性，还能显著提升预取器表的利用率，这对时序预取至关重要。Alecto 在单核下比最先进的基于强化学习的 Bandit 高 2.76%，八核下高 7.56%；在访存密集型基准上比 Bandit 高 5.25%，并在调度各类缓存预取器时始终达到最先进性能。此外，Alecto 可将访问预取器表的能耗降低 48%（整个存储层次降低 7%），仅增加不到 1 KB 存储开销。
