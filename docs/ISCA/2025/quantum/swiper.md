---
title: "SWIPER: 通过推测窗口解码最小化容错量子程序延迟"
description: "ISCA 2025论文解读：SWIPER将推测执行思想引入量子错误纠正解码，通过预测解码结果并推测性执行后续量子操作，降低容错量子计算延迟。"
tags: ["ISCA2025", "量子计算", "推测解码", "容错量子", "表面码", "UChicago"]
---

# SWIPER: Minimizing Fault-Tolerant Quantum Program Latency via Speculative Window Decoding

**作者**：Joshua Viszlai, Jason Chadwick, Sarang Joshi, Gokul Ravi, Yanjing Li, Fred Chong  
**机构**：University of Chicago 等  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 表面码解码是 FTQC 的延迟瓶颈；SWIPER 推测解码结果并提前执行后续操作，解码错误时回滚，以高预测精度获得延迟收益。

## 主要贡献

1. **推测窗口解码**：将解码过程分解为窗口，对当前窗口解码结果进行推测
2. **推测执行机制**：在解码完成前推测性执行基于解码结果的条件门
3. **回滚协议**：解码结果与推测不符时的高效量子状态恢复
4. **延迟分析**：在 d=5/7/9 表面码上量化延迟收益

## 实验结果

- 在 d=7 表面码上，推测解码将逻辑周期延迟降低 **35%**
- 预测准确率 >90%（回滚代价可控）

## 关键词

推测解码 · 表面码 · 容错量子计算 · UChicago · ISCA 2025
