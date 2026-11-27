---
title: "AutoHAAP: Automated Heterogeneity-Aware Asymmetric Partitioning for LLM Training"
description: "HPCA 2026 · Distributed and Multi-GPU Training"
tags:
  - "HPCA2026"
  - "Distributed and Multi-GPU Training"
---

# AutoHAAP: Automated Heterogeneity-Aware Asymmetric Partitioning for LLM Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Distributed and Multi-GPU Training。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Distributed and Multi-GPU Training</p>
</div>

**论文链接**：
**作者**：Yuanyuan Wang Zhejiang Lab , Nana Tang Zhejiang Lab , Yuyang Wang Zhejiang Lab , Shu Pan Zhejiang Lab , Dingding Yu Zhejiang Lab , Zeyue Wang Zhejiang Lab , Mou Sun Zhejiang Lab , Kejie Fu Zhejiang Lab , Fangyu Wang Zhejiang Lab , Yunchuan Chen Zhejiang Lab , Ning Sun Zhejiang Lab , Fei Yang Zhejiang Lab
**会议**：HPCA 2026

---

## 中文标题

AutoHAAP：面向 LLM 训练的自动化异构感知非对称划分

## 英文摘要

Heterogeneous clusters with diverse devices mitigate computational and memory burdens in large language model (LLM) training, yet their inherent resource heterogeneity, characterized by divergent computation, memory, and bandwidth capabilities, renders manual parallelization strategy optimization both challenging and time-intensive. Automatic parallelization is critical for scaling complex workloads across heterogeneous architectures. However, previous methodologies face significant inefficiencies. First, insufficient pruning of the parameter initialization space results in impractically large search spaces. Second, the prevailing automatic parallel search strategies exhibit suboptimal performance in load balancing and resource constraint adaptation. Third, dynamic parallel strategy tuning incurs substantial overhead due to redundant latency calculations for operators with unchanged configurations, leading to unnecessary computational costs. Therefore, insufficient search space pruning, suboptimal load/resource adaptation, and redundant latency computation are identified as the major bottlenecks in our research. To address these challenges, we propose AutoHAAP (Automated Heterogeneity-Aware Asymmetric Partitioning), a novel framework incorporating three core innovations: (1) memory-aware initialization to drastically reduce viable search spaces; (2) a heterogeneity-aware load-balancing estimator that guides resource-efficient configuration search; and (3) state caching mechanisms eliminating redundant latency calculations. Evaluations across GPT3 and Llama3 models of varying scales on both homogeneous and heterogeneous clusters demonstrate that AutoHAAP achieves 0.68–98× search efficiency gains, 6.57%–106.9%× throughput improvements in homogeneous environments, and 10.1%-22.28%× throughput enhancements in heterogeneous setups. These results validate AutoHAAP’s effectiveness in distributed LLM training on diverse hardware.

## 中文摘要

由多种设备构成的异构集群可缓解大语言模型（LLM）训练中的计算与内存负担，但其固有的资源异构性——计算、内存与带宽能力差异——使人工优化并行化策略既困难又耗时。自动并行化对在异构架构上扩展复杂负载至关重要，但已有方法低效：初始化空间剪枝不足致搜索空间过大，主流自动搜索策略在负载均衡与资源约束适配上表现欠佳，动态调优又因对配置未变的算子重复计算时延而开销可观。为此我们提出 AutoHAAP（自动化异构感知非对称划分），含三项创新：内存感知初始化大幅缩小搜索空间，异构感知负载均衡评估器引导资源高效的配置搜索，状态缓存机制消除冗余时延计算。在同构与异构集群上对多种规模 GPT3 与 Llama3 的评估表明，AutoHAAP 取得 0.68–98 倍搜索效率提升、同构环境 6.57%–106.9% 倍吞吐提升与异构环境 10.1%–22.28% 倍吞吐提升，验证了其在多样硬件上开展分布式 LLM 训练的有效性。
