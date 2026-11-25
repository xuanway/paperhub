---
title: "Helios: Efficient Distributed Dynamic Graph Sampling for Online GNN Inference"
description: "PPoPP 2025 Session 1（Graph Neural Networks）：事件驱动预采样 + 查询感知缓存，吞吐最高 67×、P99 延迟最低 32×"
tags:
  - "PPoPP2025"
  - "Session-1"
  - "Graph Neural Networks"
  - "Graph Sampling"
  - "GNN Inference"
  - "Distributed Systems"
authors:
  - "Jie Sun"
  - "Zuocheng Shi"
  - "Li Su"
  - "Wenting Shen"
  - "Zeke Wang"
  - "Yong Li"
  - "Wenyuan Yu"
  - "Wei Lin"
  - "Fei Wu"
  - "Jingren Zhou"
  - "Bingsheng He"
session: "Session 1: Graph Neural Networks"
session_number: 1
session_chair: "Miao Yin"
date: "2025-03-03"
time: "10:00–10:20"
room: "Acacia D"
doi: "10.1145/3710848.3710854"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Helios: Efficient Distributed Dynamic Graph Sampling for Online GNN Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向在线 GNN 推理的分布式动态图采样服务 Helios，通过事件驱动预采样和查询感知的样本缓存，在毫秒级延迟 SLO 下同时提升吞吐、压低尾延迟。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 1: Graph Neural Networks</p>
</div>

**作者**：Jie Sun, Zuocheng Shi (Zhejiang University); Li Su, Wenting Shen (Alibaba Group); Zeke Wang (Zhejiang University); Yong Li, Wenyuan Yu, Wei Lin (Alibaba Group); Fei Wu (Zhejiang University); Jingren Zhou (Alibaba Group); Bingsheng He (National University of Singapore)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 10:00–10:20 · Session 1: Graph Neural Networks（主席：Miao Yin）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710854) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向在线 GNN 推理的分布式动态图采样服务 Helios，通过事件驱动预采样和查询感知的样本缓存，在毫秒级延迟 SLO 下同时提升吞吐、压低尾延迟。

## 研究问题

基于图数据库的动态图采样受两类问题制约：数据相关的采样负载不均衡造成长尾延迟，分布式采样又带来大量跨节点通信开销，难以满足在线 GNN 推理的毫秒级 SLO。

## 方法简述

- 以事件驱动方式对动态图做增量预采样，把采样工作从查询关键路径前移。
- 维护查询感知的样本缓存，在本地直接拼装完整的 K-hop 采样结果，避免每次请求重新跨节点采样。
- 针对分布式部署优化采样任务的划分与通信，缓解跨节点通信瓶颈。

## 主要结果

- 在多个数据集上，服务吞吐相比基线最高提升 67×。
- P99 查询延迟相比基线最高降低 32×，满足毫秒级 SLO。

<details>
<summary>原文摘要（英文）</summary>

Online GNN inference has been widely explored by applications such as online recommendation and financial fraud detection systems, where even minor delays can result in significant financial impact. Real-time dynamic graph sampling enables online GNN inference to reflect the latest graph updates in real-world graphs. However, online GNN inference typically demands millisecond-level latency Service Level Objectives (SLOs) as its performance guarantees, which poses great challenges for existing dynamic graph sampling approaches based on graph databases. The issues mainly arise from two aspects: long tail latency due to imbalanced data-dependent sampling and large communication overhead incurred by distributed sampling. To address these issues, we propose Helios, an efficient distributed dynamic graph sampling service to meet the stringent latency SLOs. The key ideas of Helios are 1) pre-sampling the dynamic graph in an event-driven approach, and 2) maintaining a query-aware sample cache to build the complete K-hop sampling results locally for inference requests. Experiments on multiple datasets show that Helios achieves up to 67× higher serving throughput and up to 32× lower P99 query latency compared to baselines.

</details>

---

> 所属 Session：[Session 1: Graph Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
