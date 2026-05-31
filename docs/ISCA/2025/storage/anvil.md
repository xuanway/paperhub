---
title: "ANVIL: 键值存储的存储内加速器"
description: "ISCA 2025论文解读：ANVIL在SSD内部集成键值存储（KV Store）专用加速逻辑，将Get/Put操作的哈希查找和数据解压缩卸载到存储设备内执行。"
tags: ["ISCA2025", "存储内加速", "键值存储", "SSD", "KV Store", "Rochester"]
---

# ANVIL: An In-Storage Accelerator for Name-Value Data Stores

**作者**：Ryan Wong, Rui Ding, Haris Volos, Michael Swift  
**机构**：University of Rochester, University of Hawaii  
**会议**：ISCA 2025 · Session 3C: Storage  

---

## 一句话总结

> KV Store（Redis/RocksDB）的 Get 操作涉及大量数据从 SSD 读入 DRAM 再查找；ANVIL 将哈希索引查找和数据处理卸载到 SSD 控制器内，减少主机数据传输。

## 主要贡献

1. **In-Storage KV 引擎**：SSD 控制器实现轻量级哈希索引查找逻辑
2. **数据卸载管道**：压缩解压缩和序列化操作在存储侧执行
3. **主机接口**：标准化的 NVMe 扩展命令集成 ANVIL 功能

## 关键词

In-Storage处理 · KV Store · SSD · ISCA 2025
