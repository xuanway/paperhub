---
title: "Arena: Efficiently Training Large Models via Dynamic Scheduling and Adaptive Parallelism Co-Design"
description: "EuroSys 2026 · AI · Chunyu Xue (Shanghai Jiao Tong University), Weihao Cui (Shanghai Jiao Tong Unive"
tags:
  - "EuroSys2026"
  - "AI"
---

# Arena: Efficiently Training Large Models via Dynamic Scheduling and Adaptive Parallelism Co-Design

**中文标题：** Arena：通过动态调度与自适应并行协同设计高效训练大模型

**所属 Session：** [Session 5.1: AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · AI</p>
</div>

**作者**：Chunyu Xue (Shanghai Jiao Tong University), Weihao Cui (Shanghai Jiao Tong University), Quan Chen (Shanghai Jiao Tong University), Chen Chen (Shanghai Jiao Tong University), Han Zhao (Shanghai Jiao Tong University), Shulai Zhang (Shanghai Jiao Tong University), Linmei Wang (Lenovo Research), Yan Li (Microsoft), Limin Xiao (Lenovo Research), WeiFeng Zhang (Lenovo Research), Jing Yang (Guizhou University), Bingsheng He (National University of Singapore), Minyi Guo (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803571)

## 英文摘要

Efficiently training large-scale models (LMs) in GPU clusters involves two separate avenues: inter-job dynamic scheduling and intra-job adaptive parallelism (AP). However, existing dynamic schedulers struggle with large-model scheduling due to the mismatch between static parallelism (SP)-aware scheduling and AP-based execution, leading to cluster inefficiencies such as degraded throughput and prolonged job queuing. This paper presents Arena, a large-model training system that co-designs dynamic scheduling and adaptive parallelism to achieve high cluster efficiency. To reduce scheduling costs while improving decision quality, Arena designs low-cost, disaggregated profiling and AP-tailored, load-aware performance estimation, while unifying them by sharding the joint scheduling-parallelism optimization space via a grid abstraction. Building on this, Arena dynamically schedules profiled jobs in elasticity and heterogeneity dimensions, and executes them using efficient AP with pruned search space. Evaluated on heterogeneous testbeds and production workloads, Arena reduces job completion time by up to 49.3% and improves cluster throughput by up to 1.60×.

## 中文摘要

在 GPU 集群中高效训练大规模模型（LM）涉及两条相互独立的路径：作业间的动态调度与作业内的自适应并行（AP）。然而，现有动态调度器在大模型调度上举步维艰，原因是静态并行（SP）感知的调度与基于 AP 的执行之间存在失配，导致集群效率下降，如吞吐量降低、作业排队时间延长。本文提出 Arena，一个将动态调度与自适应并行协同设计以提升集群效率的大模型训练系统。为在降低调度开销的同时提升决策质量，Arena 设计了低成本、解耦的性能剖析，以及契合 AP 的负载感知性能估计，并通过网格抽象对联合的调度—并行优化空间进行分片，从而将二者统一起来。在此基础上，Arena 沿弹性与异构性两个维度动态调度已剖析的作业，并利用搜索空间剪枝后的高效 AP 执行它们。在异构测试床和生产负载上的评估表明，Arena 将作业完成时间最多缩短 49.3%，并将集群吞吐量最多提升 1.60 倍。

**英文关键词：** Large-scale model training, cluster scheduling

**中文关键词：** 大规模模型训练、集群调度

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
