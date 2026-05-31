---
title: "ATiM: 自调优Processing-in-DRAM张量程序"
description: "ISCA 2025论文解读：ATiM提出针对Processing-in-DRAM平台的自动调优框架，通过搜索最优张量程序配置提升PIM执行效率。"
tags: ["ISCA2025", "存内计算", "DRAM-PIM", "自动调优", "KAIST"]
---

# ATiM: Autotuning Tensor Programs for Processing-in-DRAM

**作者**：Yongwon Shin, Dookyung Kang, Hyojin Sung  
**机构**：KAIST  
**会议**：ISCA 2025 · Session 5C: Processing-in-Memory  

---

## 一句话总结

> PIM 硬件的并行度、内存访问模式与 CPU/GPU 不同；ATiM 为 Processing-in-DRAM 平台自动调优张量算子的执行策略，找到最优 tile size 和并行配置。

## 主要贡献

1. **PIM 感知调优空间**：定义 DRAM-PIM 专属的 tile/bank 并行调优参数
2. **高效搜索算法**：基于代价模型的 Bayesian 优化快速找到最优配置
3. **与现有框架集成**：与 TVM、Halide 框架集成，自动生成 PIM 优化代码

## 关键词

DRAM-PIM · 自动调优 · 张量程序 · KAIST · ISCA 2025
