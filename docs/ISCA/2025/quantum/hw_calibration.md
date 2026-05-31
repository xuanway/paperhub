---
title: "Hardware-aware Calibration Protocol for Quantum Computers"
description: "ISCA 2025论文解读：面向量子计算机的硬件感知校准协议，通过联合优化门级和系统级参数提升量子操作保真度。"
tags: ["ISCA2025", "量子计算", "量子校准", "超导量子比特", "UIUC"]
---

# Hardware-aware Calibration Protocol for Quantum Computers

**作者**：Yuchen Zhu, Jinglei Cheng, Boxi Li, Kecheng Liu, Yidong Zhou, Hanrui Wang, Yufei Ding, Zhiding Liang  
**机构**：UIUC, MIT 等  
**会议**：ISCA 2025 · Session 3A: Quantum I  

---

## 一句话总结

> 量子门的校准参数（脉冲形状、频率偏移）需频繁重新校准；Hardware-aware 方案考虑硬件串扰特性，以更少校准轮次达到更高保真度。

## 背景与动机

- 超导量子比特需要定期校准 Control Pulse 参数以补偿频率漂移和串扰
- 现有校准方法逐门独立优化，忽视量子比特间的硬件依赖关系
- 本文提出联合硬件特性的校准顺序和参数优化策略

## 主要贡献

1. **硬件感知校准图**：建模量子比特间的串扰依赖，构建最优校准顺序
2. **联合参数优化**：同时优化相邻量子比特的脉冲参数，减少串扰
3. **校准效率提升**：所需校准轮次减少 40%，门保真度提升 0.5%

## 关键词

量子校准 · 超导量子比特 · 串扰 · 门保真度 · ISCA 2025
