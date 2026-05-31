---
title: "RTSpMSpM: 光线追踪驱动的稀疏矩阵-稀疏矩阵乘法加速"
description: "ISCA 2025论文解读：RTSpMSpM将GPU中的RT Core复用于稀疏矩阵乘法的非零元素相交查找，利用BVH遍历加速SpMSpM。"
tags: ["ISCA2025", "稀疏矩阵", "SpMSpM", "光线追踪", "RT Core复用", "UCR"]
---

# RTSpMSpM: Accelerating Sparse-Sparse Matrix Multiplication via Ray Tracing

**作者**：多位作者  
**机构**：UC Riverside (UCR)  
**会议**：ISCA 2025 · Session 3B: Domain Specific I  

---

## 一句话总结

> 稀疏矩阵乘法（SpMSpM）的非零元素相交查找与光线-三角形相交本质上同构；RTSpMSpM 将 RT Core 复用于 SpMSpM，加速图计算和科学计算。

## 关键词

SpMSpM · 稀疏矩阵 · RT Core复用 · 图计算 · UCR · ISCA 2025
