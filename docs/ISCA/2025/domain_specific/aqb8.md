---
title: "AQB8: 光线追踪的自适应多级量化加速"
description: "ISCA 2025论文解读：AQB8为光线追踪BVH数据结构设计自适应量化压缩方案，通过多级量化减少BVH内存占用和带宽，提升光线追踪性能。"
tags: ["ISCA2025", "光线追踪", "BVH量化", "压缩", "NTHU"]
---

# AQB8: Adaptive Quantization for Bounding Volume Hierarchies in Ray Tracing

**作者**：多位作者  
**机构**：National Tsing Hua University (NTHU)  
**会议**：ISCA 2025 · Session 3B: Domain Specific I  

---

## 一句话总结

> BVH 数据结构占用大量内存带宽；AQB8 对 BVH 节点坐标自适应量化到 8bit，减少 BVH 内存流量，提升光线追踪吞吐量。

## 关键词

光线追踪 · BVH压缩 · 量化 · NTHU · ISCA 2025
