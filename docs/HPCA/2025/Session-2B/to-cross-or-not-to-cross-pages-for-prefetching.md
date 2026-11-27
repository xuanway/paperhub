---
title: "To Cross, or Not to Cross Pages for Prefetching?"
description: "HPCA 2025 · Speculating in Vegas"
tags:
  - "HPCA2025"
  - "Speculating in Vegas"
---

# To Cross, or Not to Cross Pages for Prefetching?

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Speculating in Vegas。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Speculating in Vegas</p>
</div>

**论文链接**：
**作者**：Georgios Vavouliotis (Huawei), Marti Torrents (Barcelona Supercomputing Center), Boris Grot (University of Edinburgh, Huawei Research), Kleovoulos Kalaitzidis (Huawei), Leeor Peled (Huawei), Marc Casas (Barcelona Supercomputing Center (BSC) – Universitat Politècnica de Catalunya (UPC))
**会议**：HPCA 2025

---

## 中文标题

预取时是否跨越页边界

## 英文摘要

Despite processor vendors reporting that cache prefetchers operating with virtual addresses are permitted to cross page boundaries, academia is focused on optimizing cache prefetching for patterns within page boundaries. This work reveals that page-cross prefetching at the first-level data cache (L1D) is seldom beneficial across different execution phases and workloads while showing that state-of-the-art L1D prefetchers are not very accurate at prefetching across page boundaries. In response, we propose MOKA, a holistic framework for designing Page-Cross Filters, i.e., microarchitectural schemes that ensure effective and accurate prefetching across page boundaries. MOKA combines (i) hashed perceptron predictors that use prefetcher-independent program features, (ii) predictors that adapt decisions based on the system state (e.g., TLB pressure), and (iii) a scheme to dynamically optimize predictions across different execution phases and workload types. We use the MOKA framework to prototype a Page-Cross Filter, named DRIPPER, for three relevant L1D prefetchers (Berti [60], IPCP [61], BOP [57]). We show that DRIPPER accurately enables page-cross prefetching only when it is beneficial for performance. For instance, Berti [60] (state-of-the-art prefetcher) combined with DRIPPER improves single-core geomean performance over Berti that always permits page-cross prefetches and Berti that always discards page-cross prefetches by 1.7%(1.2%) and 2.5%(2.1%) across 218 seen (178 unseen) workloads, respectively. Across 300 8-core mixes, the corresponding geomean speedups are 2.0% and 3.3%. Finally, we show that DRIPPER provides consistent benefits when both 4KB pages and 2MB large pages are used.

## 中文摘要

厂商称以虚拟地址工作的缓存预取器可跨页边界，但学术界只优化页边界内模式的预取。本文揭示一级数据缓存（L1D）的跨页预取在各执行阶段与各类负载中很少有益，且最先进的 L1D 预取器跨页预取并不准确。为此我们提出 MOKA，一个设计跨页过滤器的整体框架，即确保跨页预取有效且准确的微架构方案，它结合：（i）使用与预取器无关程序特征的哈希感知机预测器；（ii）依据系统状态（如 TLB 压力）调整决策的预测器；（iii）跨执行阶段与负载类型动态优化预测的方案。我们用 MOKA 为三种相关 L1D 预取器（Berti [60]、IPCP [61]、BOP [57]）原型化了跨页过滤器 DRIPPER，它仅在跨页预取有益时准确启用该预取。例如最先进的 Berti [60] 结合 DRIPPER 后，相对始终允许与始终丢弃跨页预取的 Berti，在 218 个已见（178 个未见）负载上单核几何平均提升 1.7%（1.2%）与 2.5%（2.1%）；在 300 个八核混合负载上加速比为 2.0% 与 3.3%。最后，DRIPPER 在 4KB 页与 2MB 大页下均有一致收益。
