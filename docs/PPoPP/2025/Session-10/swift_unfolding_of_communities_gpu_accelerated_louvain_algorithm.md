---
title: "Swift Unfolding of Communities: GPU-Accelerated Louvain Algorithm"
description: "PPoPP 2025 Session 10（GPU II）：模块度增益剪枝 + 负载感知 kernel，平均超越 SOTA 6×"
tags:
  - "PPoPP2025"
  - "Session-10"
  - "GPU II"
  - "Community Detection"
  - "Louvain"
  - "GPU"
authors:
  - "Zhibin Wang"
  - "Xi Lin"
  - "Xue Li"
  - "Pinhuan Wang"
  - "Ziheng Meng"
  - "Hang Liu"
  - "Chen Tian"
  - "Sheng Zhong"
session: "Session 10: GPU II"
session_number: 10
session_chair: "Zhijia Zhao"
date: "2025-03-05"
time: "10:20–10:40"
room: "Acacia D"
doi: "10.1145/3710848.3710884"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Swift Unfolding of Communities: GPU-Accelerated Louvain Algorithm

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 GPU 加速的 Louvain 算法 GALA，用带理论保证的模块度增益剪枝减少计算，并以负载感知 kernel 和多 GPU 同步策略提升社区检测性能。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 10: GPU II</p>
</div>

**作者**：Zhibin Wang, Xi Lin (Nanjing University); Xue Li (Alibaba Group); Pinhuan Wang (Rutgers, The State University of New Jersey); Ziheng Meng (Nanjing University); Hang Liu (Rutgers, The State University of New Jersey); Chen Tian, Sheng Zhong (Nanjing University)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 10:20–10:40 · Session 10: GPU II（主席：Zhijia Zhao）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710884) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 GPU 加速的 Louvain 算法 GALA，用带理论保证的模块度增益剪枝减少计算，并以负载感知 kernel 和多 GPU 同步策略提升社区检测性能。

## 研究问题

现有 Louvain 实现存在剪枝不准确和中间状态管理低效的问题，难以充分利用 GPU 的存储层次与并行能力。

## 方法简述

- 提出基于模块度增益的新型剪枝策略，具备严格的最优性理论保证，最多减少 76% 的顶点及其对应计算。
- 设计负载感知 kernel：基于 warp 级原语的 shuffle kernel 用于交换状态，优先使用共享内存的哈希 kernel 用于哈希表。
- 通过稠密-稀疏同步策略最小化 GPU 间同步开销，实现多 GPU 扩展。

## 主要结果

- 在多种真实图上的实验表明，GALA 显著提升 GPU 上并行 Louvain 的性能。
- 平均超越 SOTA 方案 6×。

<details>
<summary>原文摘要（英文）</summary>

The Louvain algorithm is one of the most popular algorithms for community detection. Observing that existing implementations suffer from inaccurate pruning and inefficient intermediate state management, we introduce GALA, GPU-Accelerated Louvain Algorithm, which incorporates two key innovations. The first innovation is a novel modularity gain-based pruning strategy, supported by rigorous theoretical guarantees of optimality and able to reduce up to 76% of vertices as well as their corresponding computations. To take advantage of the memory hierarchy and parallelism of GPUs, the second innovation is workload-aware kernels, featuring a shuffle-based kernel founded on the warp-level primitives for exchange states and a hash-based kernel that prioritizes shared memory in hashtable design. GALA further scales to multiple GPUs by minimizing the synchronization overhead between GPUs through a dense-sparse synchronization strategy. We evaluate the performance of GALA through theoretical analysis and practical experiments on various real-world graphs. The experimental results confirm that GALA significantly improves the performance of the parallel Louvain algorithm on GPUs, surpassing state-of-the-art solutions by 6× on average.

</details>

---

> 所属 Session：[Session 10: GPU II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
