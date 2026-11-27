---
title: "From Optimal to Practical: Efficient Micro-op Cache Replacement Policies for Data Center Applications"
description: "HPCA 2025 · Cacheno Royale"
tags:
  - "HPCA2025"
  - "Cacheno Royale"
---

# From Optimal to Practical: Efficient Micro-op Cache Replacement Policies for Data Center Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Cacheno Royale。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Cacheno Royale</p>
</div>

**论文链接**：
**作者**：Kan Zhu (University of Washington), Yilong Zhao (Shanghai Jiao Tong University), Yufei Gao (Tsinghua University), Peter Braun (UCSC), Tanvir Ahmed Khan (Columbia University in the City of New York), Heiner Litz (UC Santa Cruz), Baris Kasikci (University of Washington and Google), Shuwen Deng (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

从最优到实用：面向数据中心应用的高效微操作缓存替换策略

## 英文摘要

Optimizing the CPU frontend has become crucial for modern processors with intricate instruction decoding logic, especially for efficiently running planet-scale data center applications. Micro-operation (micro-op) cache is a key unit to help improve the energy efficiency of the CPU frontend. Unfortunately, we find that data center applications suffer from frequent micro-op cache misses due to the lack of an effective micro-op cache replacement policy. Developing micro-op cache-specific replacement policies is challenging, as there currently does not exist an optimal theoretical solution akin to Belady’s algorithm for conventional caches. As a result, it is unknown by how much replacement policies can be improved and how to get there. To address these challenges, we introduce FLACK, a new near-optimal offline policy that considers the key features of the micro-op cache, such as variable and disproportional costs of micro-op cache misses and partial hits. We show that FLACK substantially outperforms Belady’s algorithm, thus establishing a new baseline for micro-op cache replacement policies. We then design FURBYS, a practical policy that mimics FLACK via profile-guided methods. FURBYS has three key components to perform cache replacement decisions: (1) it uses profiles of the whole-execution hit/miss behavior, (2) it detects locally (transiently) hot data, and (3) it selectively ignores data with profiled low hit rates. We evaluate FLACK and FURBYS using 11 data center applications and find that FLACK demonstrates an average bound of 30.21% miss reduction, achieving 4.46% greater miss reduction than Belady’s algorithm. Our practical policy, FURBYS, provides 14.34% average miss reduction compared to LRU, which is 1.84× greater than the current state-of-the-art replacement policy, contributing to 3.10% of performance-per-watt improvement for the CPU core. On average, in terms of miss reduction and IPC gain, FURBYS is equivalent to LRU policy on 1.5× micro-op cache sizes (up to 2×), demonstrating the effectiveness of the proposed replacement policy.

## 中文摘要

对于指令译码逻辑复杂的现代处理器，优化 CPU 前端已变得至关重要，尤其是为高效运行行星规模的数据中心应用。微操作（micro-op）缓存是帮助提升 CPU 前端能效的关键单元。然而我们发现，由于缺乏有效的微操作缓存替换策略，数据中心应用遭受频繁的微操作缓存缺失。开发微操作缓存专用替换策略颇具挑战，因为目前尚不存在类似传统缓存中 Belady 算法那样的最优理论方案，故替换策略还有多大改进空间、如何达到都是未知的。为此我们提出 FLACK，一种新的近最优离线策略，它考虑微操作缓存的关键特征，如微操作缓存缺失与部分命中的代价可变且不成比例。FLACK 显著优于 Belady 算法，为微操作缓存替换策略确立了新的基线。随后我们设计了 FURBYS，一种通过剖析引导方法模仿 FLACK 的实用策略。FURBYS 有三个关键组件用于执行缓存替换决策：(1) 使用全执行期命中/缺失行为的剖析信息，(2) 检测局部（瞬态）热数据，(3) 选择性忽略剖析命中率低的数据。我们使用 11 个数据中心应用评估 FLACK 与 FURBYS，发现 FLACK 给出的缺失减少上界平均为 30.21%，比 Belady 算法多减少 4.46%。我们的实用策略 FURBYS 相比 LRU 提供 14.34% 的平均缺失减少，比当前最先进的替换策略高出 1.84 倍，并为 CPU 核心贡献 3.10% 的每瓦性能提升。平均而言，在缺失减少与 IPC 提升上，FURBYS 相当于容量 1.5 倍（最高 2 倍）的微操作缓存上的 LRU 策略，证明了所提策略的有效性。
