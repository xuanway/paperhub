---
title: "RAP: 可重配自动机处理器"
description: "ISCA 2025论文解读：RAP提出可重配自动机处理器架构，支持多种正则表达式和模式匹配工作负载的高效硬件加速。"
tags: ["ISCA2025", "自动机处理器", "正则表达式", "模式匹配", "Rice"]
---

# RAP: Reconfigurable Automata Processor

**作者**：Ziyuan Wen, Alexis Le Glaunec, Konstantinos Mamouras, Kaiyuan Yang  
**机构**：Rice University  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> 自动机处理器（AP）可高效执行正则表达式匹配，但现有设计缺乏可重配性；RAP 通过可重配架构在单一硬件上支持不同自动机工作负载。

## 主要贡献

1. **可重配 NFA 架构**：支持运行时重新配置自动机拓扑结构
2. **多模式支持**：同时处理多个正则表达式模式的并发匹配
3. **流式处理**：针对网络流量分析、日志处理等场景优化

## 关键词

自动机处理器 · 正则表达式 · 模式匹配 · Rice University · ISCA 2025
