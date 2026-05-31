---
title: "BingoGCN: 细粒度分区与SLT实现可扩展高效GNN加速"
description: "ISCA 2025论文解读：BingoGCN提出细粒度图分区和稀疏查找表（SLT）技术，解决GNN加速中的负载不均和内存效率问题。"
tags: ["ISCA2025", "GNN加速", "图神经网络", "细粒度分区", "SLT", "Tokyo Tech"]
---

# BingoGCN: Towards Scalable and Efficient GNN Acceleration with Fine-Grained Partitioning and SLT

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">BingoGCN 通过细粒度图分区均衡 GNN 并行负载，并引入稀疏查找表（Sparse Lookup Table, SLT）减少图聚合操作的冗余计算，实现高效可扩展的 GNN 加速。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · GNN加速 · 图神经网络 · 稀疏查找表 · Tokyo Tech · Daichi Fujiki</p>
</div>

**作者**：Jiale Yan, Hiroaki Ito, Yuta Nagahara, Kazushi Kawamura, Masato Motomura, Thiem Van Chu, Daichi Fujiki  
**机构**：Tokyo Institute of Technology 等  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 9C: Memory Technology  

---

## 一句话总结

> GNN 图数据的度分布不均导致严重负载不均；BingoGCN 通过细粒度分区和 SLT 同时解决负载不均和计算冗余问题。

## 主要贡献

1. **细粒度图分区**：超越传统 subgraph 分区，将高度节点拆分，均衡并行负载
2. **稀疏查找表 (SLT)**：识别邻居聚合中重复的特征向量加权组合，预计算并复用
3. **可扩展架构**：支持多加速器协同处理超大图（10M+ 节点）

## 实验结果

- 较现有 GNN 加速器（HyGCN、AWB-GCN）提速 **2–4×**
- 内存访问量减少 **40%**

## 关键词

GNN加速 · 图神经网络 · 细粒度分区 · SLT · Tokyo Tech · ISCA 2025
