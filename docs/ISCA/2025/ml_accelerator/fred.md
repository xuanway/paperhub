---
title: "FRED: 用于3D并行DNN训练的Wafer-scale互联结构"
description: "ISCA 2025论文解读：FRED为Wafer-scale系统设计3D并行（数据/流水/张量并行）的互联结构，使超大DNN训练效率提升2.7×。"
tags: ["ISCA2025", "ML加速器", "Wafer-scale", "分布式训练", "3D并行"]
---

# FRED: A Wafer-scale Fabric for 3D Parallel DNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">FRED 设计了专为 3D 并行（DP+PP+TP）DNN 训练优化的 Wafer-scale 互联结构，通过物理拓扑与逻辑通信模式协同设计，DNN 训练吞吐量提升 2.7× vs. 独立芯片集群。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Wafer-scale · 分布式DNN训练 · 3D并行 · 互联网络</p>
</div>

**作者**：Saeed Rashidi, William Won 等  
**机构**：Georgia Tech 及合作机构  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731055)  

---

## 一句话总结

> 现有 Wafer-scale 互联为通用 mesh 拓扑，未针对 3D 并行训练的分层通信模式优化；FRED 将 Wafer-scale 划分为与 3D 并行层次对应的通信域，消除跨域通信瓶颈。

## 背景与动机

- **问题**：3D 并行（DP+PP+TP）是训练超大 LLM（千亿参数）的标准策略，但三类通信（All-Reduce/P2P/All-Gather）对带宽和延迟的要求各不相同，Wafer-scale 的均匀 mesh 拓扑无法同时满足。
- **现有方案的不足**：独立芯片集群的跨节点通信受限于 NVLink 带宽（400-900 GB/s），成为训练瓶颈；现有 Wafer-scale 映射方案简单堆砌三类并行，未优化通信路径。
- **本文思路**：将 Wafer-scale 的 2D mesh 划分为三层通信域，分别对应 TP（近邻高带宽通信）、PP（稀疏流水线通信）和 DP（全局 All-Reduce），并在物理布线上实现域隔离。

## 方法详解

### 3D 通信域设计

```
Wafer-scale 物理分区:
┌─────────────────────────────┐
│  DP Domain (全局All-Reduce)  │
│  ┌─────────────────────┐    │
│  │  PP Pipeline Stage  │    │
│  │  ┌───────────────┐  │    │
│  │  │  TP Tensor    │  │    │
│  │  │  Parallel     │  │    │
│  │  └───────────────┘  │    │
│  └─────────────────────┘    │
└─────────────────────────────┘
```

TP 域使用最高密度互联（短距离，高带宽）；PP 域采用单向环（流水线特性）；DP 域采用混合路由减少All-Reduce延迟。

## 实验结果

| 模型 | vs. 8×H100节点 | vs. 通用Wafer-mesh |
|------|--------------|------------------|
| GPT-3 (175B) | 2.7× | 1.5× |
| PaLM (540B) | 3.1× | 1.8× |
| Megatron-LM通用配置 | 2.4× | 1.4× |

## 核心亮点

1. 首个针对 3D 并行训练的 Wafer-scale 互联设计
2. 物理拓扑与逻辑通信模式的深度协同
3. 仿真结果表明对更大模型（万亿参数）收益递增

## 局限性

- 通信域分区降低了互联拓扑的通用性
- 3D 并行策略需要预先配置，对不同模型需要重新规划
