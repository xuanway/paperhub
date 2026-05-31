---
title: "SwitchQNet: 面向量子数据中心的交换网络分布式量子计算优化"
description: "ISCA 2025论文解读：SwitchQNet针对量子数据中心场景，利用光学交换网络优化量子比特间的纠缠分发，实现大规模分布式量子计算。"
tags: ["ISCA2025", "量子数据中心", "量子网络", "交换网络", "分布式量子计算", "UCSB"]
---

# SwitchQNet: Optimizing Distributed Quantum Computing for Quantum Data Centers with Switch Networks

**作者**：Hezi Zhang, Yiran Xu, Haotian Hu, Keyi Yin, Hassan Shapourian, Jiapeng Zhao, Ramana Rao Kompella, Reza Nejabati, Yufei Ding  
**机构**：UCSB, UC San Diego 等  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 量子数据中心中多量子处理器需要共享纠缠对；SwitchQNet 设计光学交换网络拓扑和路由算法，最大化纠缠对分发吞吐量并降低延迟。

## 主要贡献

1. **量子交换网络拓扑**：设计适合量子数据中心的光学交换拓扑（vs. 固定连接）
2. **纠缠感知路由**：考虑量子信道保真度和纠缠生成速率的路由算法
3. **多用户资源调度**：量子数据中心多租户共享纠缠资源的调度策略

## 关键词

量子数据中心 · 量子网络 · 光学交换 · 分布式量子计算 · ISCA 2025
