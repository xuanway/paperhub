---
title: "Scheduling Cloud Block Storage Proactively and Reactively with Omar"
description: "EuroSys 2026 · Storage Systems · Xinqi Chen (Shanghai Jiao Tong University), Weidong Zhang (Alibaba Group), Zhong"
tags:
  - "EuroSys2026"
  - "Storage Systems"
---

# Scheduling Cloud Block Storage Proactively and Reactively with Omar

**中文标题：** 用 Omar 主动与被动地调度云块存储

**所属 Session：** [Session 7.3: Storage Systems](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Storage Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Storage Systems</p>
</div>

**作者**：Xinqi Chen (Shanghai Jiao Tong University), Weidong Zhang (Alibaba Group), Zhongyu Wang (Alibaba Group), Erci Xu (Shanghai Jiao Tong University), Xiaolu Zhang (Alibaba Group), Dong Wu (Alibaba Group), Junping Wu (Alibaba Group), Haonan Wu (Shanghai Jiao Tong University), Ruiming Lu (Shanghai Jiao Tong University), Yaheng Song (Alibaba Group), Chaolei Hu (Alibaba Group), Lijun Ding (Alibaba Group), Guangtao Xue (Shanghai Jiao Tong University), Patrick P. C. Lee (The Chinese University of Hong Kong)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769341)

## 英文摘要

We explore the performance improvements for a production Elastic Block Storage (EBS) service at Alibaba, which serves millions of users and virtual disks daily. Despite various load balancing measures, Alibaba EBS still faces frequent performance variations or even occasional Service Level Objective (SLO) violations. Our trace analysis reveals that the existing scheduling mechanism in Alibaba EBS, which adopts a common practice of focusing on load balancing alone, is insufficient for mitigating tail latency due to negligence of correlated I/O workloads, reliance on fixed scheduling frequencies, and insufficient input metrics for scheduling decisions. We present Omar, a novel hybrid proactive and reactive scheduling framework that enables dynamic, fine-grained scheduling. Evaluation on production-scale testbeds shows that Omar reduces 64 KiB tail latency by up to 52.2% and the number of scheduling operations by 44.6% compared to the baseline scheduler, while incurring limited overhead.

## 中文摘要

我们探讨阿里巴巴一个生产级弹性块存储（EBS）服务的性能改进，该服务每天为数百万用户和虚拟磁盘提供服务。尽管采取了多种负载均衡措施，阿里巴巴 EBS 仍频繁出现性能波动，甚至偶发违反服务等级目标（SLO）。我们的追踪分析表明，阿里巴巴 EBS 现有的调度机制采用只关注负载均衡的常见做法，由于忽视相关的 I/O 工作负载、依赖固定的调度频率，以及用于调度决策的输入指标不足，无法有效缓解尾延迟。我们提出 Omar，一个新颖的主动与被动混合调度框架，可实现动态、细粒度的调度。在生产规模测试床上的评估表明，与基线调度器相比，Omar 将 64 KiB 尾延迟最多降低 52.2%，将调度操作次数减少 44.6%，而带来的开销有限。

**英文关键词：** Compute-Storage Disaggregation, Elastic Block Storage, Load Balancing

**中文关键词：** 计算存储解耦、弹性块存储、负载均衡

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
