---
title: "In-Storage Acceleration of Retrieval Augmented Generation as a Service"
description: "ISCA 2025论文解读：将RAG服务的向量检索操作卸载到SSD存储设备内执行，减少主机IO带宽消耗，提升RAG服务的吞吐量和能效。"
tags: ["ISCA2025", "RAG", "存储内加速", "向量检索", "SSD", "UCSD"]
---

# In-Storage Acceleration of Retrieval Augmented Generation as a Service

**作者**：Rohan Mahapatra, Saurabh Garg, Haiyu Mao, Soroush Ghodrati, Yufei Ding, Hadi Esmaeilzadeh  
**机构**：UC San Diego  
**会议**：ISCA 2025 · Session 3C: Storage  

---

## 一句话总结

> RAG 服务的向量数据库检索每次查询需要读取 GB 级数据；将 ANN 检索卸载到 SSD 内执行，减少 PCIe 流量，大幅提升 RAG-as-a-Service 的吞吐量。

## 主要贡献

1. **存储内 ANN 引擎**：SSD 控制器内置向量距离计算和候选筛选逻辑
2. **RAGaaS 架构**：设计面向多租户 RAG 服务的 In-Storage 加速系统
3. **SSD-LLM 协同**：RAG 检索结果直接与 LLM 推理引擎对接的数据流设计

## 关键词

RAG · In-Storage · 向量检索 · SSD · UCSD · ISCA 2025
