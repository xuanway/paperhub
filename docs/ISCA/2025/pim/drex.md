---
title: "DReX: 算法-硬件协同的高精度可扩展稠密检索加速"
description: "ISCA 2025论文解读：DReX通过算法和硬件协同设计加速神经稠密检索（Dense Retrieval），在保持高精度的同时实现可扩展的高吞吐量。"
tags: ["ISCA2025", "稠密检索", "向量检索", "算法-硬件协同", "Virginia"]
---

# DReX: Accurate and Scalable Dense Retrieval Acceleration via Algorithmic-Hardware Codesign

**作者**：Derrick Quinn, E. Ezgi Yücel, Martin Prammer, Zhenxing Fan, Kevin Skadron, Jignesh Patel, José F. Martínez, Mohammad Alian  
**机构**：University of Virginia, Cornell  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> 神经稠密检索（如 DPR、ANCE）需要海量向量内积计算；DReX 通过算法简化和专用硬件协同，在召回精度不损失的前提下实现高吞吐检索。

## 主要贡献

1. **检索简化算法**：通过量化和剪枝减少候选集大小
2. **专用加速硬件**：内积计算单元和向量缓存设计
3. **精度-性能权衡**：可配置精度参数满足不同应用需求

## 关键词

稠密检索 · 向量检索 · DPR · 算法硬件协同 · Virginia · ISCA 2025
