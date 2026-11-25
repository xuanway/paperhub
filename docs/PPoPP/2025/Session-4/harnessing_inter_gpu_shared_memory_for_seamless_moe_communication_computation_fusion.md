---
title: "Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion"
description: "PPoPP 2025 Session 4（Memory）：共享内存替代 All2All，平均比 FasterMoE 快 2.48×"
tags:
  - "PPoPP2025"
  - "Session-4"
  - "Memory"
  - "MoE"
  - "Inter-GPU Shared Memory"
  - "Communication-Computation Fusion"
authors:
  - " Hulin Wang"
  - "Yaqi Xia"
  - "Donglin Yang"
  - "Xiaobo Zhou"
  - "Dazhao Cheng"
session: "Session 4: Memory"
session_number: 4
session_chair: "Dong Li"
date: "2025-03-03"
time: "16:20–16:40"
room: "Acacia D"
doi: "10.1145/3710848.3710868"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 MoE 训练框架 CCFuser，用 inter-GPU 共享内存替代昂贵的 All2All，把本地与远程数据的计算融合进同一 kernel，并以等价图变换实现无损专家重分配。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 4: Memory</p>
</div>

**作者**：Hulin Wang, Yaqi Xia (Wuhan University); Donglin Yang (Nvidia Corporation); Xiaobo Zhou (University of Macau); Dazhao Cheng (WuHan University)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 16:20–16:40 · Session 4: Memory（主席：Dong Li）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710868) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 MoE 训练框架 CCFuser，用 inter-GPU 共享内存替代昂贵的 All2All，把本地与远程数据的计算融合进同一 kernel，并以等价图变换实现无损专家重分配。

## 研究问题

MoE 分布式训练受通信开销与专家负载不均困扰；现有方法只能粗粒度重叠通信与计算，反而损害计算效率，而负载均衡方案又常以模型质量为代价。

## 方法简述

- 用高效的 inter-GPU 共享内存访问替代 MoE 中典型的 All2All 操作。
- 在融合 kernel 中并发计算本地与远程数据，提高 GEMM 的计算 FLOPS。
- 以资源高效的专家重分配策略处理负载不均，通过等价图变换保证统计精度不变。

## 主要结果

- 在 A100 服务器上平均比 FastMoE 快 2.96×、比 FasterMoE 快 2.48×。
- 最高取得 4.34× 的加速，并显著提升 GPU 利用率。

<details>
<summary>原文摘要（英文）</summary>

The Mixture of Experts (MoE) architecture enhances model quality by scaling up model parameters. However, its development is hindered in distributed training scenarios due to significant communication overhead and expert load imbalance. Existing methods, which only allow for coarse-grained overlapping of communication and computation, slightly alleviate communication costs but at the same time, they introduce a notable impairment of computational efficiency. Furthermore, current approaches to addressing load imbalance often compromise model quality. We introduce CCFuser, a novel framework designed for efficient training of MoE models. CCFuser replaces the costly All2All operations typical in MoE architectures with efficient inter-GPU shared memory access. This allows for the concurrent computation of local and remote data within a fused kernel, achieving substantially higher compute FLOPS for GEMM operations. Additionally, CCFuser addresses load imbalance with a resource-efficient expert reassignment strategy, which optimizes the use of computational resources in expert reassignment through equivalent graph transformations without sacrificing statistical accuracy. By integrating these optimizations, CCFuser significantly enhances GPU utilization efficiency. Experiments conducted on A100 servers. show that CCFuser outperforms state-of-the-art methods FastMoE and FasterMoE by an average of 2.96x and 2.48x, respectively, achieving a maximum speedup of 4.34x.

</details>

---

> 所属 Session：[Session 4: Memory](index.md) · 返回 [PPoPP 2025 总览](../index.md)
