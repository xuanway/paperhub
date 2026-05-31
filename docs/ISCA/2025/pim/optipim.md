---
title: "OptiPIM: 用整数线性规划优化PIM加速"
description: "ISCA 2025论文解读：OptiPIM将PIM加速器的任务映射和调度问题形式化为整数线性规划(ILP)，找到最优执行策略。"
tags: ["ISCA2025", "存内计算", "PIM优化", "整数线性规划", "UCSD"]
---

# OptiPIM: Optimizing Processing-in-Memory Acceleration Using Integer Linear Programming

**作者**：Jiantao Liu, Minxuan Zhou, Yue Pan, Chien-Yi Yang, Lana Josipovic, Tajana Rosing  
**机构**：UC San Diego  
**会议**：ISCA 2025 · Session 5C: Processing-in-Memory  

---

## 一句话总结

> PIM 的任务分配（哪些操作在 PIM 执行，哪些在 CPU/GPU 执行）是复杂优化问题；OptiPIM 用 ILP 找到全局最优分配方案，提升端到端性能。

## 主要贡献

1. **ILP 建模**：将 PIM-CPU 任务分配、数据搬运和同步建模为 ILP
2. **求解策略**：近似求解大规模 ILP 的启发式方法
3. **通用性**：适用于 SRAM-PIM、DRAM-PIM、ReRAM-PIM 等多种架构
4. **自动化工具**：给定 DNN 模型，自动生成最优 PIM 执行计划

## 关键词

存内计算 · PIM优化 · ILP · 任务调度 · UCSD · ISCA 2025
