---
title: "ArtMem: 强化学习驱动的分层内存自适应迁移"
description: "ISCA 2025论文解读：ArtMem使用强化学习优化分层内存系统（如DRAM+NVM）中的数据页面迁移策略，超越传统启发式迁移方法。"
tags: ["ISCA2025", "分层内存", "强化学习", "页面迁移", "NVM", "CityU"]
---

# ArtMem: Adaptive Migration in Reinforcement Learning-Enabled Tiered Memory

**作者**：Xinyue Yi, Cong Li, Lingyi Huang, Bingsheng He, Zili Shao  
**机构**：City University of Hong Kong, NUS  
**会议**：ISCA 2025 · Session 3C: Storage  

---

## 一句话总结

> 分层内存（DRAM + 慢速 NVM/CXL 内存）需要动态决定哪些页面放在快速层；ArtMem 用强化学习替代启发式迁移规则，自适应工作负载变化。

## 主要贡献

1. **RL 迁移 Agent**：以内存访问统计为状态，迁移决策为动作的在线 RL 策略
2. **快速收敛**：轻量级状态空间和奖励设计保证低迁移决策开销
3. **通用性**：适用于 DRAM+PMEM、DRAM+CXL 等不同分层组合

## 关键词

分层内存 · 强化学习 · 页面迁移 · NVM · CXL · CityU · ISCA 2025
