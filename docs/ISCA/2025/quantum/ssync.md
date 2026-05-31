---
title: "S-SYNC: 量子电荷耦合器件中的Shuttle与Swap协同优化"
description: "ISCA 2025论文解读：S-SYNC提出QCCD架构中穿梭（Shuttle）与交换（Swap）操作的协同优化策略，降低量子比特移动开销。"
tags: ["ISCA2025", "量子计算", "QCCD", "俘获离子", "Shuttle优化"]
---

# S-SYNC: Shuttle and Swap Co-Optimization in Quantum Charge-Coupled Devices

**作者**：Chenghong Zhu, Xian Wu, Jingbo Wang, Xin Wang, Chenghong Zhu  
**机构**：多家机构  
**会议**：ISCA 2025 · Session 3A: Quantum I  

---

## 一句话总结

> QCCD（量子电荷耦合器件/俘获离子）架构中，量子比特需要物理移动才能执行两比特门；S-SYNC 协同优化 Shuttle 和 Swap 操作，减少总移动开销。

## 主要贡献

1. **协同优化框架**：联合规划 Shuttle（物理传输）和 Swap（逻辑交换）的最优组合
2. **启发式调度器**：考虑 QCCD 物理拓扑约束的实时量子比特路由
3. **延迟减少**：与纯 Shuttle 或纯 Swap 策略相比，门执行总延迟降低 30%

## 关键词

QCCD · 俘获离子 · 量子比特移动 · Shuttle优化 · ISCA 2025
