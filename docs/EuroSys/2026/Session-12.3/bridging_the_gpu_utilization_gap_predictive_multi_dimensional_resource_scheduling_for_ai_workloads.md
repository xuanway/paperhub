---
title: "Bridging the GPU Utilization Gap: Predictive Multi-Dimensional Resource Scheduling for AI Workloads"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Yilei Lu (Tsinghua University), Dongbiao He (Southeast University), Teng Ma (Ali"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# Bridging the GPU Utilization Gap: Predictive Multi-Dimensional Resource Scheduling for AI Workloads

**中文标题：** 弥合 GPU 利用率差距：面向 AI 工作负载的预测式多维资源调度

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Yilei Lu (Tsinghua University), Dongbiao He (Southeast University), Teng Ma (Alibaba Group), Zhe Liu (Baihai), Letian Ruan (Shanghai Jiao Tong University), Jinlei Jiang (Tsinghua University), Yongwei Wu (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803579)

## 英文摘要

Modern AI data centers face a critical paradox: while machine learning workloads dominate infrastructure demands, actual GPU utilization remains consistently low. Existing schedulers fail to coordinate heterogeneous resources effectively, lack predictive capabilities for dynamic workloads, and cannot balance isolation requirements with sharing optimization in multi-tenant clusters. This paper presents Wind, a novel resource scheduler that bridges the GPU utilization gap through predictive scheduling and geometric resource coordination. Wind introduces three key innovations: (1) a resource prediction framework that leverages historical execution patterns to forecast task requirements and completion times with high accuracy;(2) a unified scheduling architecture supporting isolation, sharing, preemption, and prioritization policies that eliminate resource fragmentation while maintaining performance guarantees; and (3) a Hilbert curve-based multi-dimensional scheduling algorithm that maps CPU-memory-GPU resource space to preserve spatial locality while achieving linear computational complexity.

Our evaluation on a 139-node cluster demonstrates that Wind consistently outperforms K8s Default, DRF, and Synergy across diverse workloads. It reduces average response time by 33–48%, lowers P99 JCT by 37%, and improves throughput by up to 46.6% under bursty loads. GPU utilization remains above 92%, while medium-load scenarios yield up-mei to 25% resource savings, highlighting the practicality of Wind for production-scale AI clusters.

## 中文摘要

现代 AI 数据中心面临一个关键悖论：尽管机器学习工作负载主导着基础设施需求，实际 GPU 利用率却持续偏低。现有调度器无法有效协调异构资源，缺乏对动态工作负载的预测能力，也无法在多租户集群中平衡隔离需求与共享优化。本文提出 Wind，一个新颖的资源调度器，通过预测式调度和几何资源协调来弥合 GPU 利用率差距。Wind 引入三项关键创新：（1）一个资源预测框架，利用历史执行模式高精度预测任务需求和完成时间；（2）一个统一调度架构，支持隔离、共享、抢占和优先级策略，在保持性能保证的同时消除资源碎片；（3）一种基于希尔伯特曲线的多维调度算法，将 CPU-内存-GPU 资源空间进行映射，在保持空间局部性的同时实现线性计算复杂度。

我们在一个 139 节点集群上的评估表明，Wind 在多样工作负载下持续优于 K8s Default、DRF 和 Synergy。它将平均响应时间降低 33–48%，将 P99 JCT 降低 37%，并在突发负载下将吞吐量提升最多 46.6%。GPU 利用率保持在 92% 以上，而中等负载场景可节省高达 25% 的资源，凸显了 Wind 在生产规模 AI 集群中的实用性。

**英文关键词：** GPU resource scheduling, AI workloads , Predictive modeling , Hilbert curve

**中文关键词：** GPU 资源调度、AI 工作负载、预测建模、希尔伯特曲线

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
