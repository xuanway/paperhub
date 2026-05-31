---
title: "CaliQEC: 表面码量子纠错的原位量子比特校准"
description: "ISCA 2025论文解读：CaliQEC提出在量子纠错执行期间原位进行量子比特校准，无需暂停计算即可维持高量子比特质量。"
tags: ["ISCA2025", "量子计算", "量子纠错", "原位校准", "表面码", "UCSD"]
---

# CaliQEC: In-situ Qubit Calibration for Surface Code Quantum Error Correction

**作者**：Xiang Fang, Keyi Yin, Yuchen Zhu, Jixuan Ruan, Dean Tullsen, Zhiding Liang, Andrew Sornborger, Ang Li, Travis Humble, Yufei Ding, Yunong Shi, Dean Tullsen  
**机构**：UCSD, UIUC 等  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 量子比特参数随时间漂移，定期校准会中断计算；CaliQEC 在表面码纠错的稳定子测量中穿插校准操作，实现计算不停机的持续校准。

## 主要贡献

1. **原位校准协议**：利用表面码稳定子测量的冗余，插入零开销校准探针
2. **漂移检测**：实时监测量子比特频率和门保真度漂移
3. **自适应校准**：仅在检测到显著漂移时触发校准，避免不必要中断
4. **逻辑错误率分析**：证明 CaliQEC 维持的逻辑错误率与定期停机校准相当

## 关键词

量子纠错 · 原位校准 · 表面码 · 量子比特漂移 · UCSD · ISCA 2025
