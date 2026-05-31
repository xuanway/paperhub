---
title: "REIS: 高性能高能效存储内检索系统"
description: "ISCA 2025论文解读：REIS将向量检索和相似度计算推送到SSD内部执行，构建高性能高能效的In-Storage检索系统。"
tags: ["ISCA2025", "存储内处理", "向量检索", "In-Storage", "ETH Zurich", "Onur Mutlu"]
---

# REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing

**作者**：Kangqi Chen, Rakesh Nadig, Nika Mansouri Ghiasi, Yu Liang, Haiyu Mao, Jisung Park, Manos Frouzakis, Mohammad Sadrosadati, Onur Mutlu  
**机构**：ETH Zurich  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> 大规模向量数据库检索产生巨大的 SSD→DRAM 数据传输开销；REIS 将向量距离计算卸载到 SSD 控制器内部，大幅减少数据搬运。

## 主要贡献

1. **In-Storage 向量处理**：SSD 控制器内置 SIMD 向量计算单元
2. **粗粒度+精粒度两阶段检索**：SSD 端粗筛 + DRAM 端精排，最优化数据传输
3. **多 SSD 并行**：跨多个 NVMe SSD 并行检索，线性扩展吞吐量

## 实验结果
- 与 CPU+NVMe SSD 基线相比，吞吐量提升 **5×**，能效提升 **8×**

## 关键词

In-Storage处理 · 向量检索 · SSD · ETH Zurich · Onur Mutlu · ISCA 2025
