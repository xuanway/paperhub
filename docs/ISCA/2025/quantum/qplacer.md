---
title: "Qplacer: 超导量子计算机的频率感知元件布局"
description: "ISCA 2025论文解读：Qplacer提出频率感知的超导量子比特布局优化工具，通过减少频率碰撞提高量子处理器的整体性能。"
tags: ["ISCA2025", "量子计算", "量子布局", "频率碰撞", "超导量子比特", "Duke", "MIT"]
---

# Qplacer: Frequency-Aware Component Placement for Superconducting Quantum Computers

**作者**：Junyao Zhang, Hanrui Wang, Qi Ding, Jiaqi Gu, Reouven Assouly, William D. Oliver, Song Han, Kenneth R. Brown, Hai "Helen" Li, Yiran Chen  
**机构**：Duke University, MIT, Rice University  
**会议**：ISCA 2025 · Session 8B: Quantum III  

---

## 一句话总结

> 超导量子比特的频率碰撞（frequency collision）会降低门保真度；Qplacer 在设计阶段优化量子比特频率分配和布局，系统性消除碰撞。

## 主要贡献

1. **频率碰撞模型**：形式化定义超导量子比特中各类频率碰撞条件
2. **布局优化算法**：整数规划+启发式搜索找到最小碰撞的频率分配方案
3. **EDA 工具集成**：与量子芯片设计流程集成的自动化布局工具
4. **实验验证**：在 Google Sycamore、IBM Eagle 等拓扑上验证

## 实验结果

- 频率碰撞数减少 **60–80%**
- 双量子比特门平均保真度提升 0.3%

## 关键词

超导量子比特 · 频率碰撞 · 量子布局优化 · Duke · MIT · ISCA 2025
