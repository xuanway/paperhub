---
title: "Suika: Efficient and High-quality Re-scheduling of 3D-parallelized LLM Training Jobs in Shared Clusters"
description: "EuroSys 2026 · LLM Training at Scale · Yuxuan Wang (Shanghai Jiao Tong University & Institute of Artificial Intelligenc"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# Suika: Efficient and High-quality Re-scheduling of 3D-parallelized LLM Training Jobs in Shared Clusters

**中文标题：** Suika：共享集群中三维并行LLM训练任务的高效高质量重调度

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Yuxuan Wang (Shanghai Jiao Tong University & Institute of Artificial Intelligence (TeleAI), China Telecom), Yanbo Wang (Shanghai Jiao Tong University & Institute of Artificial Intelligence (TeleAI), China Telecom), Chen Chen (Shanghai Jiao Tong University), Chunyu Xue (Shanghai Jiao Tong University), Qizhen Weng (Institute of Artificial Intelligence (TeleAI), China Telecom), Yin Chen (Institute of Artificial Intelligence (TeleAI), China Telecom), Zeren Li (Huawei Technologies Co., Ltd.), Xuqi Zhu (Huawei Technologies Co., Ltd.), Yongqiang Yang (Huawei Technologies Co., Ltd.), Quan Chen (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803623)

## 英文摘要

Large Language Models (LLMs) are usually trained with 3D (data, tensor, and pipeline) parallelism—in shared GPU clusters where the available resources are highly dynamic. Rescheduling the idle resources to ongoing jobs can help improve cluster utilization, but doing so for 3D-parallelized training jobs suffers large overheads in performance modeling, decision making, and redeployment. We present Suika, a cluster training system that supports efficient and high-quality resource rescheduling for 3D-parallelized LLM training jobs. Suika holistically addresses the complexity challenges by exploiting the incremental nature of rescheduling. For performance modeling, it builds an accurate performance estimator with non-disruptive online profiling. For decision-making, it employs topology-aware sorting and an expand-and-balance algorithm to reduce the complexity of resource allocation and job parallelization, without compromising decision quality. Suika further integrates a device-to-device redeployment method to leverage the overlapping nature of incremental reconfiguration for overhead reduction. Experiments on 64-GPU physical cluster and 1024-GPU simulated cluster show that, Suika achieves 1.29 ∼1.31× reduction in average JCT compared to state-of-the-art schedulers.

## 中文摘要

大语言模型（LLM）通常采用三维（数据、张量、流水线）并行进行训练，且运行在可用资源高度动态变化的共享GPU集群中。将空闲资源重新调度给正在运行的任务有助于提升集群利用率，但针对三维并行训练任务这样做会在性能建模、决策制定和重新部署方面带来巨大开销。我们提出Suika，一个集群训练系统，为三维并行LLM训练任务提供高效且高质量的资源重调度。Suika利用重调度的增量特性，整体性地应对上述复杂性挑战。在性能建模方面，它通过非中断式在线剖析构建精确的性能估计器。在决策制定方面，它采用拓扑感知排序与“扩展—平衡”算法，在不损害决策质量的前提下降低资源分配与任务并行的复杂度。Suika还集成了设备到设备的重新部署方法，利用增量重配置的重叠特性来降低开销。在64-GPU物理集群和1024-GPU模拟集群上的实验表明，与最先进的调度器相比，Suika将平均JCT降低了1.29～1.31倍。

**英文关键词：** Job Scheduling, LLM Training, Resource Efficiency

**中文关键词：** 任务调度、LLM训练、资源效率

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
