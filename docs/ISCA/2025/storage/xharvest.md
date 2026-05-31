---
title: "XHarvest: CXL驱动的高性能低成本SSD架构"
description: "ISCA 2025论文解读：XHarvest利用CXL接口的内存语义重新设计SSD内部架构，通过利用SSD内部DRAM缓冲实现高性能存储。"
tags: ["ISCA2025", "CXL", "SSD", "存储架构", "成本效益", "NUDT"]
---

# XHarvest: Rethinking High-Performance and Cost-Efficient SSD Architecture with CXL-Driven Harvesting

**作者**：Li Peng, Duo Liu, Zhenlin Wang, Zili Shao  
**机构**：National University of Defense Technology (NUDT), Michigan Tech  
**会议**：ISCA 2025 · Session 3C: Storage  

---

## 一句话总结

> 高端 SSD 内置大量 DRAM 缓冲（数GB）但利用率低；XHarvest 通过 CXL 接口将 SSD 内部 DRAM 暴露给主机，在不增加成本的前提下扩展系统内存容量。

## 主要贡献

1. **CXL 内存语义**：通过 CXL.mem 将 SSD 内部 DRAM 暴露为可寻址内存池
2. **动态容量分配**：根据 IO 负载动态调整 DRAM 用作 SSD 缓冲或主机内存的比例
3. **成本效益分析**：量化每 GB 成本的收益相对于独立 CXL DRAM 模块的优势

## 关键词

CXL · SSD · 存储架构 · 内存扩展 · NUDT · ISCA 2025
