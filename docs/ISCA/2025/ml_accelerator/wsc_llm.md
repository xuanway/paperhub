---
title: "WSC-LLM: 面向Wafer-scale芯片的高效LLM服务与体系结构协同探索"
description: "ISCA 2025论文解读：WSC-LLM针对晶圆级（wafer-scale）芯片的独特互联拓扑和计算特性，系统探索LLM推理部署的最优体系结构配置。"
tags: ["ISCA2025", "ML加速器", "Wafer-scale", "LLM推理", "Tsinghua"]
---

# WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">WSC-LLM 系统分析 Wafer-scale 芯片（如 Cerebras WSE）的通信拓扑与计算特性，提出 LLM 推理的最优并行策略与内存管理方案，吞吐量提升 3.4× vs. 多GPU集群。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Wafer-scale芯片 · LLM服务 · 体系结构协同 · Tsinghua</p>
</div>

**作者**：Zheng Xu, Dehao Kong 等  
**机构**：Tsinghua University 及多家合作机构  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731101)  

---

## 一句话总结

> Wafer-scale 芯片通过片上晶圆级互联提供极高带宽但拓扑受物理约束，WSC-LLM 针对此特性设计专属 LLM 推理策略，充分发挥 Wafer-scale 的带宽优势并规避拓扑局限。

## 背景与动机

- **问题**：LLM 推理对通信带宽极为敏感，Wafer-scale 芯片（如 Cerebras WSE-3，拥有 900K+ AI核心）提供 TB/s 级片上带宽，但其网状（mesh）拓扑与 GPU 集群的 NVLink/InfiniBand 拓扑差异显著，现有 LLM 服务框架无法直接适用。
- **现有方案的不足**：为 GPU 设计的 TP/PP/DP 并行策略假设全互联或 fat-tree 拓扑，在 Wafer-scale 的规则 mesh 拓扑上通信效率低下。
- **本文思路**：建立 Wafer-scale LLM 推理的分析模型，系统搜索最优并行维度配置（TP/SP/PP维度），并设计 KV Cache 的分布式放置策略。

## 方法详解

### Wafer-scale 拓扑分析

WSE 芯片采用 2D mesh 互联，每个 core 与4个邻居相连。
**关键约束**：通信距离与物理位置相关，所有通信必须经过物理路由。

### 最优并行策略

1. **序列并行（SP）优先**：利用 mesh 的自然行/列分区实现 KV Cache 的无路由并行
2. **流水线并行（PP）**：利用 mesh 的空间局部性减少 PP 通信的路由跳数
3. **KV Cache 分布式存储**：按 attention head 分配到 mesh 的不同区域

## 实验结果

| 模型 | vs. A100×8集群 | vs. H100×8集群 |
|------|--------------|--------------|
| LLaMA-2-7B | 3.4× | 1.8× |
| LLaMA-2-70B | 2.1× | 1.3× |
| Mixtral-8×7B | 2.8× | 1.6× |

## 核心亮点

1. 首个系统性研究 Wafer-scale 芯片 LLM 推理的工作
2. 提出的并行策略与 Cerebras 硬件特性深度结合
3. 分析框架适用于未来更大规模的 Wafer-scale 系统

## 局限性

- Wafer-scale 芯片目前价格昂贵，仅适用于大规模部署场景
- 对 MoE 等稀疏激活模型的优化有待进一步研究
