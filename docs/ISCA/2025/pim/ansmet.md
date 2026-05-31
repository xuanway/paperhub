---
title: "ANSMET: 近存处理与混合早停的近似最近邻搜索"
description: "ISCA 2025论文解读：ANSMET结合近存处理和混合早停策略加速ANN（近似最近邻）搜索，在保持高召回率的同时大幅降低延迟。"
tags: ["ISCA2025", "近似最近邻搜索", "近存处理", "早停", "THU"]
---

# ANSMET: Approximate Nearest Neighbor Search with Near-Memory Processing and Hybrid Early Termination

**作者**：Yiwei Li, Yuxin Jin, Boyu Tian, Huanchen Zhang, Mingyu Gao  
**机构**：Tsinghua University  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> ANN 搜索遍历高维向量数据库是内存密集型操作；ANSMET 将 ANN 核心计算卸载到近存处理单元，并引入混合早停策略减少不必要的距离计算。

## 主要贡献

1. **近存 ANN 架构**：在 DRAM 控制器旁集成向量距离计算单元
2. **混合早停**：结合局部（单查询）和全局（batch 统计）的早停阈值
3. **HNSW/IVF 支持**：适配主流 ANN 索引结构

## 实验结果
- 与 GPU 相比，延迟降低 2.5×，能效提升 5×，召回率基本持平

## 关键词

ANN搜索 · 近存处理 · 早停 · 向量数据库 · THU · ISCA 2025
