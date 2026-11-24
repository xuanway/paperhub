---
title: "Improving GPU Sharing Performance through Adaptive Bubbleless Spatial-Temporal Sharing"
description: "EuroSys 2025 · GPU Systems · Shulai Zhang (Shanghai Jiao Tong University), Quan Chen (Shanghai Jiao Tong Univ"
tags:
  - "EuroSys2025"
  - "GPU Systems"
---

# Improving GPU Sharing Performance through Adaptive Bubbleless Spatial-Temporal Sharing

**中文标题：** 通过自适应无气泡时空共享提高 GPU 共享性能

**所属 Session：** [Session 4.2: GPU Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：GPU Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · GPU Systems</p>
</div>

**作者**：Shulai Zhang (Shanghai Jiao Tong University), Quan Chen (Shanghai Jiao Tong University), Weihao Cui (Shanghai Jiao Tong University), Han Zhao (Shanghai Jiao Tong University), Chunyu Xue (Shanghai Jiao Tong University), Zhen Zheng (Microsoft), Wei Lin (Alibaba Group), Minyi Guo (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696070)

## 英文摘要

Data centers now allow multiple applications that have lightweight workloads to share a GPU. Existing temporal or spatial sharing systems struggle to provide efficient and accurate quota assignments. We observe that the performance of the multi-user system is often underestimated because of the existence of unused GPU “bubbles” and can be enhanced by squeezing the bubbles. Based on this observation, we design Bless, a bubble-less spatial-temporal sharing GPU system that fine-tunes the GPU resource allocation to improve multi-user performance. Bless leverages precise computing resource management and fine-grained kernel scheduling to ensure stringent quota guarantees and reduce latency fairly for applications with varying GPU quotas. We implement and evaluate Bless with multiple applications and workloads. Our result shows that Bless achieves 21.1% −37.3% average latency reduction over the state-of-the-art while guaranteeing the promised quota for all applications.

## 中文摘要

数据中心如今允许多个具有轻量级工作负载的应用共享一块 GPU。现有的时间或空间共享系统难以提供高效且准确的配额分配。我们观察到，由于存在未使用的 GPU“气泡”，多用户系统的性能往往被低估，并且可以通过挤压这些气泡来提升。基于这一观察，我们设计了 Bless，一个无气泡的时空共享 GPU 系统，它微调 GPU 资源分配以提升多用户性能。Bless 利用精确的计算资源管理和细粒度的内核调度，确保严格的配额保证，并为具有不同 GPU 配额的应用公平地降低延迟。我们用多个应用和工作负载实现并评估了 Bless。结果表明，Bless 相比最先进系统平均降低延迟 21.1%–37.3%，同时为所有应用保证承诺的配额。

**英文关键词：** GPU sharing, cloud computing

**中文关键词：** GPU 共享、云计算

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
