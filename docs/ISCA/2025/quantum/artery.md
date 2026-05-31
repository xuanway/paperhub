---
title: "ARTERY: 利用分支预测实现快速量子反馈"
description: "ISCA 2025论文解读：ARTERY将经典处理器的分支预测思想引入量子测量反馈路径，提前推测测量结果并执行条件门，减少量子计算延迟。"
tags: ["ISCA2025", "量子计算", "量子反馈", "分支预测", "PKU", "THU"]
---

# ARTERY: Fast Quantum Feedback using Branch Prediction

**作者**：Wuwei Tian, Liqiang Lu, Siwei Tan, Yun Liang, Tingting Li, Kaiwen Zhou, Xinghui Jia, Jianwei Yin  
**机构**：Peking University, Tsinghua University 等  
**会议**：ISCA 2025 · Session 3A: Quantum I  

---

## 一句话总结

> 量子测量结果驱动的条件门执行是量子纠错的核心，但测量延迟是瓶颈；ARTERY 借鉴 CPU 分支预测，预测测量结果并提前执行条件门，测量失败时回滚。

## 主要贡献

1. **量子分支预测器**：基于量子比特历史测量结果训练轻量预测模型
2. **推测量子门执行**：在测量完成前预测性执行条件门，减少等待延迟
3. **回滚机制**：预测错误时通过反向量子门恢复量子状态
4. **延迟分析**：理论和实验证明在 >85% 预测准确率下获得净延迟收益

## 实验结果

- 量子纠错电路端到端延迟降低 **25–40%**
- 与 Sycamore 等硬件平台的测量延迟兼容

## 关键词

量子反馈 · 分支预测 · 量子纠错 · 推测执行 · PKU · ISCA 2025
