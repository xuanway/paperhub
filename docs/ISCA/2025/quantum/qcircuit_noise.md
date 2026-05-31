---
title: "Accelerating Simulation of Quantum Circuits under Noise via Computational Reuse"
description: "ISCA 2025论文解读：通过计算复用加速噪声量子电路模拟，识别并缓存重复的子电路演化矩阵，大幅减少模拟时间。"
tags: ["ISCA2025", "量子模拟", "噪声量子电路", "计算复用", "Wisconsin"]
---

# Accelerating Simulation of Quantum Circuits under Noise via Computational Reuse

**作者**：Meng Wang, Swamit Tannu, Prashant J Nair  
**机构**：University of Wisconsin-Madison, UBC  
**会议**：ISCA 2025 · Session 8B: Quantum III  

---

## 一句话总结

> 噪声量子电路模拟需反复计算相似的密度矩阵演化；本文识别可复用的子电路计算，通过缓存和复用大幅加速噪声模拟器。

## 主要贡献

1. **子电路识别**：自动检测电路中重复出现的门序列
2. **密度矩阵缓存**：存储常用子电路的噪声演化结果，避免重复计算
3. **模拟加速**：在典型 NISQ 电路上实现 3–10× 模拟加速

## 关键词

量子电路模拟 · 噪声模型 · 计算复用 · NISQ · Wisconsin · ISCA 2025
