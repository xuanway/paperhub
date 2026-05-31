---
title: "HeterRAG: 异构存内计算加速检索增强生成"
description: "ISCA 2025论文解读：HeterRAG设计异构PIM架构专门加速RAG（检索增强生成）系统的向量检索和上下文融合操作。"
tags: ["ISCA2025", "存内计算", "RAG加速", "异构PIM", "HUST"]
---

# HeterRAG: Heterogeneous Processing-in-Memory Acceleration for Retrieval-augmented Generation

**作者**：Chaoqiang Liu, Haifeng Liu, Dan Chen, Yu Huang, Yi Zhang, Wenjing Xiao, XIAOFEI LIAO, Hai Jin  
**机构**：Huazhong University of Science and Technology (HUST)  
**会议**：ISCA 2025 · Session 5C: Processing-in-Memory  

---

## 一句话总结

> RAG 系统的向量检索（ANN搜索）和文本融合操作内存密集；HeterRAG 设计专用异构 PIM 加速这两个阶段，大幅提升 RAG 服务吞吐量。

## 主要贡献

1. **RAG 访存分析**：揭示 ANN 检索和 Cross-Attention 融合是主要内存瓶颈
2. **异构 PIM 设计**：DRAM-PIM 用于向量检索，SRAM-PIM 用于上下文融合
3. **系统整合**：与 LLM 推理引擎（如 vLLM）的调度接口

## 关键词

RAG加速 · 存内计算 · 向量检索 · HUST · ISCA 2025
