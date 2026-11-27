---
title: "SMTcheck: Accurate SMT Interference Prediction to Improve Scheduling Efficiency in Datacenters"
description: "HPCA 2026 · CPU Microarchitecture Optimization"
tags:
  - "HPCA2026"
  - "CPU Microarchitecture Optimization"
---

# SMTcheck: Accurate SMT Interference Prediction to Improve Scheduling Efficiency in Datacenters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: CPU Microarchitecture Optimization。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · CPU Microarchitecture Optimization</p>
</div>

**论文链接**：
**作者**：Sanghyun Kim Sungkyunkwan University , Jinhyeok Oh Sungkyunkwan University , Taehun Kim Sungkyunkwan University , Gyutae Kim Sungkyunkwan University , Youngsok Kim Yonsei University , Jaehyun Hwang Sungkyunkwan University , Joonsung Kim Sungkyunkwan University
**会议**：HPCA 2026

---

## 中文标题

SMTcheck：精准预测 SMT 干扰以提升数据中心调度效率

## 英文摘要

Simultaneous multithreading (SMT) is widely used in modern x86 processors to improve core utilization by sharing hardware resources between co-located threads. However, such resource sharing often leads to severe performance interference, making efficient workload co-scheduling difficult, especially given the complexity and diversity of modern x86 CPUs. Our analysis reveals that SMT-aware workload scheduling can significantly improve system throughput and reduce tail latency for datacenter workloads, but identifying optimal thread combinations is challenging due to the lack of visibility into platform-specific resource sharing behaviors. In this paper, we present SMTcheck, a lightweight, accurate, and platform-independent methodology for predicting SMT interference for diverse x86 processors. SMTcheck uses carefully designed code snippets (Diags) to extract hidden microarchitectural features of performance-critical shared resources. With these extracted features, SMTcheck builds per-resource microbenchmarks (Injectors) to apply pinpoint pressure to specific target resources in order to capture workload-specific contention characteristics. SMTcheck then constructs a hardware-aware contention model to predict performance interference between arbitrary workload pairs without requiring exhaustive profiling. We evaluate SMTcheck on six x86 desktop processors and five x86 server processors from Intel and AMD across different generations and show that it achieves high prediction accuracy by up to 95.5% (94.6% on average). We further demonstrate its effectiveness by implementing a contention-aware scheduler in the Linux kernel. Compared to the default Linux scheduler, our contention-aware scheduler significantly reduces tail latency for latency-critical workloads (e.g., database, key-value store) by up to 36.09%, and improves the overall system throughput by up to 1.072×. Finally, using real-world cluster traces from Alibaba and Google, we demonstrate that SMTcheck incurs negligible profiling overheads (≈ 0.113%), making it practical for deployment in production-scale datacenter environments.

## 中文摘要

同时多线程（SMT）在现代 x86 处理器中被广泛用于通过在共置线程间共享硬件资源来提高核利用率。然而，这种资源共享常导致严重的性能干扰，使高效的负载协同调度变得困难，尤其考虑到现代 x86 CPU 的复杂性与多样性。我们的分析表明，SMT 感知的负载调度能显著提升系统吞吐并降低数据中心负载的尾时延，但由于缺乏对平台特定资源共享行为的可见性，识别最优线程组合颇具挑战。本文提出 SMTcheck，一种轻量、准确且与平台无关的方法，用于预测多种 x86 处理器的 SMT 干扰。SMTcheck 使用精心设计的代码片段（Diags）提取性能关键共享资源的隐藏微架构特征。基于这些特征，SMTcheck 构建按资源划分的微基准（Injector），对特定目标资源施加精准压力，以刻画负载特有的竞争特征。随后，SMTcheck 构建硬件感知的竞争模型，在无需穷举剖析的情况下预测任意负载对之间的性能干扰。我们在 Intel 与 AMD 不同世代的六款 x86 桌面处理器和五款 x86 服务器处理器上评估 SMTcheck，其预测准确率最高达 95.5%（平均 94.6%）。我们进一步在 Linux 内核中实现竞争感知调度器以验证其有效性。与默认 Linux 调度器相比，我们的调度器对时延敏感负载（如数据库、键值存储）将尾时延最多降低 36.09%，并将系统整体吞吐最多提升 1.072 倍。最后，我们利用来自阿里巴巴与 Google 的真实集群轨迹表明，SMTcheck 的剖析开销可忽略（约 0.113%），适合生产级数据中心环境。
