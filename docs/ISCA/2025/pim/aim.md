---
title: "AIM: 高性能PIM中架构级IR降压缓解的软硬件协同设计"
description: "ISCA 2025论文解读：AIM提出PIM系统中架构级IR压降（IR-drop）缓解方案，通过软硬件协同降低高并发PIM运算的电压波动危害。"
tags: ["ISCA2025", "存内计算", "PIM", "IR降压", "软硬件协同", "PKU"]
---

# AIM: Software and Hardware Co-design for Architecture-level IR-drop Mitigation in High-performance PIM

**作者**：Yuanpeng Zhang, Xing Hu, Xi Chen, Zhihang Yuan, Cong Li, Jingchen Zhu, Zhao Wang, Chenguang Zhang, Xin Si, Wei Gao, Qiang Wu, Runsheng Wang, Guangyu Sun  
**机构**：Peking University 等  
**会议**：ISCA 2025 · Session 5C: Processing-in-Memory  

---

## 一句话总结

> PIM 高并发计算时电流瞬变引发 IR 降压，导致操作错误；AIM 通过软硬件协同调度计算时序，系统性减少 IR 降压对 PIM 正确性的危害。

## 主要贡献

1. **IR 降压建模**：量化 PIM 阵列并发激活数与 IR 降压幅度的关系
2. **调度算法**：软件层将高并发 PIM 操作分散执行，避免电流峰值叠加
3. **硬件补偿**：微小容性缓冲设计减缓电流瞬变
4. **验证**：在真实 DRAM PIM（三星 HBM-PIM）硬件上验证效果

## 关键词

存内计算 · PIM · IR降压 · 软硬件协同 · PKU · ISCA 2025
