---
title: "NearFetch: Saving Inter-Module Bandwidth in Many-Chip-Module GPUs"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# NearFetch: Saving Inter-Module Bandwidth in Many-Chip-Module GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Xia Zhao (Defense Innovation Institute), Guangda Zhang (Defense Innovation Institute), Lu Wang (Defense Innovation Institute), Shiqing Zhang (Defense Innovation Institute), Huadong Dai (Defense Innovation Institute)
**会议**：HPCA 2025

---

## 中文标题

NearFetch：在多芯片模块 GPU 中节省模块间带宽

## 英文摘要

As Graphics Processing Units (GPUs) face increasing computing demands that surpass single-module capabilities due to transistor scaling and lithography constraints, the necessity for expanding the module count within GPUs grows. This escalation faces a significant challenge: the total inter-module bandwidth in many-chip-module GPUs is limited by manufacturing constraints in organic substrates or silicon interposers. Unlike Central Processing Units (CPUs), which are latency-sensitive, GPUs leverage their high thread-level parallelism to effectively hide memory access latency through simultaneous multithreading. This attribute makes GPUs inherently sensitive to bandwidth constraints, making the efficient exploitation of available intermodule bandwidth important. In this paper, we identify that fetching data from faraway memory in many-chip-module GPUs can easily cause bandwidth contention which degrades the real achieved data bandwidth per GPU module compared to fetching data from nearby memory. To further analyze this problem, we introduce the Inter-Module Bandwidth per Access (IBPA) metric for quantifying bandwidth usage and finding the network hop count directly impacts the IBPA and network contention. Next, we propose NearFetch, a routing-based solution to reduce IBPA. NearFetch works due to the fact that GPU modules along the routing path are typically much closer to the source GPU module while these GPU modules can supply 29.1% of data for high-sharing applications. Near-Fetch consists of two primary components: a data forwarding scheme, enabling data forwarding when the data resides in a remote GPU module, and a topology-aware Miss Status Handling Register (MSHR) coalescing scheme, responsible for recording the memory address information for future use in case of a data miss. By leveraging the data locality among various GPU modules, NearFetch substantially minimizes inter-module bandwidth usage, eliminating the need to fetch data from distant memory partitions. Our evaluation of NearFetch within the context of many-chip-module GPUs, across applications exhibiting diverse degrees of data locality, reveals that it reduces IBPA by 42.6% and enhances performance by an average of 52.2% (with up to 98.1% improvement) for high-sharing workloads.

## 中文摘要

随着 GPU 的计算需求因晶体管缩放与光刻限制而超越单模块能力，扩展 GPU 内模块数量的必要性日增。但这面临重大挑战：多芯片模块 GPU 的模块间总带宽受有机基板或硅中介层制造约束的限制。与对延迟敏感的 CPU 不同，GPU 凭借高线程级并行性，以同时多线程隐藏访存延迟，因而天生对带宽敏感，高效利用可用模块间带宽十分重要。本文指出，在多芯片模块 GPU 中从远端内存取数易引发带宽争用，相较近端取数会降低每个 GPU 模块实际达到的数据带宽。为深入分析，我们引入每次访问的模块间带宽（IBPA）指标来量化带宽使用，并发现网络跳数直接影响 IBPA 与网络争用。据此我们提出 NearFetch，一种基于路由降低 IBPA 的方案。其有效性源于：路由路径上的 GPU 模块通常远比源 GPU 模块更近，且这些模块能为高共享应用提供 29.1% 的数据。NearFetch 包含两个主要组件：数据转发方案，在数据位于远端 GPU 模块时转发数据；以及拓扑感知的缺失状态处理寄存器（MSHR）合并方案，负责记录内存地址信息以备数据缺失时使用。借助各 GPU 模块间的数据局部性，NearFetch 大幅减少模块间带宽使用，无需从远端内存分区取数。我们在数据局部性不同的应用上评测 NearFetch，结果显示其使 IBPA 降低 42.6%，高共享负载性能平均提升 52.2%（最高达 98.1%）。
