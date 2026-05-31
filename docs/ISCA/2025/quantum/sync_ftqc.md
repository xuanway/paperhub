---
title: "Synchronization for Fault-Tolerant Quantum Computers"
description: "ISCA 2025论文解读：研究容错量子计算机中不同逻辑量子比特操作的同步问题，提出高效同步协议减少空闲等待开销。"
tags: ["ISCA2025", "量子计算", "容错量子", "同步", "Wisconsin"]
---

# Synchronization for Fault-Tolerant Quantum Computers

**作者**：Satvik Maurya, Swamit Tannu  
**机构**：University of Wisconsin-Madison  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 容错量子计算（FTQC）中，不同逻辑量子比特的操作延迟不同，导致同步等待开销；本文设计高效同步协议，以最小化逻辑门间的空闲周期。

## 主要贡献

1. **FTQC 同步问题形式化**：量化不同逻辑量子比特因错误纠正延迟差异导致的同步开销
2. **调度算法**：优化量子电路中 barrier 操作的插入位置，减少总延迟
3. **资源分析**：评估同步开销在完整量子算法中的比例

## 关键词

容错量子计算 · 量子同步 · 逻辑量子比特 · Wisconsin · ISCA 2025
