---
title: "EOD: 通过近存合并聚合实现低延迟GNN推理"
description: "ISCA 2025论文解读：EOD提出近存合并聚合方法，将GNN图聚合操作下推到内存侧执行，消除主要带宽瓶颈，实现低延迟GNN推理。"
tags: ["ISCA2025", "GNN推理", "近存处理", "图聚合", "KAIST"]
---

# EOD: Enabling Low Latency GNN Inference via Near-Memory Concatenate Aggregation

**作者**：Taehwan Kim, Yunki Han, Seohye Ha, Jiwan Kim, Lee-Sup Kim  
**机构**：KAIST  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> GNN 聚合操作需要大量不规则内存访问；EOD 将 Concatenate 聚合操作近存执行，减少 80% 的主存流量，实现低延迟推理。

## 主要贡献

1. **近存 Concatenate 聚合**：在内存控制器旁实现特征向量合并和聚合
2. **内存流量分析**：量化聚合操作的内存访问特征
3. **与 GPU 集成**：聚合结果直接传输到 GPU 进行后续更新操作

## 关键词

GNN推理 · 近存处理 · 图聚合 · KAIST · ISCA 2025
